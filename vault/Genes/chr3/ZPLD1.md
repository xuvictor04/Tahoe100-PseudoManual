---
symbol: "ZPLD1"
type: "gene"
col: 9899
ensembl_id: "ENSG00000170044"
name: "zona pellucida like domain containing 1"
location: "3q12.3"
module: 165
arm: "+"
pooled_cpm: 2.69
n_lines_expressing: 43
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# ZPLD1

*zona pellucida like domain containing 1* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.99× (z +21.3, q 0e+00, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.624× (z -3.9, q 0.046, down in 9 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.0544×, A-172 0.0297×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (RKO 0.0524×; ⚠ cell-cycle shift, explains ~56% of this change); [[Tazarotene (drug)]] 0.5 µM in 1 line (C32 0.0534×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RDUR]] (+0.75, fdr 7e-06), [[DOCK2]] (+0.72, fdr 7e-06), [[PLXNA4]] (+0.69, fdr 1e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[RDUR]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC26A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.99×** | +21.3 | 0e+00 | 17/22 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +10.5 | 3e-23 | 4/10 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.62×** | +10.4 | 4e-23 | 2/4 (LOX-IMVI, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.43×** | +10.4 | 4e-23 | 18/28 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +9.8 | 2e-20 | 12/28 (hTERT-HPNE, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.11×** | +9.6 | 1e-19 | 19/32 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.97×** | +8.1 | 5e-14 | 14/34 (CFPAC-1, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +6.5 | 6e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.1 | 6e-08 | 10/27 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +5.4 | 4e-06 | 3/18 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.2 | 1e-05 | 9/34 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +5.0 | 3e-05 | 1/8 (HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 0.001 | 7/27 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.048 | 7/24 (SHP-77, J82, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.45×** | +3.2 | 0.058 | 3/24 (J82, SHP-77, …) | inconsistent across doses |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.077 | 3/16 (HS-578T, LoVo, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.0 | 0.083 | 3/16 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9899.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 2 lines (LOX-IMVI 0.0544×, A-172 0.0297×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (RKO 0.0524×; ⚠ cell-cycle shift, explains ~56% of this change); [[Tazarotene (drug)]] 0.5 µM in 1 line (C32 0.0534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -3.9 | 0.046 | 9/34 (COLO 205, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.680× | -3.2 | 0.17 | 9/26 (RKO, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ciclopirox (drug)]] 5 µM |  | 0.763× | -3.2 | 0.17 | 7/28 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.684× | -3.2 | 0.17 | 10/32 (LOX-IMVI, C32, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.684× | -3.2 | 0.17 | 11/33 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -3.0 | 0.23 | 8/37 (HOP62, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.70 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0297× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 6.19 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0534× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.71× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 1.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 1.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 2.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.5× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0544× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0524× (z -9.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.9× (z +8.9) | — |
| [[A-427 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.707 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.799 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.734 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.684 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.906 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.868 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.977 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.676 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.752 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.737 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.716 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.663 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RDUR]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[DOCK2]] | +0.72 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PLXNA4]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[FGF1]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[CD96]] | +0.68 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CDK6-AS1]] | +0.67 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LINC01358]] | +0.66 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MIR4280HG]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SLC26A4]] | +0.65 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PECAM1]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SYT16]] | +0.65 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDUR]] | B | RDUR activity raises ZPLD1's level | lines that do not express RDUR (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without RDUR | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC |
| [[LINC01812]] | B | LINC01812 activity raises ZPLD1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.52× lower at baseline in the lines without LINC01812 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[ECSCR]] | B | ECSCR activity raises ZPLD1's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without ECSCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ZPLD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCDC190]] | B | CCDC190 activity raises ZPLD1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 1.75× lower at baseline in the lines without CCDC190 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337 |
| [[AIM2]] | B | AIM2 activity raises ZPLD1's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without AIM2 | 0.058 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[LINC00702]] | B | LINC00702 activity raises ZPLD1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without LINC00702 | 0.060 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[ROBO4]] | B | ROBO4 activity raises ZPLD1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without ROBO4 | 0.070 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[LINC01592]] | B | LINC01592 activity raises ZPLD1's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 1.74× lower at baseline in the lines without LINC01592 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent |
| [[TNC]] | B | TNC activity raises ZPLD1's level | lines that do not express TNC (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without TNC | 0.087 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622 |
| [[CTHRC1]] | B | CTHRC1 activity raises ZPLD1's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 1.72× lower at baseline in the lines without CTHRC1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A4]] | B | ZPLD1 activity lowers SLC26A4's level | lines that do not express ZPLD1 (7) vs lines expressing it (43) | 1.53× higher at baseline in the lines without ZPLD1 | 0.024 | ⚠ within organs, on part of the lines; also absent: STAT4, ABCA12, ANKRD7; maybe low, not absent |
| [[LMNB1-DT]] | B | ZPLD1 activity lowers LMNB1-DT's level | lines that do not express ZPLD1 (7) vs lines expressing it (43) | 1.00× higher at baseline in the lines without ZPLD1 | 0.072 | ⚠ within organs, on part of the lines; also absent: STAT4, ABCA12, ANKRD7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.1, 11.0); signed map (15.4, 47.0). **Vector** length 52.6, 9.04% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +21.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zona pellucida like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:102,099,244-102,479,841 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCW7](https://www.uniprot.org/uniprotkb/Q8TCW7) (Zona pellucida-like domain-containing protein 1):

> Glycoprotein which is a component of the gelatinous extracellular matrix in the cupulae of the vestibular organ.

**Summary**, from NCBI Gene [131368](https://www.ncbi.nlm.nih.gov/gene/131368):

> Predicted to act upstream of or within vestibular reflex. Predicted to be located in cytoplasmic vesicle membrane. Predicted to be active in cell surface and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27022) · Entrez [131368](https://www.ncbi.nlm.nih.gov/gene/131368) · UniProt [Q8TCW7](https://www.uniprot.org/uniprotkb/Q8TCW7) · Ensembl [ENSG00000170044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170044)

## Data

Gene col 9899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9899); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9899]; `tensor/DDL_lfc|DDL_z.npy` [9899]; `embed/gene_vectors.npy` [9899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9899 or target_col == 9899). Every well: [[ZPLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZPLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
