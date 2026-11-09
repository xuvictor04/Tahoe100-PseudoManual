---
symbol: "SUSD4"
type: "gene"
col: 6759
ensembl_id: "ENSG00000143502"
name: "sushi domain containing 4"
location: "1q41"
module: 115
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 39
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# SUSD4

*sushi domain containing 4* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 9.52× (z +27.2, q 0e+00, up in 28 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cepharanthine (drug)]] 5 µM in 1 line (BT-474 0.225×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0568×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGSM1]] (+0.71, fdr 1e-05), [[HPSE]] (+0.69, fdr 5e-05), [[ATP1A3]] (+0.65, fdr 1e-04); moves opposite to [[EFCAB2]] (-0.59, fdr 2e-04), [[C8orf33]] (-0.57, fdr 1e-04), [[RPAP2]] (-0.56, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EBF2]] → it (grade B ⚠); 5 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **9.52×** | +27.2 | 0e+00 | 28/30 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **9.27×** | +19.0 | 0e+00 | 30/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **8.13×** | +17.9 | 0e+00 | 30/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.39×** | +17.1 | 0e+00 | 28/29 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.58×** | +16.1 | 0e+00 | 26/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **5.03×** | +13.8 | 3e-41 | 22/22 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.21×** | +13.6 | 6e-40 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +13.1 | 3e-37 | 12/20 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +9.1 | 8e-18 | 2/4 (Hs 766T, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **5.50×** | +7.6 | 2e-12 | 19/21 (PANC-1, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +7.0 | 1e-10 | 1/10 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.17×** | +6.6 | 2e-09 | 11/18 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.11×** | +6.4 | 9e-09 | 8/26 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +5.2 | 1e-05 | 5/22 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.32×** | +5.1 | 1e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +4.6 | 1e-04 | 3/15 (NCI-H2347, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.4 | 4e-04 | 4/23 (HOP62, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.002 | 8/24 (SK-MEL-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.005 | 0/20 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6759.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Cepharanthine (drug)]] 5 µM in 1 line (BT-474 0.225×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0568×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -3.5 | 0.25 | 6/33 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.687× | -3.2 | 0.37 | 7/29 (SW480, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.703× | -3.0 | 0.48 | 5/24 (SW480, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 0.797 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 28.4× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 0.971 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 48.0× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 2.54 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +9.8) | — |
| [[A-172 (line)]] | wt | 1.90 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.9× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.225× (z -9.8) |
| [[HCT15 (line)]] | alt | 9.41 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0568× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 1.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.1× (z +9.8) | — |
| [[LoVo (line)]] | wt | 6.30 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.97× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 1.16 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 19.4× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 7.70 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.01× (z +9.8) | — |
| [[SW480 (line)]] | alt | 6.18 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.64× (z +11.6) | — |
| [[A-427 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.635 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.602 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.627 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.859 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.674 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.562 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.448 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.890 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.622 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.939 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM1]] | +0.71 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[HPSE]] | +0.69 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[ATP1A3]] | +0.65 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[SLAIN1]] | +0.65 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[SH3GL3]] | +0.64 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[LINC00937]] | +0.63 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[APBA1]] | +0.61 | +0.35 / +0.70 | both halves | 1e-04 |  |
| [[SHF]] | +0.61 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[CCDC110]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TMEM63C]] | +0.61 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[KCNK13]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.60 | +0.23 / +0.66 | both halves | 5e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.59 | -0.29 / -0.64 | both halves | 2e-04 |  |
| [[C8orf33]] | -0.57 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[RPAP2]] | -0.56 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[NMNAT1]] | -0.55 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[MAPKAPK5]] | -0.55 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[ACAD9]] | -0.55 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[UBE3B]] | -0.55 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ZNF714]] | -0.55 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[C1orf109]] | -0.55 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[UBTF]] | -0.54 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[RABL2B]] | -0.54 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[SPRY3]] | -0.53 | -0.26 / -0.55 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF2]] | B | EBF2 activity raises SUSD4's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without EBF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[LRP2]] | B | LRP2 activity raises SUSD4's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without LRP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[ENTREP2]] | B | ENTREP2 activity raises SUSD4's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without ENTREP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises SUSD4's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without SEPTIN3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[PREX1]] | B | PREX1 activity raises SUSD4's level | lines that do not express PREX1 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without PREX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, SOGA3, PCBP3 |
| [[PARM1]] | B | PARM1 activity raises SUSD4's level | lines that do not express PARM1 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without PARM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | SUSD4 activity lowers LMTK3's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.84× higher at baseline in the lines without SUSD4 | 0.064 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |
| [[NDRG4]] | B | SUSD4 activity raises NDRG4's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without SUSD4 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |
| [[VAV1]] | B | SUSD4 activity lowers VAV1's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.99× higher at baseline in the lines without SUSD4 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |
| [[ADGRB2]] | B | SUSD4 activity raises ADGRB2's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without SUSD4 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |
| [[SLC17A7]] | C | SUSD4 activity raises SLC17A7's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without SUSD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.2, 36.0); signed map (-22.3, 30.3). **Vector** length 51.5, 8.88% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +27.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +17.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.2 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | sushi domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:223,220,819-223,364,233 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10052 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VX71](https://www.uniprot.org/uniprotkb/Q5VX71) (Sushi domain-containing protein 4):

> Acts as a complement inhibitor by disrupting the formation of the classical C3 convertase. Isoform 3 inhibits the classical complement pathway, while membrane-bound isoform 1 inhibits deposition of C3b via both the classical and alternative complement pathways.

**Summary**, from NCBI Gene [55061](https://www.ncbi.nlm.nih.gov/gene/55061):

> Involved in negative regulation of complement activation, alternative pathway and negative regulation of complement activation, classical pathway. Predicted to be located in extracellular region and membrane. Predicted to be active in parallel fiber to Purkinje cell synapse and postsynaptic membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25470) · Entrez [55061](https://www.ncbi.nlm.nih.gov/gene/55061) · UniProt [Q5VX71](https://www.uniprot.org/uniprotkb/Q5VX71) · Ensembl [ENSG00000143502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143502)

## Data

Gene col 6759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6759); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6759]; `tensor/DDL_lfc|DDL_z.npy` [6759]; `embed/gene_vectors.npy` [6759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6759 or target_col == 6759). Every well: [[SUSD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUSD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
