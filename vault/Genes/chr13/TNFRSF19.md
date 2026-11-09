---
symbol: "TNFRSF19"
type: "gene"
col: 4837
ensembl_id: "ENSG00000127863"
name: "TNF receptor superfamily member 19"
location: "13q12.12"
module: 19
arm: "+"
pooled_cpm: 45.0
n_lines_expressing: 29
n_dd_up: 14
n_dd_down: 35
n_dd_up_clean: 13
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 16
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TNFRSF19

*TNF receptor superfamily member 19* — 13q12.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +13.2, q 3e-37, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.345× (z -12.7, q 2e-34, down in 24 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA3]] (+0.62, fdr 7e-06), [[PLCB1]] (+0.55, fdr 1e-05), [[LINC01967]] (+0.55, fdr 1e-05); moves opposite to [[ARHGEF35-AS1]] (-0.48, fdr 1e-04), [[DUSP5-DT]] (-0.45, fdr 4e-05), [[C1RL-AS1]] (-0.44, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[VSNL1]] → it (grade B ⚠); 8 go from it, the strongest it → [[ARHGAP25]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +13.2 | 3e-37 | 14/27 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +10.9 | 5e-25 | 15/27 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.30×** | +10.0 | 3e-21 | 14/27 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.20×** | +4.9 | 1e-04 | 17/26 (A-172, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.15×** | +4.8 | 2e-04 | 13/26 (A-172, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +4.5 | 6e-04 | 7/28 (LS 180, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.1 | 0.003 | 6/26 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.003 | 10/27 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.024 | 12/28 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.72×** | +3.4 | 0.039 | 10/26 (A-172, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.043 | 11/28 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.045 | 10/27 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.045 | 7/27 (COLO 205, SW480, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.051 | 11/28 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.345×** | -12.7 | 2e-34 | 24/27 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -8.3 | 2e-14 | 25/27 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.506×** | -8.2 | 6e-14 | 21/27 (NCI-H460, C32, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -7.6 | 4e-12 | 23/26 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.639×** | -7.6 | 4e-12 | 26/27 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -7.1 | 1e-10 | 19/26 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -6.7 | 2e-09 | 19/27 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -6.6 | 2e-09 | 22/27 (C32, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.580×** | -6.5 | 4e-09 | 21/26 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.621×** | -5.7 | 7e-07 | 18/27 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -5.7 | 8e-07 | 18/27 (NCI-H460, COLO 205, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.626×** | -5.6 | 9e-07 | 17/27 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.640×** | -5.3 | 4e-06 | 17/26 (SW480, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.633×** | -5.2 | 9e-06 | 21/27 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.649×** | -5.2 | 9e-06 | 19/27 (C32, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -5.1 | 1e-05 | 15/28 (NCI-H460, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 273 | 0 | 30 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0373× (z -36.0) |
| [[C32 (line)]] | wt | 524 | 0 | 26 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0432× (z -29.9) |
| [[SW480 (line)]] | alt | 85.0 | 6 (1 ⚠) | 11 (2 ⚠) | [[Trametinib (drug)]] 5 µM 3.10× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 2.68× (z +9.2) | [[Ixazomib citrate (drug)]] 5 µM 0.168× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -12.5) |
| [[COLO 205 (line)]] | alt | 42.8 | 1 (1 ⚠) | 8 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 9.93× (z +10.0) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.0127× (z -18.3) |
| [[SHP-77 (line)]] | alt | 162 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -16.0) |
| [[A-427 (line)]] | wt | 102 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.211× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 67.1 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -11.9) |
| [[SW48 (line)]] | wt | 68.3 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.0942× (z -11.2) |
| [[A-172 (line)]] | wt | 26.1 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 9.79× (z +11.7) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.172× (z -8.7) |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -9.9) |
| [[SNU-423 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0903× (z -10.6) |
| [[A498 (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.90 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.55 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA3]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[PLCB1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LINC01967]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CDH19]] | +0.54 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SEMA3D]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[COL8A1]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[GRIA2]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[BMP5]] | +0.52 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SESN3]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PHYHIPL]] | +0.51 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[HS3ST5]] | +0.51 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[A2M]] | +0.50 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF35-AS1]] | -0.48 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[DUSP5-DT]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[C1RL-AS1]] | -0.44 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[PXDC1]] | -0.42 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[BCL10-AS1]] | -0.41 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[SLC22A15]] | -0.40 | -0.35 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 13, C 3. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSNL1]] | B | VSNL1 activity raises TNFRSF19's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 1.90× lower at baseline in the lines without VSNL1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[LINC01035]] | B | LINC01035 activity raises TNFRSF19's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 4.21× lower at baseline in the lines without LINC01035 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2 |
| [[MAP2K6]] | B | MAP2K6 activity raises TNFRSF19's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.43× lower at baseline in the lines without MAP2K6 | 0.033 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[KCNE4]] | B | KCNE4 activity raises TNFRSF19's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without KCNE4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[CHL1]] | B | CHL1 activity raises TNFRSF19's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 4.71× lower at baseline in the lines without CHL1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SOX6]] | B | SOX6 activity raises TNFRSF19's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without SOX6 | 0.050 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[RMST]] | B | RMST activity raises TNFRSF19's level | lines that do not express RMST (35) vs lines expressing it (15) | 3.10× lower at baseline in the lines without RMST | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TNFRSF19's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ADGRV1]] | B | ADGRV1 activity raises TNFRSF19's level | lines that do not express ADGRV1 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without ADGRV1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[SERPINF1]] | B | SERPINF1 activity raises TNFRSF19's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without SERPINF1 | 0.074 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[ARHGAP28]] | B | ARHGAP28 activity raises TNFRSF19's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without ARHGAP28 | 0.087 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1 |
| [[LRRTM4]] | B | LRRTM4 activity raises TNFRSF19's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without LRRTM4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP25]] | B | TNFRSF19 activity raises ARHGAP25's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without TNFRSF19 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3 |
| [[MAP2K6]] | B | TNFRSF19 activity raises MAP2K6's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without TNFRSF19 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3 |
| [[LOXL3]] | C | TNFRSF19 activity raises LOXL3's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.19× lower at baseline in the lines without TNFRSF19 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |
| [[PCDH9]] | C | TNFRSF19 activity raises PCDH9's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 3.90× lower at baseline in the lines without TNFRSF19 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |
| [[TTTY10]] | C | TNFRSF19 activity raises TTTY10's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without TNFRSF19 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |
| [[EDNRB]] | C | TNFRSF19 activity raises EDNRB's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without TNFRSF19 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |
| [[EIF1AY]] | C | TNFRSF19 activity raises EIF1AY's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without TNFRSF19 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |
| [[NRN1]] | C | TNFRSF19 activity raises NRN1's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.98× lower at baseline in the lines without TNFRSF19 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.400). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.0, 39.4); signed map (47.0, 37.6). **Vector** length 103, 30.4% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.7 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.6 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | -7.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.7 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12 — chr13:23,570,370-23,676,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAJ-alpha, TROY, TAJ, TRADE |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS68](https://www.uniprot.org/uniprotkb/Q9NS68) (Tumor necrosis factor receptor superfamily member 19):

> Can mediate activation of JNK and NF-kappa-B. May promote caspase-independent cell death.

**Summary**, from NCBI Gene [55504](https://www.ncbi.nlm.nih.gov/gene/55504):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor is highly expressed during embryonic development. It has been shown to interact with TRAF family members, and to activate JNK signaling pathway when overexpressed in cells. This receptor is capable of inducing apoptosis by a caspase-independent mechanism, and it is thought to play an essential role in embryonic development. Alternatively spliced transcript variants encoding distinct isoforms have been …

**Accessions** — [HGNC:11915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11915) · Entrez [55504](https://www.ncbi.nlm.nih.gov/gene/55504) · UniProt [Q9NS68](https://www.uniprot.org/uniprotkb/Q9NS68) · Ensembl [ENSG00000127863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127863)

## Data

Gene col 4837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4837); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4837]; `tensor/DDL_lfc|DDL_z.npy` [4837]; `embed/gene_vectors.npy` [4837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4837 or target_col == 4837). Every well: [[TNFRSF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
