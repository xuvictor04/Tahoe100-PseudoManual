---
symbol: "AFAP1L2"
type: "gene"
col: 9758
ensembl_id: "ENSG00000169129"
name: "actin filament associated protein 1 like 2"
location: "10q25.3"
module: 55
arm: "+"
pooled_cpm: 22.52
n_lines_expressing: 23
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 27
direction_downstream: 24
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# AFAP1L2

*actin filament associated protein 1 like 2* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.10× (z +15.8, q 0e+00, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.680× (z -5.8, q 4e-06, down in 16 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.694× (z -5.5, q 1e-05, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC52A3]] (+0.77, fdr 7e-06), [[LGR6]] (+0.77, fdr 7e-06), [[SLC5A1]] (+0.72, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[VSIR]] → it (grade B ⚠); 24 go from it, the strongest it → [[VSIR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +15.8 | 0e+00 | 12/21 (SW 900, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +9.6 | 2e-19 | 11/20 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +9.6 | 2e-19 | 7/18 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +9.3 | 2e-18 | 6/17 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.1 | 1e-17 | 3/15 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.5 | 3e-06 | 10/21 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +4.3 | 0.002 | 7/21 (LoVo, KATO III, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.029 | 6/21 (SW 900, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.033 | 6/21 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.045 | 5/19 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.067 | 3/21 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.22× | +3.0 | 0.11 | 7/21 (KATO III, Hs 766T, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.11 | 0/20 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -5.8 | 4e-06 | 16/20 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -5.5 | 1e-05 | 16/21 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -5.2 | 5e-05 | 11/20 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.729×** | -4.7 | 3e-04 | 6/20 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -4.3 | 0.002 | 7/20 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.610×** | -3.9 | 0.010 | 15/21 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.613×** | -3.8 | 0.010 | 4/21 (Hs 766T, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.763×** | -3.7 | 0.013 | 1/20 (SW480) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.013 | 10/21 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.013 | 11/20 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.041 | 5/21 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.044 | 5/21 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.799×** | -3.2 | 0.055 | 7/20 (COLO 205, SW480, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 134 | 0 | 25 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.1) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.184× (z -14.6) |
| [[LoVo (line)]] | wt | 34.4 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -13.8) |
| [[COLO 205 (line)]] | alt | 110 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -21.0) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -10.1) |
| [[HT-29 (line)]] | alt | 42.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.8) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.225× (z -10.5) |
| [[Hs 766T (line)]] | wt | 96.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.0) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 65.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 46.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.2) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.0) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0228× (z -18.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 6.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.64 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0849× (z -10.0) |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC52A3]] | +0.77 | +0.76 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LGR6]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC5A1]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.70 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[CYP2S1]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SKAP1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | same gene group |
| [[INPP5D]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[VWA2]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[EDAR]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[HR]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 5, C 22. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | VSIR activity raises AFAP1L2's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.95× lower at baseline in the lines without VSIR | 0.002 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[TSPAN2]] | B | TSPAN2 activity raises AFAP1L2's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without TSPAN2 | 0.023 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[ALS2CL]] | B | ALS2CL activity raises AFAP1L2's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.92× lower at baseline in the lines without ALS2CL | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AFAP1L2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LASTR]] | B | LASTR activity raises AFAP1L2's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.63× lower at baseline in the lines without LASTR | 0.089 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[CAPN8]] | C | CAPN8 activity raises AFAP1L2's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 4.25× lower at baseline in the lines without CAPN8 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises AFAP1L2's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 4.23× lower at baseline in the lines without VWA2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[PPARG]] | C | PPARG activity raises AFAP1L2's level | lines that do not express PPARG (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without PPARG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL; co-absent with the target |
| [[ANO1]] | C | ANO1 activity raises AFAP1L2's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without ANO1 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises AFAP1L2's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without HSD17B2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[CALB1]] | C | CALB1 activity raises AFAP1L2's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 4.78× lower at baseline in the lines without CALB1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises AFAP1L2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 4.56× lower at baseline in the lines without SLC5A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 11, C 13. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | AFAP1L2 activity raises VSIR's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without AFAP1L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[ARHGEF3]] | B | AFAP1L2 activity raises ARHGEF3's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without AFAP1L2 | 0.011 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| cells under [[Trametinib (drug)]] 0.05 µM | B | AFAP1L2 activity lowers the cells' numbers under Trametinib 0.05 µM (makes them more sensitive) | lines that do not express AFAP1L2 (27) vs lines expressing it (21) | the lines without AFAP1L2: 1.11× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[DTX2P1]] | B | AFAP1L2 activity raises DTX2P1's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without AFAP1L2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[VPS37B]] | B | AFAP1L2 activity raises VPS37B's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without AFAP1L2 | 0.038 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[IGSF9]] | B | AFAP1L2 activity raises IGSF9's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without AFAP1L2 | 0.061 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[TSPAN2]] | B | AFAP1L2 activity raises TSPAN2's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without AFAP1L2 | 0.068 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[DLG3]] | B | AFAP1L2 activity strengthens DLG3's drug response | lines that do not express AFAP1L2 (23) vs lines expressing it (19) | the lines without AFAP1L2 respond 0.66× as strongly (z diff +1.55); strongest at Homoharringtonine 0.5 µM: 0.48x vs 0.31x (z diff +3.9) | 0.076 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH; target measured in part of the lines; artifact flags |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM | B | AFAP1L2 activity lowers the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express AFAP1L2 (27) vs lines expressing it (21) | the lines without AFAP1L2: 1.10× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[RASSF5]] | B | AFAP1L2 activity raises RASSF5's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without AFAP1L2 | 0.097 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[ABHD11]] | B | AFAP1L2 activity raises ABHD11's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without AFAP1L2 | 0.098 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[PPARG]] | C | AFAP1L2 activity raises PPARG's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without AFAP1L2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, 48.6); signed map (63.8, 10.1). **Vector** length 72.3, 22.2% of its response variance represented; |z| ≥ 3 in 540 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +9.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | actin filament associated protein 1 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:114,294,824-114,404,756 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14564, Em:AC005383.4, XB130; previously KIAA1914 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Hallmark sets | APICAL_SURFACE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4X5](https://www.uniprot.org/uniprotkb/Q8N4X5) (Actin filament-associated protein 1-like 2):

> May play a role in a signaling cascade by enhancing the kinase activity of SRC. Contributes to SRC-regulated transcription activation.

**Summary**, from NCBI Gene [84632](https://www.ncbi.nlm.nih.gov/gene/84632):

> Enables SH2 domain binding activity; SH3 domain binding activity; and protein tyrosine kinase activator activity. Involved in several processes, including positive regulation of epidermal growth factor receptor signaling pathway; regulation of gene expression; and regulation of mitotic cell cycle. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25901) · Entrez [84632](https://www.ncbi.nlm.nih.gov/gene/84632) · UniProt [Q8N4X5](https://www.uniprot.org/uniprotkb/Q8N4X5) · Ensembl [ENSG00000169129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169129)

## Data

Gene col 9758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9758); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9758]; `tensor/DDL_lfc|DDL_z.npy` [9758]; `embed/gene_vectors.npy` [9758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9758 or target_col == 9758). Every well: [[AFAP1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFAP1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
