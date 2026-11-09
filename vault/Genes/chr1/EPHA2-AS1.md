---
symbol: "EPHA2-AS1"
type: "gene"
col: 13616
ensembl_id: "ENSG00000227959"
name: "EPHA2 antisense RNA 1"
location: "1p36.13"
module: 141
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 34
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 49
direction_downstream: 27
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# EPHA2-AS1

*EPHA2 antisense RNA 1* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.16× (z +11.5, q 1e-27, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +8.6, q 8e-16, up in 5 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.564× (z -5.7, q 6e-06, down in 9 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00659]] (+0.78, fdr 7e-06), [[EPHA2]] (+0.76, fdr 7e-06, ⚠ same locus), [[SH2D3A]] (+0.75, fdr 7e-06), [[BLACAT1]] (+0.69, fdr 7e-06).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[KLK10]] → it (grade B ⚠); 27 go from it, the strongest it → [[RHOF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.16×** | +11.5 | 1e-27 | 3/5 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.3 | 3e-18 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +9.0 | 4e-17 | 3/12 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.6 | 8e-16 | 5/21 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +5.8 | 9e-07 | 9/23 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.82×** | +4.9 | 8e-05 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.8 | 0.011 | 0/17 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.79×** | +3.8 | 0.012 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +3.7 | 0.012 | 2/17 (HCT15, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +3.6 | 0.017 | 5/26 (NCI-H1573, HCT15, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.031 | 2/20 (LS 180, SW48) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.033 | 1/12 (PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.074 | 4/21 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.076 | 6/28 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.083 | 2/28 (HEC-1-A, NCI-H2347) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.096 | 2/17 (SW480, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.564×** | -5.7 | 6e-06 | 9/30 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.530×** | -5.1 | 9e-05 | 8/29 (SW480, HCT15, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.673×** | -4.5 | 0.001 | 20/28 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.690×** | -4.4 | 0.002 | 9/30 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.637×** | -4.1 | 0.005 | 8/24 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.731×** | -3.4 | 0.074 | 10/28 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.32 | 0 | 11 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.163× (z -11.8) |
| [[A-172 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.668 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.661 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.678 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.808 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.714 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00659]] | +0.78 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[EPHA2]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SH2D3A]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[BLACAT1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LEMD1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L1-AS1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | same gene group |
| [[GJB3]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[PADI1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MST1R]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[LCK]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[KIAA0040]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 33, C 16. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLK10]] | B | KLK10 activity raises EPHA2-AS1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without KLK10 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[MDFI]] | B | MDFI activity raises EPHA2-AS1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without MDFI | 0.003 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[TRIM15]] | B | TRIM15 activity raises EPHA2-AS1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.87× lower at baseline in the lines without TRIM15 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises EPHA2-AS1's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.46× lower at baseline in the lines without TMPRSS4 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[KIAA0040]] | B | KIAA0040 activity raises EPHA2-AS1's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without KIAA0040 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises EPHA2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HS3ST1]] | B | HS3ST1 activity raises EPHA2-AS1's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.37× lower at baseline in the lines without HS3ST1 | 0.012 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[B3GNT3]] | B | B3GNT3 activity raises EPHA2-AS1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.34× lower at baseline in the lines without B3GNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[MAOB]] | B | MAOB activity raises EPHA2-AS1's level | lines that do not express MAOB (34) vs lines expressing it (16) | 2.15× lower at baseline in the lines without MAOB | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A4, LGR6, AZGP1 |
| [[SH2D3A]] | B | SH2D3A activity raises EPHA2-AS1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without SH2D3A | 0.016 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[CRYBG2]] | B | CRYBG2 activity raises EPHA2-AS1's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without CRYBG2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[ABCC3]] | B | ABCC3 activity raises EPHA2-AS1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without ABCC3 | 0.028 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 18, C 9. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOF]] | B | EPHA2-AS1 activity raises RHOF's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without EPHA2-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[BAIAP2L1]] | B | EPHA2-AS1 activity raises BAIAP2L1's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without EPHA2-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[SLC16A5]] | B | EPHA2-AS1 activity raises SLC16A5's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 3.20× lower at baseline in the lines without EPHA2-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[SLC25A45]] | B | EPHA2-AS1 activity raises SLC25A45's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without EPHA2-AS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[PDE9A]] | B | EPHA2-AS1 activity raises PDE9A's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without EPHA2-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[BCL2L1-AS1]] | B | EPHA2-AS1 activity raises BCL2L1-AS1's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without EPHA2-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[PXN]] | B | EPHA2-AS1 activity raises PXN's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without EPHA2-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[TMC6]] | B | EPHA2-AS1 activity raises TMC6's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 3.06× lower at baseline in the lines without EPHA2-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[BCL2L1]] | B | EPHA2-AS1 activity raises BCL2L1's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.97× lower at baseline in the lines without EPHA2-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[ARHGAP27]] | B | EPHA2-AS1 activity raises ARHGAP27's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without EPHA2-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[ALS2CL]] | B | EPHA2-AS1 activity raises ALS2CL's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 2.96× lower at baseline in the lines without EPHA2-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[TMEM40]] | B | EPHA2-AS1 activity raises TMEM40's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without EPHA2-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.1, 51.6); signed map (4.2, 38.9). **Vector** length 53.2, 10.6% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +9.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +3.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.1 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | EPHA2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.13 — chr1:16,155,176-16,158,148 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40216](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40216) · Entrez [101927479](https://www.ncbi.nlm.nih.gov/gene/101927479) · Ensembl [ENSG00000227959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227959)

## Data

Gene col 13616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13616); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13616]; `tensor/DDL_lfc|DDL_z.npy` [13616]; `embed/gene_vectors.npy` [13616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13616 or target_col == 13616). Every well: [[EPHA2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
