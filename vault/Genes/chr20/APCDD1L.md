---
symbol: "APCDD1L"
type: "gene"
col: 12672
ensembl_id: "ENSG00000198768"
name: "APC down-regulated 1 like"
location: "20q13.32"
module: 13
arm: "+"
pooled_cpm: 13.9
n_lines_expressing: 16
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 85
direction_downstream: 101
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# APCDD1L

*APC down-regulated 1 like* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.34× (z +11.1, q 6e-26, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.19× (z +7.2, q 1e-10, up in 8 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.560× (z -5.3, q 5e-05, down in 12 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1L-DT]] (+0.85, fdr 7e-06, ⚠ same locus), [[NAV1]] (+0.78, fdr 7e-06), [[ITGA11]] (+0.78, fdr 7e-06), [[LINC01615]] (+0.78, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 85 arrows point to it, the strongest [[NEBL]] → it (grade B ⚠); 101 go from it, the strongest it → [[TMEM92-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.1 | 6e-26 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +10.9 | 2e-25 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +7.2 | 1e-10 | 8/13 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.1 | 5e-05 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.9 | 9e-05 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.9 | 0.010 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.26× | +3.0 | 0.17 | 4/14 (NCI-H1573, H4, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.43× | +3.0 | 0.17 | 0/12 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.560×** | -5.3 | 5e-05 | 12/13 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -4.3 | 0.005 | 13/13 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -4.2 | 0.005 | 11/13 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.669×** | -3.7 | 0.031 | 9/13 (RPMI-7951, HOP62, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.681×** | -3.5 | 0.047 | 10/13 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.507×** | -3.3 | 0.090 | 4/11 (RPMI-7951, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.701×** | -3.3 | 0.090 | 11/13 (HOP62, RPMI-7951, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.2 | 0.096 | 8/13 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.697× | -3.1 | 0.11 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 425 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -14.6) |
| [[HOP62 (line)]] | alt | 97.9 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -10.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -9.8) |
| [[H4 (line)]] | wt | 11.8 | 0 | 3 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0617× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0713× (z -9.8) |
| [[J82 (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.128× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0442× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -11.6) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0581× (z -9.8) |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -9.8) |
| [[A-172 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1L-DT]] | +0.85 | +0.79 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NAV1]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.78 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.78 | +0.80 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SYNDIG1]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[COL5A1]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PDGFRB]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[DENND2A]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SPOCD1]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[COL6A3]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CARMN]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*85 arrows, 85 of them with an alert ⚠; grade A 0, B 2, C 83. Shown: the 12 strongest; 73 more arrows (73 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEBL]] | B | NEBL activity lowers APCDD1L's level | lines that do not express NEBL (17) vs lines expressing it (33) | 2.79× higher at baseline in the lines without NEBL | 0.089 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |
| [[HDAC6]] | B | HDAC6 activity raises APCDD1L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDGFRB]] | C | PDGFRB activity raises APCDD1L's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 5.93× lower at baseline in the lines without PDGFRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises APCDD1L's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 6.87× lower at baseline in the lines without LINC01411 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises APCDD1L's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 6.81× lower at baseline in the lines without LINC01615 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises APCDD1L's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 5.44× lower at baseline in the lines without CDH13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises APCDD1L's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 5.03× lower at baseline in the lines without ITGA4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises APCDD1L's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.01× lower at baseline in the lines without COL5A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises APCDD1L's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.17× lower at baseline in the lines without WNT5A | 0.006 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises APCDD1L's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.87× lower at baseline in the lines without ADAMTS12 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises APCDD1L's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 5.30× lower at baseline in the lines without ITGA11 | 0.006 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises APCDD1L's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.98× lower at baseline in the lines without COL1A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |

### Downstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 16, C 85. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | APCDD1L activity raises TMEM92-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without APCDD1L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[C2orf92]] | B | APCDD1L activity raises C2orf92's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without APCDD1L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[IPO9-AS1]] | B | APCDD1L activity raises IPO9-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 1.85× lower at baseline in the lines without APCDD1L | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[GPR68]] | B | APCDD1L activity raises GPR68's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without APCDD1L | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[LOXL1]] | B | APCDD1L activity raises LOXL1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without APCDD1L | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[ARHGAP22]] | B | APCDD1L activity raises ARHGAP22's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.24× lower at baseline in the lines without APCDD1L | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[THBS2-AS1]] | B | APCDD1L activity raises THBS2-AS1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without APCDD1L | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[EVC]] | B | APCDD1L activity raises EVC's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.70× lower at baseline in the lines without APCDD1L | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[SYTL3]] | B | APCDD1L activity raises SYTL3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without APCDD1L | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[FAM167A]] | B | APCDD1L activity raises FAM167A's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without APCDD1L | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[MSC-AS1]] | B | APCDD1L activity strengthens MSC-AS1's drug response | lines that do not express APCDD1L (7) vs lines expressing it (16) | the lines without APCDD1L respond 1.00× as strongly (z diff +0.22); strongest at Panobinostat 5 µM: 0.42x vs 0.21x (z diff +4.0) | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; target measured in part of the lines; artifact flags |
| [[MANCR]] | B | APCDD1L activity raises MANCR's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without APCDD1L | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.907). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.2, 17.3); signed map (24.5, 46.7). **Vector** length 63.8, 27.9% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *epithelial mesenchymal transition* (hallmark, mean cos +0.53 to 29); *Extracellular matrix organization* (reactome, mean cos +0.56 to 22); *Collagen formation* (reactome, mean cos +0.57 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | APC down-regulated 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,459,101-58,515,399 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90166 |
| Matched by | ensembl_id |

UniProt [Q8NCL9](https://www.uniprot.org/uniprotkb/Q8NCL9) carries no function annotation.

**Summary**, from NCBI Gene [164284](https://www.ncbi.nlm.nih.gov/gene/164284):

> Predicted to enable Wnt-protein binding activity. Predicted to be involved in negative regulation of Wnt signaling pathway. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26892) · Entrez [164284](https://www.ncbi.nlm.nih.gov/gene/164284) · UniProt [Q8NCL9](https://www.uniprot.org/uniprotkb/Q8NCL9) · Ensembl [ENSG00000198768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198768)

## Data

Gene col 12672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12672); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12672]; `tensor/DDL_lfc|DDL_z.npy` [12672]; `embed/gene_vectors.npy` [12672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12672 or target_col == 12672). Every well: [[APCDD1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APCDD1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
