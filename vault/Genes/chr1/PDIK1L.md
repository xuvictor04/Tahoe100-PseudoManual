---
symbol: "PDIK1L"
type: "gene"
col: 10560
ensembl_id: "ENSG00000175087"
name: "PDLIM1 interacting kinase 1 like"
location: "1p36.11"
module: 28
arm: "+"
pooled_cpm: 9.47
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# PDIK1L

*PDLIM1 interacting kinase 1 like* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +13.9, q 7e-41, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.709× (z -7.9, q 2e-12, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD2]] (+0.64, fdr 9e-06), [[SMARCE1]] (+0.60, fdr 1e-05), [[DIS3L]] (+0.60, fdr 7e-06); moves opposite to [[KLHL29]] (-0.61, fdr 3e-05), [[TPTEP2-CSNK1E]] (-0.55, fdr 2e-05), [[RABGEF1]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +13.9 | 7e-41 | 36/47 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +8.8 | 3e-16 | 9/18 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +7.4 | 2e-11 | 23/47 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.3 | 3e-11 | 16/36 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.3 | 3e-11 | 19/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +7.2 | 4e-11 | 21/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.9 | 4e-10 | 22/42 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +5.9 | 3e-07 | 15/46 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 14/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.5 | 4e-04 | 10/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 6e-04 | 14/47 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 6e-04 | 14/47 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.3 | 7e-04 | 16/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.002 | 12/44 (A-427, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 12/45 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 9/45 (SW480, SW48, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.020 | 9/45 (HT-29, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.709×** | -7.9 | 2e-12 | 26/48 (Hs 766T, PANC-1, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.643×** | -7.1 | 3e-10 | 26/46 (COLO 205, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -5.6 | 4e-06 | 19/45 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.756×** | -4.5 | 9e-04 | 12/45 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.061 | 12/43 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.819× | -3.2 | 0.11 | 9/46 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.825× | -3.1 | 0.14 | 1/48 (A-427) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.826× | -3.1 | 0.14 | 10/45 (HCT15, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 11.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 11.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0895× (z -11.4) |
| [[A498 (line)]] | wt | 10.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.9× (z +13.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.79 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0757× (z -11.9) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0366× (z -10.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 9.21 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.190× (z -10.7) |
| [[LoVo (line)]] | wt | 8.83 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.73× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.198× (z -9.0) |
| [[SW48 (line)]] | wt | 20.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0651× (z -11.5) |
| [[A549 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD2]] | +0.64 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[SMARCE1]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[DIS3L]] | +0.60 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LSM14A]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[MDM1]] | +0.59 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CLUAP1]] | +0.58 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[RNF214]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PEX1]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SCRN3]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HINT3]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ASB8]] | +0.56 | +0.70 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL29]] | -0.61 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RABGEF1]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TPT1-AS1]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TTLL3]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[RAB7A]] | -0.51 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[LINC01128]] | -0.49 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[CYTH1]] | -0.49 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[LIPE-AS1]] | -0.49 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[SLC9A1]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[FBXW7]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[BUD23]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PDIK1L's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC16A3]] | B | SLC16A3 activity lowers PDIK1L's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.26× higher at baseline in the lines without SLC16A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity raises PDIK1L's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.6, 2.3); signed map (6.5, -26.9). **Vector** length 72.7, 12.0% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PDLIM1 interacting kinase 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,111,165-26,125,555 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLIK1L, STK35L2 |
| Gene groups (HGNC) | Serine/threonine kinase 35 family |
| Matched by | ensembl_id |

UniProt [Q8N165](https://www.uniprot.org/uniprotkb/Q8N165) carries no function annotation.

**Summary**, from NCBI Gene [149420](https://www.ncbi.nlm.nih.gov/gene/149420):

> Predicted to enable protein kinase activity. Predicted to be involved in negative regulation of G2/M transition of mitotic cell cycle and negative regulation of G2/MI transition of meiotic cell cycle. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18981) · Entrez [149420](https://www.ncbi.nlm.nih.gov/gene/149420) · UniProt [Q8N165](https://www.uniprot.org/uniprotkb/Q8N165) · Ensembl [ENSG00000175087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175087)

## Data

Gene col 10560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10560); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10560]; `tensor/DDL_lfc|DDL_z.npy` [10560]; `embed/gene_vectors.npy` [10560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10560 or target_col == 10560). Every well: [[PDIK1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDIK1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
