---
symbol: "NHSL1-AS1"
type: "gene"
col: 13438
ensembl_id: "ENSG00000225177"
name: "NHSL1 antisense RNA 1"
location: "6q24.1"
module: 84
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 40
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# NHSL1-AS1

*NHSL1 antisense RNA 1* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +8.2, q 2e-13, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.435× (z -8.4, q 2e-14, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHSL1]] (+0.57, fdr 1e-05, ⚠ same locus), [[PARVB]] (+0.57, fdr 1e-05), [[LINC02454]] (+0.55, fdr 2e-05), [[NPAS2]] (+0.53, fdr 1e-05); moves opposite to [[GAREM1]] (-0.46, fdr 3e-05), [[HPGD]] (-0.45, fdr 1e-04), [[KIAA1522]] (-0.44, fdr 5e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MUC16]] → it (grade B ⚠); 2 go from it, the strongest it → [[OSCAR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +8.2 | 2e-13 | 13/29 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.4 | 2e-05 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +4.7 | 6e-04 | 13/36 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.003 | 13/36 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.005 | 9/36 (H4, Hs 766T, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.005 | 3/28 (HOP62, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.015 | 8/36 (Hs 766T, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.017 | 4/29 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.043 | 0/24 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | 1.38× | +3.1 | 0.12 | 6/32 (HS-578T, NCI-H2030, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -8.4 | 2e-14 | 20/36 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.588×** | -7.6 | 6e-12 | 23/31 (C32, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -7.5 | 1e-11 | 19/34 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.499×** | -7.1 | 2e-10 | 21/36 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.502×** | -7.0 | 3e-10 | 13/29 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -6.8 | 1e-09 | 22/36 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.563×** | -5.8 | 4e-07 | 20/35 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.567×** | -5.8 | 6e-07 | 18/34 (C32, H4, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.293×** | -5.5 | 3e-06 | 16/27 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.609×** | -4.8 | 1e-04 | 13/34 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.629×** | -4.7 | 1e-04 | 14/34 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -4.7 | 1e-04 | 13/34 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -4.6 | 1e-04 | 14/35 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -4.4 | 4e-04 | 11/23 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.639×** | -4.3 | 6e-04 | 13/34 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.714×** | -4.1 | 0.002 | 13/34 (MIA PaCa-2, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.651×** | -4.0 | 0.002 | 10/36 (C32, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 32.9 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0283× (z -24.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0407× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -16.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0292× (z -16.0) |
| [[H4 (line)]] | wt | 22.1 | 0 | 12 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0318× (z -13.8) |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0723× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 8 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.393× (z -13.1) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0435× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 9.80 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0486× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 4.03 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.1000× (z -9.4) |
| [[A-172 (line)]] | wt | 3.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 3.00 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0443× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 2.36 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.0567× (z -8.6) |
| [[HS-578T (line)]] | alt | 5.74 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0790× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 6.34 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0517× (z -9.4) |
| [[A-427 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHSL1]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PARVB]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LINC02454]] | +0.55 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[NPAS2]] | +0.53 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CPNE5]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PAX3]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[PYGL]] | +0.50 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[COL13A1]] | +0.50 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LEF1-AS1]] | +0.49 | +0.46 / +0.52 | both halves | 3e-05 | same gene group |
| [[GLDC]] | +0.49 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[OSCAR]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[PARVG]] | +0.49 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SPRED2]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAREM1]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[HPGD]] | -0.45 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[KIAA1522]] | -0.44 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[TJP2]] | -0.43 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[NPEPPSP1]] | -0.41 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[CD24]] | -0.41 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC5]] | -0.41 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[MTUS1]] | -0.40 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[MUC16]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[TC2N]] | -0.40 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[KLF3]] | -0.40 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[NT5C2]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC16]] | B | MUC16 activity weakens NHSL1-AS1's drug response | lines that do not express MUC16 (28) vs lines expressing it (8) | the lines without MUC16 respond 1.92× as strongly (z diff -1.81); strongest at Panobinostat 0.5 µM: 0.31x vs 0.76x (z diff -3.5) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers NHSL1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BRSK1]] | B | BRSK1 activity raises NHSL1-AS1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without BRSK1 | 0.065 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSCAR]] | B | NHSL1-AS1 activity raises OSCAR's level | lines that do not express NHSL1-AS1 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without NHSL1-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: DLX2; maybe low, not absent |
| [[NHSL1]] | B | NHSL1-AS1 activity raises NHSL1's level | lines that do not express NHSL1-AS1 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without NHSL1-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: DLX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.453). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.8, 4.8); signed map (14.0, 49.2). **Vector** length 77.8, 16.0% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +0.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NHSL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q24.1 — chr6:138,692,548-138,697,288 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ46906 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40947) · Entrez [441172](https://www.ncbi.nlm.nih.gov/gene/441172) · Ensembl [ENSG00000225177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225177)

## Data

Gene col 13438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13438); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13438]; `tensor/DDL_lfc|DDL_z.npy` [13438]; `embed/gene_vectors.npy` [13438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13438 or target_col == 13438). Every well: [[NHSL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHSL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
