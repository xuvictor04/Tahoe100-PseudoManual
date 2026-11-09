---
symbol: "SERPINE1"
type: "gene"
col: 2751
ensembl_id: "ENSG00000106366"
name: "serpin family E member 1"
location: "7q22.1"
module: 113
arm: "+"
pooled_cpm: 724.11
n_lines_expressing: 23
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 15
direction_downstream: 29
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# SERPINE1

*serpin family E member 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.18× (z +7.8, q 4e-12, up in 4 of 22 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.21× (z +7.2, q 1e-10, up in 20 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.651× (z -6.1, q 7e-07, down in 18 of 21 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.532× (z -5.9, q 1e-06, down in 12 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP12]] (+0.66, fdr 7e-06), [[ANGPTL4]] (+0.64, fdr 7e-06), [[ERRFI1]] (+0.63, fdr 1e-05); moves opposite to [[KCP]] (-0.49, fdr 9e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TESMIN]] → it (grade B ⚠); 29 go from it, the strongest it → [[ITPRIP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.18×** | +7.8 | 4e-12 | 4/22 (SW 1271, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.15×** | +7.4 | 5e-11 | 3/18 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.21×** | +7.2 | 1e-10 | 20/22 (MIA PaCa-2, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.8 | 2e-09 | 15/21 (LOX-IMVI, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.9 | 9e-05 | 16/22 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.59×** | +4.3 | 0.002 | 1/19 (SNU-423) | all doses, stronger at high dose | composition shift |
| [[palbociclib (drug)]] 0.05 µM |  | **1.53×** | +4.0 | 0.004 | 18/21 (PANC-1, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.7 | 0.014 | 2/21 (SW480, Hs 766T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.081 | 5/21 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.081 | 8/22 (Hs 766T, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.651×** | -6.1 | 7e-07 | 18/21 (J82, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.532×** | -5.9 | 1e-06 | 12/21 (SW480, RKO, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.622×** | -4.8 | 4e-04 | 21/21 (HS-578T, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.714×** | -4.7 | 4e-04 | 8/21 (SW480, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.722×** | -4.6 | 4e-04 | 17/21 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.645×** | -4.4 | 0.001 | 9/20 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -4.3 | 0.001 | 16/21 (RKO, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.678×** | -3.9 | 0.007 | 21/21 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.677×** | -3.8 | 0.010 | 11/20 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.692×** | -3.7 | 0.013 | 7/20 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.663×** | -3.6 | 0.015 | 13/23 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.025 | 15/21 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.504×** | -3.4 | 0.025 | 19/21 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.030 | 19/21 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.718×** | -3.3 | 0.035 | 12/21 (LOX-IMVI, H4, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.703×** | -3.3 | 0.038 | 0/21 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.725×** | -3.2 | 0.043 | 3/20 (RKO, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 458 | 0 | 15 | — | [[Trametinib (drug)]] 5 µM 0.0937× (z -15.4) |
| [[J82 (line)]] | alt | 3,328 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -21.4) |
| [[HOP62 (line)]] | alt | 4,576 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -21.8) |
| [[Hs 766T (line)]] | wt | 245 | 10 | 0 | [[TAK-901 (drug)]] 5 µM 26.0× (z +10.8) | — |
| [[H4 (line)]] | wt | 597 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -14.9) |
| [[HS-578T (line)]] | alt | 2,647 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -15.5) |
| [[HepG2_C3A (line)]] | wt | 3,252 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 1,021 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -17.5) |
| [[A-172 (line)]] | wt | 1,872 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 833 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -12.4) |
| [[PANC-1 (line)]] | alt | 1,515 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 211 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 4.79× (z +9.2) | [[Cobimetinib (drug)]] 5 µM 0.118× (z -11.9) |
| [[A498 (line)]] | wt | 983 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.370× (z -9.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.283× (z -8.6) |
| [[A549 (line)]] | wt | 1,341 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.6× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 2,076 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 751 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 28.6× (z +12.5) | [[Adagrasib (drug)]] 0.05 µM 0.586× (z -14.1) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -11.9) |
| [[SNU-423 (line)]] | alt | 768 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -9.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 615 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.59× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 1,086 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.9) |
| [[SW 1088 (line)]] | alt | 1,027 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -10.2) |
| [[A-427 (line)]] | wt | 42.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 135 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 76.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 43.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 54.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 48.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 49.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 114 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 49.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 66.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 66.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 62.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 49.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 43.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 49.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 42.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 43.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 420 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.3 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 55.4 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 69.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 510 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 85.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 54.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 52.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 56.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 57.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP12]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ANGPTL4]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 496 |
| [[ERRFI1]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[ELL2]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[GFPT2]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TGM2]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 410 |
| [[COL6A3]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[WDFY2]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ITGA5]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 564 |
| [[PTPN1]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 | pathway: Platelet activation, signaling and aggregation |
| [[RHBDF2]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ERGIC1]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCP]] | -0.49 | -0.49 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TESMIN]] | B | TESMIN activity lowers SERPINE1's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 4.83× higher at baseline in the lines without TESMIN | 0.012 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[SLC45A1]] | B | SLC45A1 activity raises SERPINE1's level | lines that do not express SLC45A1 (19) vs lines expressing it (31) | 3.43× lower at baseline in the lines without SLC45A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |
| [[ITPRIP]] | B | ITPRIP activity raises SERPINE1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 5.62× lower at baseline in the lines without ITPRIP | 0.050 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[MEIS3]] | B | MEIS3 activity raises SERPINE1's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 4.50× lower at baseline in the lines without MEIS3 | 0.079 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[PGF]] | B | PGF activity raises SERPINE1's level | lines that do not express PGF (12) vs lines expressing it (38) | 4.14× lower at baseline in the lines without PGF | 0.079 | ⚠ within organs, on part of the lines; also absent: ZSCAN12, LOXL1, REEP2; maybe low, not absent |
| [[ANPEP]] | C | ANPEP activity raises SERPINE1's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 6.58× lower at baseline in the lines without ANPEP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865; co-absent with the target |
| [[GFPT2]] | C | GFPT2 activity raises SERPINE1's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 4.17× lower at baseline in the lines without GFPT2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises SERPINE1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.24× lower at baseline in the lines without COL5A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises SERPINE1's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 5.04× lower at baseline in the lines without NAV1 | 0.048 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[NAV2]] | C | NAV2 activity raises SERPINE1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 4.31× lower at baseline in the lines without NAV2 | 0.049 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1; co-absent with the target |
| [[PDGFRA]] | C | PDGFRA activity raises SERPINE1's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 2.46× lower at baseline in the lines without PDGFRA | 0.061 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[MIR100HG]] | C | MIR100HG activity raises SERPINE1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 4.50× lower at baseline in the lines without MIR100HG | 0.061 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 18, C 11. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPRIP]] | B | SERPINE1 activity raises ITPRIP's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 3.14× lower at baseline in the lines without SERPINE1 | 0.005 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[SH2B3]] | B | SERPINE1 activity raises SH2B3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without SERPINE1 | 0.006 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[ITGA5]] | B | SERPINE1 activity raises ITGA5's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 4.05× lower at baseline in the lines without SERPINE1 | 0.020 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[ZHX3]] | B | SERPINE1 activity raises ZHX3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without SERPINE1 | 0.020 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[ARHGAP22]] | B | SERPINE1 activity raises ARHGAP22's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 3.48× lower at baseline in the lines without SERPINE1 | 0.026 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[PALM2AKAP2]] | B | SERPINE1 activity raises PALM2AKAP2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 3.25× lower at baseline in the lines without SERPINE1 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[ANGPTL4]] | B | SERPINE1 activity raises ANGPTL4's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.94× lower at baseline in the lines without SERPINE1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[PHC2]] | B | SERPINE1 activity raises PHC2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without SERPINE1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[RASA3]] | B | SERPINE1 activity raises RASA3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.13× lower at baseline in the lines without SERPINE1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[PTPN1]] | B | SERPINE1 activity weakens PTPN1's drug response | lines that do not express SERPINE1 (27) vs lines expressing it (23) | the lines without SERPINE1 respond 1.15× as strongly (z diff -0.95); strongest at Idarubicin (hydrochloride) 5 µM: 1.77x vs 1.35x (z diff -3.4) | 0.046 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615; artifact flags |
| [[MEIS3]] | B | SERPINE1 activity raises MEIS3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.45× lower at baseline in the lines without SERPINE1 | 0.060 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[PTPN1]] | B | SERPINE1 activity raises PTPN1's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.49× lower at baseline in the lines without SERPINE1 | 0.063 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 11.2); signed map (14.3, 36.7). **Vector** length 114, 36.8% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.6 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | -1.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.0 | +2.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -5.0 | -6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -4.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | serpin family E member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,127,104-101,139,247 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAI; previously PLANH1, PAI1 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | TGF_BETA_SIGNALING, COAGULATION, INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, XENOBIOTIC_METABOLISM, COMPLEMENT, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 24 pathways, smallest: Dissolution of Fibrin Clot; Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; SARS-CoV-1 targets host intracellular signalling and regulatory pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [P05121](https://www.uniprot.org/uniprotkb/P05121) (Plasminogen activator inhibitor 1):

> Serine protease inhibitor. Inhibits TMPRSS7. Is a primary inhibitor of tissue-type plasminogen activator (PLAT) and urokinase-type plasminogen activator (PLAU). As PLAT inhibitor, it is required for fibrinolysis down-regulation and is responsible for the controlled degradation of blood clots. As PLAU inhibitor, it is involved in the regulation of cell adhesion and spreading. Acts as a regulator of cell migration, independently of its role as protease inhibitor. It is required for stimulation of …

**Summary**, from NCBI Gene [5054](https://www.ncbi.nlm.nih.gov/gene/5054):

> This gene encodes a member of the serine proteinase inhibitor (serpin) superfamily. This member is the principal inhibitor of tissue plasminogen activator (tPA) and urokinase (uPA), and hence is an inhibitor of fibrinolysis. The protein also functions as a component of innate antiviral immunity. Defects in this gene are the cause of plasminogen activator inhibitor-1 deficiency (PAI-1 deficiency), and high concentrations of the gene product are associated with thrombophilia. [provided by RefSeq, …

**Accessions** — [HGNC:8583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8583) · Entrez [5054](https://www.ncbi.nlm.nih.gov/gene/5054) · UniProt [P05121](https://www.uniprot.org/uniprotkb/P05121) · Ensembl [ENSG00000106366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106366)

## Data

Gene col 2751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2751); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2751]; `tensor/DDL_lfc|DDL_z.npy` [2751]; `embed/gene_vectors.npy` [2751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2751 or target_col == 2751). Every well: [[SERPINE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
