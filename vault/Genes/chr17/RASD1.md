---
symbol: "RASD1"
type: "gene"
col: 2963
ensembl_id: "ENSG00000108551"
name: "ras related dexamethasone induced 1"
location: "17p11.2"
module: 109
arm: "+"
pooled_cpm: 5.57
n_lines_expressing: 29
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# RASD1

*ras related dexamethasone induced 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 11.9× (z +17.8, q 0e+00, up in 11 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +11.5, q 1e-28, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.461× (z -5.2, q 9e-05, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPAS1]] (+0.59, fdr 1e-05), [[ZSWIM6]] (+0.56, fdr 3e-05), [[SGK1]] (+0.56, fdr 1e-05); moves opposite to [[GUSBP2-1]] (-0.45, fdr 3e-04), [[RFXAP]] (-0.44, fdr 5e-05), [[CDC23]] (-0.42, fdr 1e-04).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RAB31]] → it (grade B ⚠); 10 go from it, the strongest it → [[SMOX]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **11.9×** | +17.8 | 0e+00 | 11/15 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.20×** | +12.6 | 7e-34 | 5/9 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +11.5 | 1e-28 | 8/20 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **4.24×** | +10.4 | 5e-23 | 10/21 (PANC-1, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.49×** | +10.0 | 2e-21 | 6/12 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.33×** | +8.6 | 6e-16 | 13/22 (A549, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.13×** | +8.2 | 2e-14 | 13/24 (SW480, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.7 | 9e-07 | 7/15 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.71×** | +5.5 | 3e-06 | 4/20 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +5.4 | 4e-06 | 10/23 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.06×** | +5.2 | 1e-05 | 6/22 (SHP-77, SW 900, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.91×** | +4.6 | 2e-04 | 2/19 (CFPAC-1, SW1417) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.93×** | +4.5 | 2e-04 | 3/20 (SW480, SW1417, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.005 | 7/23 (HOP62, A549, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +3.7 | 0.008 | 9/21 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.461×** | -5.2 | 9e-05 | 14/24 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.508×** | -4.7 | 8e-04 | 12/20 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.666×** | -4.1 | 0.007 | 11/23 (A549, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.542×** | -4.1 | 0.007 | 11/23 (BT-474, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.573×** | -3.9 | 0.013 | 11/22 (SHP-77, HS-578T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.701×** | -3.5 | 0.037 | 10/23 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.623× | -3.1 | 0.12 | 5/23 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.646× | -3.1 | 0.12 | 8/24 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.448× | -3.0 | 0.16 | 1/23 (BT-474) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 62.8 | 1 | 3 (2 ⚠) | [[Betamethasone dipropionate (drug)]] 0.5 µM 6.14× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H1792 (line)]] | alt | 6.94 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0527× (z -9.0) |
| [[PANC-1 (line)]] | alt | 1.84 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.9× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPAS1]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ZSWIM6]] | +0.56 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[SGK1]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[MCL1]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TCIM]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[EGR3]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PITPNC1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ATP2B1]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[EGR2]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[RGS2]] | +0.51 | +0.40 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP2-1]] | -0.45 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[RFXAP]] | -0.44 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CDC23]] | -0.42 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB31]] | B | RAB31 activity raises RASD1's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 1.01× lower at baseline in the lines without RAB31 | 0.082 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |
| [[TOP2A]] | B | TOP2A activity lowers RASD1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises RASD1's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SHC4]] | B | SHC4 activity raises RASD1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without SHC4 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMOX]] | B | RASD1 activity raises SMOX's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without RASD1 | 0.066 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[HES1]] | B | RASD1 activity raises HES1's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.21× lower at baseline in the lines without RASD1 | 0.072 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| cells under [[Dinaciclib (drug)]] 5 µM | B | RASD1 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express RASD1 (21) vs lines expressing it (27) | the lines without RASD1: 0.50× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[ARC]] | B | RASD1 activity raises ARC's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without RASD1 | 0.083 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| cells under [[Dinaciclib (drug)]] 0.5 µM | B | RASD1 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express RASD1 (21) vs lines expressing it (27) | the lines without RASD1: 0.50× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[ADGRE2]] | B | RASD1 activity raises ADGRE2's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without RASD1 | 0.093 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[SLC38A2]] | B | RASD1 activity lowers SLC38A2's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.14× higher at baseline in the lines without RASD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[EGR2]] | B | RASD1 activity raises EGR2's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without RASD1 | 0.097 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| cells under [[Brivudine (drug)]] 5 µM | B | RASD1 activity raises the cells' numbers under Brivudine 5 µM (protects the cells) | lines that do not express RASD1 (21) vs lines expressing it (27) | the lines without RASD1: 0.78× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | RASD1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express RASD1 (21) vs lines expressing it (27) | the lines without RASD1: 0.67× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.5, 9.1); signed map (9.6, 30.3). **Vector** length 48.9, 10.7% of its response variance represented; |z| ≥ 3 in 528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +10.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -4.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ras related dexamethasone induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,494,437-17,496,395 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEXRAS1, AGS1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y272](https://www.uniprot.org/uniprotkb/Q9Y272) (Dexamethasone-induced Ras-related protein 1):

> Small GTPase. Negatively regulates the transcription regulation activity of the APBB1/FE65-APP complex via its interaction with APBB1/FE65 (By similarity).

**Summary**, from NCBI Gene [51655](https://www.ncbi.nlm.nih.gov/gene/51655):

> This gene encodes a member of the Ras superfamily of small GTPases and is induced by dexamethasone. The encoded protein is an activator of G-protein signaling and acts as a direct nucleotide exchange factor for Gi-Go proteins. This protein interacts with the neuronal nitric oxide adaptor protein CAPON, and a nuclear adaptor protein FE65, which interacts with the Alzheimer's disease amyloid precursor protein. This gene may play a role in dexamethasone-induced alterations in cell morphology, …

**Accessions** — [HGNC:15828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15828) · Entrez [51655](https://www.ncbi.nlm.nih.gov/gene/51655) · UniProt [Q9Y272](https://www.uniprot.org/uniprotkb/Q9Y272) · Ensembl [ENSG00000108551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108551)

## Data

Gene col 2963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2963); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2963]; `tensor/DDL_lfc|DDL_z.npy` [2963]; `embed/gene_vectors.npy` [2963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2963 or target_col == 2963). Every well: [[RASD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
