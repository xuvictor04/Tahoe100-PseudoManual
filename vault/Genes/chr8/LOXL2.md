---
symbol: "LOXL2"
type: "gene"
col: 5497
ensembl_id: "ENSG00000134013"
name: "lysyl oxidase like 2"
location: "8p21.3"
module: 13
arm: "+"
pooled_cpm: 269.88
n_lines_expressing: 32
n_dd_up: 0
n_dd_down: 53
n_dd_up_clean: 0
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 44
direction_downstream: 17
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LOXL2

*lysyl oxidase like 2* — 8p21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2030 2.84×).
> Pooled over the cell lines (median), lowered significantly by 53 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.191× (z -40.3, q 0e+00, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFBP3]] (+0.73, fdr 7e-06), [[NAV1]] (+0.71, fdr 7e-06), [[COL5A1]] (+0.68, fdr 7e-06); moves opposite to [[SYK]] (-0.54, fdr 4e-05), [[ABO]] (-0.52, fdr 4e-05), [[ANK3]] (-0.51, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[VSTM4]] → it (grade B ⚠); 17 go from it, the strongest it → [[LTBP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H2030 2.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.23× | +3.6 | 0.11 | 15/30 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.23× | +3.6 | 0.11 | 13/30 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.05 µM |  | 1.22× | +3.4 | 0.11 | 13/30 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.14 | 15/30 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.21 | 14/29 (SW480, SW 900, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.20× | +3.0 | 0.23 | 11/29 (RPMI-7951, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 53 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.191×** | -40.3 | 0e+00 | 30/30 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.130×** | -33.7 | 0e+00 | 30/30 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.186×** | -29.0 | 0e+00 | 30/30 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -19.5 | 0e+00 | 29/30 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.342×** | -18.4 | 0e+00 | 29/30 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.360×** | -17.6 | 0e+00 | 28/30 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.370×** | -16.4 | 0e+00 | 28/29 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.393×** | -16.0 | 0e+00 | 30/30 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.394×** | -15.4 | 0e+00 | 26/29 (Hs 766T, H4, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -14.9 | 0e+00 | 29/30 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.458×** | -13.4 | 2e-39 | 28/30 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -10.7 | 7e-25 | 27/30 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -10.3 | 3e-23 | 27/30 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.563×** | -9.8 | 3e-21 | 24/30 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.671×** | -9.7 | 1e-20 | 19/30 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -9.4 | 2e-19 | 26/30 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -8.9 | 2e-17 | 24/30 (H4, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -7.9 | 9e-14 | 26/30 (hTERT-HPNE, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -7.4 | 3e-12 | 25/30 (LOX-IMVI, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 563 | 0 | 20 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0228× (z -35.8) |
| [[NCI-H460 (line)]] | wt | 162 | 0 | 18 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0903× (z -29.0) |
| [[HOP62 (line)]] | alt | 651 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -33.3) |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 17 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0572× (z -22.0) |
| [[A-172 (line)]] | wt | 1,209 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -50.3) |
| [[hTERT-HPNE (line)]] | wt | 797 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.4) |
| [[A498 (line)]] | wt | 593 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -27.7) |
| [[A549 (line)]] | wt | 461 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -40.0) |
| [[HS-578T (line)]] | alt | 1,428 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -36.0) |
| [[J82 (line)]] | alt | 339 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -33.2) |
| [[RPMI-7951 (line)]] | alt | 868 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -29.3) |
| [[SNU-423 (line)]] | alt | 518 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -43.2) |
| [[Hs 766T (line)]] | wt | 284 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -31.8) |
| [[MIA PaCa-2 (line)]] | alt | 596 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -30.5) |
| [[NCI-H1792 (line)]] | alt | 580 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0950× (z -26.2) |
| [[NCI-H23 (line)]] | alt | 263 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -22.2) |
| [[NCI-H2347 (line)]] | alt | 191 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -24.1) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -16.1) |
| [[SW 900 (line)]] | alt | 461 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -31.4) |
| [[C32 (line)]] | wt | 119 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -29.1) |
| [[PANC-1 (line)]] | alt | 151 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -39.3) |
| [[SW480 (line)]] | alt | 72.8 | 0 | 9 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.132× (z -20.2) |
| [[NCI-H2030 (line)]] | alt | 171 | 1 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.128× (z -20.1) |
| [[BT-474 (line)]] | alt | 72.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 97.3 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -20.3) |
| [[SW 1088 (line)]] | alt | 1,037 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0701× (z -16.3) |
| [[CHP-212 (line)]] | wt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -12.8) |
| [[AN3 CA (line)]] | alt | 190 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.9) |
| [[NCI-H661 (line)]] | alt | 88.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -8.9) |
| [[A-427 (line)]] | wt | 32.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 42.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 50.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 34.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 60.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 55.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 50.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 30.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 66.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 29.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP3]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 551 |
| [[NAV1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[COL5A1]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 523 |
| [[KLF7]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[IL1RAP]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ITGB3]] | +0.63 | +0.68 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC01411]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[FAM20C]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SLC6A6]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[VEGFC]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 409 |
| [[ITPR1]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYK]] | -0.54 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ABO]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ANK3]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PUM2]] | -0.51 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[RAVER2]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 12, C 32. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSTM4]] | B | VSTM4 activity raises LOXL2's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 4.67× lower at baseline in the lines without VSTM4 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[LINC01411]] | B | LINC01411 activity raises LOXL2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 7.36× lower at baseline in the lines without LINC01411 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032 |
| [[FAM20C]] | B | FAM20C activity raises LOXL2's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.89× lower at baseline in the lines without FAM20C | 0.048 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[FBN1]] | B | FBN1 activity raises LOXL2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.33× lower at baseline in the lines without FBN1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[GLYATL2]] | B | GLYATL2 activity raises LOXL2's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 3.79× lower at baseline in the lines without GLYATL2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |
| [[LINC03047]] | B | LINC03047 activity raises LOXL2's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 3.86× lower at baseline in the lines without LINC03047 | 0.075 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[SYK]] | B | SYK activity lowers LOXL2's level | lines that do not express SYK (30) vs lines expressing it (20) | 4.45× higher at baseline in the lines without SYK | 0.080 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[ITGA11]] | B | ITGA11 activity raises LOXL2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.87× lower at baseline in the lines without ITGA11 | 0.083 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[CA12]] | B | CA12 activity raises LOXL2's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.42× lower at baseline in the lines without CA12 | 0.090 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[ZCCHC24]] | B | ZCCHC24 activity raises LOXL2's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 3.84× lower at baseline in the lines without ZCCHC24 | 0.091 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[CERCAM]] | B | CERCAM activity raises LOXL2's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 5.10× lower at baseline in the lines without CERCAM | 0.092 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[TMEM255B]] | B | TMEM255B activity raises LOXL2's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 3.38× lower at baseline in the lines without TMEM255B | 0.097 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 9, C 8. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBP3]] | B | LOXL2 activity raises LTBP3's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without LOXL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[ZCCHC24]] | B | LOXL2 activity raises ZCCHC24's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without LOXL2 | 0.035 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[FAM219A]] | B | LOXL2 activity raises FAM219A's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without LOXL2 | 0.056 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[AFAP1]] | B | LOXL2 activity raises AFAP1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without LOXL2 | 0.059 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[COL13A1]] | B | LOXL2 activity raises COL13A1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 3.50× lower at baseline in the lines without LOXL2 | 0.074 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[TTYH2]] | B | LOXL2 activity raises TTYH2's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without LOXL2 | 0.079 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| cells under [[9-ING-41 (drug)]] 0.5 µM | B | LOXL2 activity raises the cells' numbers under 9-ING-41 0.5 µM (protects the cells) | lines that do not express LOXL2 (18) vs lines expressing it (30) | the lines without LOXL2: 0.80× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[EHD2]] | B | LOXL2 activity raises EHD2's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 3.65× lower at baseline in the lines without LOXL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[MTCL1]] | B | LOXL2 activity raises MTCL1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without LOXL2 | 0.098 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[ABCA1]] | C | LOXL2 activity raises ABCA1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 6.71× lower at baseline in the lines without LOXL2 | 0.002 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1; co-absent with the target |
| [[SLC8A1]] | C | LOXL2 activity raises SLC8A1's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 5.54× lower at baseline in the lines without LOXL2 | 0.027 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1; co-absent with the target |
| [[GSDME]] | C | LOXL2 activity raises GSDME's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 3.47× lower at baseline in the lines without LOXL2 | 0.047 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.5, 17.2); signed map (24.8, 47.7). **Vector** length 120, 45.8% of its response variance represented; |z| ≥ 3 in 1,413 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Integrin cell surface interactions* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.0 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | -17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Omeprazole (sodium) (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.6 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -16.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -9.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.0 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.5 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | lysyl oxidase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,296,897-23,425,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WS9-14, LOR |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Lysyl oxidase family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Crosslinking of collagen fibrils; Elastic fibre formation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4K0](https://www.uniprot.org/uniprotkb/Q9Y4K0) (Lysyl oxidase homolog 2):

> Mediates the post-translational oxidative deamination of lysine residues on target proteins leading to the formation of deaminated lysine (allysine). Acts as a transcription corepressor and specifically mediates deamination of trimethylated 'Lys-4' of histone H3 (H3K4me3), a specific tag for epigenetic transcriptional activation. Shows no activity against histone H3 when it is trimethylated on 'Lys-9' (H3K9me3) or 'Lys-27' (H3K27me3) or when 'Lys-4' is monomethylated (H3K4me1) or dimethylated …

**Summary**, from NCBI Gene [4017](https://www.ncbi.nlm.nih.gov/gene/4017):

> This gene encodes a member of the lysyl oxidase gene family. The prototypic member of the family is essential to the biogenesis of connective tissue, encoding an extracellular copper-dependent amine oxidase that catalyses the first step in the formation of crosslinks in collagens and elastin. A highly conserved amino acid sequence at the C-terminus end appears to be sufficient for amine oxidase activity, suggesting that each family member may retain this function. The N-terminus is poorly …

**Accessions** — [HGNC:6666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6666) · Entrez [4017](https://www.ncbi.nlm.nih.gov/gene/4017) · UniProt [Q9Y4K0](https://www.uniprot.org/uniprotkb/Q9Y4K0) · Ensembl [ENSG00000134013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134013)

## Data

Gene col 5497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5497); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5497]; `tensor/DDL_lfc|DDL_z.npy` [5497]; `embed/gene_vectors.npy` [5497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5497 or target_col == 5497). Every well: [[LOXL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LOXL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
