---
symbol: "CARMN"
type: "gene"
col: 14626
ensembl_id: "ENSG00000249669"
name: "cardiac mesoderm enhancer-associated non-coding RNA"
location: "5q32"
module: 13
arm: "+"
pooled_cpm: 8.12
n_lines_expressing: 10
n_dd_up: 3
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 37
direction_downstream: 53
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CARMN

*cardiac mesoderm enhancer-associated non-coding RNA* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.97× (z +8.1, q 4e-13, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.402× (z -5.1, q 2e-04, down in 6 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (HS-578T 0.0225×, hTERT-HPNE 0.0304×, RPMI-7951 0.0104×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (hTERT-HPNE 0.0581×, HS-578T 0.0752×, RPMI-7951 0.0204×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0168×, HS-578T 0.0313×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 0.00756×, hTERT-HPNE 0.0184×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFRB]] (+0.78, fdr 7e-06), [[LINC01615]] (+0.71, fdr 7e-06), [[APCDD1L]] (+0.69, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[IHO1]] → it (grade C ⚠); 53 go from it, the strongest it → [[DIRC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.97×** | +8.1 | 4e-13 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.98×** | +7.8 | 2e-12 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +5.3 | 2e-05 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14626.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (HS-578T 0.0225×, hTERT-HPNE 0.0304×, RPMI-7951 0.0104×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (hTERT-HPNE 0.0581×, HS-578T 0.0752×, RPMI-7951 0.0204×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0168×, HS-578T 0.0313×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 0.00756×, hTERT-HPNE 0.0184×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.402×** | -5.1 | 2e-04 | 6/6 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.521×** | -3.8 | 0.038 | 7/7 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.682× | -3.2 | 0.28 | 0/7 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 234 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0313× (z -18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.00756× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0168× (z -20.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0184× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0256× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0377× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0104× (z -10.9) |
| [[A-172 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.585 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFRB]] | +0.78 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.71 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[COL5A1]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LINC02109]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PTGFR]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SEMA5A]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PRRX1]] | +0.66 | +0.58 / +0.66 | both halves | 8e-06 | **novel candidate** |
| [[GPR173]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FBN1]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[LINC01411]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ARMCX2]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 0, C 37. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IHO1]] | C | IHO1 activity raises CARMN's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.77× lower at baseline in the lines without IHO1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[DIRAS3]] | C | DIRAS3 activity raises CARMN's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.48× lower at baseline in the lines without DIRAS3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[SLC24A3]] | C | SLC24A3 activity raises CARMN's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 2.07× lower at baseline in the lines without SLC24A3 | 0.009 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises CARMN's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.41× lower at baseline in the lines without AEBP1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[GDNF-AS1]] | C | GDNF-AS1 activity raises CARMN's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.56× lower at baseline in the lines without GDNF-AS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises CARMN's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 3.59× lower at baseline in the lines without COL3A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises CARMN's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.29× lower at baseline in the lines without PDGFRB | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[LINC02109]] | C | LINC02109 activity raises CARMN's level | lines that do not express LINC02109 (40) vs lines expressing it (10) | 4.57× lower at baseline in the lines without LINC02109 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287474, ENSG00000253642, LINC00879; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises CARMN's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.27× lower at baseline in the lines without HTR1F | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises CARMN's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.14× lower at baseline in the lines without ADAMTS2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises CARMN's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.54× lower at baseline in the lines without COL1A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises CARMN's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.62× lower at baseline in the lines without ITGA11 | 0.042 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 6, C 47. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | CARMN activity raises DIRC3's level | lines that do not express CARMN (40) vs lines expressing it (10) | 5.70× lower at baseline in the lines without CARMN | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[LDB2]] | B | CARMN activity raises LDB2's level | lines that do not express CARMN (40) vs lines expressing it (10) | 4.75× lower at baseline in the lines without CARMN | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[SOCS5]] | B | CARMN activity raises SOCS5's level | lines that do not express CARMN (40) vs lines expressing it (10) | 1.79× lower at baseline in the lines without CARMN | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[RNF152]] | B | CARMN activity raises RNF152's level | lines that do not express CARMN (40) vs lines expressing it (10) | 3.66× lower at baseline in the lines without CARMN | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[LINC01119]] | B | CARMN activity raises LINC01119's level | lines that do not express CARMN (40) vs lines expressing it (10) | 2.53× lower at baseline in the lines without CARMN | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[SYTL3]] | B | CARMN activity raises SYTL3's level | lines that do not express CARMN (40) vs lines expressing it (10) | 2.95× lower at baseline in the lines without CARMN | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN |
| [[PDGFRB]] | C | CARMN activity raises PDGFRB's level | lines that do not express CARMN (40) vs lines expressing it (10) | 17.21× lower at baseline in the lines without CARMN | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[ITGA11]] | C | CARMN activity raises ITGA11's level | lines that do not express CARMN (40) vs lines expressing it (10) | 12.81× lower at baseline in the lines without CARMN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[TNS1]] | C | CARMN activity raises TNS1's level | lines that do not express CARMN (40) vs lines expressing it (10) | 5.86× lower at baseline in the lines without CARMN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[WNT5A]] | C | CARMN activity raises WNT5A's level | lines that do not express CARMN (40) vs lines expressing it (10) | 14.39× lower at baseline in the lines without CARMN | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[AEBP1]] | C | CARMN activity raises AEBP1's level | lines that do not express CARMN (40) vs lines expressing it (10) | 4.57× lower at baseline in the lines without CARMN | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[TGFBI]] | C | CARMN activity raises TGFBI's level | lines that do not express CARMN (40) vs lines expressing it (10) | 8.48× lower at baseline in the lines without CARMN | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.7, 18.6); signed map (25.7, 46.4). **Vector** length 47.6, 23.9% of its response variance represented; |z| ≥ 3 in 254 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.53 to 9); *Collagen chain trimerization* (reactome, mean cos +0.51 to 7); *NCAM1 interactions* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | -0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.8 | +0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cardiac mesoderm enhancer-associated non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q32 — chr5:149,406,689-149,432,835 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CARMEN; previously MIR143HG |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [728264](https://www.ncbi.nlm.nih.gov/gene/728264):

> Acts upstream of or within cardiac muscle cell differentiation. Predicted to be part of RISC complex. Biomarker of atherosclerosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:42872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42872) · Entrez [728264](https://www.ncbi.nlm.nih.gov/gene/728264) · Ensembl [ENSG00000249669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249669)

## Data

Gene col 14626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14626); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14626]; `tensor/DDL_lfc|DDL_z.npy` [14626]; `embed/gene_vectors.npy` [14626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14626 or target_col == 14626). Every well: [[CARMN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARMN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
