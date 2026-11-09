---
symbol: "SYNDIG1"
type: "gene"
col: 2144
ensembl_id: "ENSG00000101463"
name: "synapse differentiation inducing 1"
location: "20p11.21"
module: 13
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 18
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 22
direction_downstream: 41
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SYNDIG1

*synapse differentiation inducing 1* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.56× (z +14.7, q 0e+00, up in 5 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.587× (z -4.1, q 0.028, down in 5 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 0.00919×, RPMI-7951 0.0570×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.0902×, HS-578T 0.0793×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0902×, HS-578T 0.129×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0400×, HS-578T 0.0625×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA11]] (+0.79, fdr 7e-06), [[GDNF-AS1]] (+0.78, fdr 7e-06), [[APCDD1L]] (+0.76, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[ITGA11]] → it (grade C ⚠); 41 go from it, the strongest it → [[LRIG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +14.7 | 0e+00 | 5/11 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +8.9 | 1e-16 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +8.6 | 1e-15 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.87×** | +8.6 | 1e-15 | 1/8 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.06×** | +8.4 | 7e-15 | 7/14 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +5.9 | 3e-07 | 3/11 (A549, A498, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.7 | 2e-04 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.4 | 9e-04 | 1/7 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.002 | 3/10 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +3.6 | 0.021 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.54×** | +3.5 | 0.023 | 1/12 (NCI-H23) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.3 | 0.051 | 1/7 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.051 | 0/9 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +3.2 | 0.052 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.2 | 0.052 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.054 | 0/9 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.065 | 2/14 (A549, BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.075 | 4/14 (BT-474, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.48×** | +2.9 | 0.090 | 1/12 (HOP62) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +2.9 | 0.096 | 1/14 (NCI-H1573) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2144.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (HS-578T 0.00919×, RPMI-7951 0.0570×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.0902×, HS-578T 0.0793×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0902×, HS-578T 0.129×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RPMI-7951 0.0400×, HS-578T 0.0625×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.587×** | -4.1 | 0.028 | 5/14 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.626× | -3.6 | 0.10 | 0/14 | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.667× | -3.3 | 0.15 | 4/14 (HOP62, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 35.2 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00919× (z -20.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -18.1) |
| [[A549 (line)]] | wt | 9.17 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.92 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0376× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 5.59 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0320× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.714 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.713 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA11]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GDNF-AS1]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCNK3]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[VSTM4]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS14]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GDNF]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GPR68]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GPR173]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[FAM167A]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA11]] | C | ITGA11 activity raises SYNDIG1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without ITGA11 | 0.018 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises SYNDIG1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 4.08× lower at baseline in the lines without LINC01411 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises SYNDIG1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.15× lower at baseline in the lines without PDGFRB | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[AK5]] | C | AK5 activity raises SYNDIG1's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without AK5 | 0.039 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises SYNDIG1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.51× lower at baseline in the lines without DKK3 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises SYNDIG1's level | lines that do not express SRGN (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without SRGN | 0.046 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[GLYATL2]] | C | GLYATL2 activity raises SYNDIG1's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 3.42× lower at baseline in the lines without GLYATL2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises SYNDIG1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.95× lower at baseline in the lines without ADAMTS12 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[IL33]] | C | IL33 activity raises SYNDIG1's level | lines that do not express IL33 (35) vs lines expressing it (15) | 2.96× lower at baseline in the lines without IL33 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises SYNDIG1's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without NAV1 | 0.053 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises SYNDIG1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.30× lower at baseline in the lines without COL5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises SYNDIG1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without COL7A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 6, C 35. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRIG1]] | B | SYNDIG1 activity raises LRIG1's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without SYNDIG1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[LINC01119]] | B | SYNDIG1 activity raises LINC01119's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.17× lower at baseline in the lines without SYNDIG1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[RNF152]] | B | SYNDIG1 activity raises RNF152's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.73× lower at baseline in the lines without SYNDIG1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[ARHGAP22]] | B | SYNDIG1 activity strengthens ARHGAP22's drug response | lines that do not express SYNDIG1 (14) vs lines expressing it (13) | the lines without SYNDIG1 respond 0.79× as strongly (z diff +1.75); strongest at Panobinostat 5 µM: 0.47x vs 0.24x (z diff +4.6) | 0.049 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; target measured in part of the lines; artifact flags |
| [[FAM167A]] | B | SYNDIG1 activity raises FAM167A's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without SYNDIG1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[TMEM92-AS1]] | B | SYNDIG1 activity raises TMEM92-AS1's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.56× lower at baseline in the lines without SYNDIG1 | 0.069 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1 |
| [[NTF3]] | C | SYNDIG1 activity raises NTF3's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.73× lower at baseline in the lines without SYNDIG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[ITGA11]] | C | SYNDIG1 activity raises ITGA11's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 5.55× lower at baseline in the lines without SYNDIG1 | 0.015 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[APCDD1L-DT]] | C | SYNDIG1 activity raises APCDD1L-DT's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 4.36× lower at baseline in the lines without SYNDIG1 | 0.015 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[OR9Q1]] | C | SYNDIG1 activity raises OR9Q1's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.61× lower at baseline in the lines without SYNDIG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[LINC01411]] | C | SYNDIG1 activity raises LINC01411's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 7.70× lower at baseline in the lines without SYNDIG1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[APCDD1L]] | C | SYNDIG1 activity raises APCDD1L's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.61× lower at baseline in the lines without SYNDIG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.817). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.4, 16.3); signed map (23.8, 47.2). **Vector** length 50.2, 15.4% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen formation* (reactome, mean cos +0.51 to 12); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.50 to 10); *Defective B3GALTL causes PpS* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | synapse differentiation inducing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:24,469,629-24,666,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14220, IFITMD5, DSPC2; previously C20orf39, TMEM90B |
| Gene groups (HGNC) | Dispanins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7V2](https://www.uniprot.org/uniprotkb/Q9H7V2) (Synapse differentiation-inducing gene protein 1):

> May regulate AMPA receptor content at nascent synapses, and have a role in postsynaptic development and maturation.

**Summary**, from NCBI Gene [79953](https://www.ncbi.nlm.nih.gov/gene/79953):

> This gene encodes a protein that belongs to the interferon-induced transmembrane family of proteins. A similar protein in rat is thought to regulate the development of excitatory synapses. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:15885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15885) · Entrez [79953](https://www.ncbi.nlm.nih.gov/gene/79953) · UniProt [Q9H7V2](https://www.uniprot.org/uniprotkb/Q9H7V2) · Ensembl [ENSG00000101463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101463)

## Data

Gene col 2144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2144); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2144]; `tensor/DDL_lfc|DDL_z.npy` [2144]; `embed/gene_vectors.npy` [2144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2144 or target_col == 2144). Every well: [[SYNDIG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNDIG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
