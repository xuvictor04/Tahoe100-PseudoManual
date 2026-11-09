---
symbol: "GAB3"
type: "gene"
col: 8325
ensembl_id: "ENSG00000160219"
name: "GRB2 associated binding protein 3"
location: "Xq28"
module: 104
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 33
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# GAB3

*GRB2 associated binding protein 3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.64× (z +9.0, q 2e-16, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.87× (z +8.5, q 6e-15, up in 15 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.473× (z -6.9, q 2e-09, down in 13 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.0458×, hTERT-HPNE 0.0945×, SNU-423 0.171×, PANC-1 0.431×; ⚠ cell-cycle shift, explains ~57% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0310×); [[Daptomycin (drug)]] 0.5 µM in 1 line (HOP62 0.0681×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3RF3]] (+0.63, fdr 1e-05), [[RNF175]] (+0.59, fdr 3e-05), [[ABLIM3]] (+0.59, fdr 1e-05); moves opposite to [[RRAD]] (-0.45, fdr 7e-05), [[PATJ]] (-0.45, fdr 6e-05), [[EPB41]] (-0.44, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[JCAD]] → it (grade B ⚠); 5 go from it, the strongest it → [[ANGPTL4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +9.0 | 2e-16 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +8.5 | 6e-15 | 15/27 (SW480, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +7.4 | 2e-11 | 9/23 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.8 | 1e-09 | 4/20 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +5.9 | 3e-07 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +5.6 | 2e-06 | 7/24 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +5.3 | 7e-06 | 8/28 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.5 | 5e-04 | 2/16 (A549, SNU-423) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 0.002 | 1/17 (A498) | inconsistent across doses | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.003 | 10/27 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 11/28 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 2/21 (HOP62, LOX-IMVI) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 8/28 (PANC-1, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +3.8 | 0.005 | 1/14 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.008 | 7/24 (A549, PANC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.51×** | +3.7 | 0.009 | 6/21 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.015 | 10/24 (A549, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.017 | 6/24 (HOP62, A549, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.017 | 7/24 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.0458×, hTERT-HPNE 0.0945×, SNU-423 0.171×, PANC-1 0.431×; ⚠ cell-cycle shift, explains ~57% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0310×); [[Daptomycin (drug)]] 0.5 µM in 1 line (HOP62 0.0681×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.473×** | -6.9 | 2e-09 | 13/23 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.728×** | -4.3 | 0.005 | 14/22 (A-172, hTERT-HPNE, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.4 | 0.12 | 6/29 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.713× | -3.2 | 0.17 | 8/29 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 0.539× | -3.1 | 0.21 | 7/22 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 6.38 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0945× (z -9.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 4.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0458× (z -16.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0681× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 3.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0310× (z -13.9) |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-423 (line)]] | alt | 6.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.791 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3RF3]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[RNF175]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 | **novel candidate** |
| [[ABLIM3]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TLR2]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[JCAD]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PID1]] | +0.57 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[AFAP1L1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[PXYLP1]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[IL18R1]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[HSD11B1]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CLMP]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAD]] | -0.45 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[PATJ]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[EPB41]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[TNFRSF9]] | -0.43 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[PLAU]] | -0.43 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RFX3]] | -0.43 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[AKR1B1]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JCAD]] | B | JCAD activity raises GAB3's level | lines that do not express JCAD (20) vs lines expressing it (30) | 1.78× lower at baseline in the lines without JCAD | 0.082 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[NR3C1]] | B | NR3C1 activity raises GAB3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[ADGRG2]] | B | ADGRG2 activity raises GAB3's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without ADGRG2 | 0.095 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[RGS17]] | C | RGS17 activity raises GAB3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.07× lower at baseline in the lines without RGS17 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPTL4]] | B | GAB3 activity raises ANGPTL4's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 3.54× lower at baseline in the lines without GAB3 | 0.054 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3 |
| [[FOXL1]] | C | GAB3 activity raises FOXL1's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 2.78× lower at baseline in the lines without GAB3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3; co-absent with the target |
| [[AKAP12]] | C | GAB3 activity raises AKAP12's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 4.13× lower at baseline in the lines without GAB3 | 0.070 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3; co-absent with the target |
| [[CLMP]] | C | GAB3 activity raises CLMP's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 5.07× lower at baseline in the lines without GAB3 | 0.080 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3; co-absent with the target |
| [[LPAR1]] | C | GAB3 activity raises LPAR1's level | lines that do not express GAB3 (17) vs lines expressing it (33) | 4.57× lower at baseline in the lines without GAB3 | 0.083 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, SOGA3; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.5, 14.3); signed map (17.2, 35.2). **Vector** length 42.2, 6.79% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -1.3 | -4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | GRB2 associated binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,675,249-154,751,583 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 2 pathways, smallest: Signaling by CSF1 (M-CSF) in myeloid cells; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

UniProt [Q8WWW8](https://www.uniprot.org/uniprotkb/Q8WWW8) carries no function annotation.

**Summary**, from NCBI Gene [139716](https://www.ncbi.nlm.nih.gov/gene/139716):

> This gene is a member of the GRB2-associated binding protein gene family. These proteins are scaffolding/docking proteins that are involved in several growth factor and cytokine signaling pathways, and they contain a pleckstrin homology domain, and bind SHP2 tyrosine phosphatase and GRB2 adapter protein. The protein encoded by this gene facilitates macrophage differentiation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:17515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17515) · Entrez [139716](https://www.ncbi.nlm.nih.gov/gene/139716) · UniProt [Q8WWW8](https://www.uniprot.org/uniprotkb/Q8WWW8) · Ensembl [ENSG00000160219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160219)

## Data

Gene col 8325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8325); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8325]; `tensor/DDL_lfc|DDL_z.npy` [8325]; `embed/gene_vectors.npy` [8325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8325 or target_col == 8325). Every well: [[GAB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
