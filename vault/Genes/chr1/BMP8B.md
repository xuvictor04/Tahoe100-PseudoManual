---
symbol: "BMP8B"
type: "gene"
col: 3862
ensembl_id: "ENSG00000116985"
name: "bone morphogenetic protein 8b"
location: "1p34.2"
module: 82
arm: "+"
pooled_cpm: 2.47
n_lines_expressing: 45
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# BMP8B

*bone morphogenetic protein 8b* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.18× (z +17.8, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.424× (z -8.1, q 3e-13, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC3]] (+0.69, fdr 1e-05), [[JAG2]] (+0.66, fdr 3e-05), [[TNK2]] (+0.66, fdr 4e-05); moves opposite to [[TIA1]] (-0.64, fdr 6e-05), [[RBM23]] (-0.59, fdr 2e-04), [[DECR1]] (-0.58, fdr 1e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 3 go from it, the strongest it → [[RTN4R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.18×** | +17.8 | 0e+00 | 39/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.91×** | +17.4 | 0e+00 | 36/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.84×** | +13.2 | 3e-37 | 32/38 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +9.5 | 4e-19 | 27/39 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +8.5 | 2e-15 | 25/39 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +7.6 | 4e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.2 | 4e-08 | 3/10 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.8 | 4e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.8 | 4e-07 | 10/30 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +4.7 | 1e-04 | 6/24 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.41×** | +4.5 | 3e-04 | 5/36 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 8e-04 | 10/36 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.007 | 3/24 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.011 | 7/23 (A549, SW480, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.5 | 0.020 | 6/41 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.035 | 3/25 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.048 | 1/38 (BT-474) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.056 | 3/11 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Proglumide (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.057 | 3/33 (SW48, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.424×** | -8.1 | 3e-13 | 23/36 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -7.5 | 2e-11 | 22/39 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.608×** | -6.9 | 9e-10 | 17/31 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -5.2 | 2e-05 | 15/34 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -4.5 | 8e-04 | 12/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -4.4 | 8e-04 | 10/34 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.693×** | -3.6 | 0.025 | 9/21 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.700×** | -3.5 | 0.032 | 6/41 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.546× | -3.1 | 0.12 | 8/25 (NCI-H2347, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.84 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.6× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 0.788 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.866 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.757 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC3]] | +0.69 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[JAG2]] | +0.66 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[TNK2]] | +0.66 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[FCHSD1]] | +0.65 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[BAIAP3]] | +0.64 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[HEYL]] | +0.64 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[LHX6]] | +0.64 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[SPTLC2]] | +0.63 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[AIF1L]] | +0.63 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[IGSF8]] | +0.62 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[ZDHHC9]] | +0.62 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[FBXL16]] | +0.62 | +0.35 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.64 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[RBM23]] | -0.59 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[DECR1]] | -0.58 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[MCTS1]] | -0.58 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[NDUFS1]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[CASC9]] | -0.57 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[TBCK]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SENP1]] | -0.57 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CCAR1]] | -0.57 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.57 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[NDUFB5]] | -0.56 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.56 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises BMP8B's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without RASGEF1A | 0.023 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[ABCA3]] | B | ABCA3 activity raises BMP8B's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without ABCA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[SNTA1]] | B | SNTA1 activity raises BMP8B's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without SNTA1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises BMP8B's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without SLC29A4 | 0.052 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises BMP8B's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without JAG2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[HES2]] | B | HES2 activity raises BMP8B's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without HES2 | 0.076 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[SCN5A]] | B | SCN5A activity raises BMP8B's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 1.41× lower at baseline in the lines without SCN5A | 0.087 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[RGS9]] | B | RGS9 activity raises BMP8B's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without RGS9 | 0.097 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |
| [[KLC3]] | B | KLC3 activity raises BMP8B's level | lines that do not express KLC3 (10) vs lines expressing it (40) | 1.78× lower at baseline in the lines without KLC3 | 0.098 | ⚠ within organs, on part of the lines; also absent: PRKCZ, VWA1, PNPLA4; maybe low, not absent |
| [[PBX4]] | C | PBX4 activity raises BMP8B's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without PBX4 | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTN4R]] | B | BMP8B activity raises RTN4R's level | lines that do not express BMP8B (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without BMP8B | 0.067 | ⚠ within organs, on part of the lines; also absent: PBX4, SPECC1, CTSV; maybe low, not absent; its own permutation p |
| [[GAS2L1]] | B | BMP8B activity lowers GAS2L1's level | lines that do not express BMP8B (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without BMP8B | 0.067 | ⚠ within organs, on part of the lines; also absent: PBX4, SPECC1, CTSV; maybe low, not absent; its own permutation p |
| [[MMP15]] | B | BMP8B activity raises MMP15's level | lines that do not express BMP8B (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without BMP8B | 0.073 | ⚠ within organs, on part of the lines; also absent: PBX4, SPECC1, CTSV; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.6, -0.9); signed map (-23.9, 33.5). **Vector** length 49.7, 6.65% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +6.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.0 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -0.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -0.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 8b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:39,757,182-39,788,865 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OP-2; previously BMP8 |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P34820](https://www.uniprot.org/uniprotkb/P34820) (Bone morphogenetic protein 8B):

> Induces cartilage and bone formation. May be the osteoinductive factor responsible for the phenomenon of epithelial osteogenesis. Plays a role in calcium regulation and bone homeostasis (By similarity).

**Summary**, from NCBI Gene [656](https://www.ncbi.nlm.nih.gov/gene/656):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. The encoded protein stimulates thermogenesis in brown adipose tissue. Expression of this gene may be …

**Accessions** — [HGNC:1075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1075) · Entrez [656](https://www.ncbi.nlm.nih.gov/gene/656) · UniProt [P34820](https://www.uniprot.org/uniprotkb/P34820) · Ensembl [ENSG00000116985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116985)

## Data

Gene col 3862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3862); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3862]; `tensor/DDL_lfc|DDL_z.npy` [3862]; `embed/gene_vectors.npy` [3862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3862 or target_col == 3862). Every well: [[BMP8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
