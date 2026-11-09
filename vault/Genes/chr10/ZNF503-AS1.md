---
symbol: "ZNF503-AS1"
type: "gene"
col: 13507
ensembl_id: "ENSG00000226051"
name: "ZNF503 antisense RNA 1"
location: "10q22.2"
module: 55
arm: "+"
pooled_cpm: 5.35
n_lines_expressing: 30
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 44
direction_downstream: 38
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# ZNF503-AS1

*ZNF503 antisense RNA 1* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.17× (z +33.2, q 0e+00, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.455× (z -8.4, q 4e-14, down in 16 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYK]] (+0.75, fdr 7e-06), [[LINC01819]] (+0.73, fdr 7e-06), [[TPRXL]] (+0.71, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[LINC03040]] → it (grade B ⚠); 38 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.17×** | +33.2 | 0e+00 | 13/20 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.9 | 4e-25 | 1/6 (SW480) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +10.7 | 3e-24 | 6/21 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +10.3 | 1e-22 | 1/9 (SW480) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.6 | 7e-20 | 2/10 (NCI-H2347, A498) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.6 | 6e-16 | 5/26 (A498, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +8.0 | 9e-14 | 4/21 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.4 | 1e-08 | 3/17 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +6.3 | 2e-08 | 4/24 (SK-MEL-2, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.8 | 4e-07 | 1/14 (A498) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +5.0 | 3e-05 | 4/25 (AN3 CA, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.9 | 4e-05 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 3e-04 | 10/23 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 1e-03 | 0/19 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +3.9 | 0.003 | 4/26 (KATO III, SW1417, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.008 | 7/26 (SW1417, COLO 205, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.015 | 5/23 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.019 | 1/23 (A498) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.024 | 2/14 (RPMI-7951, LOX-IMVI) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.032 | 1/21 (NCI-H2030) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.455×** | -8.4 | 4e-14 | 16/24 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -4.8 | 5e-04 | 10/27 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -4.4 | 0.002 | 18/23 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.657×** | -4.3 | 0.002 | 11/24 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -3.6 | 0.035 | 12/16 (LoVo, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ciclopirox (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.035 | 5/24 (KATO III, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.659×** | -3.3 | 0.066 | 9/22 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.754× | -3.0 | 0.16 | 4/25 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.754× | -3.0 | 0.16 | 2/26 (AN3 CA, HepG2/C3A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 49.9 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0760× (z -20.5) |
| [[KATO III (line)]] | alt | 21.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0686× (z -22.2) |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -15.7) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.119× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -11.8) |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0827× (z -12.2) |
| [[A498 (line)]] | wt | 1.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.3× (z +13.7) | — |
| [[A549 (line)]] | wt | 1.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.46× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0834× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 1.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYK]] | +0.75 | +0.69 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.73 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ABO]] | +0.71 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PROM1]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TSPOAP1]] | +0.70 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[GPX2]] | +0.69 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[KCNE3]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[BCAR3-AS1]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 | same gene group |
| [[NCALD]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC02331]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[NPSR1-AS1]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 33, C 11. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03040]] | B | LINC03040 activity raises ZNF503-AS1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without LINC03040 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[GALNT5]] | B | GALNT5 activity raises ZNF503-AS1's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without GALNT5 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[HPGD]] | B | HPGD activity raises ZNF503-AS1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without HPGD | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5 |
| [[TPRXL]] | B | TPRXL activity raises ZNF503-AS1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without TPRXL | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises ZNF503-AS1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without LINC01814 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[GPX2]] | B | GPX2 activity raises ZNF503-AS1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.00× lower at baseline in the lines without GPX2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31 |
| [[ABO]] | B | ABO activity raises ZNF503-AS1's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without ABO | 0.023 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[TMPRSS2]] | B | TMPRSS2 activity raises ZNF503-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.63× lower at baseline in the lines without TMPRSS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TOP2A]] | B | TOP2A activity lowers ZNF503-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC5A1]] | B | SLC5A1 activity raises ZNF503-AS1's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 2.81× lower at baseline in the lines without SLC5A1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[LINC02474]] | B | LINC02474 activity raises ZNF503-AS1's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.72× lower at baseline in the lines without LINC02474 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[CLRN3]] | B | CLRN3 activity raises ZNF503-AS1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 3.57× lower at baseline in the lines without CLRN3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 28, C 10. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | ZNF503-AS1 activity raises SLC44A3's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without ZNF503-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[SLC44A3-AS1]] | B | ZNF503-AS1 activity raises SLC44A3-AS1's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ZNF503-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[RGS6]] | B | ZNF503-AS1 activity raises RGS6's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without ZNF503-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[LINC02331]] | B | ZNF503-AS1 activity raises LINC02331's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.87× lower at baseline in the lines without ZNF503-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[LINC03040]] | B | ZNF503-AS1 activity raises LINC03040's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without ZNF503-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[IL20RA]] | B | ZNF503-AS1 activity raises IL20RA's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without ZNF503-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[LARGE2]] | B | ZNF503-AS1 activity raises LARGE2's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without ZNF503-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[KCTD14]] | B | ZNF503-AS1 activity raises KCTD14's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without ZNF503-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[STEAP2-AS1]] | B | ZNF503-AS1 activity raises STEAP2-AS1's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without ZNF503-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[ABO]] | B | ZNF503-AS1 activity raises ABO's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without ZNF503-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[FAM83F]] | B | ZNF503-AS1 activity raises FAM83F's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without ZNF503-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[LINC01814]] | B | ZNF503-AS1 activity raises LINC01814's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.57× lower at baseline in the lines without ZNF503-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 48.3); signed map (62.7, 8.8). **Vector** length 55.2, 12.4% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +33.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ZNF503 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q22.2 — chr10:75,243,568-75,373,500 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.286 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27370) · Entrez [253264](https://www.ncbi.nlm.nih.gov/gene/253264) · Ensembl [ENSG00000226051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226051)

## Data

Gene col 13507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13507); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13507]; `tensor/DDL_lfc|DDL_z.npy` [13507]; `embed/gene_vectors.npy` [13507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13507 or target_col == 13507). Every well: [[ZNF503-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF503-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
