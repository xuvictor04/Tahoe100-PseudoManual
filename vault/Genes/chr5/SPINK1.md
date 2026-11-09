---
symbol: "SPINK1"
type: "gene"
col: 8915
ensembl_id: "ENSG00000164266"
name: "serine peptidase inhibitor Kazal type 1"
location: "5q32"
module: 125
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 22
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# SPINK1

*serine peptidase inhibitor Kazal type 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.03× (z +7.9, q 1e-12, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.38× (z +7.2, q 2e-10, up in 13 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.519× (z -3.9, q 0.052, down in 14 of 17 measured lines) ⚠ cell-cycle shift, explains ~62% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0989×, HT-29 0.191×); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.134×; ⚠ cell-cycle shift, explains ~62% of this change); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.265×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCP]] (+0.63, fdr 1e-05), [[LINC02154]] (+0.62, fdr 1e-05), [[DPYD-AS1]] (+0.62, fdr 1e-05); moves opposite to [[NCBP1]] (-0.50, fdr 3e-05), [[CCAR2]] (-0.48, fdr 1e-04), [[SLX4]] (-0.48, fdr 6e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GBP2]] → it (grade B ⚠); 13 go from it, the strongest it → [[GBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.03×** | +7.9 | 1e-12 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.38×** | +7.2 | 2e-10 | 13/18 (A-172, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.89×** | +5.8 | 1e-06 | 2/6 (LoVo, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +5.3 | 2e-05 | 8/15 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +4.8 | 2e-04 | 8/16 (COLO 205, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +4.7 | 2e-04 | 1/14 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +4.5 | 5e-04 | 10/17 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.3 | 0.001 | 2/12 (A-172, LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.006 | 6/17 (LoVo, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +3.8 | 0.007 | 8/17 (COLO 205, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +3.8 | 0.009 | 10/17 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.88×** | +3.6 | 0.015 | 9/16 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +3.6 | 0.015 | 2/10 (SW1417, KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +3.6 | 0.015 | 7/17 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.28×** | +3.5 | 0.020 | 4/16 (KATO III, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **1.76×** | +3.3 | 0.029 | 6/17 (NCI-H1573, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +3.2 | 0.043 | 9/18 (COLO 205, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.043 | 7/17 (NCI-H460, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +3.1 | 0.048 | 4/13 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.59×** | +3.1 | 0.049 | 9/18 (HT-29, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +3.0 | 0.078 | 7/18 (HT-29, COLO 205, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0989×, HT-29 0.191×); [[Panobinostat (drug)]] 5 µM in 1 line (COLO 205 0.134×; ⚠ cell-cycle shift, explains ~62% of this change); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.265×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.519×** | -3.9 | 0.052 | 14/17 (COLO 205, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.600× | -3.0 | 0.29 | 13/17 (COLO 205, A-172, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.698× | -3.0 | 0.29 | 9/17 (COLO 205, LoVo, …) | rises with dose | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.577× | -3.0 | 0.29 | 3/18 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.604× | -3.0 | 0.29 | 12/18 (A-172, COLO 205, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.66 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 86.3 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.29× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.134× (z -11.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.265× (z -10.3) |
| [[A-172 (line)]] | wt | 9.16 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +15.2) | — |
| [[LoVo (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -12.8) |
| [[HT-29 (line)]] | alt | 52.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.3) |
| [[SW 1088 (line)]] | alt | 1.64 | 1 | 0 | [[Anastrozole (drug)]] 0.5 µM 1.54× (z +32.8) | — |
| [[A-427 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.825 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.445 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCP]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[LINC02154]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DPYD-AS1]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PRRG4]] | +0.61 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HPS1]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[HRK]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[RAB32]] | +0.57 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ENTHD1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PNLIPRP3]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC9C1]] | +0.56 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[ATP6V0E1]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP1]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CCAR2]] | -0.48 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[SLX4]] | -0.48 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[NCAPD3]] | -0.47 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP2]] | B | GBP2 activity raises SPINK1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without GBP2 | 0.056 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CRYM]] | B | CRYM activity raises SPINK1's level | lines that do not express CRYM (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without CRYM | 0.073 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers SPINK1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[KMO]] | B | KMO activity raises SPINK1's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without KMO | 0.096 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[HKDC1]] | C | HKDC1 activity raises SPINK1's level | lines that do not express HKDC1 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without HKDC1 | 0.013 | ⚠ within organs, on part of the lines; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |
| [[IGFL2-AS1]] | C | IGFL2-AS1 activity raises SPINK1's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.37× lower at baseline in the lines without IGFL2-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559; co-absent with the target |
| [[HLA-DRA]] | C | HLA-DRA activity raises SPINK1's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without HLA-DRA | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises SPINK1's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.63× lower at baseline in the lines without LCN2 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[PSG9]] | C | PSG9 activity raises SPINK1's level | lines that do not express PSG9 (45) vs lines expressing it (5) | 2.31× lower at baseline in the lines without PSG9 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, PSG1, NPPB; co-absent with the target; its own permutation p |
| [[LINC02154]] | C | LINC02154 activity raises SPINK1's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 1.35× lower at baseline in the lines without LINC02154 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises SPINK1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 1.47× lower at baseline in the lines without PSG4 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP2]] | B | SPINK1 activity raises GBP2's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.95× lower at baseline in the lines without SPINK1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[MAPK6]] | B | SPINK1 activity raises MAPK6's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without SPINK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[APOL2]] | B | SPINK1 activity raises APOL2's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without SPINK1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[CASP4]] | B | SPINK1 activity raises CASP4's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without SPINK1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[MVP-DT]] | B | SPINK1 activity raises MVP-DT's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without SPINK1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[LINC01504]] | B | SPINK1 activity raises LINC01504's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.35× lower at baseline in the lines without SPINK1 | 0.040 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[C4orf19]] | B | SPINK1 activity raises C4orf19's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without SPINK1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[LURAP1L]] | B | SPINK1 activity raises LURAP1L's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without SPINK1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[NCAPD3]] | B | SPINK1 activity lowers NCAPD3's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.50× higher at baseline in the lines without SPINK1 | 0.092 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[CCAR2]] | B | SPINK1 activity lowers CCAR2's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.29× higher at baseline in the lines without SPINK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| cells under [[Infigratinib (drug)]] 0.5 µM | B | SPINK1 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express SPINK1 (28) vs lines expressing it (20) | the lines without SPINK1: 0.88× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[HKDC1]] | C | SPINK1 activity raises HKDC1's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without SPINK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.6, 23.2); signed map (36.6, 23.0). **Vector** length 51.3, 13.9% of its response variance represented; |z| ≥ 3 in 462 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | serine peptidase inhibitor Kazal type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:147,824,572-147,831,671 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Spink3, PCTT, PSTI, TATI |
| Gene groups (HGNC) | Serine peptidase inhibitors, Kazal type |
| Matched by | ensembl_id |

**Function**, from UniProt [P00995](https://www.uniprot.org/uniprotkb/P00995) (Serine protease inhibitor Kazal-type 1):

> Serine protease inhibitor which exhibits anti-trypsin activity. In the pancreas, protects against trypsin-catalyzed premature activation of zymogens (By similarity).; In the male reproductive tract, binds to sperm heads where it modulates sperm capacitance by inhibiting calcium uptake and nitrogen oxide (NO) production.

**Summary**, from NCBI Gene [6690](https://www.ncbi.nlm.nih.gov/gene/6690):

> The protein encoded by this gene is a trypsin inhibitor, which is secreted from pancreatic acinar cells into pancreatic juice. It is thought to function in the prevention of trypsin-catalyzed premature activation of zymogens within the pancreas and the pancreatic duct. Mutations in this gene are associated with hereditary pancreatitis and tropical calcific pancreatitis. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:11244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11244) · Entrez [6690](https://www.ncbi.nlm.nih.gov/gene/6690) · UniProt [P00995](https://www.uniprot.org/uniprotkb/P00995) · Ensembl [ENSG00000164266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164266)

## Data

Gene col 8915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8915); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8915]; `tensor/DDL_lfc|DDL_z.npy` [8915]; `embed/gene_vectors.npy` [8915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8915 or target_col == 8915). Every well: [[SPINK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
