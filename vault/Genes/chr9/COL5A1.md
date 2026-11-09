---
symbol: "COL5A1"
type: "gene"
col: 5089
ensembl_id: "ENSG00000130635"
name: "collagen type V alpha 1 chain"
location: "9q34.3"
module: 13
arm: "+"
pooled_cpm: 164.33
n_lines_expressing: 20
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 77
direction_downstream: 87
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL5A1

*collagen type V alpha 1 chain* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +13.7, q 4e-40, up in 7 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.73× (z +5.3, q 2e-05, up in 2 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.360× (z -13.3, q 1e-37, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFRB]] (+0.79, fdr 7e-06), [[THBS2]] (+0.77, fdr 7e-06), [[COL6A3]] (+0.76, fdr 7e-06); moves opposite to [[SRGN]] (-0.51, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 77 arrows point to it, the strongest [[RNF152]] → it (grade B ⚠); 87 go from it, the strongest it → [[SLC6A6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +13.7 | 4e-40 | 7/19 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +11.8 | 1e-29 | 8/16 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +9.2 | 1e-17 | 6/16 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +5.3 | 2e-05 | 2/18 (AN3 CA, SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 2/18 (PANC-1, SNU-423) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.6 | 0.029 | 0/18 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.047 | 0/18 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.26× | +3.2 | 0.11 | 5/18 (CHP-212, SW 900, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.11 | 0/20 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.360×** | -13.3 | 1e-37 | 18/18 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.570×** | -10.8 | 2e-24 | 16/18 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.505×** | -9.2 | 4e-18 | 17/18 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.524×** | -8.7 | 3e-16 | 15/18 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -6.6 | 6e-09 | 16/18 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.663×** | -5.5 | 3e-06 | 5/17 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.683×** | -5.1 | 2e-05 | 17/18 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.691×** | -5.0 | 4e-05 | 16/18 (J82, HOP62, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.710×** | -4.4 | 7e-04 | 0/18 | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.724×** | -4.4 | 7e-04 | 17/18 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.762×** | -3.7 | 0.012 | 12/18 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.752×** | -3.6 | 0.013 | 0/18 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.753×** | -3.5 | 0.017 | 0/18 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.834× | -3.5 | 0.021 | 17/18 (SW 1088, A498, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.3 | 0.031 | 10/18 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Tazarotene (drug)]] 5 µM |  | **0.790×** | -3.2 | 0.050 | 14/18 (NCI-H1792, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,342 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -22.3) |
| [[J82 (line)]] | alt | 608 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.3) |
| [[H4 (line)]] | wt | 620 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 742 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.2) |
| [[A-172 (line)]] | wt | 1,122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.8) |
| [[Hs 766T (line)]] | wt | 100 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -18.9) |
| [[HS-578T (line)]] | alt | 894 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 54.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.6) |
| [[SW 1088 (line)]] | alt | 913 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.2) |
| [[PANC-1 (line)]] | alt | 50.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.7) |
| [[SNU-423 (line)]] | alt | 432 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.0) |
| [[SW 900 (line)]] | alt | 71.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.6) |
| [[A-427 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 237 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 95.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.70 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 291 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.96 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 36.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFRB]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 406 |
| [[THBS2]] | +0.77 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 742 |
| [[COL6A3]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 892 |
| [[DENND2A]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GPR173]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[DKK3]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NAV1]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SEMA5A]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SARDH]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[CARMN]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 2, C 75. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF152]] | B | RNF152 activity raises COL5A1's level | lines that do not express RNF152 (18) vs lines expressing it (32) | 4.11× lower at baseline in the lines without RNF152 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, SNCAIP, OR9Q1; maybe low, not absent |
| [[EML1]] | B | EML1 activity raises COL5A1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 6.17× lower at baseline in the lines without EML1 | 0.086 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |
| [[PDGFRB]] | C | PDGFRB activity raises COL5A1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 17.92× lower at baseline in the lines without PDGFRB | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises COL5A1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 11.52× lower at baseline in the lines without DKK3 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises COL5A1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 20.07× lower at baseline in the lines without LINC01411 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises COL5A1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 15.17× lower at baseline in the lines without ITGA11 | 0.001 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises COL5A1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 12.04× lower at baseline in the lines without INSYN2B | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises COL5A1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 7.31× lower at baseline in the lines without ADAMTS6 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises COL5A1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 12.51× lower at baseline in the lines without ADAMTS12 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises COL5A1's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 11.18× lower at baseline in the lines without LINC01615 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises COL5A1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 9.79× lower at baseline in the lines without PTGFR | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises COL5A1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 8.98× lower at baseline in the lines without COL7A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*87 arrows, 87 of them with an alert ⚠; grade A 0, B 20, C 67. Shown: the 12 strongest; 75 more arrows (75 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A6]] | B | COL5A1 activity raises SLC6A6's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without COL5A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[PRSS23]] | B | COL5A1 activity raises PRSS23's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.18× lower at baseline in the lines without COL5A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[TMEM92-AS1]] | B | COL5A1 activity raises TMEM92-AS1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without COL5A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[LINC01119]] | B | COL5A1 activity raises LINC01119's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without COL5A1 | 0.026 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[EVC]] | B | COL5A1 activity raises EVC's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.63× lower at baseline in the lines without COL5A1 | 0.028 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[C14orf132]] | B | COL5A1 activity raises C14orf132's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.89× lower at baseline in the lines without COL5A1 | 0.038 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[B3GNT9]] | B | COL5A1 activity raises B3GNT9's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without COL5A1 | 0.045 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[ANXA6]] | B | COL5A1 activity raises ANXA6's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.84× lower at baseline in the lines without COL5A1 | 0.050 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[RAI14]] | B | COL5A1 activity raises RAI14's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without COL5A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[TGFB1I1]] | B | COL5A1 activity raises TGFB1I1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without COL5A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[MXRA7]] | B | COL5A1 activity raises MXRA7's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without COL5A1 | 0.065 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[P3H1]] | B | COL5A1 activity raises P3H1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without COL5A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.1, 18.0); signed map (25.1, 46.4). **Vector** length 93.0, 39.8% of its response variance represented; |z| ≥ 3 in 587 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective B3GALTL causes PpS* (reactome, mean cos +0.56 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.56 to 8); *Diseases of glycosylation* (reactome, mean cos +0.54 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +0.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.3 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -13.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | collagen type V alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:134,641,803-134,844,843 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibrillar collagens |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 30 pathways, smallest: Fibronectin matrix formation; Attachment of bacteria to epithelial cells; Biofilm formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P20908](https://www.uniprot.org/uniprotkb/P20908) (Collagen alpha-1(V) chain):

> Type V collagen is a member of group I collagen (fibrillar forming collagen). It is a minor connective tissue component of nearly ubiquitous distribution. Type V collagen binds to DNA, heparan sulfate, thrombospondin, heparin, and insulin.

**Summary**, from NCBI Gene [1289](https://www.ncbi.nlm.nih.gov/gene/1289):

> This gene encodes an alpha chain for one of the low abundance fibrillar collagens. Fibrillar collagen molecules are trimers that can be composed of one or more types of alpha chains. Type V collagen is found in tissues containing type I collagen and appears to regulate the assembly of heterotypic fibers composed of both type I and type V collagen. This gene product is closely related to type XI collagen and it is possible that the collagen chains of types V and XI constitute a single collagen …

**Accessions** — [HGNC:2209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2209) · Entrez [1289](https://www.ncbi.nlm.nih.gov/gene/1289) · UniProt [P20908](https://www.uniprot.org/uniprotkb/P20908) · Ensembl [ENSG00000130635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130635)

## Data

Gene col 5089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5089); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5089]; `tensor/DDL_lfc|DDL_z.npy` [5089]; `embed/gene_vectors.npy` [5089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5089 or target_col == 5089). Every well: [[COL5A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL5A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
