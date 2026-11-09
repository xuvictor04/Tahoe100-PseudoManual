---
symbol: "HEYL"
type: "gene"
col: 8806
ensembl_id: "ENSG00000163909"
name: "hes related family bHLH transcription factor with YRPW motif like"
location: "1p34.2"
module: 82
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 25
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# HEYL

*hes related family bHLH transcription factor with YRPW motif like* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.48× (z +9.3, q 1e-17, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.20× (z +7.3, q 7e-11, up in 13 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.159×, SW480 0.235×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0568×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMP8B]] (+0.64, fdr 4e-05), [[SEMA3F]] (+0.60, fdr 3e-05), [[CARMIL2]] (+0.59, fdr 1e-04); moves opposite to [[TBC1D5]] (-0.51, fdr 3e-05), [[MFF-DT]] (-0.51, fdr 6e-04), [[C5orf15]] (-0.50, fdr 4e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PDZD4]] → it (grade B ⚠); 2 go from it, the strongest it → [[ACOXL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +9.3 | 1e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +7.7 | 4e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +7.3 | 7e-11 | 13/19 (NCI-H2347, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +6.1 | 1e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.62×** | +6.0 | 2e-07 | 1/5 (A549) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +5.9 | 5e-07 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +5.8 | 5e-07 | 19/22 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.43×** | +5.8 | 5e-07 | 16/21 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +5.0 | 5e-05 | 9/21 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.04×** | +4.7 | 2e-04 | 9/16 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +4.4 | 5e-04 | 1/8 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.95×** | +4.3 | 7e-04 | 1/13 (LoVo) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.2 | 0.001 | 1/14 (NCI-H2030) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.1 | 0.002 | 2/11 (NCI-H460, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.0 | 0.002 | 2/12 (NCI-H460, SHP-77) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +4.0 | 0.002 | 1/9 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.010 | 1/15 (NCI-H1573) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.06×** | +3.3 | 0.026 | 1/11 (A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.035 | 1/12 (PANC-1) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.63×** | +3.2 | 0.045 | 0/9 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.62×** | +3.1 | 0.050 | 0/13 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.85×** | +3.1 | 0.050 | 1/13 (NCI-H460) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.080 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.56×** | +2.9 | 0.087 | 2/11 (NCI-H23, SW480) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8806.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.159×, SW480 0.235×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.0568×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Econazole (drug)]] 0.5 µM |  | 0.593× | -3.5 | 0.22 | 1/20 (hTERT-HPNE) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.607× | -3.4 | 0.22 | 2/19 (A-427, PANC-1) | inconsistent across doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.533× | -3.2 | 0.22 | 1/20 (NCI-H2030) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.14 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0568× (z -10.1) |
| [[SW480 (line)]] | alt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -9.1) |
| [[A-172 (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.202 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMP8B]] | +0.64 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SEMA3F]] | +0.60 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CARMIL2]] | +0.59 | +0.49 / +0.33 | both halves | 1e-04 |  |
| [[KCTD17]] | +0.58 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[KCNK3]] | +0.57 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[ESYT3]] | +0.57 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ETNK2]] | +0.57 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[BAIAP3]] | +0.57 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[GPRIN1]] | +0.56 | +0.39 / +0.38 | both halves | 7e-05 |  |
| [[LHX6]] | +0.56 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[KIF21B]] | +0.56 | +0.37 / +0.39 | both halves | 9e-05 |  |
| [[RIMS3]] | +0.56 | +0.35 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D5]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.51 | -0.27 / -0.22 | both halves | 6e-04 |  |
| [[C5orf15]] | -0.50 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[PSME3IP1]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.50 | -0.22 / -0.28 | both halves | 6e-04 |  |
| [[MCTS1]] | -0.49 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[METTL4]] | -0.47 | -0.20 / -0.32 | both halves | 7e-04 |  |
| [[UBE3B]] | -0.47 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[CDK2AP1]] | -0.47 | -0.22 / -0.28 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZD4]] | B | PDZD4 activity raises HEYL's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.64× lower at baseline in the lines without PDZD4 | 0.023 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[ADAMTS18]] | B | ADAMTS18 activity raises HEYL's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without ADAMTS18 | 0.035 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[VAT1L]] | B | VAT1L activity raises HEYL's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without VAT1L | 0.061 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises HEYL's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.06× lower at baseline in the lines without PLEKHG4B | 0.003 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[DAGLA]] | C | DAGLA activity raises HEYL's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.29× lower at baseline in the lines without DAGLA | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[FXYD6]] | C | FXYD6 activity raises HEYL's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without FXYD6 | 0.085 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOXL]] | B | HEYL activity raises ACOXL's level | lines that do not express HEYL (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without HEYL | 0.060 | ⚠ within organs, on part of the lines; also absent: HCG11, GAL, LRRN2 |
| [[MOCS1]] | B | HEYL activity raises MOCS1's level | lines that do not express HEYL (25) vs lines expressing it (25) | 1.15× lower at baseline in the lines without HEYL | 0.084 | ⚠ within organs, on part of the lines; also absent: HCG11, GAL, LRRN2 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.1, 32.7); signed map (-24.5, 33.2). **Vector** length 36.8, 7.82% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.8 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +5.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +3.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.7 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | hes related family bHLH transcription factor with YRPW motif like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:39,623,435-39,639,643 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHb33, HEY3, HESR3 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Hey bHLH transcription factor family |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 19 pathways, smallest: Regulation of CDH11 gene transcription; NOTCH3 Intracellular Domain Regulates Transcription; Regulation of CDH11 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ87](https://www.uniprot.org/uniprotkb/Q9NQ87) (Hairy/enhancer-of-split related with YRPW motif-like protein):

> Downstream effector of Notch signaling which may be required for cardiovascular development (By similarity). Transcriptional repressor which binds preferentially to the canonical E box sequence 5'-CACGTG-3' (By similarity). Represses transcription by the cardiac transcriptional activators GATA4 and GATA6.

**Summary**, from NCBI Gene [26508](https://www.ncbi.nlm.nih.gov/gene/26508):

> This gene encodes a member of the hairy and enhancer of split-related (HESR) family of basic helix-loop-helix (bHLH)-type transcription factors. The sequence of the encoded protein contains a conserved bHLH and orange domain, but its YRPW motif has diverged from other HESR family members. It is thought to be an effector of Notch signaling and a regulator of cell fate decisions. Alternatively spliced transcript variants have been found, but their biological validity has not been determined. …

**Accessions** — [HGNC:4882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4882) · Entrez [26508](https://www.ncbi.nlm.nih.gov/gene/26508) · UniProt [Q9NQ87](https://www.uniprot.org/uniprotkb/Q9NQ87) · Ensembl [ENSG00000163909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163909)

## Data

Gene col 8806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8806); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8806]; `tensor/DDL_lfc|DDL_z.npy` [8806]; `embed/gene_vectors.npy` [8806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8806 or target_col == 8806). Every well: [[HEYL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEYL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
