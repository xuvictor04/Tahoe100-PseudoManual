---
symbol: "ACOT12"
type: "gene"
col: 10263
ensembl_id: "ENSG00000172497"
name: "acyl-CoA thioesterase 12"
location: "5q14.1"
module: 39
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ACOT12

*acyl-CoA thioesterase 12* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +9.1, q 3e-17, up in 17 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.468× (z -5.5, q 2e-05, down in 22 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01031]] (+0.71, fdr 7e-06), [[ALDH8A1]] (+0.65, fdr 7e-06), [[SPOCK2]] (+0.64, fdr 7e-06); moves opposite to [[ALG6]] (-0.51, fdr 6e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IMPA1P1]] → it (grade B ⚠); 5 go from it, the strongest it → [[FLACC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +9.1 | 3e-17 | 17/29 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +8.9 | 2e-16 | 18/32 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +7.4 | 2e-11 | 2/5 (PANC-1, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +5.7 | 2e-06 | 20/39 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.19×** | +5.7 | 2e-06 | 19/41 (SNU-1, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +5.0 | 6e-05 | 14/37 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +4.2 | 0.002 | 7/26 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +4.0 | 0.005 | 4/15 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.006 | 10/32 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.006 | 12/40 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.69×** | +3.8 | 0.007 | 7/34 (H4, A-172, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +3.8 | 0.007 | 1/6 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.75×** | +3.7 | 0.008 | 5/24 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.015 | 9/33 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.016 | 6/34 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.1 | 0.081 | 6/39 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.468×** | -5.5 | 2e-05 | 22/38 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.633×** | -4.7 | 7e-04 | 13/40 (A498, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.520×** | -4.5 | 9e-04 | 11/34 (NCI-H1573, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -4.5 | 9e-04 | 16/33 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.543×** | -4.5 | 9e-04 | 18/37 (RPMI-7951, SNU-423, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -4.1 | 0.004 | 14/39 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.346×** | -4.0 | 0.004 | 8/24 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Glasdegib (drug)]] 5 µM | ⚠ unreliable plate only | 0.649× | -3.2 | 0.11 | 10/39 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.641× | -3.1 | 0.12 | 11/30 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.647× | -3.1 | 0.12 | 4/39 (HCT15, hTERT-HPNE, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0840× (z -9.0) ⚠ transcription drop · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0787× (z -8.9) |
| [[C32 (line)]] | wt | 13.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0629× (z -10.1) |
| [[LoVo (line)]] | wt | 1.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.2× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0434× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 3.89 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0355× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 8.57 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0528× (z -12.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.946 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01031]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SPOCK2]] | +0.64 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.63 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ADAM32]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FLACC1]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TG]] | +0.60 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.60 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CCNP]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[USP50]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG6]] | -0.51 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPA1P1]] | B | IMPA1P1 activity raises ACOT12's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without IMPA1P1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ACOT12's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ACOT12's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLACC1]] | B | ACOT12 activity raises FLACC1's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without ACOT12 | 0.050 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[LRRC39]] | B | ACOT12 activity raises LRRC39's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without ACOT12 | 0.083 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[FAM228B]] | B | ACOT12 activity raises FAM228B's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without ACOT12 | 0.091 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[LINC00486]] | B | ACOT12 activity raises LINC00486's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without ACOT12 | 0.097 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[SCUBE2]] | B | ACOT12 activity raises SCUBE2's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 2.88× lower at baseline in the lines without ACOT12 | 0.098 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, -13.3); signed map (17.5, 7.8). **Vector** length 56.7, 8.54% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.0 | -5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.0 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:81,329,996-81,394,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cach, THEAL, STARD15 |
| Gene groups (HGNC) | Acyl-CoA thioesterases; StAR related lipid transfer domain containing; Thioester hydrolases |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYK0](https://www.uniprot.org/uniprotkb/Q8WYK0) (Acetyl-coenzyme A thioesterase):

> Catalyzes the hydrolysis of acyl-CoAs into free fatty acids and coenzyme A (CoASH), regulating their respective intracellular levels. Preferentially hydrolyzes acetyl-CoA.

**Summary**, from NCBI Gene [134526](https://www.ncbi.nlm.nih.gov/gene/134526):

> Enables identical protein binding activity. Predicted to be involved in acetyl-CoA metabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24436](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24436) · Entrez [134526](https://www.ncbi.nlm.nih.gov/gene/134526) · UniProt [Q8WYK0](https://www.uniprot.org/uniprotkb/Q8WYK0) · Ensembl [ENSG00000172497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172497)

## Data

Gene col 10263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10263); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10263]; `tensor/DDL_lfc|DDL_z.npy` [10263]; `embed/gene_vectors.npy` [10263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10263 or target_col == 10263). Every well: [[ACOT12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
