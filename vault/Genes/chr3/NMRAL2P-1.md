---
symbol: "NMRAL2P-1"
type: "gene"
col: 16518
ensembl_id: "ENSG00000290862"
name: ""
location: ""
module: 117
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 9
direction_downstream: 27
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# NMRAL2P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.75× (z +10.6, q 1e-23, up in 20 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.316× (z -7.1, q 1e-09, down in 22 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMRAL2P]] (+0.90, fdr 7e-06, ⚠ same locus), [[TRIM16L]] (+0.77, fdr 7e-06), [[CYP4F11]] (+0.71, fdr 7e-06), [[ABCC2]] (+0.67, fdr 7e-06); moves opposite to [[APAF1]] (-0.53, fdr 3e-05), [[IDH2]] (-0.52, fdr 7e-05), [[GPN3]] (-0.51, fdr 1e-04).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[AKR1C2]] → it (grade B ⚠); 27 go from it, the strongest it → [[CASP7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.75×** | +10.6 | 1e-23 | 20/24 (LoVo, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +8.6 | 2e-15 | 3/7 (AsPC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.21×** | +8.4 | 8e-15 | 1/3 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.76×** | +7.4 | 1e-11 | 1/4 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.61×** | +5.5 | 4e-06 | 15/21 (COLO 205, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.12×** | +4.6 | 5e-04 | 14/25 (COLO 205, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +4.4 | 1e-03 | 12/28 (NCI-H1573, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.3 | 0.001 | 2/12 (CFPAC-1, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.88×** | +3.8 | 0.008 | 12/25 (AsPC-1, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.7 | 0.013 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.82×** | +3.6 | 0.015 | 7/25 (LoVo, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.29×** | +3.6 | 0.015 | 3/13 (SW480, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +3.6 | 0.015 | 7/21 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +3.4 | 0.025 | 7/24 (COLO 205, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.20×** | +3.4 | 0.025 | 2/8 (NCI-H1573, NCI-H2030) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.056 | 3/27 (CFPAC-1, A498, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.081 | 3/25 (KATO III, NCI-H1573, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.70×** | +3.0 | 0.090 | 0/13 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.316×** | -7.1 | 1e-09 | 22/28 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.367×** | -6.1 | 2e-07 | 22/26 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.383×** | -5.9 | 7e-07 | 20/27 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.374× | -3.2 | 0.19 | 7/25 (NCI-H1573, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.603× | -3.1 | 0.19 | 2/26 (Panc 03.27, NCI-H460) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.606× | -3.1 | 0.19 | 8/27 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 33.5 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0963× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0543× (z -19.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -8.9) |
| [[SW480 (line)]] | alt | 1.49 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0376× (z -10.4) |
| [[A-172 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.790 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.770 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.470 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMRAL2P]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TRIM16L]] | +0.77 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[CYP4F11]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[VEGFD]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SLC7A11]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[AKR1C1]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[LINC01564]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[GCLM]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[PIR]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MGST1]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[FBXW10B]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[IDH2]] | -0.52 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[GPN3]] | -0.51 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[MOSPD3]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[RNASET2]] | -0.49 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[DDHD2]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[FUCA1]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ARL3]] | -0.48 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[AKR7A2]] | -0.48 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[SNX25]] | -0.48 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[SPATA33]] | -0.47 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[OXR1]] | -0.47 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C2]] | B | AKR1C2 activity raises NMRAL2P-1's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.22× lower at baseline in the lines without AKR1C2 | 0.002 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[AKR1C1]] | B | AKR1C1 activity raises NMRAL2P-1's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without AKR1C1 | 0.026 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |
| [[HDAC6]] | B | HDAC6 activity raises NMRAL2P-1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01564]] | B | LINC01564 activity raises NMRAL2P-1's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without LINC01564 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[MGST1]] | B | MGST1 activity raises NMRAL2P-1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without MGST1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[NMRAL2P]] | C | NMRAL2P activity raises NMRAL2P-1's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without NMRAL2P | 0.001 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises NMRAL2P-1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without CYP4F3 | 0.008 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises NMRAL2P-1's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.09× lower at baseline in the lines without CYP4F11 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[AKR1C3]] | C | AKR1C3 activity raises NMRAL2P-1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 1.68× lower at baseline in the lines without AKR1C3 | 0.046 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 22, C 5. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP7]] | B | NMRAL2P-1 activity raises CASP7's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without NMRAL2P-1 | 0.011 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[CYP39A1]] | B | NMRAL2P-1 activity raises CYP39A1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without NMRAL2P-1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[MGST1]] | B | NMRAL2P-1 activity raises MGST1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without NMRAL2P-1 | 0.021 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[ZFAND5]] | B | NMRAL2P-1 activity raises ZFAND5's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without NMRAL2P-1 | 0.028 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[LINC02057]] | B | NMRAL2P-1 activity raises LINC02057's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without NMRAL2P-1 | 0.033 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[GPN3]] | B | NMRAL2P-1 activity lowers GPN3's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.28× higher at baseline in the lines without NMRAL2P-1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[TLR6]] | B | NMRAL2P-1 activity raises TLR6's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without NMRAL2P-1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[LINC01564]] | B | NMRAL2P-1 activity raises LINC01564's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without NMRAL2P-1 | 0.050 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[FBXW10B]] | B | NMRAL2P-1 activity raises FBXW10B's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without NMRAL2P-1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[TLR1]] | B | NMRAL2P-1 activity weakens TLR1's drug response | lines that do not express NMRAL2P-1 (10) vs lines expressing it (22) | the lines without NMRAL2P-1 respond 1.03× as strongly (z diff -0.09); strongest at Homoharringtonine 5 µM: 5.05x vs 1.21x (z diff -6.2) | 0.059 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1; target measured in part of the lines; both ways; artifact flags |
| [[TLR1]] | B | NMRAL2P-1 activity raises TLR1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without NMRAL2P-1 | 0.068 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[SYNE1]] | B | NMRAL2P-1 activity raises SYNE1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without NMRAL2P-1 | 0.068 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.0, 48.2); signed map (51.1, -9.8). **Vector** length 53.8, 11.1% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.59 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.60 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.60 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.4 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -7.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | +0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

> [!warning] No registry record
> NMRAL2P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16518); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16518]; `tensor/DDL_lfc|DDL_z.npy` [16518]; `embed/gene_vectors.npy` [16518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16518 or target_col == 16518). Every well: [[NMRAL2P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMRAL2P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
