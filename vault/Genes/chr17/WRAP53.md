---
symbol: "WRAP53"
type: "gene"
col: 6529
ensembl_id: "ENSG00000141499"
name: "WD repeat containing antisense to TP53"
location: "17p13.1"
module: 105
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# WRAP53

*WD repeat containing antisense to TP53* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.16× (z +15.9, q 0e+00, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.66× (z +11.1, q 1e-26, up in 35 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.108×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.107×; ⚠ toxic); [[Radotinib (drug)]] 0.5 µM in 1 line (HCT15 0.101×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APAF1]] (+0.59, fdr 2e-05), [[SNAPC3]] (+0.58, fdr 6e-05), [[FAM104A]] (+0.58, fdr 5e-05); moves opposite to [[NPIPB4]] (-0.65, fdr 1e-05), [[NPIPB5]] (-0.63, fdr 1e-05), [[CACNA2D1]] (-0.59, fdr 1e-04).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.16×** | +15.9 | 0e+00 | 41/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.96×** | +15.0 | 0e+00 | 43/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.48×** | +12.6 | 6e-34 | 43/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.66×** | +11.1 | 1e-26 | 35/44 (PANC-1, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +10.7 | 1e-24 | 33/43 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +8.2 | 3e-14 | 26/42 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +8.2 | 3e-14 | 31/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +7.5 | 5e-12 | 21/43 (NCI-H2030, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +6.9 | 3e-10 | 18/35 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +6.5 | 4e-09 | 20/43 (SW480, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.1 | 5e-08 | 15/47 (PANC-1, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.48×** | +5.4 | 4e-06 | 13/35 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 6e-06 | 14/41 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +4.8 | 8e-05 | 12/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.43×** | +4.7 | 8e-05 | 14/45 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.6 | 2e-04 | 12/47 (KATO III, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 12/48 (NCI-H460, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.3 | 4e-04 | 11/47 (LoVo, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.001 | 8/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.027 | 3/47 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.029 | 2/47 (A-427, HCT15) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.033 | 4/47 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.17× | +3.1 | 0.041 | 6/47 (NCI-H460, HCT15, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.108×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.107×; ⚠ toxic); [[Radotinib (drug)]] 0.5 µM in 1 line (HCT15 0.101×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.160× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Radotinib (drug)]] 0.5 µM 0.101× (z -9.3) |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -9.4) ⚠ toxic |
| [[C32 (line)]] | wt | 7.82 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0908× (z -9.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.58 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 7.56× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A-172 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[SNAPC3]] | +0.58 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[FAM104A]] | +0.58 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[UBE2O]] | +0.57 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[POM121C]] | +0.57 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[PHF12]] | +0.56 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[MINK1]] | +0.56 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[PPIL3]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ABCB9]] | +0.56 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[SUGP1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SH3GL1]] | +0.55 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[CNOT8]] | +0.55 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB4]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[NPIPB5]] | -0.63 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.59 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TENM3]] | -0.58 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A13]] | -0.56 | -0.57 / -0.32 | both halves | 1e-04 |  |
| [[NFE2L2]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.53 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[RUFY3]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NUTM2B-AS1]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ATE1]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ATXN10]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[WARS2-AS1]] | -0.52 | -0.32 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises WRAP53's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without EID2B | 0.012 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity lowers WRAP53's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.40× higher at baseline in the lines without ADAM8 | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[ABHD17C]] | B | ABHD17C activity lowers WRAP53's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without ABHD17C | 0.041 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers WRAP53's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[POGLUT2]] | C | POGLUT2 activity raises WRAP53's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.8, -12.8); signed map (-40.5, 20.2). **Vector** length 48.4, 5.64% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +6.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.9 | +8.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | +1.7 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +0.9 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -1.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.4 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat containing antisense to TP53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,686,071-7,703,502 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10385, TCAB1; previously WDR79 |
| Gene groups (HGNC) | WD repeat domain containing; Telomerase holoenzyme subunits |
| Reactome | 8 pathways, smallest: Telomere Extension By Telomerase; Association of TriC/CCT with target proteins during biosynthesis; Extension of Telomeres |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUR4](https://www.uniprot.org/uniprotkb/Q9BUR4) (Telomerase Cajal body protein 1):

> RNA chaperone that plays a key role in telomere maintenance and RNA localization to Cajal bodies. Specifically recognizes and binds the Cajal body box (CAB box) present in both small Cajal body RNAs (scaRNAs) and telomerase RNA template component (TERC). Essential component of the telomerase holoenzyme complex, a ribonucleoprotein complex essential for the replication of chromosome termini that elongates telomeres in most eukaryotes. In the telomerase holoenzyme complex, required to stimulate …

**Summary**, from NCBI Gene [55135](https://www.ncbi.nlm.nih.gov/gene/55135):

> This gene encodes an essential component of the telomerase holoenzyme complex, a ribonucleoprotein complex required for telomere synthesis. This protein is enriched in Cajal bodies, nuclear sites of RNP processing that are important for telomerase function. It interacts with dyskerin, TERT and TERC, other components of active telomerase, and with small Cajal body RNAs (scaRNAs), which are involved in modifying splicing RNAs. This mRNA also functions as a p53 antisense transcript, that regulates …

**Accessions** — [HGNC:25522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25522) · Entrez [55135](https://www.ncbi.nlm.nih.gov/gene/55135) · UniProt [Q9BUR4](https://www.uniprot.org/uniprotkb/Q9BUR4) · Ensembl [ENSG00000141499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141499)

## Data

Gene col 6529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6529); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6529]; `tensor/DDL_lfc|DDL_z.npy` [6529]; `embed/gene_vectors.npy` [6529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6529 or target_col == 6529). Every well: [[WRAP53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WRAP53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
