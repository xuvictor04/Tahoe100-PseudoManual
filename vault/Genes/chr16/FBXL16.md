---
symbol: "FBXL16"
type: "gene"
col: 4824
ensembl_id: "ENSG00000127585"
name: "F-box and leucine rich repeat protein 16"
location: "16p13.3"
module: 85
arm: "+"
pooled_cpm: 5.63
n_lines_expressing: 43
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# FBXL16

*F-box and leucine rich repeat protein 16* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +5.7, q 6e-06, up in 10 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +5.0, q 1e-04, up in 16 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.321× (z -15.8, q 0e+00, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.76, fdr 1e-05), [[ANKRD27]] (+0.70, fdr 2e-05), [[FAM118A]] (+0.69, fdr 1e-05); moves opposite to [[PBLD]] (-0.66, fdr 7e-04), [[MCTS1]] (-0.65, fdr 3e-05), [[DECR1]] (-0.64, fdr 2e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); 3 go from it, the strongest it → [[JAG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.7 | 6e-06 | 10/19 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.0 | 1e-04 | 16/40 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.0 | 1e-04 | 5/7 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +4.8 | 3e-04 | 17/39 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.7 | 3e-04 | 12/22 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.012 | 10/39 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.026 | 7/39 (NCI-H460, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.321×** | -15.8 | 0e+00 | 31/35 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.264×** | -12.6 | 6e-34 | 30/37 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.303×** | -11.7 | 2e-29 | 25/34 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -8.0 | 2e-13 | 28/39 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -7.2 | 5e-11 | 22/33 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -6.8 | 8e-10 | 21/39 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.311×** | -6.0 | 2e-07 | 17/30 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -5.8 | 4e-07 | 16/30 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.581×** | -5.3 | 6e-06 | 18/39 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -5.3 | 7e-06 | 19/36 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -5.3 | 8e-06 | 17/38 (SNU-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -5.1 | 2e-05 | 18/39 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -4.8 | 9e-05 | 18/38 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -4.3 | 6e-04 | 17/38 (LS 180, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -4.1 | 0.002 | 17/39 (NCI-H23, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.1) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -17.8) |
| [[A498 (line)]] | wt | 17.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0568× (z -18.9) |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 7.47 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0618× (z -10.6) |
| [[PANC-1 (line)]] | alt | 6.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.9) |
| [[RKO (line)]] | wt | 11.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -10.8) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0724× (z -12.7) |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -10.0) |
| [[HCT15 (line)]] | alt | 8.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -8.5) |
| [[KATO III (line)]] | alt | 9.00 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.4) |
| [[LS 180 (line)]] | wt | 7.24 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 3.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0820× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 2.30 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0702× (z -9.4) |
| [[SW 900 (line)]] | alt | 5.67 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0583× (z -10.3) |
| [[SW1417 (line)]] | alt | 8.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.9) |
| [[A549 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.76 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.70 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FAM118A]] | +0.69 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.69 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[BRAT1]] | +0.68 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.67 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[IGSF8]] | +0.66 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CFD]] | +0.66 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TNNI3]] | +0.65 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.65 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[CABLES2]] | +0.65 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[DOK4]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBLD]] | -0.66 | -0.61 / -0.20 | both halves | 7e-04 |  |
| [[MCTS1]] | -0.65 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[DECR1]] | -0.64 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.63 | -0.57 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[MMADHC-DT]] | -0.63 | -0.58 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[PSME3IP1]] | -0.62 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[VBP1]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZBED5]] | -0.62 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[CRPPA]] | -0.61 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.61 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[EFCAB2]] | -0.60 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[LINC02542]] | -0.60 | -0.54 / -0.28 | both halves | 3e-04 |  |
| [[MCPH1]] | -0.60 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[CPSF2]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises FBXL16's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.53× lower at baseline in the lines without KIF26A | 0.007 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[TOP2A]] | B | TOP2A activity raises FBXL16's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SBK1]] | B | SBK1 activity raises FBXL16's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without SBK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[GNAZ]] | B | GNAZ activity raises FBXL16's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.19× lower at baseline in the lines without GNAZ | 0.027 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FBXL16's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FBXL16's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[JAG2]] | B | JAG2 activity raises FBXL16's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without JAG2 | 0.075 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[CACNA1H]] | B | CACNA1H activity raises FBXL16's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without CACNA1H | 0.077 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3 |
| [[NOVA2]] | B | NOVA2 activity raises FBXL16's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without NOVA2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[EPHA10]] | B | EPHA10 activity raises FBXL16's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without EPHA10 | 0.097 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | FBXL16 activity raises JAG2's level | lines that do not express FBXL16 (7) vs lines expressing it (43) | 2.69× lower at baseline in the lines without FBXL16 | 0.035 | ⚠ within organs, on part of the lines; also absent: SHC2, PLEKHG3 |
| [[FOXK1]] | B | FBXL16 activity raises FOXK1's level | lines that do not express FBXL16 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without FBXL16 | 0.073 | ⚠ within organs, on part of the lines; also absent: SHC2, PLEKHG3 |
| [[KIF26A]] | B | FBXL16 activity raises KIF26A's level | lines that do not express FBXL16 (7) vs lines expressing it (43) | 3.09× lower at baseline in the lines without FBXL16 | 0.096 | ⚠ within organs, on part of the lines; also absent: SHC2, PLEKHG3 |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.782). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.7, 0.4); signed map (-39.9, -4.6). **Vector** length 57.9, 9.35% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:692,498-705,801 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33974, Fbl16; previously C16orf22 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N461](https://www.uniprot.org/uniprotkb/Q8N461) (F-box/LRR-repeat protein 16):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [146330](https://www.ncbi.nlm.nih.gov/gene/146330):

> Members of the F-box protein family, such as FBXL16, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14150) · Entrez [146330](https://www.ncbi.nlm.nih.gov/gene/146330) · UniProt [Q8N461](https://www.uniprot.org/uniprotkb/Q8N461) · Ensembl [ENSG00000127585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127585)

## Data

Gene col 4824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4824); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4824]; `tensor/DDL_lfc|DDL_z.npy` [4824]; `embed/gene_vectors.npy` [4824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4824 or target_col == 4824). Every well: [[FBXL16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
