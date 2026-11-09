---
symbol: "LEF1-AS1"
type: "gene"
col: 13830
ensembl_id: "ENSG00000232021"
name: "LEF1 antisense RNA 1"
location: "4q25"
module: 87
arm: "+"
pooled_cpm: 3.47
n_lines_expressing: 17
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 20
direction_downstream: 26
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# LEF1-AS1

*LEF1 antisense RNA 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.2× (z +22.4, q 0e+00, up in 4 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 21 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (C32 0.0651×, SW480 0.0717×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (SW480 0.0355×, C32 0.0868×; ⚠ cell-cycle shift, explains ~62% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.0287×; ⚠ cell-cycle shift, explains ~22% of this change); [[c-Kit-IN-1 (drug)]] 0.5 µM in 1 line (SW 1088 0.407×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 0.0104×); [[Harringtonine (drug)]] 5 µM in 1 line (C32 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C10orf90]] (+0.83, fdr 7e-06), [[LEF1]] (+0.80, fdr 7e-06, ⚠ same locus), [[COL19A1]] (+0.79, fdr 7e-06), [[SAMMSON]] (+0.77, fdr 7e-06); moves opposite to [[DCT]] (-0.47, fdr 3e-05), [[TRIQK]] (-0.42, fdr 9e-05), [[LINC00698]] (-0.42, fdr 7e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 26 go from it, the strongest it → [[PARVG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.2×** | +22.4 | 0e+00 | 4/5 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.74×** | +9.8 | 3e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.90×** | +8.9 | 1e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.99×** | +8.7 | 4e-16 | 4/5 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.21×** | +7.1 | 2e-10 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.7 | 8e-07 | 1/12 (SW480) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +5.7 | 8e-07 | 2/5 (SW480, NCI-H460) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.8 | 1e-04 | 4/8 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.92×** | +4.3 | 0.001 | 1/5 (A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.46×** | +4.2 | 0.001 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.32×** | +3.9 | 0.005 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.7 | 0.009 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.96×** | +3.7 | 0.009 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.011 | 0/5 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.71×** | +3.5 | 0.018 | 1/6 (SK-MEL-2) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.031 | 3/10 (RKO, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.040 | 3/12 (A498, NCI-H23, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.090 | 0/12 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 21 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (C32 0.0651×, SW480 0.0717×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (SW480 0.0355×, C32 0.0868×; ⚠ cell-cycle shift, explains ~62% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.0287×; ⚠ cell-cycle shift, explains ~22% of this change); [[c-Kit-IN-1 (drug)]] 0.5 µM in 1 line (SW 1088 0.407×); [[PH-797804 (drug)]] 5 µM in 1 line (C32 0.0104×); [[Harringtonine (drug)]] 5 µM in 1 line (C32 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.602× | -3.1 | 0.78 | 4/12 (C32, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 132 | 0 | 25 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0287× (z -25.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0104× (z -11.9) |
| [[SW480 (line)]] | alt | 4.12 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.0355× (z -13.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A498 (line)]] | wt | 1.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.0× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 0.882 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0993× (z -9.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW 1088 (line)]] | alt | 1.69 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 0.5 µM 0.407× (z -12.1) |
| [[A-172 (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.633 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C10orf90]] | +0.83 | +0.74 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[LEF1]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[COL19A1]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SAMMSON]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[SOX10]] | +0.76 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[MIR3681HG]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FKBP9P1-1]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[LINC01812]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[A2M]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 |  |
| [[PTPRZ1]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[CD96]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[OPRD1]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RHOJ]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCT]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRIQK]] | -0.42 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[LINC00698]] | -0.42 | -0.57 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 2, C 18. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LEF1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NTRK2]] | B | NTRK2 activity raises LEF1-AS1's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without NTRK2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent |
| [[RHOJ]] | C | RHOJ activity raises LEF1-AS1's level | lines that do not express RHOJ (33) vs lines expressing it (17) | 1.84× lower at baseline in the lines without RHOJ | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000203434, TF, LINC02240; co-absent with the target |
| [[DCT]] | C | DCT activity raises LEF1-AS1's level | lines that do not express DCT (42) vs lines expressing it (8) | 3.69× lower at baseline in the lines without DCT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises LEF1-AS1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 5.26× lower at baseline in the lines without LHFPL3-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[LEF1]] | C | LEF1 activity raises LEF1-AS1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without LEF1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises LEF1-AS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without COL19A1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[PTPRZ1]] | C | PTPRZ1 activity raises LEF1-AS1's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 3.01× lower at baseline in the lines without PTPRZ1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |
| [[TYR]] | C | TYR activity raises LEF1-AS1's level | lines that do not express TYR (43) vs lines expressing it (7) | 4.46× lower at baseline in the lines without TYR | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, A2M, SOX10; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises LEF1-AS1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.80× lower at baseline in the lines without FKBP9P1-1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises LEF1-AS1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 2.13× lower at baseline in the lines without GJB1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[A2M]] | C | A2M activity raises LEF1-AS1's level | lines that do not express A2M (42) vs lines expressing it (8) | 3.62× lower at baseline in the lines without A2M | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 9, C 17. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVG]] | B | LEF1-AS1 activity raises PARVG's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.27× lower at baseline in the lines without LEF1-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[PARVB]] | B | LEF1-AS1 activity raises PARVB's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without LEF1-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[LINC02226]] | B | LEF1-AS1 activity raises LINC02226's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 1.85× lower at baseline in the lines without LEF1-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[ALK]] | B | LEF1-AS1 activity raises ALK's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without LEF1-AS1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| cells under [[Daptomycin (drug)]] 0.05 µM | B | LEF1-AS1 activity lowers the cells' numbers under Daptomycin 0.05 µM (makes them more sensitive) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 1.19× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; cell counts less trustworthy |
| cells under [[Peretinoin (drug)]] 5 µM | B | LEF1-AS1 activity lowers the cells' numbers under Peretinoin 5 µM (makes them more sensitive) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 1.21× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 5 µM | B | LEF1-AS1 activity raises the cells' numbers under Pyridoxine (hydrochloride) 5 µM (protects the cells) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 0.89× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[HPSE2]] | B | LEF1-AS1 activity raises HPSE2's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without LEF1-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| cells under [[Pasireotide (acetate) (drug)]] 5 µM | B | LEF1-AS1 activity lowers the cells' numbers under Pasireotide (acetate) 5 µM (makes them more sensitive) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 1.10× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[LEF1]] | C | LEF1-AS1 activity raises LEF1's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 5.22× lower at baseline in the lines without LEF1-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[DAAM2]] | C | LEF1-AS1 activity raises DAAM2's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 2.55× lower at baseline in the lines without LEF1-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[COL19A1]] | C | LEF1-AS1 activity raises COL19A1's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 3.38× lower at baseline in the lines without LEF1-AS1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.874). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.1, 28.8); signed map (28.9, 38.8). **Vector** length 51.6, 20.4% of its response variance represented; |z| ≥ 3 in 325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +22.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.9 |
|  | [[Oxaprozin (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +0.7 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | LEF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q25 — chr4:108,167,525-108,258,037 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40339) · Entrez [641518](https://www.ncbi.nlm.nih.gov/gene/641518) · Ensembl [ENSG00000232021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232021)

## Data

Gene col 13830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13830); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13830]; `tensor/DDL_lfc|DDL_z.npy` [13830]; `embed/gene_vectors.npy` [13830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13830 or target_col == 13830). Every well: [[LEF1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEF1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
