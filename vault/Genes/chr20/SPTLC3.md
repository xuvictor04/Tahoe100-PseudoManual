---
symbol: "SPTLC3"
type: "gene"
col: 10236
ensembl_id: "ENSG00000172296"
name: "serine palmitoyltransferase long chain base subunit 3"
location: "20p12.1"
module: 8
arm: "+"
pooled_cpm: 8.51
n_lines_expressing: 34
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 19
direction_downstream: 33
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SPTLC3

*serine palmitoyltransferase long chain base subunit 3* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.41× (z +12.0, q 4e-30, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.572× (z -5.4, q 2e-05, down in 19 of 31 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.572× (z -5.4, q 2e-05, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX1]] (+0.61, fdr 1e-05), [[SLC40A1]] (+0.60, fdr 1e-05), [[ARID5B]] (+0.57, fdr 1e-05); moves opposite to [[ZFYVE21]] (-0.57, fdr 1e-05), [[TPTEP2-CSNK1E]] (-0.55, fdr 1e-05), [[FBH1]] (-0.55, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[GDA]] → it (grade B ⚠); 33 go from it, the strongest it → [[LIMA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +12.0 | 4e-30 | 30/31 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.0 | 4e-17 | 11/26 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.0 | 4e-17 | 4/15 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.42×** | +8.5 | 3e-15 | 27/31 (KATO III, SW 900, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +6.4 | 2e-08 | 19/30 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +5.2 | 2e-05 | 21/31 (RPMI-7951, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.72×** | +5.2 | 2e-05 | 14/31 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.0 | 3e-05 | 20/32 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.66×** | +5.0 | 3e-05 | 17/32 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.0 | 3e-05 | 14/31 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.0 | 3e-05 | 6/19 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 3e-04 | 12/31 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +4.4 | 4e-04 | 17/31 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +4.3 | 6e-04 | 15/32 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 6e-04 | 12/29 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.001 | 14/30 (LoVo, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.002 | 15/30 (LS 180, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +3.9 | 0.003 | 12/31 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.020 | 9/31 (HEC-1-A, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.572×** | -5.4 | 2e-05 | 19/31 (H4, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -5.4 | 2e-05 | 21/31 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -4.5 | 0.001 | 14/31 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.639×** | -4.3 | 0.002 | 14/31 (H4, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -4.1 | 0.004 | 18/31 (LS 180, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.1 | 0.004 | 16/31 (NCI-H1792, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.491×** | -3.6 | 0.029 | 12/29 (LoVo, SW 1088, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -3.5 | 0.029 | 11/31 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.711× | -3.1 | 0.12 | 12/31 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 46.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -15.7) |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -16.9) |
| [[A498 (line)]] | wt | 7.35 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0608× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[HEC-1-A (line)]] | alt | 31.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 19.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.82× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -9.0) |
| [[COLO 205 (line)]] | alt | 6.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0553× (z -8.9) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.138× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 6.05 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0498× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 3.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.35× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -10.6) |
| [[SW 900 (line)]] | alt | 9.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0887× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.52 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.87× (z +9.1) | — |
| [[A-172 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX1]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ARID5B]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MECOM]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[AKR1C3]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[FIGN]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[LNX1]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[HAVCR1]] | +0.52 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[C4orf19]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE21]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[FBH1]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SHPK]] | -0.53 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[CTNNBIP1]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MLYCD]] | -0.50 | -0.20 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[MROH1]] | -0.50 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[GLE1]] | -0.49 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[AXIN1]] | -0.49 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[PTPN9]] | -0.48 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[KCTD5]] | -0.48 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[TAF12]] | -0.48 | -0.21 / -0.37 | both halves | 7e-04 |  |
| [[GMIP]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 15, C 4. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDA]] | B | GDA activity raises SPTLC3's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without GDA | 0.011 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[PPARGC1A]] | B | PPARGC1A activity raises SPTLC3's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without PPARGC1A | 0.020 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[BICC1]] | B | BICC1 activity raises SPTLC3's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without BICC1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[SMIM10]] | B | SMIM10 activity raises SPTLC3's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without SMIM10 | 0.031 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[ARSL]] | B | ARSL activity raises SPTLC3's level | lines that do not express ARSL (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without ARSL | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[PALLD]] | B | PALLD activity raises SPTLC3's level | lines that do not express PALLD (11) vs lines expressing it (39) | 2.64× lower at baseline in the lines without PALLD | 0.040 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, PAG1; maybe low, not absent |
| [[ALDH3B1]] | B | ALDH3B1 activity raises SPTLC3's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.33× lower at baseline in the lines without ALDH3B1 | 0.041 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[CFH]] | B | CFH activity raises SPTLC3's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without CFH | 0.042 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[MEF2C]] | B | MEF2C activity raises SPTLC3's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without MEF2C | 0.056 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[EFEMP1]] | B | EFEMP1 activity raises SPTLC3's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.54× lower at baseline in the lines without EFEMP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |
| [[MAP2K1]] | B | MAP2K1 activity lowers SPTLC3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF608]] | B | ZNF608 activity raises SPTLC3's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without ZNF608 | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 28, C 5. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIMA1]] | B | SPTLC3 activity raises LIMA1's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without SPTLC3 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | B | SPTLC3 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.79× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 0.5 µM | B | SPTLC3 activity raises the cells' numbers under Trifluridine 0.5 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.88× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[ANK3]] | B | SPTLC3 activity raises ANK3's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 1.95× lower at baseline in the lines without SPTLC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | SPTLC3 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.18× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[PLSCR4]] | B | SPTLC3 activity raises PLSCR4's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without SPTLC3 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[GDA]] | B | SPTLC3 activity raises GDA's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without SPTLC3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | SPTLC3 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.20× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | SPTLC3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.85× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[EFEMP1]] | B | SPTLC3 activity raises EFEMP1's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without SPTLC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[ALCAM]] | B | SPTLC3 activity raises ALCAM's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without SPTLC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| cells under [[Erythromycin (drug)]] 0.5 µM | B | SPTLC3 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.20× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, 42.9); signed map (50.1, 17.6). **Vector** length 68.5, 14.8% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | serine palmitoyltransferase long chain base subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:13,008,972-13,169,103 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LCB2B, FLJ11112, hLCB2b; previously C20orf38, SPTLC2L |
| Gene groups (HGNC) | Serine palmitoyltransferase long chain base subunits |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUV7](https://www.uniprot.org/uniprotkb/Q9NUV7) (Serine palmitoyltransferase 3):

> Component of the serine palmitoyltransferase multisubunit enzyme (SPT) that catalyzes the initial and rate-limiting step in sphingolipid biosynthesis by condensing L-serine and activated acyl-CoA (most commonly palmitoyl-CoA) to form long-chain bases. The SPT complex is composed of SPTLC1, SPTLC2 or SPTLC3 and SPTSSA or SPTSSB. Within this complex, the heterodimer consisting of SPTLC1 and SPTLC2/SPTLC3 forms the catalytic core. The composition of the serine palmitoyltransferase (SPT) complex …

**Summary**, from NCBI Gene [55304](https://www.ncbi.nlm.nih.gov/gene/55304):

> This gene encodes a subunit of the serine palmitoyltransferase complex which catalyzes the rate-limiting step in sphingolipid biosynthesis. This subunit metabolizes lauroyl- and myristoyl-CoA and generates C14 and C16-sphingoid bases. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:16253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16253) · Entrez [55304](https://www.ncbi.nlm.nih.gov/gene/55304) · UniProt [Q9NUV7](https://www.uniprot.org/uniprotkb/Q9NUV7) · Ensembl [ENSG00000172296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172296)

## Data

Gene col 10236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10236); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10236]; `tensor/DDL_lfc|DDL_z.npy` [10236]; `embed/gene_vectors.npy` [10236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10236 or target_col == 10236). Every well: [[SPTLC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTLC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
