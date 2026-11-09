---
symbol: "FSD1"
type: "gene"
col: 2572
ensembl_id: "ENSG00000105255"
name: "fibronectin type III and SPRY domain containing 1"
location: "19p13.3"
module: 82
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 33
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 14
direction_downstream: 28
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# FSD1

*fibronectin type III and SPRY domain containing 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.76× (z +13.4, q 4e-38, up in 25 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.548× (z -5.6, q 1e-05, down in 11 of 26 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNQ2]] (+0.65, fdr 1e-05), [[PDZD4]] (+0.64, fdr 1e-05), [[NOVA2]] (+0.60, fdr 1e-05); moves opposite to [[ANKRD17-DT]] (-0.51, fdr 6e-04), [[LEPR]] (-0.50, fdr 2e-04), [[POLR1HASP]] (-0.49, fdr 3e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MYT1]] → it (grade B ⚠); 28 go from it, the strongest it → [[PTPRS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.76×** | +13.4 | 4e-38 | 25/27 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +12.4 | 8e-33 | 13/24 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.74×** | +12.3 | 2e-32 | 8/9 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.59×** | +11.9 | 2e-30 | 24/30 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.46×** | +11.6 | 8e-29 | 18/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.3 | 1e-27 | 2/2 (HS-578T, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +10.2 | 2e-22 | 19/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +8.0 | 8e-14 | 1/4 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +6.7 | 1e-09 | 14/28 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +5.8 | 3e-07 | 10/29 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.4 | 3e-06 | 7/12 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.02×** | +4.7 | 1e-04 | 2/6 (A-427, A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.65×** | +4.6 | 1e-04 | 9/25 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +4.5 | 3e-04 | 8/27 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 6/29 (SW480, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.78×** | +3.8 | 0.004 | 3/15 (NCI-H23, C-33 A, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.009 | 7/25 (HOP62, A-427, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.6 | 0.009 | 2/11 (SHP-77, MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.1 | 0.052 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.069 | 4/24 (PANC-1, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -5.6 | 1e-05 | 11/26 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -4.6 | 0.001 | 10/25 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -4.3 | 0.003 | 10/29 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -4.1 | 0.007 | 12/28 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.4 | 0.085 | 9/23 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.718× | -3.1 | 0.18 | 10/15 (HS-578T, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 25.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -22.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.191× (z -11.6) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -10.2) |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 2.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 4.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0781× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 7.47 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0889× (z -9.2) |
| [[SW480 (line)]] | alt | 1.73 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.67× (z +9.0) | — |
| [[A-172 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.835 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.745 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.348 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNQ2]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.64 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NOVA2]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[BRSK2]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ETNK2]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[VASH1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SEMA6B]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SYT11]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ROBO3]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 | same gene group |
| [[JAKMIP1]] | +0.56 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.51 | -0.21 / -0.41 | both halves | 6e-04 |  |
| [[LEPR]] | -0.50 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[POLR1HASP]] | -0.49 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[ORMDL1]] | -0.47 | -0.47 / -0.21 | both halves | 7e-04 |  |
| [[ENTPD3-AS1]] | -0.46 | -0.24 / -0.42 | both halves | 4e-04 |  |
| [[NIFK-AS1]] | -0.46 | -0.15 / -0.35 | ⚠ not reproduced | 0.001 |  |
| [[DNAI4]] | -0.45 | -0.10 / -0.41 | ⚠ not reproduced | 0.003 |  |
| [[DECR1]] | -0.45 | -0.22 / -0.35 | both halves | 6e-04 |  |
| [[ZBTB11]] | -0.44 | -0.32 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 6, C 8. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYT1]] | B | MYT1 activity raises FSD1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without MYT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[GNAZ]] | B | GNAZ activity raises FSD1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without GNAZ | 0.036 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[KIF1A]] | B | KIF1A activity raises FSD1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without KIF1A | 0.041 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[CHD5]] | B | CHD5 activity raises FSD1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without CHD5 | 0.042 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[XKR7]] | B | XKR7 activity raises FSD1's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.55× lower at baseline in the lines without XKR7 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[SEMA6B]] | B | SEMA6B activity raises FSD1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without SEMA6B | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[NFASC]] | C | NFASC activity raises FSD1's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without NFASC | 0.011 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[SYT11]] | C | SYT11 activity raises FSD1's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.87× lower at baseline in the lines without SYT11 | 0.018 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises FSD1's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.69× lower at baseline in the lines without VASH1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises FSD1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without PDZD4 | 0.047 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[FAM184A]] | C | FAM184A activity raises FSD1's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without FAM184A | 0.050 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent; co-absent with the target |
| [[NOVA2]] | C | NOVA2 activity raises FSD1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without NOVA2 | 0.073 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 21, C 7. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRS]] | B | FSD1 activity raises PTPRS's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 3.58× lower at baseline in the lines without FSD1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[KIF3C]] | B | FSD1 activity raises KIF3C's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without FSD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[TICAM1]] | B | FSD1 activity lowers TICAM1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.02× higher at baseline in the lines without FSD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[KCTD17]] | B | FSD1 activity raises KCTD17's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without FSD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[DPF1]] | B | FSD1 activity raises DPF1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without FSD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[GNAZ]] | B | FSD1 activity raises GNAZ's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without FSD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[JPH3]] | B | FSD1 activity raises JPH3's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.35× lower at baseline in the lines without FSD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[POLR1HASP]] | B | FSD1 activity raises POLR1HASP's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without FSD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[NIFK-AS1]] | B | FSD1 activity raises NIFK-AS1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without FSD1 | 0.039 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[RAB6B]] | B | FSD1 activity raises RAB6B's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without FSD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[SLC45A1]] | B | FSD1 activity raises SLC45A1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without FSD1 | 0.045 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[CHD5]] | B | FSD1 activity raises CHD5's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without FSD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.4, 39.7); signed map (25.9, 27.2). **Vector** length 43.5, 7.53% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.5 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.4 | -4.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin type III and SPRY domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,304,598-4,323,843 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3213, MIR1 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTV5](https://www.uniprot.org/uniprotkb/Q9BTV5) (Fibronectin type III and SPRY domain-containing protein 1):

> May be involved in microtubule organization and stabilization.

**Summary**, from NCBI Gene [79187](https://www.ncbi.nlm.nih.gov/gene/79187):

> This gene encodes a centrosome associated protein that is characterized by an N-terminal coiled-coil region downstream of B-box (BBC) domain, a central fibronectin type III domain, and a C-terminal repeats in splA and RyR (SPRY) domain. The encoded protein associates with a subset of microtubules and may be involved in the stability and organization of microtubules during cytokinesis. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:13745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13745) · Entrez [79187](https://www.ncbi.nlm.nih.gov/gene/79187) · UniProt [Q9BTV5](https://www.uniprot.org/uniprotkb/Q9BTV5) · Ensembl [ENSG00000105255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105255)

## Data

Gene col 2572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2572); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2572]; `tensor/DDL_lfc|DDL_z.npy` [2572]; `embed/gene_vectors.npy` [2572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2572 or target_col == 2572). Every well: [[FSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
