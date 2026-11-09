---
symbol: "PRRX1"
type: "gene"
col: 3764
ensembl_id: "ENSG00000116132"
name: "paired related homeobox 1"
location: "1q24.2"
module: 13
arm: "+"
pooled_cpm: 16.42
n_lines_expressing: 16
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 47
direction_downstream: 40
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PRRX1

*paired related homeobox 1* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +8.3, q 6e-14, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.55× (z +3.8, q 0.025, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.454× (z -7.1, q 9e-10, down in 12 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 6 lines (NCI-H1792 0.104×, hTERT-HPNE 0.0662×, C32 0.108×, A-172 0.125×, …); [[Panobinostat (drug)]] 5 µM in 5 lines (hTERT-HPNE 0.0328×, C32 0.0570×, NCI-H1792 0.0763×, HS-578T 0.0632×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H1792 0.199×, hTERT-HPNE 0.179×, C32 0.232×, HS-578T 0.256×, …); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.151×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTHRC1]] (+0.70, fdr 7e-06), [[CARMN]] (+0.66, fdr 8e-06), [[APCDD1L]] (+0.65, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 40 go from it, the strongest it → [[ABCA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +8.3 | 6e-14 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +6.8 | 3e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.025 | 6/14 (RPMI-7951, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.025 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +3.6 | 0.035 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD-7648 (drug)]] 0.5 µM |  | 1.63× | +3.2 | 0.15 | 0/13 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.16 | 1/12 (RPMI-7951) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.61× | +3.0 | 0.16 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3764.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 6 lines (NCI-H1792 0.104×, hTERT-HPNE 0.0662×, C32 0.108×, A-172 0.125×, …); [[Panobinostat (drug)]] 5 µM in 5 lines (hTERT-HPNE 0.0328×, C32 0.0570×, NCI-H1792 0.0763×, HS-578T 0.0632×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H1792 0.199×, hTERT-HPNE 0.179×, C32 0.232×, HS-578T 0.256×, …); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.151×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -7.1 | 9e-10 | 12/14 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.499×** | -6.2 | 2e-07 | 13/14 (hTERT-HPNE, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.536×** | -5.6 | 4e-06 | 13/13 (hTERT-HPNE, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -3.6 | 0.054 | 12/14 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 75.7 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0570× (z -16.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.108× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 276 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0328× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0662× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0763× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 71.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.185× (z -9.8) |
| [[HS-578T (line)]] | alt | 151 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0632× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.119× (z -11.5) |
| [[A-172 (line)]] | wt | 81.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.125× (z -12.6) |
| [[CHP-212 (line)]] | wt | 82.3 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.114× (z -8.7) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTHRC1]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CARMN]] | +0.66 | +0.58 / +0.66 | both halves | 8e-06 | **novel candidate** |
| [[APCDD1L]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[LOXL3]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[FRMD4A]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[EDNRA]] | +0.64 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[KC6]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ZNF521]] | +0.63 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[EVC2]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[NAV1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MAGI2]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[HS3ST3A1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 3, C 44. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers PRRX1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 12.90× higher at baseline in the lines without NOXA1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PRRX1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PATJ]] | B | PATJ activity lowers PRRX1's level | lines that do not express PATJ (9) vs lines expressing it (41) | 11.22× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[AEBP1]] | C | AEBP1 activity raises PRRX1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 12.49× lower at baseline in the lines without AEBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises PRRX1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 4.30× lower at baseline in the lines without FBN1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises PRRX1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 6.27× lower at baseline in the lines without INSYN2B | 0.008 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises PRRX1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 5.83× lower at baseline in the lines without COL1A2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises PRRX1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 5.99× lower at baseline in the lines without GYPC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[ADAMTS14]] | C | ADAMTS14 activity raises PRRX1's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 4.17× lower at baseline in the lines without ADAMTS14 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises PRRX1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 6.44× lower at baseline in the lines without LINC01411 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises PRRX1's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 4.23× lower at baseline in the lines without LINC01687 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises PRRX1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.81× lower at baseline in the lines without WNT5A | 0.009 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 3, C 37. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA1]] | B | PRRX1 activity raises ABCA1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without PRRX1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN |
| [[IPO9-AS1]] | B | PRRX1 activity raises IPO9-AS1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 1.51× lower at baseline in the lines without PRRX1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN |
| [[NAV1]] | B | PRRX1 activity raises NAV1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without PRRX1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN |
| [[COL1A2]] | C | PRRX1 activity raises COL1A2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 7.88× lower at baseline in the lines without PRRX1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[ADAMTS14]] | C | PRRX1 activity raises ADAMTS14's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without PRRX1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[FBN1]] | C | PRRX1 activity raises FBN1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 5.50× lower at baseline in the lines without PRRX1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[EDNRA]] | C | PRRX1 activity raises EDNRA's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.66× lower at baseline in the lines without PRRX1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[ZEB2]] | C | PRRX1 activity raises ZEB2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 5.81× lower at baseline in the lines without PRRX1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[ADAMTS12]] | C | PRRX1 activity raises ADAMTS12's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.51× lower at baseline in the lines without PRRX1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[PDGFRA]] | C | PRRX1 activity raises PDGFRA's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.87× lower at baseline in the lines without PRRX1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[INSYN2B]] | C | PRRX1 activity raises INSYN2B's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 4.39× lower at baseline in the lines without PRRX1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[AK5]] | C | PRRX1 activity raises AK5's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.79× lower at baseline in the lines without PRRX1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.7, 18.6); signed map (26.2, 47.1). **Vector** length 55.2, 19.9% of its response variance represented; |z| ≥ 3 in 372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +0.5 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | paired related homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:170,662,728-170,739,421 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHOX1; previously PMX1 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Hallmark sets | KRAS_SIGNALING_UP, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P54821](https://www.uniprot.org/uniprotkb/P54821) (Paired mesoderm homeobox protein 1):

> Master transcription factor of stromal fibroblasts for myofibroblastic lineage progression. Orchestrates the functional drift of fibroblasts into myofibroblastic phenotype via TGF-beta signaling by remodeling a super-enhancer landscape. Through this function, plays an essential role in wound healing process. Acts as a transcriptional regulator of muscle creatine kinase (MCK) and so has a role in the establishment of diverse mesodermal muscle types. The protein binds to an A/T-rich element in …

**Summary**, from NCBI Gene [5396](https://www.ncbi.nlm.nih.gov/gene/5396):

> The DNA-associated protein encoded by this gene is a member of the paired family of homeobox proteins localized to the nucleus. The protein functions as a transcription co-activator, enhancing the DNA-binding activity of serum response factor, a protein required for the induction of genes by growth and differentiation factors. The protein regulates muscle creatine kinase, indicating a role in the establishment of diverse mesodermal muscle types. Alternative splicing yields two isoforms that …

**Accessions** — [HGNC:9142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9142) · Entrez [5396](https://www.ncbi.nlm.nih.gov/gene/5396) · UniProt [P54821](https://www.uniprot.org/uniprotkb/P54821) · Ensembl [ENSG00000116132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116132)

## Data

Gene col 3764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3764); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3764]; `tensor/DDL_lfc|DDL_z.npy` [3764]; `embed/gene_vectors.npy` [3764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3764 or target_col == 3764). Every well: [[PRRX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
