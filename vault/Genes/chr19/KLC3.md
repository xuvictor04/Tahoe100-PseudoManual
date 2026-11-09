---
symbol: "KLC3"
type: "gene"
col: 2520
ensembl_id: "ENSG00000104892"
name: "kinesin light chain 3"
location: "19q13.32"
module: 208
arm: "+"
pooled_cpm: 4.85
n_lines_expressing: 40
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# KLC3

*kinesin light chain 3* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.53× (z +20.3, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.701× (z -3.9, q 0.064, down in 1 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.238×; ⚠ cell-cycle shift, explains ~2% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDPD5]] (+0.69, fdr 1e-05), [[BMP8B]] (+0.69, fdr 1e-05), [[ATG9B]] (+0.67, fdr 1e-05); moves opposite to [[SNX5]] (-0.59, fdr 4e-05), [[ZFP91]] (-0.59, fdr 7e-05), [[MBNL3]] (-0.58, fdr 4e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIK3CD]] → it (grade B ⚠); 6 go from it, the strongest it → [[SERINC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.53×** | +20.3 | 0e+00 | 36/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.09×** | +19.5 | 0e+00 | 35/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.12×** | +15.3 | 0e+00 | 35/36 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +14.3 | 3e-44 | 24/31 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +10.8 | 5e-25 | 2/8 (SW1417, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +10.0 | 2e-21 | 6/18 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +9.8 | 7e-21 | 27/36 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +7.8 | 3e-13 | 18/33 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +7.0 | 2e-10 | 19/36 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +6.9 | 3e-10 | 23/34 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.6 | 9e-07 | 10/20 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.5 | 2e-06 | 12/34 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 4e-05 | 8/31 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.7 | 1e-04 | 4/11 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.4 | 5e-04 | 0/14 | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +4.3 | 5e-04 | 5/27 (AsPC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 3/36 (HOP62, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.003 | 13/30 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.004 | 11/36 (A498, Panc 03.27, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.007 | 7/22 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2520.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.238×; ⚠ cell-cycle shift, explains ~2% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.701×** | -3.9 | 0.064 | 1/37 (SW 900) | two highest doses | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.703×** | -3.6 | 0.079 | 5/35 (PANC-1, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.735× | -3.4 | 0.14 | 7/36 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.743× | -3.3 | 0.15 | 10/35 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.746× | -3.2 | 0.15 | 4/37 (CFPAC-1, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 14.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.51× (z +11.4) | — |
| [[SW480 (line)]] | alt | 5.72 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.59× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.22× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 1.84 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 43.3× (z +9.1) | — |
| [[KATO III (line)]] | alt | 2.55 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 43.2× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 5.64 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.67× (z +8.8) | — |
| [[LoVo (line)]] | wt | 7.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.62× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -9.4) ⚠ cell-cycle shift, explains ~2% of this change |
| [[NCI-H460 (line)]] | wt | 1.71 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDPD5]] | +0.69 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BMP8B]] | +0.69 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ATG9B]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.67 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SLC17A7]] | +0.66 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RTN2]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 | STRING 566 |
| [[F11R]] | +0.66 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GIPR]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[RAB11FIP1]] | +0.65 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[CDC34]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX5]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZFP91]] | -0.59 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[MBNL3]] | -0.58 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.58 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ECHDC1]] | -0.57 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MCCC2]] | -0.57 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[XRCC5]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[SENP1]] | -0.56 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[SLC12A2-DT]] | -0.56 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZMYND11]] | -0.56 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[DECR1]] | -0.55 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.55 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CD]] | B | PIK3CD activity raises KLC3's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 1.97× lower at baseline in the lines without PIK3CD | 0.033 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[PDE4D]] | B | PDE4D activity lowers KLC3's level | lines that do not express PDE4D (13) vs lines expressing it (37) | 1.78× higher at baseline in the lines without PDE4D | 0.045 | ⚠ within organs, on part of the lines; also absent: RGS2, LINC02269; maybe low, not absent |
| [[RGS9]] | B | RGS9 activity raises KLC3's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 2.03× lower at baseline in the lines without RGS9 | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |
| [[MAP3K9-DT]] | B | MAP3K9-DT activity raises KLC3's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 1.82× lower at baseline in the lines without MAP3K9-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[S100A14]] | B | S100A14 activity raises KLC3's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.94× lower at baseline in the lines without S100A14 | 0.083 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[LMTK3]] | B | LMTK3 activity raises KLC3's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.80× lower at baseline in the lines without LMTK3 | 0.084 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERINC2]] | B | KLC3 activity raises SERINC2's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 2.66× lower at baseline in the lines without KLC3 | 0.084 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent |
| [[LMTK3]] | B | KLC3 activity raises LMTK3's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 2.26× lower at baseline in the lines without KLC3 | 0.087 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent |
| [[ESAM]] | B | KLC3 activity strengthens ESAM's drug response | lines that do not express KLC3 (8) vs lines expressing it (34) | the lines without KLC3 respond the other way (z diff +2.14); strongest at Topotecan (hydrochloride) 5 µM: 0.08x vs 1.15x (z diff +8.7) | 0.094 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CAPG]] | B | KLC3 activity raises CAPG's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without KLC3 | 0.097 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent |
| [[BMP8B]] | B | KLC3 activity raises BMP8B's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 1.78× lower at baseline in the lines without KLC3 | 0.098 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent |
| [[PRKCZ]] | C | KLC3 activity raises PRKCZ's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without KLC3 | 0.064 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.5, -0.1); signed map (-24.7, 23.1). **Vector** length 69.3, 14.1% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +20.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +19.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.6 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin light chain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,333,434-45,351,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KLC2L, KNS2B, KLCt |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 17 pathways, smallest: RHO GTPases activate KTN1; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P597](https://www.uniprot.org/uniprotkb/Q6P597) (Kinesin light chain 3):

> Kinesin is a microtubule-associated force-producing protein that may play a role in organelle transport. Plays a role during spermiogenesis in the development of the sperm tail midpiece and in the normal function of spermatozoa (By similarity). May play a role in the formation of the mitochondrial sheath formation in the developing spermatid midpiece (By similarity).

**Summary**, from NCBI Gene [147700](https://www.ncbi.nlm.nih.gov/gene/147700):

> This gene encodes a member of the kinesin light chain gene family. Kinesins are molecular motors involved in the transport of cargo along microtubules, and are composed of two kinesin heavy chain (KHC) and two kinesin light chain (KLC) molecules. KLCs are thought to typically be involved in binding cargo and regulating kinesin activity. In the rat, a protein similar to this gene product is expressed in post-meiotic spermatids, where it associates with structural components of sperm tails and …

**Accessions** — [HGNC:20717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20717) · Entrez [147700](https://www.ncbi.nlm.nih.gov/gene/147700) · UniProt [Q6P597](https://www.uniprot.org/uniprotkb/Q6P597) · Ensembl [ENSG00000104892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104892)

## Data

Gene col 2520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2520); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2520]; `tensor/DDL_lfc|DDL_z.npy` [2520]; `embed/gene_vectors.npy` [2520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2520 or target_col == 2520). Every well: [[KLC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
