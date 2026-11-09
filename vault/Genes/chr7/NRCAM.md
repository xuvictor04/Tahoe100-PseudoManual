---
symbol: "NRCAM"
type: "gene"
col: 1653
ensembl_id: "ENSG00000091129"
name: "neuronal cell adhesion molecule"
location: "7q31.1"
module: 19
arm: "+"
pooled_cpm: 75.69
n_lines_expressing: 14
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 12
direction_downstream: 15
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NRCAM

*neuronal cell adhesion molecule* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.34× (z +21.6, q 0e+00, up in 5 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.633× (z -5.4, q 4e-05, down in 3 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMB4]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[RTN1]] (+0.75, fdr 7e-06), [[LIN7A]] (+0.71, fdr 7e-06), [[CTNND2]] (+0.70, fdr 7e-06); moves opposite to [[ADRA2C]] (-0.45, fdr 4e-05), [[NPTX1]] (-0.44, fdr 8e-05), [[NR0B1]] (-0.43, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[RHOBTB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.34×** | +21.6 | 0e+00 | 5/13 (SW 900, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +16.3 | 0e+00 | 8/13 (SHP-77, A549, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +14.7 | 0e+00 | 10/12 (HEC-1-A, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +12.6 | 5e-34 | 7/12 (SW 900, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.7 | 2e-29 | 5/11 (BT-474, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +10.7 | 6e-25 | 4/11 (BT-474, C32, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +8.4 | 4e-15 | 4/14 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +7.2 | 4e-11 | 8/13 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.1 | 9e-11 | 4/12 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.59×** | +5.9 | 2e-07 | 6/12 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +5.1 | 2e-05 | 7/12 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 2e-05 | 6/12 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.47×** | +4.9 | 5e-05 | 4/12 (SW 900, BT-474, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 1e-04 | 6/12 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.7 | 1e-04 | 5/12 (C-33 A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +4.7 | 1e-04 | 6/12 (HepG2/C3A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 2e-04 | 0/12 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 3e-04 | 4/12 (A498, C32, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 6/12 (NCI-H1792, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.633×** | -5.4 | 4e-05 | 3/12 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.728×** | -4.0 | 0.015 | 5/12 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.752×** | -3.6 | 0.048 | 5/12 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.048 | 3/12 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.752×** | -3.4 | 0.087 | 0/12 | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.790× | -3.2 | 0.15 | 3/14 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 809 | 0 | 23 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0707× (z -23.4) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0665× (z -17.0) |
| [[NCI-H1792 (line)]] | alt | 205 | 18 | 2 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.80× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -9.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -8.6) |
| [[A549 (line)]] | wt | 192 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -10.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.0) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HEC-1-A (line)]] | alt | 23.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.76× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.216× (z -8.6) |
| [[Hs 766T (line)]] | wt | 195 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.6) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A-172 (line)]] | wt | 8.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 275 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.82 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.43 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 17.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMB4]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: LAMB4 lies 17.3 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[RTN1]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_HEDGEHOG_SIGNALING |
| [[LIN7A]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CHL1]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 | same gene group; pathway: L1CAM interactions |
| [[SCARA5]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GTF2I-AS1]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[LINC00824]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SLC15A5]] | +0.63 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[IL18R1]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[EPGN]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADRA2C]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NPTX1]] | -0.44 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[NR0B1]] | -0.43 | -0.50 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NRCAM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLAC4]] | B | PLAC4 activity raises NRCAM's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without PLAC4 | 0.079 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[LAMB4]] | C | LAMB4 activity raises NRCAM's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 4.39× lower at baseline in the lines without LAMB4 | 0.003 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[SOX6]] | C | SOX6 activity raises NRCAM's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.88× lower at baseline in the lines without SOX6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises NRCAM's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without LIN7A | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises NRCAM's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.37× lower at baseline in the lines without GPRIN3 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[NR0B1]] | C | NR0B1 activity raises NRCAM's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 4.30× lower at baseline in the lines without NR0B1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT; co-absent with the target |
| [[SLITRK4]] | C | SLITRK4 activity raises NRCAM's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.16× lower at baseline in the lines without SLITRK4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[LINC00824]] | C | LINC00824 activity raises NRCAM's level | lines that do not express LINC00824 (46) vs lines expressing it (4) | 10.51× lower at baseline in the lines without LINC00824 | 0.066 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SUCNR1, ENSG00000289530; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises NRCAM's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.22× lower at baseline in the lines without DPP10 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[SERPINB11]] | C | SERPINB11 activity raises NRCAM's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 5.03× lower at baseline in the lines without SERPINB11 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[RTN1]] | C | RTN1 activity raises NRCAM's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.39× lower at baseline in the lines without RTN1 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOBTB1]] | B | NRCAM activity raises RHOBTB1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.89× lower at baseline in the lines without NRCAM | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[ADGRG2]] | B | NRCAM activity raises ADGRG2's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without NRCAM | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[ELMO1]] | B | NRCAM activity raises ELMO1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.93× lower at baseline in the lines without NRCAM | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[ITPK1]] | B | NRCAM activity raises ITPK1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.57× lower at baseline in the lines without NRCAM | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[TRPM3]] | B | NRCAM activity raises TRPM3's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.68× lower at baseline in the lines without NRCAM | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[SLC4A11]] | B | NRCAM activity raises SLC4A11's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.34× lower at baseline in the lines without NRCAM | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[LAMB4]] | C | NRCAM activity raises LAMB4's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.59× lower at baseline in the lines without NRCAM | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[GPRIN3]] | C | NRCAM activity raises GPRIN3's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 4.28× lower at baseline in the lines without NRCAM | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[RTN1]] | C | NRCAM activity raises RTN1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.84× lower at baseline in the lines without NRCAM | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[SLC7A2]] | C | NRCAM activity raises SLC7A2's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 5.08× lower at baseline in the lines without NRCAM | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[LIN7A]] | C | NRCAM activity raises LIN7A's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 3.65× lower at baseline in the lines without NRCAM | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[LINC01508]] | C | NRCAM activity raises LINC01508's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.63× lower at baseline in the lines without NRCAM | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 36.9); signed map (43.7, 44.7). **Vector** length 64.6, 23.9% of its response variance represented; |z| ≥ 3 in 420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +16.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +21.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +14.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +5.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.3 | +5.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.3 | +3.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -1.3 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -1.1 | +2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | neuronal cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:108,147,623-108,456,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0343, Bravo |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 6 pathways, smallest: Neurofascin interactions; NrCAM interactions; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92823](https://www.uniprot.org/uniprotkb/Q92823) (Neuronal cell adhesion molecule):

> Cell adhesion protein that is required for normal responses to cell-cell contacts in brain and in the peripheral nervous system. Plays a role in neurite outgrowth in response to contactin binding. Plays a role in mediating cell-cell contacts between Schwann cells and axons. Plays a role in the formation and maintenance of the nodes of Ranvier on myelinated axons. Nodes of Ranvier contain clustered sodium channels that are crucial for the saltatory propagation of action potentials along …

**Summary**, from NCBI Gene [4897](https://www.ncbi.nlm.nih.gov/gene/4897):

> Cell adhesion molecules (CAMs) are members of the immunoglobulin superfamily. This gene encodes a neuronal cell adhesion molecule with multiple immunoglobulin-like C2-type domains and fibronectin type-III domains. This ankyrin-binding protein is involved in neuron-neuron adhesion and promotes directional signaling during axonal cone growth. This gene is also expressed in non-neural tissues and may play a general role in cell-cell communication via signaling from its intracellular domain to the …

**Accessions** — [HGNC:7994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7994) · Entrez [4897](https://www.ncbi.nlm.nih.gov/gene/4897) · UniProt [Q92823](https://www.uniprot.org/uniprotkb/Q92823) · Ensembl [ENSG00000091129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091129)

## Data

Gene col 1653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1653); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1653]; `tensor/DDL_lfc|DDL_z.npy` [1653]; `embed/gene_vectors.npy` [1653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1653 or target_col == 1653). Every well: [[NRCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
