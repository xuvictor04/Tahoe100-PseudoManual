---
symbol: "PDZD4"
type: "gene"
col: 872
ensembl_id: "ENSG00000067840"
name: "PDZ domain containing 4"
location: "Xq28"
module: 132
arm: "+"
pooled_cpm: 4.64
n_lines_expressing: 28
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 37
direction_downstream: 41
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# PDZD4

*PDZ domain containing 4* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.59× (z +9.8, q 7e-20, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 2.08× (z +7.9, q 1e-12, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.368× (z -10.3, q 5e-22, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRSK2]] (+0.78, fdr 7e-06), [[SEPTIN5]] (+0.73, fdr 7e-06), [[VASH1]] (+0.71, fdr 1e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 41 go from it, the strongest it → [[UPK1A-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +9.8 | 7e-20 | 6/9 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +7.9 | 1e-12 | 14/23 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +7.8 | 1e-12 | 12/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +7.3 | 5e-11 | 8/16 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.5 | 9e-04 | 7/24 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.4 | 0.001 | 3/18 (HOP62, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +3.9 | 0.007 | 4/10 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.017 | 6/22 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +3.4 | 0.037 | 1/25 (NCI-H460) | all doses, flat | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.33× | +3.1 | 0.11 | 1/24 (NCI-H460) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.368×** | -10.3 | 5e-22 | 16/22 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.391×** | -10.1 | 3e-21 | 17/21 (A-172, A-427, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.452×** | -8.5 | 4e-15 | 19/24 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -8.2 | 4e-14 | 15/24 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.603×** | -7.6 | 2e-12 | 17/22 (A-172, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -7.0 | 2e-10 | 18/22 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.577×** | -5.9 | 4e-07 | 13/24 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -5.8 | 4e-07 | 12/24 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.643×** | -4.7 | 2e-04 | 12/24 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.674×** | -4.2 | 0.001 | 10/25 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -4.0 | 0.003 | 7/23 (PANC-1, HOP62, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.526×** | -3.6 | 0.015 | 5/23 (A-427, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.727×** | -3.4 | 0.029 | 4/24 (CHP-212, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.727×** | -3.2 | 0.053 | 8/23 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.062 | 11/25 (MIA PaCa-2, SW 1088, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.065 | 7/22 (SK-MEL-2, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.2) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -9.5) |
| [[A-427 (line)]] | wt | 15.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.133× (z -11.8) |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0818× (z -17.5) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 10.00 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.67 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0934× (z -9.8) |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0665× (z -8.8) |
| [[C32 (line)]] | wt | 9.47 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 6.36 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -9.8) |
| [[A498 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK2]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SEPTIN5]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[VASH1]] | +0.71 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[KIF26A]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[JAG2]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SHANK3]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 | same gene group |
| [[GNAZ]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[SULT4A1]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[KCNQ2]] | +0.65 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[RAB6B]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[FSD1]] | +0.64 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 9, C 28. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises PDZD4's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without GNAZ | 0.015 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[GLIPR2]] | B | GLIPR2 activity raises PDZD4's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 2.91× lower at baseline in the lines without GLIPR2 | 0.024 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[CHD5]] | B | CHD5 activity raises PDZD4's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without CHD5 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SEMA6B]] | B | SEMA6B activity raises PDZD4's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.20× lower at baseline in the lines without SEMA6B | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[MMP15]] | B | MMP15 activity raises PDZD4's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without MMP15 | 0.064 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PDZD4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PDZD4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HES2]] | B | HES2 activity raises PDZD4's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without HES2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[SLC4A3]] | B | SLC4A3 activity raises PDZD4's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without SLC4A3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[CACNG7]] | C | CACNG7 activity raises PDZD4's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without CACNG7 | 0.005 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B; co-absent with the target |
| [[RET]] | C | RET activity raises PDZD4's level | lines that do not express RET (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without RET | 0.006 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[CYS1]] | C | CYS1 activity raises PDZD4's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without CYS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4; co-absent with the target |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 22, C 19. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UPK1A-AS1]] | B | PDZD4 activity raises UPK1A-AS1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.55× lower at baseline in the lines without PDZD4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[GRIP2]] | B | PDZD4 activity raises GRIP2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without PDZD4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[TCF7L1]] | B | PDZD4 activity raises TCF7L1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.99× lower at baseline in the lines without PDZD4 | 0.001 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SDC3]] | B | PDZD4 activity raises SDC3's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without PDZD4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[KIF3C]] | B | PDZD4 activity raises KIF3C's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without PDZD4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[CIB2]] | B | PDZD4 activity raises CIB2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without PDZD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[RASGEF1C]] | B | PDZD4 activity raises RASGEF1C's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without PDZD4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SLC4A3]] | B | PDZD4 activity raises SLC4A3's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without PDZD4 | 0.017 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[GLIPR2]] | B | PDZD4 activity raises GLIPR2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without PDZD4 | 0.017 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[HEYL]] | B | PDZD4 activity raises HEYL's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.64× lower at baseline in the lines without PDZD4 | 0.023 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[DLK2]] | B | PDZD4 activity raises DLK2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without PDZD4 | 0.030 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[SEPTIN5]] | B | PDZD4 activity raises SEPTIN5's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without PDZD4 | 0.038 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.5, 39.9); signed map (25.7, 27.2). **Vector** length 49.9, 10.2% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PDZ domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,802,166-153,830,565 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1444, LU1, FLJ34125, PDZRN4L, LNX5; previously PDZK4 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

UniProt [Q76G19](https://www.uniprot.org/uniprotkb/Q76G19) carries no function annotation.

**Summary**, from NCBI Gene [57595](https://www.ncbi.nlm.nih.gov/gene/57595):

> Predicted to be located in cell cortex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21167) · Entrez [57595](https://www.ncbi.nlm.nih.gov/gene/57595) · UniProt [Q76G19](https://www.uniprot.org/uniprotkb/Q76G19) · Ensembl [ENSG00000067840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067840)

## Data

Gene col 872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 872); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 872]; `tensor/DDL_lfc|DDL_z.npy` [872]; `embed/gene_vectors.npy` [872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 872 or target_col == 872). Every well: [[PDZD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
