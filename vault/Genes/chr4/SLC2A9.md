---
symbol: "SLC2A9"
type: "gene"
col: 3068
ensembl_id: "ENSG00000109667"
name: "solute carrier family 2 member 9"
location: "4p16.1"
module: 47
arm: "+"
pooled_cpm: 7.14
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 38
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SLC2A9

*solute carrier family 2 member 9* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.53× (z +17.1, q 0e+00, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.626× (z -4.5, q 0.003, down in 17 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAC8L1]] (+0.83, fdr 7e-06), [[LINC00486]] (+0.80, fdr 7e-06), [[LINC01191]] (+0.79, fdr 7e-06); moves opposite to [[FLYWCH2]] (-0.67, fdr 1e-05), [[SNX1]] (-0.66, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 38 go from it, the strongest it → [[FLYWCH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.53×** | +17.1 | 0e+00 | 21/34 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +12.5 | 4e-33 | 28/34 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.54×** | +12.1 | 2e-31 | 25/35 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +10.8 | 3e-25 | 11/13 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.78×** | +9.8 | 2e-20 | 28/39 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.8 | 1e-16 | 15/24 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +8.6 | 8e-16 | 5/16 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.32×** | +7.6 | 3e-12 | 26/38 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.95×** | +6.4 | 1e-08 | 26/41 (LoVo, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.0 | 1e-07 | 18/36 (LOX-IMVI, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.4 | 3e-06 | 16/34 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.5 | 4e-04 | 10/42 (A498, HOP62, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.006 | 9/41 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.14×** | +3.8 | 0.006 | 4/33 (SW 900, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.007 | 6/41 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.017 | 6/39 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.98×** | +3.4 | 0.022 | 5/40 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.033 | 14/38 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.626×** | -4.5 | 0.003 | 17/41 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -4.3 | 0.004 | 14/37 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.684×** | -3.7 | 0.034 | 17/41 (NCI-H1573, NCI-H23, …) | all doses, flat | composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.673×** | -3.6 | 0.034 | 9/38 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimitespib (drug)]] 0.05 µM |  | **0.674×** | -3.6 | 0.034 | 9/39 (A498, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.718× | -3.2 | 0.12 | 15/39 (NCI-H23, BT-474, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.543× | -3.1 | 0.16 | 5/32 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.221× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 11.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +20.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -9.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0728× (z -8.9) ⚠ cell-cycle shift, explains ~23% of this change |
| [[C32 (line)]] | wt | 3.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 4.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 3.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 9.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0889× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 4.84 | 0 | 1 | — | [[Ligustrazine (drug)]] 0.5 µM 0.0635× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0612× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 8.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +10.3) | — |
| [[A-172 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAC8L1]] | +0.83 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.80 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.79 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.78 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[USP50]] | +0.78 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[MSH4]] | +0.78 | +0.80 / +0.48 | both halves | 2e-05 |  |
| [[IDI2-AS1]] | +0.77 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.77 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[ALDH8A1]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.76 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.76 | +0.79 / +0.52 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.76 | +0.80 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLYWCH2]] | -0.67 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SNX1]] | -0.66 | -0.63 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC2A9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TBX15]] | B | TBX15 activity raises SLC2A9's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without TBX15 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01348]] | B | LINC01348 activity raises SLC2A9's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 1.74× lower at baseline in the lines without LINC01348 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[FER1L6]] | B | FER1L6 activity raises SLC2A9's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without FER1L6 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[PLSCR2]] | C | PLSCR2 activity raises SLC2A9's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without PLSCR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent; co-absent with the target |
| [[SSUH2]] | C | SSUH2 activity raises SLC2A9's level | lines that do not express SSUH2 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without SSUH2 | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GNA14, FRMD3, OXTR; maybe low, not absent |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 37, C 1. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLYWCH2]] | B | SLC2A9 activity lowers FLYWCH2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.50× higher at baseline in the lines without SLC2A9 | 0.008 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[YJEFN3]] | B | SLC2A9 activity lowers YJEFN3's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.69× higher at baseline in the lines without SLC2A9 | 0.015 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[PGAP1]] | B | SLC2A9 activity lowers PGAP1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.81× higher at baseline in the lines without SLC2A9 | 0.017 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | SLC2A9 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.70× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[SEMA4A]] | B | SLC2A9 activity raises SEMA4A's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 3.03× lower at baseline in the lines without SLC2A9 | 0.028 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[ERI2]] | B | SLC2A9 activity raises ERI2's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without SLC2A9 | 0.029 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[LINC03036]] | B | SLC2A9 activity lowers LINC03036's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without SLC2A9 | 0.030 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[SNHG26]] | B | SLC2A9 activity lowers SNHG26's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 3.12× higher at baseline in the lines without SLC2A9 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[PLEKHA6]] | B | SLC2A9 activity raises PLEKHA6's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 3.75× lower at baseline in the lines without SLC2A9 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[IMPA1P1]] | B | SLC2A9 activity raises IMPA1P1's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without SLC2A9 | 0.041 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[WTIP]] | B | SLC2A9 activity lowers WTIP's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 2.93× higher at baseline in the lines without SLC2A9 | 0.042 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | SLC2A9 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.71× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.4, -11.8); signed map (19.8, 6.9). **Vector** length 79.0, 14.1% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +17.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +7.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.8 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:9,771,153-10,054,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Glut9, GLUTX, URATv1 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Reactome | 5 pathways, smallest: Cellular hexose transport; SLC transporter disorders; Disorders of transmembrane transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRM0](https://www.uniprot.org/uniprotkb/Q9NRM0) (Solute carrier family 2, facilitated glucose transporter member 9):

> High-capacity urate transporter, which may play a role in the urate reabsorption by proximal tubules. May have a residual high-affinity, low-capacity glucose and fructose transporter activity. Transports urate at rates 45- to 60-fold faster than glucose. Does not transport galactose. May mediate small uptake of adenine but not of other nucleobases.

**Summary**, from NCBI Gene [56606](https://www.ncbi.nlm.nih.gov/gene/56606):

> This gene encodes a member of the SLC2A facilitative glucose transporter family. Members of this family play a significant role in maintaining glucose homeostasis. The encoded protein may play a role in the development and survival of chondrocytes in cartilage matrices. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13446) · Entrez [56606](https://www.ncbi.nlm.nih.gov/gene/56606) · UniProt [Q9NRM0](https://www.uniprot.org/uniprotkb/Q9NRM0) · Ensembl [ENSG00000109667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109667)

## Data

Gene col 3068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3068); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3068]; `tensor/DDL_lfc|DDL_z.npy` [3068]; `embed/gene_vectors.npy` [3068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3068 or target_col == 3068). Every well: [[SLC2A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
