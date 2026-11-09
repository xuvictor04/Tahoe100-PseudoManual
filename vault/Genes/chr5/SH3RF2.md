---
symbol: "SH3RF2"
type: "gene"
col: 7981
ensembl_id: "ENSG00000156463"
name: "SH3 domain containing ring finger 2"
location: "5q32"
module: 123
arm: "+"
pooled_cpm: 44.93
n_lines_expressing: 34
n_dd_up: 52
n_dd_down: 7
n_dd_up_clean: 42
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 19
direction_downstream: 12
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# SH3RF2

*SH3 domain containing ring finger 2* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 52 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.40× (z +15.1, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.743× (z -5.1, q 1e-04, down in 16 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KRT80]] (+0.59, fdr 3e-05), [[PLS3]] (+0.55, fdr 2e-05), [[PALLD]] (+0.55, fdr 1e-05); moves opposite to [[RSRP1]] (-0.53, fdr 3e-05), [[C16orf46]] (-0.50, fdr 3e-05), [[C14orf28]] (-0.49, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[MACC1]] → it (grade B ⚠); 12 go from it, the strongest it → [[IL18]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 52 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +15.1 | 0e+00 | 29/32 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.48×** | +11.1 | 4e-26 | 27/32 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.08×** | +8.9 | 7e-17 | 22/31 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.98×** | +8.4 | 9e-15 | 20/32 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.93×** | +8.0 | 1e-13 | 19/32 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +7.7 | 1e-12 | 24/31 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +7.0 | 3e-10 | 17/31 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.74×** | +6.8 | 1e-09 | 19/32 (MIA PaCa-2, AsPC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.71×** | +6.5 | 4e-09 | 20/31 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.77×** | +6.5 | 5e-09 | 18/31 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.68×** | +6.3 | 2e-08 | 23/32 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.65×** | +5.9 | 2e-07 | 20/31 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.59×** | +5.7 | 6e-07 | 19/31 (SK-MEL-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.59×** | +5.6 | 7e-07 | 18/31 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.56×** | +5.6 | 8e-07 | 18/32 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.39×** | +5.6 | 1e-06 | 17/31 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +5.5 | 1e-06 | 19/32 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +5.4 | 2e-06 | 22/32 (SW 900, PANC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 3e-05 | 15/32 (LoVo, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.8 | 4e-05 | 15/31 (KATO III, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.743×** | -5.1 | 1e-04 | 16/32 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -4.9 | 2e-04 | 19/31 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.676×** | -4.8 | 3e-04 | 14/31 (KATO III, NCI-H460, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.791×** | -4.1 | 0.007 | 12/32 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -3.9 | 0.011 | 19/32 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.803×** | -3.8 | 0.012 | 13/32 (Hs 766T, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.012 | 19/32 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.2 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 4.39× (z +10.0) | — |
| [[LoVo (line)]] | wt | 182 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -12.7) |
| [[LS 180 (line)]] | wt | 174 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 37.3 | 4 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.42× (z +12.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 24.0× (z +9.5) | — |
| [[SW480 (line)]] | alt | 26.5 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.70× (z +11.4) | — |
| [[A-427 (line)]] | wt | 32.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 3.82× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.47× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 41.0 | 2 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.07× (z +11.4) | — |
| [[SW48 (line)]] | wt | 293 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -17.6) |
| [[A498 (line)]] | wt | 34.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.64× (z +10.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 28.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.15× (z +10.2) | — |
| [[J82 (line)]] | alt | 41.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.83× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.08× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 4.19× (z +9.2) | — |
| [[A-172 (line)]] | wt | 7.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.96 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT80]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[PLS3]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PALLD]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[IL18]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ANXA3]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[TRAK1]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[WWC1]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 | same gene group |
| [[GPR87]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[COBL]] | +0.51 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[C6orf132]] | +0.49 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[SPTLC3]] | +0.48 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SRPX2]] | +0.48 | +0.42 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[C16orf46]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NPHP3]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[FAM76B]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[UBN2]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[C12orf57]] | -0.47 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PIK3CA]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[IKZF4]] | -0.44 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[GCAT]] | -0.44 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[HBP1]] | -0.43 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[UBXN7]] | -0.43 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 16, C 3. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MACC1]] | B | MACC1 activity raises SH3RF2's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 3.31× lower at baseline in the lines without MACC1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2 |
| [[LINC02595]] | B | LINC02595 activity raises SH3RF2's level | lines that do not express LINC02595 (9) vs lines expressing it (41) | 3.23× lower at baseline in the lines without LINC02595 | 0.012 | ⚠ within organs, on part of the lines |
| [[ST14]] | B | ST14 activity raises SH3RF2's level | lines that do not express ST14 (32) vs lines expressing it (18) | 3.25× lower at baseline in the lines without ST14 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[HTR1D]] | B | HTR1D activity raises SH3RF2's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without HTR1D | 0.020 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[C1orf116]] | B | C1orf116 activity raises SH3RF2's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.51× lower at baseline in the lines without C1orf116 | 0.022 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[IL18]] | B | IL18 activity raises SH3RF2's level | lines that do not express IL18 (18) vs lines expressing it (32) | 3.04× lower at baseline in the lines without IL18 | 0.023 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[PKP1]] | B | PKP1 activity raises SH3RF2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 3.09× lower at baseline in the lines without PKP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[SLC9A2]] | B | SLC9A2 activity raises SH3RF2's level | lines that do not express SLC9A2 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without SLC9A2 | 0.033 | ⚠ within organs, on part of the lines; also absent: TC2N, MAP7, ENSG00000262302 |
| [[PKP1]] | B | PKP1 activity weakens SH3RF2's drug response | lines that do not express PKP1 (19) vs lines expressing it (13) | the lines without PKP1 respond 2.44× as strongly (z diff -2.37); strongest at c-Kit-IN-1 0.05 µM: 2.28x vs 1.05x (z diff -4.5) | 0.033 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; target measured in part of the lines; artifact flags |
| [[CDH1]] | B | CDH1 activity raises SH3RF2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.31× lower at baseline in the lines without CDH1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CLIC5]] | B | CLIC5 activity raises SH3RF2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.97× lower at baseline in the lines without CLIC5 | 0.045 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SH3RF2's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.0% of all compounds | 0.048 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL18]] | B | SH3RF2 activity raises IL18's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.70× lower at baseline in the lines without SH3RF2 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[SOAT1]] | B | SH3RF2 activity strengthens SOAT1's drug response | lines that do not express SH3RF2 (16) vs lines expressing it (29) | the lines without SH3RF2 respond 0.72× as strongly (z diff +1.15); strongest at Belinostat 5 µM: 2.30x vs 3.12x (z diff +2.1) | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EDN1]] | B | SH3RF2 activity raises EDN1's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 4.59× lower at baseline in the lines without SH3RF2 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[CRYBG2]] | B | SH3RF2 activity raises CRYBG2's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without SH3RF2 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[HKDC1]] | B | SH3RF2 activity raises HKDC1's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 4.08× lower at baseline in the lines without SH3RF2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[C1orf116]] | B | SH3RF2 activity raises C1orf116's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.55× lower at baseline in the lines without SH3RF2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[FRK]] | B | SH3RF2 activity raises FRK's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.37× lower at baseline in the lines without SH3RF2 | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[ACTN4]] | B | SH3RF2 activity raises ACTN4's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without SH3RF2 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[LINC02595]] | B | SH3RF2 activity raises LINC02595's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without SH3RF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[RAB10]] | B | SH3RF2 activity raises RAB10's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 1.30× lower at baseline in the lines without SH3RF2 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[MACC1]] | B | SH3RF2 activity raises MACC1's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without SH3RF2 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[INAVA]] | C | SH3RF2 activity raises INAVA's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 3.94× lower at baseline in the lines without SH3RF2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.262). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.9, 43.1); signed map (49.7, 16.2). **Vector** length 106, 28.7% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.1 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.9 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +5.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.6 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +4.8 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain containing ring finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:145,936,578-146,081,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23654, RNF158, Hepp1, POSHER; previously PPP1R39 |
| Gene groups (HGNC) | Ring finger proteins; Protein phosphatase 1 regulatory subunits; SH3 domain containing; SH3 domain containing ring finger family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEC5](https://www.uniprot.org/uniprotkb/Q8TEC5) (E3 ubiquitin-protein ligase SH3RF2):

> Has E3 ubiquitin-protein ligase activity. Acts as an anti-apoptotic regulator of the JNK pathway by ubiquitinating and promoting the degradation of SH3RF1, a scaffold protein that is required for pro-apoptotic JNK activation. Facilitates TNF-mediated recruitment of adapter proteins TRADD and RIPK1 to TNFRSF1A and regulates PAK4 protein stability via inhibition of its ubiquitin-mediated proteasomal degradation. Inhibits PPP1CA phosphatase activity.

**Summary**, from NCBI Gene [153769](https://www.ncbi.nlm.nih.gov/gene/153769):

> Enables protein phosphatase 1 binding activity and ubiquitin protein ligase activity. Involved in several processes, including positive regulation of JNK cascade; protein autoubiquitination; and regulation of protein metabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26299) · Entrez [153769](https://www.ncbi.nlm.nih.gov/gene/153769) · UniProt [Q8TEC5](https://www.uniprot.org/uniprotkb/Q8TEC5) · Ensembl [ENSG00000156463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156463)

## Data

Gene col 7981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7981); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7981]; `tensor/DDL_lfc|DDL_z.npy` [7981]; `embed/gene_vectors.npy` [7981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7981 or target_col == 7981). Every well: [[SH3RF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3RF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
