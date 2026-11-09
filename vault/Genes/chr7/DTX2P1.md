---
symbol: "DTX2P1"
type: "gene"
col: 11847
ensembl_id: "ENSG00000186704"
name: "DTX2 pseudogene 1"
location: "7q11.23"
module: 153
arm: "+"
pooled_cpm: 6.62
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# DTX2P1

*DTX2 pseudogene 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Abemaciclib (drug)]] 0.05 µM: 1.56× (z +3.9, q 0.047, up in 10 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 1.58× (z +3.6, q 0.091, up in 15 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.580× (z -4.9, q 6e-04, down in 20 of 37 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.628× (z -4.2, q 0.009, down in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (LoVo 0.127×, C32 0.130×, NCI-H1573 0.133×, SK-MEL-2 0.162×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 0.0978×, AsPC-1 0.0739×, A498 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.126×, AsPC-1 0.0732×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SW1417 0.0696×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (A-427 0.0767×); [[Silodosin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0826×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JMJD7]] (+0.60, fdr 1e-05), [[PLXNB1]] (+0.56, fdr 1e-05), [[ARHGEF16]] (+0.55, fdr 2e-05); moves opposite to [[MYO9A]] (-0.49, fdr 5e-05), [[DNAAF9]] (-0.47, fdr 1e-04), [[SNAPIN]] (-0.46, fdr 3e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TMPRSS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +3.9 | 0.047 | 10/45 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.58×** | +3.6 | 0.091 | 15/46 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.43× | +3.2 | 0.28 | 9/43 (A498, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11847.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (LoVo 0.127×, C32 0.130×, NCI-H1573 0.133×, SK-MEL-2 0.162×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 0.0978×, AsPC-1 0.0739×, A498 0.164×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.126×, AsPC-1 0.0732×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SW1417 0.0696×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (A-427 0.0767×); [[Silodosin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0826×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.580×** | -4.9 | 6e-04 | 20/37 (SW480, C32, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -4.2 | 0.009 | 19/45 (C32, A-427, …) | two highest doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.738×** | -3.9 | 0.022 | 16/37 (LoVo, C32, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.678× | -3.1 | 0.28 | 13/42 (LoVo, C32, …) | two highest doses | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0739× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 10.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 4.35 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0756× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 7.92 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.0826× (z -8.5) |
| [[SW1417 (line)]] | alt | 9.28 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0696× (z -10.8) |
| [[A-427 (line)]] | wt | 3.68 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0767× (z -8.6) |
| [[A549 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0978× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 8.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.67 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMJD7]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PLXNB1]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[EPS8L3]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ANAPC2]] | +0.52 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[SRC]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[WASH9P]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[DTX2]] | +0.49 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[WASH8P]] ⚠ | +0.49 | +0.38 / +0.53 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ELMO3]] | +0.49 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[CYP2D7]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[IGSF9]] | +0.48 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[DAB2IP]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9A]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[DNAAF9]] | -0.47 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[SNAPIN]] | -0.46 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[KMT5B]] | -0.46 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[NEK1]] | -0.46 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[POLK]] | -0.46 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[EPC1]] | -0.45 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SMAD9]] | -0.45 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[FOXD1]] | -0.44 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[MED19]] | -0.43 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[NPHP3]] | -0.43 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[MRPS33]] | -0.43 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS2]] | B | TMPRSS2 activity raises DTX2P1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 1.61× lower at baseline in the lines without TMPRSS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[AFAP1L2]] | B | AFAP1L2 activity raises DTX2P1's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without AFAP1L2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[ANO9]] | B | ANO9 activity raises DTX2P1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without ANO9 | 0.042 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[INAVA]] | B | INAVA activity raises DTX2P1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without INAVA | 0.059 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SMAD9]] | B | SMAD9 activity lowers DTX2P1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.61× higher at baseline in the lines without SMAD9 | 0.077 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[CLIC5]] | B | CLIC5 activity raises DTX2P1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without CLIC5 | 0.083 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[GPR35]] | B | GPR35 activity raises DTX2P1's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without GPR35 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[HNF4A]] | B | HNF4A activity raises DTX2P1's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 1.58× lower at baseline in the lines without HNF4A | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[LMNTD2]] | C | LMNTD2 activity raises DTX2P1's level | lines that do not express LMNTD2 (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without LMNTD2 | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGAP27, MMP25, RBMS2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.367). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, 45.0); signed map (50.4, -2.4). **Vector** length 48.0, 5.90% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.4 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +0.9 | -1.8 |
|  | [[Ivermectin (drug)]] 5 µM |  | +0.8 | +1.0 |
|  | [[Altretamine (drug)]] 0.5 µM |  | +0.8 | +1.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +0.8 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | -3.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.5 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | DTX2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:76,978,617-77,004,308 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42352) · Entrez [107161144](https://www.ncbi.nlm.nih.gov/gene/107161144) · Ensembl [ENSG00000186704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186704)

## Data

Gene col 11847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11847); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11847]; `tensor/DDL_lfc|DDL_z.npy` [11847]; `embed/gene_vectors.npy` [11847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11847 or target_col == 11847). Every well: [[DTX2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTX2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
