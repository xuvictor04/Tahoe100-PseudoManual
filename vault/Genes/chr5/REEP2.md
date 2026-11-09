---
symbol: "REEP2"
type: "gene"
col: 5339
ensembl_id: "ENSG00000132563"
name: "receptor accessory protein 2"
location: "5q31.2"
module: 100
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 38
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# REEP2

*receptor accessory protein 2* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.24× (z +10.9, q 1e-24, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +9.5, q 3e-19, up in 14 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.537× (z -6.0, q 1e-06, down in 12 of 34 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC88B]] (+0.64, fdr 2e-05), [[SEMA6B]] (+0.62, fdr 3e-05), [[PCOLCE]] (+0.60, fdr 1e-05); moves opposite to [[TTF2]] (-0.47, fdr 1e-04), [[ZNF731P]] (-0.47, fdr 3e-05), [[PUM3]] (-0.46, fdr 3e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 7 go from it, the strongest it → [[NUAK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.24×** | +10.9 | 1e-24 | 4/6 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +9.8 | 3e-20 | 10/15 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +9.5 | 3e-19 | 14/25 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.9 | 7e-17 | 22/33 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +8.0 | 1e-13 | 15/30 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +7.2 | 6e-11 | 7/26 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +6.8 | 7e-10 | 15/33 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.8 | 7e-10 | 10/14 (A-172, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +6.7 | 2e-09 | 13/33 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +6.4 | 7e-09 | 5/7 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +5.7 | 8e-07 | 11/34 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +5.5 | 2e-06 | 13/33 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.003 | 6/24 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.9 | 0.004 | 5/12 (LoVo, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 6/32 (A-172, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.049 | 3/20 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.059 | 3/34 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.060 | 1/24 (A549) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.067 | 3/19 (C-33 A, NCI-H1792, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.077 | 3/32 (A-172, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -6.0 | 1e-06 | 12/34 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -5.6 | 5e-06 | 16/33 (SK-MEL-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -5.0 | 1e-04 | 11/25 (A549, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.628×** | -4.5 | 0.001 | 13/30 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.721× | -3.1 | 0.15 | 7/34 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.15 | 12/30 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +9.2) | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -8.6) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC88B]] | +0.64 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SEMA6B]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[PCOLCE]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TMCC2]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[GAMT]] | +0.58 | +0.40 / +0.74 | both halves | 5e-05 |  |
| [[CBX8]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TMEM266]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[DBP]] | +0.55 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TCEA3]] | +0.54 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[NUAK1]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[LMX1B]] | +0.54 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTF2]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ZNF731P]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PUM3]] | -0.46 | -0.28 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises REEP2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without SEMA6B | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[NPTXR]] | B | NPTXR activity raises REEP2's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without NPTXR | 0.070 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[APLP1]] | B | APLP1 activity raises REEP2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without APLP1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[FSD1]] | B | FSD1 activity raises REEP2's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.57× lower at baseline in the lines without FSD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[FAM229B]] | B | FAM229B activity raises REEP2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without FAM229B | 0.085 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[TMCC2]] | B | TMCC2 activity raises REEP2's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 2.52× lower at baseline in the lines without TMCC2 | 0.086 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises REEP2's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 2.36× lower at baseline in the lines without SLC29A4 | 0.096 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[ADGRB2]] | B | ADGRB2 activity raises REEP2's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without ADGRB2 | 0.098 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUAK1]] | B | REEP2 activity raises NUAK1's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 2.44× lower at baseline in the lines without REEP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[PTK7]] | B | REEP2 activity raises PTK7's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without REEP2 | 0.040 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[ADGRB2]] | B | REEP2 activity raises ADGRB2's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without REEP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[RTN4RL2]] | B | REEP2 activity raises RTN4RL2's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without REEP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[APBB1]] | B | REEP2 activity raises APBB1's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without REEP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[PPM1M]] | B | REEP2 activity raises PPM1M's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without REEP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| cells under [[Erdafitinib (drug)]] 5 µM | B | REEP2 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express REEP2 (12) vs lines expressing it (36) | the lines without REEP2: 1.12× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.3, 35.6); signed map (20.6, 22.2). **Vector** length 33.7, 3.93% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +9.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.7 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | receptor accessory protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,439,057-138,446,969 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SGC32445, SPG72, Yip2d; previously C5orf19 |
| Gene groups (HGNC) | Receptor accessory proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRK0](https://www.uniprot.org/uniprotkb/Q9BRK0) (Receptor expression-enhancing protein 2):

> Required for endoplasmic reticulum (ER) network formation, shaping and remodeling. May enhance the cell surface expression of odorant receptors (By similarity).

**Summary**, from NCBI Gene [51308](https://www.ncbi.nlm.nih.gov/gene/51308):

> This gene encodes a member of the receptor expression enhancing protein family. Studies of a related gene in mouse suggest that the encoded protein is found in the cell membrane and enhances the function of sweet taste receptors. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:17975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17975) · Entrez [51308](https://www.ncbi.nlm.nih.gov/gene/51308) · UniProt [Q9BRK0](https://www.uniprot.org/uniprotkb/Q9BRK0) · Ensembl [ENSG00000132563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132563)

## Data

Gene col 5339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5339); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5339]; `tensor/DDL_lfc|DDL_z.npy` [5339]; `embed/gene_vectors.npy` [5339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5339 or target_col == 5339). Every well: [[REEP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REEP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
