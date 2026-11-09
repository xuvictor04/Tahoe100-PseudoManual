---
symbol: "CYP27C1"
type: "gene"
col: 11845
ensembl_id: "ENSG00000186684"
name: "cytochrome P450 family 27 subfamily C member 1"
location: "2q14.3"
module: 13
arm: "+"
pooled_cpm: 10.92
n_lines_expressing: 31
n_dd_up: 6
n_dd_down: 47
n_dd_up_clean: 3
n_dd_down_clean: 43
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CYP27C1

*cytochrome P450 family 27 subfamily C member 1* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.74× (z +7.0, q 2e-09, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.151× (z -24.7, q 0e+00, down in 27 of 28 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDGA1]] (+0.55, fdr 9e-05), [[TSHZ3-AS1]] (+0.53, fdr 4e-05), [[FBXL8]] (+0.53, fdr 4e-05); moves opposite to [[NUDT11]] (-0.54, fdr 3e-05), [[SHROOM2]] (-0.53, fdr 4e-05), [[THEM6]] (-0.52, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SIRLNT]] → it (grade C ⚠); 2 go from it, the strongest it → [[BCL10-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.74×** | +7.0 | 2e-09 | 18/27 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 2e-07 | 15/27 (NCI-H460, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.7 | 4e-04 | 4/18 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **1.28×** | +4.6 | 5e-04 | 11/28 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.3 | 0.002 | 4/16 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +3.7 | 0.022 | 5/28 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.17 | 6/27 (NCI-H460, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.55× | +3.0 | 0.17 | 5/28 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.27× | +3.0 | 0.17 | 3/27 (H4, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.151×** | -24.7 | 0e+00 | 27/28 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.167×** | -23.5 | 0e+00 | 27/28 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.191×** | -21.7 | 0e+00 | 27/29 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.416×** | -16.2 | 0e+00 | 25/28 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.307×** | -14.9 | 0e+00 | 24/28 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.354×** | -13.6 | 4e-40 | 23/28 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.370×** | -13.0 | 1e-36 | 26/29 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.496×** | -9.2 | 4e-18 | 20/29 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.612×** | -9.1 | 8e-18 | 20/28 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.523×** | -8.5 | 1e-15 | 24/29 (A-172, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.530×** | -8.3 | 6e-15 | 20/27 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.313×** | -7.9 | 9e-14 | 22/28 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.554×** | -7.7 | 5e-13 | 20/29 (H4, NCI-H1792, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -7.2 | 3e-11 | 19/26 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.589×** | -6.5 | 3e-09 | 18/27 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -6.3 | 1e-08 | 20/27 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.620×** | -6.2 | 1e-08 | 17/28 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 48.3 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0307× (z -28.8) |
| [[A-172 (line)]] | wt | 28.3 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0271× (z -24.7) |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0775× (z -16.4) |
| [[A549 (line)]] | wt | 14.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0825× (z -18.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0873× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -22.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0907× (z -16.0) |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0973× (z -14.9) |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0539× (z -17.6) |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0756× (z -22.5) |
| [[H4 (line)]] | wt | 22.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0210× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0423× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0414× (z -23.7) |
| [[AsPC-1 (line)]] | alt | 8.78 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0618× (z -12.0) |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0671× (z -20.5) |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0892× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 8.88 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0703× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 6.40 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0587× (z -10.3) |
| [[C-33 A (line)]] | alt | 7.27 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0521× (z -9.4) |
| [[LoVo (line)]] | wt | 5.75 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.102× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 9.33 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -9.9) |
| [[C32 (line)]] | wt | 5.18 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0313× (z -11.1) |
| [[SW 900 (line)]] | alt | 6.67 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0270× (z -13.3) |
| [[A-427 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDGA1]] | +0.55 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[TSHZ3-AS1]] | +0.53 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[FBXL8]] | +0.53 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[SIRLNT]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[RSPH9]] | +0.52 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[PPP4R1L]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[AADACL2-AS1]] | +0.52 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[CACNG8]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[VEGFC]] | +0.51 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GJA1]] | +0.50 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ANXA10]] | +0.49 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[CACNG6]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT11]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SHROOM2]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[THEM6]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[BABAM2]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MAOA]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SLC27A2]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CDCA7L]] | -0.49 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ANK3]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PKP2]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[RAPGEF5]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[WDR17]] | -0.46 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[SAMD12]] | -0.46 | -0.44 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRLNT]] | C | SIRLNT activity raises CYP27C1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.40× lower at baseline in the lines without SIRLNT | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[CACNG6]] | C | CACNG6 activity raises CYP27C1's level | lines that do not express CACNG6 (18) vs lines expressing it (32) | 4.12× lower at baseline in the lines without CACNG6 | 0.020 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, RAB31, CYP27C1; co-absent with the target |
| [[VEGFC]] | C | VEGFC activity raises CYP27C1's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 3.92× lower at baseline in the lines without VEGFC | 0.038 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL10-AS1]] | B | CYP27C1 activity raises BCL10-AS1's level | lines that do not express CYP27C1 (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without CYP27C1 | 0.030 | ⚠ within organs, on part of the lines; also absent: CACNG6, ENSG00000289526, RAB31 |
| [[CACNG8]] | C | CYP27C1 activity raises CACNG8's level | lines that do not express CYP27C1 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without CYP27C1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CACNG6, ENSG00000289526, RAB31; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.395). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 11.6); signed map (25.0, 50.9). **Vector** length 76.6, 18.8% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +6.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | -0.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -13.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 27 subfamily C member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,183,832-127,220,313 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16008 |
| Gene groups (HGNC) | Cytochrome P450 family 27 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0S4](https://www.uniprot.org/uniprotkb/Q4G0S4) (Cytochrome P450 27C1):

> [Isoform 2]: A cytochrome P450 monooxygenase that catalyzes the 3,4 desaturation of all-trans-retinol (also called vitamin A1) to all-trans-3,4-didehydroretinol (also called vitamin A2) in the skin. Desaturates with lower efficiency all-trans retinal and all-trans retinoic acid. Forms minor amounts of 3-hydroxy and 4-hydroxy all-trans-retinol derivatives. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate and reducing the second into a water molecule. Two …

**Summary**, from NCBI Gene [339761](https://www.ncbi.nlm.nih.gov/gene/339761):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:33480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33480) · Entrez [339761](https://www.ncbi.nlm.nih.gov/gene/339761) · UniProt [Q4G0S4](https://www.uniprot.org/uniprotkb/Q4G0S4) · Ensembl [ENSG00000186684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186684)

## Data

Gene col 11845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11845); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11845]; `tensor/DDL_lfc|DDL_z.npy` [11845]; `embed/gene_vectors.npy` [11845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11845 or target_col == 11845). Every well: [[CYP27C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP27C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
