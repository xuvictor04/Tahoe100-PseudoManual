---
symbol: "PPP1R14C"
type: "gene"
col: 12657
ensembl_id: "ENSG00000198729"
name: "protein phosphatase 1 regulatory inhibitor subunit 14C"
location: "6q25.1"
module: 84
arm: "+"
pooled_cpm: 9.08
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# PPP1R14C

*protein phosphatase 1 regulatory inhibitor subunit 14C* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.70× (z +25.1, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.504× (z -4.9, q 7e-04, down in 14 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRAMD1C]] (+0.62, fdr 2e-05), [[TOX2]] (+0.61, fdr 2e-05), [[RGS17]] (+0.60, fdr 1e-05); moves opposite to [[LRRC27]] (-0.50, fdr 5e-05), [[ENTPD3-AS1]] (-0.48, fdr 3e-04), [[PPP4R3B]] (-0.48, fdr 4e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 2 go from it, the strongest it → [[KSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.70×** | +25.1 | 0e+00 | 33/34 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.46×** | +16.9 | 0e+00 | 28/33 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +16.7 | 0e+00 | 26/33 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.23×** | +15.9 | 0e+00 | 26/31 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +15.8 | 0e+00 | 21/30 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.07×** | +15.2 | 0e+00 | 29/33 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.04×** | +15.1 | 0e+00 | 27/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +9.8 | 6e-21 | 17/32 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +8.7 | 2e-16 | 17/29 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.25×** | +8.4 | 3e-15 | 20/32 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +6.1 | 6e-08 | 12/31 (C32, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.55×** | +6.0 | 1e-07 | 11/33 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.7 | 5e-07 | 13/29 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +5.1 | 2e-05 | 11/33 (COLO 205, C32, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.37×** | +4.1 | 0.002 | 10/32 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.004 | 8/33 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.013 | 5/34 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.5 | 0.014 | 8/34 (COLO 205, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.504×** | -4.9 | 7e-04 | 14/28 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.788×** | -4.6 | 0.001 | 11/34 (SW1417, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.718×** | -4.5 | 0.001 | 9/33 (NCI-H460, J82, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.724×** | -4.2 | 0.004 | 11/33 (A498, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.743×** | -4.0 | 0.007 | 10/33 (HS-578T, NCI-H460, …) | all doses, flat |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.744×** | -3.9 | 0.011 | 11/33 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.773×** | -3.5 | 0.040 | 8/34 (A498, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.5 µM |  | **0.775×** | -3.5 | 0.040 | 5/32 (RPMI-7951, SHP-77, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.767×** | -3.4 | 0.041 | 13/32 (C32, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.041 | 8/33 (HS-578T, SW48, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.066 | 10/32 (A498, HS-578T, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.092 | 7/34 (NCI-H460, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.3 | 6 | 0 | [[Panobinostat (drug)]] 0.05 µM 6.59× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[NCI-H2030 (line)]] | alt | 22.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.67× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 15.3 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.90× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[NCI-H2347 (line)]] | alt | 15.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 11.9 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 5.21× (z +12.2) | — |
| [[NCI-H460 (line)]] | wt | 3.82 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 8.34× (z +13.0) | [[Mifepristone (drug)]] 0.05 µM 0.0486× (z -12.1) |
| [[A-172 (line)]] | wt | 8.50 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.87× (z +9.5) | — |
| [[A-427 (line)]] | wt | 12.9 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -10.0) |
| [[C32 (line)]] | wt | 43.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 20.7× (z +9.2) | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0539× (z -8.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 11.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.34× (z +9.1) | [[Trametinib (drug)]] 5 µM 0.175× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 3.39 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 11.8× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[A498 (line)]] | wt | 15.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.190× (z -10.3) |
| [[BT-474 (line)]] | alt | 4.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 8.24 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0716× (z -8.5) |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0387× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRAMD1C]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[TOX2]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RGS17]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MAP4K4]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DISP3]] | +0.58 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[HTR7]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SH3GL2]] | +0.57 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[PALM2AKAP2]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MARCHF3]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MTUS2]] | +0.57 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[PLAT]] | +0.56 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.50 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ENTPD3-AS1]] | -0.48 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[PPP4R3B]] | -0.48 | -0.26 / -0.57 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PPP1R14C's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[APBA1]] | B | APBA1 activity raises PPP1R14C's level | lines that do not express APBA1 (6) vs lines expressing it (44) | 3.21× lower at baseline in the lines without APBA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: MATN2, CCDC102A, ENSG00000267131; maybe low, not absent |
| [[HS6ST3]] | B | HS6ST3 activity raises PPP1R14C's level | lines that do not express HS6ST3 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without HS6ST3 | 0.087 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KSR1]] | B | PPP1R14C activity lowers KSR1's level | lines that do not express PPP1R14C (14) vs lines expressing it (36) | 1.15× higher at baseline in the lines without PPP1R14C | 0.089 | ⚠ within organs, on part of the lines; also absent: APLP1, CACNA1B, ENTREP1 |
| [[BEAN1]] | B | PPP1R14C activity raises BEAN1's level | lines that do not express PPP1R14C (14) vs lines expressing it (36) | 1.11× lower at baseline in the lines without PPP1R14C | 0.092 | ⚠ within organs, on part of the lines; also absent: APLP1, CACNA1B, ENTREP1 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.5, 14.0); signed map (12.5, 36.1). **Vector** length 76.4, 15.1% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.6 | +25.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | +5.5 | +3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +5.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +8.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -1.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory inhibitor subunit 14C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:150,143,044-150,250,392 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPI17-like, NY-BR-81, KEPI |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAE6](https://www.uniprot.org/uniprotkb/Q8TAE6) (Protein phosphatase 1 regulatory subunit 14C):

> Inhibitor of the PP1 regulatory subunit PPP1CA.

**Summary**, from NCBI Gene [81706](https://www.ncbi.nlm.nih.gov/gene/81706):

> The degree of protein phosphorylation is regulated by a balance of protein kinase and phosphatase activities. Protein phosphatase-1 (PP1; see MIM 176875) is a signal-transducing phosphatase that influences neuronal activity, protein synthesis, metabolism, muscle contraction, and cell division. PPP1R14C is an inhibitor of PP1 (Liu et al., 2002 [PubMed 11812771]).[supplied by OMIM, Feb 2010]

**Accessions** — [HGNC:14952](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14952) · Entrez [81706](https://www.ncbi.nlm.nih.gov/gene/81706) · UniProt [Q8TAE6](https://www.uniprot.org/uniprotkb/Q8TAE6) · Ensembl [ENSG00000198729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198729)

## Data

Gene col 12657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12657); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12657]; `tensor/DDL_lfc|DDL_z.npy` [12657]; `embed/gene_vectors.npy` [12657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12657 or target_col == 12657). Every well: [[PPP1R14C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R14C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
