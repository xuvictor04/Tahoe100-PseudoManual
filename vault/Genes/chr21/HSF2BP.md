---
symbol: "HSF2BP"
type: "gene"
col: 8317
ensembl_id: "ENSG00000160207"
name: "heat shock transcription factor 2 binding protein"
location: "21q22.3"
module: 1
arm: "+"
pooled_cpm: 6.92
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 15
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# HSF2BP

*heat shock transcription factor 2 binding protein* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.71× (z +5.7, q 6e-06, up in 15 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.421× (z -9.2, q 1e-17, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNRD3]] (+0.66, fdr 7e-06), [[SNHG26]] (+0.64, fdr 1e-05), [[ZNF239]] (+0.63, fdr 7e-06); moves opposite to [[MPC2]] (-0.55, fdr 3e-05), [[CBFA2T2]] (-0.54, fdr 3e-05), [[PDE8A]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TRIM2]] → it (grade B ⚠); 15 go from it, the strongest it → [[SLC4A3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +5.7 | 6e-06 | 15/40 (A-427, LoVo, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.9 | 3e-04 | 6/44 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.8 | 3e-04 | 4/16 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.7 | 4e-04 | 2/12 (HEC-1-A, A-172) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 0.001 | 14/35 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.61×** | +4.3 | 0.001 | 10/39 (HOP62, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.30×** | +3.9 | 0.006 | 6/41 (NCI-H2347, C-33 A, …) | top dose only | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.015 | 10/42 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.018 | 4/20 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.019 | 10/34 (A-172, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.019 | 7/43 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.12 | 6/43 (A498, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -9.2 | 1e-17 | 30/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.449×** | -8.5 | 3e-15 | 23/40 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.462×** | -8.2 | 3e-14 | 23/40 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -7.9 | 3e-13 | 24/33 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -6.2 | 6e-08 | 21/41 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.617×** | -5.0 | 6e-05 | 15/28 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.683×** | -4.1 | 0.004 | 15/40 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -3.9 | 0.008 | 9/39 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.665×** | -3.7 | 0.014 | 11/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.031 | 12/41 (SNU-1, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.036 | 10/38 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.730×** | -3.4 | 0.036 | 13/42 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0267× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -15.1) |
| [[A-172 (line)]] | wt | 28.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.177× (z -8.8) |
| [[J82 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -10.1) |
| [[A-427 (line)]] | wt | 7.41 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.91 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0553× (z -9.2) |
| [[LoVo (line)]] | wt | 6.74 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0770× (z -11.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0478× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 7.94 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0766× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 5.41 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.111× (z -10.6) |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0800× (z -9.2) |
| [[A498 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD3]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SNHG26]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[FTCDNL1]] | +0.60 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ZNF485]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SP2-AS1]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.57 | +0.57 / +0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM185B]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[TCERG1]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[P2RX5]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[KICS2]] | +0.56 | +0.62 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.55 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CBFA2T2]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[PDE8A]] | -0.52 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[PLEKHH3]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ATF6B]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[GNB2]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[LMBR1L]] | -0.51 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[GMCL1]] | -0.50 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.50 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[TSC22D4]] | -0.50 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TRIM62]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[DCAF11]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM2]] | B | TRIM2 activity lowers HSF2BP's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 1.53× higher at baseline in the lines without TRIM2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[TERT]] | B | TERT activity raises HSF2BP's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without TERT | 0.031 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[ZP3]] | B | ZP3 activity raises HSF2BP's level | lines that do not express ZP3 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without ZP3 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRIM2]] | B | TRIM2 activity weakens HSF2BP's drug response | lines that do not express TRIM2 (15) vs lines expressing it (29) | the lines without TRIM2 respond 1.48× as strongly (z diff -0.81); strongest at Ouabain (Octahydrate) 5 µM: 0.26x vs 0.44x (z diff -2.4) | 0.058 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5; target measured in part of the lines; artifact flags |
| [[DAW1]] | B | DAW1 activity raises HSF2BP's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 1.71× lower at baseline in the lines without DAW1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[ABCA17P]] | B | ABCA17P activity raises HSF2BP's level | lines that do not express ABCA17P (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without ABCA17P | 0.078 | ⚠ within organs, on part of the lines; also absent: NTN1, KIF26A, DOCK3; maybe low, not absent |
| [[SLC4A3]] | C | SLC4A3 activity raises HSF2BP's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.06× lower at baseline in the lines without SLC4A3 | 0.026 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | C | HSF2BP activity raises SLC4A3's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 3.85× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[RIF1]] | C | HSF2BP activity raises RIF1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |
| [[METTL1]] | C | HSF2BP activity raises METTL1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |
| [[TCERG1]] | C | HSF2BP activity raises TCERG1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.39× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |
| [[TRIM65]] | C | HSF2BP activity raises TRIM65's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without HSF2BP | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[TRABD2B]] | C | HSF2BP activity raises TRABD2B's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 3.80× lower at baseline in the lines without HSF2BP | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[ATP6V1E2]] | C | HSF2BP activity raises ATP6V1E2's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without HSF2BP | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[ABCE1]] | C | HSF2BP activity raises ABCE1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without HSF2BP | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[PNO1]] | C | HSF2BP activity raises PNO1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without HSF2BP | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| [[TEX22]] | C | HSF2BP activity raises TEX22's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.47× lower at baseline in the lines without HSF2BP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |
| [[TXNRD3]] | C | HSF2BP activity raises TXNRD3's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 3.04× lower at baseline in the lines without HSF2BP | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | HSF2BP's natural level lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | HSF2BP's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.71 | 0.285 over the table, 0.068 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.3, -36.0); signed map (2.3, -43.4). **Vector** length 68.2, 11.6% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -8.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | heat shock transcription factor 2 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,529,186-43,659,488 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEILB2 |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75031](https://www.uniprot.org/uniprotkb/O75031) (Heat shock factor 2-binding protein):

> Meiotic recombination factor component of recombination bridges involved in meiotic double-strand break repair. Modulates the localization of recombinases DMC1:RAD51 to meiotic double-strand break (DSB) sites through the interaction with BRCA2 and its recruitment during meiotic recombination (By similarity). Indispensable for the DSB repair, homologous synapsis, and crossover formation that are needed for progression past metaphase I, is essential for spermatogenesis and male fertility (By …

**Summary**, from NCBI Gene [11077](https://www.ncbi.nlm.nih.gov/gene/11077):

> HSF2 binding protein (HSF2BP) associates with HSF2. The interaction occurs between the trimerization domain of HSF2 and the amino terminal hydrophilic region of HSF2BP that comprises two leucine zipper motifs. HSF2BP may therefore be involved in modulating HSF2 activation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5226) · Entrez [11077](https://www.ncbi.nlm.nih.gov/gene/11077) · UniProt [O75031](https://www.uniprot.org/uniprotkb/O75031) · Ensembl [ENSG00000160207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160207)

## Data

Gene col 8317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8317); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8317]; `tensor/DDL_lfc|DDL_z.npy` [8317]; `embed/gene_vectors.npy` [8317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8317 or target_col == 8317). Every well: [[HSF2BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSF2BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
