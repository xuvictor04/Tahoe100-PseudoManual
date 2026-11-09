---
symbol: "SLC16A1-AS1"
type: "gene"
col: 13532
ensembl_id: "ENSG00000226419"
name: "SLC16A1 antisense RNA 1"
location: "1p13.2"
module: 124
arm: "+"
pooled_cpm: 49.26
n_lines_expressing: 45
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# SLC16A1-AS1

*SLC16A1 antisense RNA 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +6.2, q 4e-07, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.465× (z -9.2, q 2e-17, down in 37 of 43 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.550× (z -6.9, q 1e-09, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPH5-DT]] (+0.71, fdr 1e-05), [[GABPB1-AS1]] (+0.70, fdr 1e-05), [[ITPRIPL2]] (+0.67, fdr 1e-05); moves opposite to [[ALAD]] (-0.66, fdr 3e-05), [[RAB3A]] (-0.64, fdr 1e-04), [[DNAAF3]] (-0.60, fdr 3e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[KLHL42]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.2 | 4e-07 | 33/43 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.8 | 4e-04 | 26/43 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.004 | 23/43 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.004 | 22/43 (HT-29, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.081 | 17/43 (NCI-H1573, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.086 | 19/43 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.26× | +3.2 | 0.10 | 17/43 (SW480, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.2 | 0.10 | 15/43 (HCT15, SW480, …) | rises with dose | position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | 1.29× | +3.1 | 0.13 | 14/43 (MIA PaCa-2, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13532.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.465×** | -9.2 | 2e-17 | 37/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -6.9 | 1e-09 | 32/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.560×** | -6.7 | 3e-09 | 31/42 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -6.7 | 3e-09 | 35/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.616×** | -5.8 | 7e-07 | 25/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -5.0 | 5e-05 | 26/44 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.666×** | -4.9 | 9e-05 | 28/43 (C32, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.707×** | -4.2 | 0.002 | 22/43 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -3.8 | 0.009 | 22/43 (SNU-1, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -3.7 | 0.013 | 21/43 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **0.758×** | -3.3 | 0.042 | 21/43 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.758×** | -3.3 | 0.042 | 22/43 (SK-MEL-2, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -3.3 | 0.045 | 15/42 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.057 | 14/43 (J82, PANC-1, …) | top dose only | plate-row cell shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.614×** | -3.1 | 0.082 | 18/42 (RKO, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 216 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0867× (z -26.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.365× (z -11.0) |
| [[LoVo (line)]] | wt | 61.0 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.389× (z -8.8) |
| [[A-172 (line)]] | wt | 64.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.9) |
| [[PANC-1 (line)]] | alt | 36.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.364× (z -9.7) |
| [[A498 (line)]] | wt | 81.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 66.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -12.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.304× (z -9.0) |
| [[A-427 (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 36.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 85.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +9.5) | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -9.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 46.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0561× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 53.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.173× (z -9.4) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 106 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0794× (z -9.1) |
| [[SW48 (line)]] | wt | 44.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0447× (z -8.5) |
| [[SW480 (line)]] | alt | 45.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.0) | — |
| [[A549 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH5-DT]] | +0.71 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[GABPB1-AS1]] | +0.70 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[ITPRIPL2]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[HMGA1P4]] | +0.67 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SNHG26]] | +0.67 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[MCPH1]] | +0.66 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ITPA]] | +0.66 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[SPTY2D1OS]] | +0.65 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[RXYLT1]] | +0.64 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[ST7L]] | +0.63 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | +0.63 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[MRM1]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.66 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.64 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.60 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[ZNF511]] | -0.58 | -0.65 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[FOXO6]] | -0.58 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[EFNA4]] | -0.58 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[NXPH4]] | -0.57 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[PJA2]] | -0.57 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[SLC26A6]] | -0.57 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[PIN1]] | -0.57 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[MATCAP1]] | -0.56 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[GUSBP18]] | -0.56 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[ARL3]] | -0.55 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC16A1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises SLC16A1-AS1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without TMEM9B-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers SLC16A1-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PYGO1]] | B | PYGO1 activity raises SLC16A1-AS1's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without PYGO1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL42]] | B | SLC16A1-AS1 activity raises KLHL42's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without SLC16A1-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[CKMT2-AS1]] | B | SLC16A1-AS1 activity raises CKMT2-AS1's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without SLC16A1-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[MBD3]] | B | SLC16A1-AS1 activity raises MBD3's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without SLC16A1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[ANKRD18B]] | B | SLC16A1-AS1 activity raises ANKRD18B's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 2.82× lower at baseline in the lines without SLC16A1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[FBXO10]] | B | SLC16A1-AS1 activity raises FBXO10's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without SLC16A1-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |
| [[EXOSC6]] | B | SLC16A1-AS1 activity raises EXOSC6's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without SLC16A1-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-2.1, 8.8); signed map (25.9, -28.4). **Vector** length 98.3, 27.3% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -3.7 | -3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | -3.3 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | SLC16A1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p13.2 — chr1:112,849,821-113,047,055 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000421157.1; previously LINC01357 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49445) · Entrez [100506392](https://www.ncbi.nlm.nih.gov/gene/100506392) · Ensembl [ENSG00000226419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226419)

## Data

Gene col 13532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13532); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13532]; `tensor/DDL_lfc|DDL_z.npy` [13532]; `embed/gene_vectors.npy` [13532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13532 or target_col == 13532). Every well: [[SLC16A1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
