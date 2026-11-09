---
symbol: "TLCD4-RWDD3"
type: "gene"
col: 15675
ensembl_id: "ENSG00000271092"
name: "TLCD4-RWDD3 readthrough"
location: "1p21.3"
module: 68
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 39
n_dd_up: 30
n_dd_down: 7
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# TLCD4-RWDD3

*TLCD4-RWDD3 readthrough* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.41× (z +13.3, q 1e-37, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.597× (z -5.5, q 2e-05, down in 11 of 33 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.651× (z -4.6, q 0.001, down in 11 of 33 measured lines).
> Its strongest partners by |cos| (51 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 50 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLCD4]] (+0.68, fdr 7e-06, ⚠ read-through risk), [[BTG3-AS1]] (+0.52, fdr 1e-04), [[LGALSL-DT]] (+0.52, fdr 4e-04), [[PHACTR2]] (+0.52, fdr 5e-04); moves opposite to [[STUB1]] (-0.59, fdr 3e-04), [[RPUSD1]] (-0.55, fdr 2e-04), [[GGA1]] (-0.54, fdr 5e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PARD3B]] → it (grade B ⚠); 6 go from it, the strongest it → [[PARD3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +13.3 | 1e-37 | 17/22 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +10.5 | 3e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +9.4 | 1e-18 | 12/19 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.6 | 6e-12 | 12/31 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +5.4 | 8e-06 | 10/30 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.0 | 4e-05 | 8/23 (LS 180, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 2e-04 | 3/24 (SNU-423, A498, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.33×** | +4.3 | 1e-03 | 1/32 (NCI-H2030) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.3 | 1e-03 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.003 | 6/24 (BT-474, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 0.003 | 3/32 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +3.9 | 0.004 | 1/7 (A498) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Orlistat (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.006 | 2/18 (LoVo, J82) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 3/32 (LoVo, A498, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 2/30 (CFPAC-1, A498) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.007 | 4/32 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.007 | 4/32 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.007 | 3/20 (HCT15, A-427, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.007 | 1/32 (HEC-1-A) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.597×** | -5.5 | 2e-05 | 11/33 (NCI-H460, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.651×** | -4.6 | 0.001 | 11/33 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -4.4 | 0.002 | 11/32 (SNU-423, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -4.1 | 0.005 | 10/31 (NCI-H23, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -3.8 | 0.017 | 4/26 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | **0.712×** | -3.5 | 0.045 | 3/32 (SNU-423, C32, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.047 | 6/30 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.730× | -3.2 | 0.11 | 1/31 (SNU-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0817× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 4.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.55 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -9.4) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.667 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 32 of them with an alert (⚠; 31 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD4]] | +0.68 | +0.67 / +0.73 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of TLCD4 on the same strand (can correlate by spillover, not regulation) |
| [[BTG3-AS1]] | +0.52 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[LGALSL-DT]] | +0.52 | +0.44 / +0.25 | both halves | 4e-04 |  |
| [[PHACTR2]] | +0.52 | +0.50 / +0.24 | both halves | 5e-04 |  |
| [[CABYR]] | +0.52 | +0.44 / +0.28 | both halves | 3e-04 |  |
| [[ARHGEF37]] | +0.51 | +0.36 / +0.32 | both halves | 2e-04 |  |
| [[PRDM6]] | +0.50 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[CCDC170]] | +0.50 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[CHODL]] | +0.50 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[LINC02542]] | +0.50 | +0.39 / +0.26 | both halves | 4e-04 |  |
| [[DERA]] | +0.50 | +0.41 / +0.24 | both halves | 4e-04 |  |
| [[SEPTIN8]] | +0.50 | +0.36 / +0.18 | ⚠ not reproduced | 1e-03 |  |
| [[RASGRP1]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PDE8B]] | +0.49 | +0.40 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.59 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[RPUSD1]] | -0.55 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[GGA1]] | -0.54 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[AAMP]] | -0.53 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[GCDH]] | -0.53 | -0.14 / -0.35 | ⚠ not reproduced | 0.002 |  |
| [[RTN2]] | -0.50 | -0.47 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[SPATA2L]] | -0.50 | -0.34 / -0.21 | both halves | 6e-04 |  |
| [[PHC2]] | -0.49 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[NAB2]] | -0.49 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[ARMC9]] | -0.49 | -0.30 / -0.23 | both halves | 5e-04 |  |
| [[SLC27A1]] | -0.49 | -0.44 / +0.06 | ⚠ not reproduced | 1.00 |  |
| [[STX1A]] | -0.48 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[C8orf82]] | -0.48 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[ATG16L1]] | -0.47 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[DUSP5]] | -0.46 | -0.47 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD3B]] | B | PARD3B activity raises TLCD4-RWDD3's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 1.88× lower at baseline in the lines without PARD3B | 0.048 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |
| [[LINC01186]] | B | LINC01186 activity raises TLCD4-RWDD3's level | lines that do not express LINC01186 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without LINC01186 | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC01836, STXBP2, EEPD1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARD3B]] | B | TLCD4-RWDD3 activity raises PARD3B's level | lines that do not express TLCD4-RWDD3 (11) vs lines expressing it (39) | 3.94× lower at baseline in the lines without TLCD4-RWDD3 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[RASGRP1]] | B | [[TLCD4]], TLCD4-RWDD3 activity raises RASGRP1's level | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (39) | 2.08× lower at baseline in the lines without TLCD4, TLCD4-RWDD3 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |
| [[LGALSL-DT]] | B | TLCD4-RWDD3 activity raises LGALSL-DT's level | lines that do not express TLCD4-RWDD3 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without TLCD4-RWDD3 | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[PM20D2]] | B | TLCD4-RWDD3 activity raises PM20D2's level | lines that do not express TLCD4-RWDD3 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without TLCD4-RWDD3 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[DERA]] | B | [[TLCD4]], TLCD4-RWDD3 activity raises DERA's level | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (39) | 1.55× lower at baseline in the lines without TLCD4, TLCD4-RWDD3 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |
| cells under [[Digitoxin (drug)]] 5 µM | B | [[TLCD4]], TLCD4-RWDD3 activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (37) | the lines without TLCD4, TLCD4-RWDD3: 0.69× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.4, 13.6); signed map (19.9, -1.1). **Vector** length 37.3, 4.55% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.3 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -4.1 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -0.8 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.6 | -0.1 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -0.6 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | TLCD4-RWDD3 readthrough |
| Locus type | readthrough (other) |
| Location | 1p21.3 — chr1:95,117,923-95,247,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM56-RWDD3 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100527978](https://www.ncbi.nlm.nih.gov/gene/100527978):

> This locus represents naturally occurring read-through transcription between the neighboring TMEM56 (transmembrane protein 56) and RWDD3 (RWD domain containing 3) genes on chromosome 1. The read-through transcript encodes a protein that shares sequence identity with the upstream gene product, but it contains a distinct C-terminus due to frameshifts versus the downstream gene coding sequence. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:49388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49388) · Entrez [100527978](https://www.ncbi.nlm.nih.gov/gene/100527978) · Ensembl [ENSG00000271092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271092)

## Data

Gene col 15675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15675); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15675]; `tensor/DDL_lfc|DDL_z.npy` [15675]; `embed/gene_vectors.npy` [15675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15675 or target_col == 15675). Every well: [[TLCD4-RWDD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD4-RWDD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
