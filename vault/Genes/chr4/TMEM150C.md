---
symbol: "TMEM150C"
type: "gene"
col: 14596
ensembl_id: "ENSG00000249242"
name: "transmembrane protein 150C"
location: "4q21.22"
module: 82
arm: "+"
pooled_cpm: 4.24
n_lines_expressing: 37
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# TMEM150C

*transmembrane protein 150C* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.07× (z +11.7, q 1e-28, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.14× (z +11.6, q 1e-28, up in 23 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.482× (z -7.6, q 1e-11, down in 20 of 29 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAGLR]] (+0.60, fdr 1e-05), [[FAM124A]] (+0.56, fdr 3e-05), [[EMID1]] (+0.56, fdr 2e-05); moves opposite to [[METTL15]] (-0.43, fdr 3e-04), [[CFAP44]] (-0.41, fdr 2e-04), [[LMBRD2]] (-0.40, fdr 9e-04, ⚠ not reproduced).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[DPYSL5]] → it (grade B ⚠); 8 go from it, the strongest it → [[DGCR5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +11.7 | 1e-28 | 2/6 (SW1417, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +11.6 | 1e-28 | 23/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.4 | 1e-18 | 12/24 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.24×** | +8.7 | 3e-16 | 21/28 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.9 | 6e-10 | 2/16 (BT-474, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.030 | 4/31 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.6 | 0.030 | 1/15 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +3.5 | 0.030 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.5 | 0.030 | 2/19 (HOP62, NCI-H1792) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Fulvestrant (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.035 | 2/29 (PANC-1, J82) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.038 | 3/26 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.041 | 3/30 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.045 | 10/34 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.070 | 3/30 (SHP-77, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -7.6 | 1e-11 | 20/29 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -5.8 | 1e-06 | 21/34 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.687×** | -5.8 | 1e-06 | 15/24 (A549, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -5.7 | 2e-06 | 17/30 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -4.7 | 3e-04 | 14/21 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -4.5 | 6e-04 | 16/34 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.679×** | -4.2 | 0.002 | 15/28 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -3.7 | 0.014 | 15/24 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -3.6 | 0.018 | 15/33 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.020 | 8/33 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.557×** | -3.3 | 0.045 | 12/29 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.731×** | -3.2 | 0.074 | 3/32 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -15.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0912× (z -11.7) |
| [[A549 (line)]] | wt | 8.20 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0401× (z -20.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0864× (z -11.0) |
| [[LoVo (line)]] | wt | 8.01 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0676× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -11.3) |
| [[SW480 (line)]] | alt | 6.62 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 8.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 4.49 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0469× (z -9.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAGLR]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FAM124A]] | +0.56 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[EMID1]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MAP6]] | +0.56 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PRKCQ]] | +0.56 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[LINC02223]] | +0.55 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[DGCR5]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[DPYSL5]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[LINC00937]] | +0.54 | +0.37 / +0.73 | both halves | 9e-05 |  |
| [[CIB2]] | +0.54 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[TMEM171]] | +0.54 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[LRRN2]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL15]] | -0.43 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[CFAP44]] | -0.41 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[LMBRD2]] | -0.40 | -0.18 / -0.46 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPYSL5]] | B | DPYSL5 activity raises TMEM150C's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.85× lower at baseline in the lines without DPYSL5 | 0.012 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[SCN8A]] | B | SCN8A activity raises TMEM150C's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without SCN8A | 0.022 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[MYT1]] | B | MYT1 activity raises TMEM150C's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without MYT1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[RET]] | B | RET activity raises TMEM150C's level | lines that do not express RET (28) vs lines expressing it (22) | 2.58× lower at baseline in the lines without RET | 0.052 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[CACNA1B]] | B | CACNA1B activity raises TMEM150C's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 2.27× lower at baseline in the lines without CACNA1B | 0.059 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[DLL3]] | B | DLL3 activity raises TMEM150C's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without DLL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |
| [[JPH3]] | B | JPH3 activity raises TMEM150C's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without JPH3 | 0.079 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises TMEM150C's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.35× lower at baseline in the lines without FAXC | 0.091 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[FXYD6]] | C | FXYD6 activity raises TMEM150C's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without FXYD6 | 0.054 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |
| [[RFPL1S]] | C | RFPL1S activity raises TMEM150C's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without RFPL1S | 0.056 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGCR5]] | B | TMEM150C activity raises DGCR5's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without TMEM150C | 0.048 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[SCD5]] | B | TMEM150C activity raises SCD5's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without TMEM150C | 0.050 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[FAXC]] | B | TMEM150C activity raises FAXC's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without TMEM150C | 0.053 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[SPTB]] | B | TMEM150C activity raises SPTB's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without TMEM150C | 0.061 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[RHBDL3]] | B | TMEM150C activity strengthens RHBDL3's drug response | lines that do not express TMEM150C (7) vs lines expressing it (31) | the lines without TMEM150C respond 0.74× as strongly (z diff +1.04); strongest at Tucidinostat 5 µM: 1.42x vs 3.39x (z diff +3.3) | 0.076 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TMOD2]] | B | TMEM150C activity raises TMOD2's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without TMEM150C | 0.078 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[DPYSL5]] | B | TMEM150C activity raises DPYSL5's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without TMEM150C | 0.089 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[RFPL1S]] | C | TMEM150C activity raises RFPL1S's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without TMEM150C | 0.057 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, 38.2); signed map (25.6, 28.5). **Vector** length 51.1, 8.80% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -5.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 150C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,483,170-82,562,357 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRAM4, FLJ12993, TTN3 |
| Gene groups (HGNC) | DRAM autophagy modulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [B9EJG8](https://www.uniprot.org/uniprotkb/B9EJG8) (Transmembrane protein 150C):

> Nonselective cationic channel with high permeability to Ca(2+). Component of a mechanosensitive cation channel, confers mechanically activated (MA) currents with slow inactivation kinetics. May contribute to proprioception.

**Summary**, from NCBI Gene [441027](https://www.ncbi.nlm.nih.gov/gene/441027):

> This gene encodes a transmembrane protein component of a mechanosensitve ion channel that is activated by mechanical stimuli in various cell types and confers slowly adapting, mechanically activated currents in dorsal root ganglion neurons. Mechanically activated ion channels are sensors that are critical for hearing, touch, pain, and blood pressure regulation. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:37263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37263) · Entrez [441027](https://www.ncbi.nlm.nih.gov/gene/441027) · UniProt [B9EJG8](https://www.uniprot.org/uniprotkb/B9EJG8) · Ensembl [ENSG00000249242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249242)

## Data

Gene col 14596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14596); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14596]; `tensor/DDL_lfc|DDL_z.npy` [14596]; `embed/gene_vectors.npy` [14596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14596 or target_col == 14596). Every well: [[TMEM150C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM150C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
