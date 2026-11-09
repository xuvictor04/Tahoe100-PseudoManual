---
symbol: "PRKAR2B"
type: "gene"
col: 77
ensembl_id: "ENSG00000005249"
name: "protein kinase cAMP-dependent type II regulatory subunit beta"
location: "7q22.3"
module: 176
arm: "+"
pooled_cpm: 10.58
n_lines_expressing: 38
n_dd_up: 27
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# PRKAR2B

*protein kinase cAMP-dependent type II regulatory subunit beta* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 6.06× (z +26.5, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.766× (z -4.0, q 0.040, down in 10 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM22]] (+0.67, fdr 7e-06), [[HLTF]] (+0.61, fdr 3e-05), [[LRRC1]] (+0.61, fdr 8e-06); moves opposite to [[NMNAT1]] (-0.59, fdr 5e-05), [[FAM120B]] (-0.58, fdr 2e-05), [[ANKRD17-DT]] (-0.56, fdr 1e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GPR37]] → it (grade B ⚠); 8 go from it, the strongest it → [[BCL11A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 77.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **6.06×** | +26.5 | 0e+00 | 33/34 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.90×** | +26.1 | 0e+00 | 35/35 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.88×** | +26.1 | 0e+00 | 33/34 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.48×** | +26.0 | 0e+00 | 32/35 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.41×** | +21.9 | 0e+00 | 34/35 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.85×** | +13.9 | 9e-42 | 29/34 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.64×** | +13.7 | 6e-41 | 9/13 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **5.45×** | +13.1 | 4e-37 | 33/35 (A498, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.35×** | +12.5 | 3e-34 | 24/30 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.03×** | +10.4 | 2e-23 | 25/34 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.94×** | +9.0 | 1e-17 | 9/19 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +7.2 | 2e-11 | 18/34 (C32, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.2 | 3e-11 | 17/35 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +5.8 | 2e-07 | 14/34 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.31×** | +5.7 | 6e-07 | 11/34 (C32, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +5.6 | 9e-07 | 10/35 (CHP-212, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 9e-04 | 4/35 (NCI-H23, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.003 | 8/34 (SK-MEL-2, SNU-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.004 | 10/36 (C32, SW48, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 77.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.766×** | -4.0 | 0.040 | 10/34 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.769×** | -3.7 | 0.041 | 11/35 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.780×** | -3.7 | 0.041 | 15/33 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -3.6 | 0.051 | 11/35 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.086 | 7/34 (SW 900, NCI-H1573, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.086 | 11/34 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.735×** | -3.3 | 0.089 | 8/34 (SW48, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.806×** | -3.2 | 0.092 | 12/33 (H4, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 77. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.34 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +13.8) | — |
| [[C32 (line)]] | wt | 67.4 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.97× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.10× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 5.77 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.26× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 5.98 | 4 | 0 | [[Belinostat (drug)]] 5 µM 9.51× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.64× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +11.1) | — |
| [[A-172 (line)]] | wt | 10.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.46× (z +9.2) | — |
| [[J82 (line)]] | alt | 5.31 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.37× (z +9.4) | — |
| [[LoVo (line)]] | wt | 10.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.60× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 4.21 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -8.6) |
| [[A-427 (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 6.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0734× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.10 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.35× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 5.11 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.87× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 6.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 3.86 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 14.5× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 77), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM22]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[HLTF]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[LRRC1]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[SOAT1]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[FHL1]] | +0.60 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[TMEM170B]] | +0.60 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[MPP1]] | +0.60 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[CDCA7L]] | +0.60 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ZDHHC20]] | +0.59 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[HMGN3]] | +0.59 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[ATP1A3]] | +0.59 | +0.33 / +0.68 | both halves | 1e-04 |  |
| [[RADX]] | +0.58 | +0.36 / +0.60 | both halves | 9e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT1]] | -0.59 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[FAM120B]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD17-DT]] | -0.56 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[RABL2B]] | -0.56 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RABL2A]] | -0.54 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[GPATCH2]] | -0.54 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[DDX59]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CSTF3]] | -0.53 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[FBXW4]] | -0.53 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[ZNF586]] | -0.53 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[FBXL9P]] | -0.53 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[UBE2CP5]] | -0.53 | -0.49 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR37]] | B | GPR37 activity raises PRKAR2B's level | lines that do not express GPR37 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without GPR37 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ECHDC3, L3MBTL4 |
| [[ADAM22]] | B | ADAM22 activity raises PRKAR2B's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.26× lower at baseline in the lines without ADAM22 | 0.070 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises PRKAR2B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM170B]] | B | TMEM170B activity raises PRKAR2B's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 3.22× lower at baseline in the lines without TMEM170B | 0.084 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[APBA1]] | C | APBA1 activity raises PRKAR2B's level | lines that do not express APBA1 (6) vs lines expressing it (44) | 4.68× lower at baseline in the lines without APBA1 | 0.077 | ⚠ within organs, on part of the lines; also absent: MATN2, CCDC102A, ENSG00000267131; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL11A]] | B | PRKAR2B activity raises BCL11A's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 2.09× lower at baseline in the lines without PRKAR2B | 0.040 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[LRRC41]] | B | PRKAR2B activity raises LRRC41's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without PRKAR2B | 0.048 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[NEO1]] | B | PRKAR2B activity raises NEO1's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without PRKAR2B | 0.053 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[TMOD2]] | B | PRKAR2B activity raises TMOD2's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without PRKAR2B | 0.054 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[PRKY]] | B | PRKAR2B activity raises PRKY's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 3.77× lower at baseline in the lines without PRKAR2B | 0.056 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[RAB28]] | B | PRKAR2B activity raises RAB28's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.24× lower at baseline in the lines without PRKAR2B | 0.068 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[TOX2]] | B | PRKAR2B activity raises TOX2's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 2.95× lower at baseline in the lines without PRKAR2B | 0.071 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[RPAP2]] | B | PRKAR2B activity raises RPAP2's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 1.30× lower at baseline in the lines without PRKAR2B | 0.098 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.6, 38.7); signed map (24.0, 31.0). **Vector** length 77.9, 16.2% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +26.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +13.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +21.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +26.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-dependent type II regulatory subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:107,044,705-107,161,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRKAR2 |
| Gene groups (HGNC) | Protein kinase A subunits |
| Hallmark sets | UV_RESPONSE_DN, ESTROGEN_RESPONSE_LATE |
| Reactome | 61 pathways, smallest: CREB1 phosphorylation through the activation of Adenylate Cyclase; PKA activation in glucagon signalling; PKA activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P31323](https://www.uniprot.org/uniprotkb/P31323) (cAMP-dependent protein kinase type II-beta regulatory subunit):

> Regulatory subunit of the cAMP-dependent protein kinases involved in cAMP signaling in cells. Type II regulatory chains mediate membrane association by binding to anchoring proteins, including the MAP2 kinase.

**Summary**, from NCBI Gene [5577](https://www.ncbi.nlm.nih.gov/gene/5577):

> cAMP is a signaling molecule important for a variety of cellular functions. cAMP exerts its effects by activating the cAMP-dependent protein kinase, which transduces the signal through phosphorylation of different target proteins. The inactive kinase holoenzyme is a tetramer composed of two regulatory and two catalytic subunits. cAMP causes the dissociation of the inactive holoenzyme into a dimer of regulatory subunits bound to four cAMP and two free monomeric catalytic subunits. Four different …

**Accessions** — [HGNC:9392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9392) · Entrez [5577](https://www.ncbi.nlm.nih.gov/gene/5577) · UniProt [P31323](https://www.uniprot.org/uniprotkb/P31323) · Ensembl [ENSG00000005249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005249)

## Data

Gene col 77: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 77); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 77, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 77]; `tensor/DDL_lfc|DDL_z.npy` [77]; `embed/gene_vectors.npy` [77]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 77 or target_col == 77). Every well: [[PRKAR2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAR2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
