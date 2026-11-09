---
symbol: "NAPA"
type: "gene"
col: 2598
ensembl_id: "ENSG00000105402"
name: "NSF attachment protein alpha"
location: "19q13.33"
module: 32
arm: "+"
pooled_cpm: 38.9
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# NAPA

*NSF attachment protein alpha* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +13.4, q 4e-38, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.682× (z -7.3, q 2e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM140]] (+0.65, fdr 7e-06), [[GTPBP1]] (+0.64, fdr 2e-05), [[STAT2]] (+0.63, fdr 7e-06); moves opposite to [[GNPNAT1]] (-0.49, fdr 3e-05), [[MPHOSPH6]] (-0.48, fdr 5e-05), [[ZNF215]] (-0.47, fdr 4e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +13.4 | 4e-38 | 42/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +13.3 | 4e-38 | 44/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.71×** | +13.3 | 5e-38 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +10.9 | 2e-25 | 40/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +9.0 | 4e-17 | 40/48 (NCI-H460, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.41×** | +8.5 | 1e-15 | 41/49 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +8.3 | 1e-14 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +7.2 | 6e-11 | 26/40 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +6.8 | 5e-10 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.38×** | +6.0 | 9e-08 | 30/48 (RPMI-7951, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.57×** | +6.0 | 9e-08 | 34/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +5.9 | 2e-07 | 29/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.1 | 1e-05 | 25/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +5.0 | 2e-05 | 31/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.9 | 3e-05 | 26/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 2e-04 | 25/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.001 | 27/48 (AsPC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.002 | 19/48 (J82, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.010 | 18/49 (AsPC-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -7.3 | 2e-10 | 37/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.636×** | -6.1 | 4e-07 | 40/48 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.742×** | -5.7 | 3e-06 | 28/48 (COLO 205, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.804×** | -4.1 | 0.004 | 24/48 (A549, LoVo, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.735×** | -4.1 | 0.004 | 27/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.773×** | -3.5 | 0.053 | 23/48 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.841× | -3.3 | 0.078 | 21/49 (CHP-212, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.0 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +23.9) | — |
| [[SW480 (line)]] | alt | 23.1 | 11 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 19.4 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.97× (z +14.1) | — |
| [[J82 (line)]] | alt | 50.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.1) | — |
| [[KATO III (line)]] | alt | 54.3 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.458× (z -9.0) |
| [[HOP62 (line)]] | alt | 14.1 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.80× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 30.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.385× (z -9.3) |
| [[SW1417 (line)]] | alt | 84.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +10.4) | — |
| [[A549 (line)]] | wt | 49.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.414× (z -10.1) |
| [[COLO 205 (line)]] | alt | 71.2 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.322× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 34.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +11.9) | — |
| [[RKO (line)]] | wt | 38.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.4) | [[Tucidinostat (drug)]] 0.5 µM 0.291× (z -8.9) |
| [[A-172 (line)]] | wt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.9) | — |
| [[A-427 (line)]] | wt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.2) | — |
| [[A498 (line)]] | wt | 69.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.562× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 35.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.8) | — |
| [[C32 (line)]] | wt | 34.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.458× (z -8.5) |
| [[CHP-212 (line)]] | wt | 34.9 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.172× (z -9.1) |
| [[H4 (line)]] | wt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0634× (z -15.2) |
| [[Hs 766T (line)]] | wt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 83.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +10.2) | — |
| [[LoVo (line)]] | wt | 53.1 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.477× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 37.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 38.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.7) | — |
| [[SW48 (line)]] | wt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM140]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GTPBP1]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[STAT2]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[UBA7]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[ADAR]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RNF213]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MOV10]] | +0.61 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TRIM22]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LAP3]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[LIPA]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PARP10]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[REC8]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPNAT1]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[MPHOSPH6]] | -0.48 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ZNF215]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises NAPA's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without OAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises NAPA's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without FBXO39 | 0.020 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[TRIM22]] | B | TRIM22 activity raises NAPA's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without TRIM22 | 0.031 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[GBP1]] | B | GBP1 activity raises NAPA's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.36× lower at baseline in the lines without GBP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[TOP2A]] | B | TOP2A activity lowers NAPA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IFI44L]] | B | IFI44L activity raises NAPA's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without IFI44L | 0.042 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[CCDC194]] | B | CCDC194 activity raises NAPA's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without CCDC194 | 0.058 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[TMEM140]] | B | TMEM140 activity raises NAPA's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.48× lower at baseline in the lines without TMEM140 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises NAPA's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without IFI44 | 0.064 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[MX1]] | B | MX1 activity raises NAPA's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.37× lower at baseline in the lines without MX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SLC15A3]] | B | SLC15A3 activity raises NAPA's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without SLC15A3 | 0.068 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[RSAD2]] | B | RSAD2 activity raises NAPA's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without RSAD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.0, 55.4); signed map (67.1, 33.4). **Vector** length 114, 34.9% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.52 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.52 to 27); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.52 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +13.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.8 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.8 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.6 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.3 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | NSF attachment protein alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:47,487,637-47,515,091 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 14 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; Golgi Associated Vesicle Biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P54920](https://www.uniprot.org/uniprotkb/P54920) (Alpha-soluble NSF attachment protein):

> Required for vesicular transport between the endoplasmic reticulum and the Golgi apparatus (Probable). Together with GNA12 promotes CDH5 localization to plasma membrane.

**Summary**, from NCBI Gene [8775](https://www.ncbi.nlm.nih.gov/gene/8775):

> This gene encodes a member of the soluble NSF attachment protein (SNAP) family. SNAP proteins play a critical role in the docking and fusion of vesicles to target membranes as part of the 20S NSF-SNAP-SNARE complex. The encoded protein plays a role in the completion of membrane fusion by mediating the interaction of N-ethylmaleimide-sensitive factor (NSF) with the vesicle-associated and membrane-associated SNAP receptor (SNARE) complex, and stimulating the ATPase activity of NSF. Alternatively …

**Accessions** — [HGNC:7641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7641) · Entrez [8775](https://www.ncbi.nlm.nih.gov/gene/8775) · UniProt [P54920](https://www.uniprot.org/uniprotkb/P54920) · Ensembl [ENSG00000105402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105402)

## Data

Gene col 2598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2598); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2598]; `tensor/DDL_lfc|DDL_z.npy` [2598]; `embed/gene_vectors.npy` [2598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2598 or target_col == 2598). Every well: [[NAPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
