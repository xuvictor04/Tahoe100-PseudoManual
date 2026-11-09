---
symbol: "SDSL"
type: "gene"
col: 6303
ensembl_id: "ENSG00000139410"
name: "serine dehydratase like"
location: "12q24.13"
module: 94
arm: "+"
pooled_cpm: 3.1
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 7
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# SDSL

*serine dehydratase like* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.05× (z +17.5, q 0e+00, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.396× (z -7.1, q 8e-10, down in 27 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL18]] (+0.78, fdr 7e-06), [[ZNF747]] (+0.77, fdr 7e-06), [[TIGD6]] (+0.77, fdr 7e-06); moves opposite to [[CALU]] (-0.66, fdr 1e-05), [[TCF3]] (-0.65, fdr 1e-05), [[DCUN1D2]] (-0.63, fdr 7e-06).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.05×** | +17.5 | 0e+00 | 27/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.28×** | +14.1 | 2e-42 | 31/34 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **3.43×** | +13.4 | 2e-38 | 40/44 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.69×** | +12.6 | 2e-34 | 38/42 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.11×** | +10.8 | 3e-25 | 40/44 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +10.4 | 4e-23 | 29/33 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +8.2 | 3e-14 | 11/13 (BT-474, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **2.74×** | +7.7 | 8e-13 | 34/45 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.47×** | +6.9 | 3e-10 | 28/38 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.47×** | +6.9 | 3e-10 | 24/39 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.42×** | +6.8 | 6e-10 | 27/41 (LS 180, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +6.7 | 1e-09 | 1/2 (A498) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +6.6 | 2e-09 | 4/5 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +6.2 | 2e-08 | 20/30 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.15×** | +5.9 | 2e-07 | 20/42 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.8 | 3e-07 | 17/46 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +4.5 | 2e-04 | 15/35 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.77×** | +4.0 | 0.002 | 12/31 (A-427, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.396×** | -7.1 | 8e-10 | 27/41 (A-172, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -5.8 | 2e-06 | 23/41 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.574×** | -4.3 | 0.004 | 14/38 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -4.1 | 0.005 | 15/46 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.636×** | -3.5 | 0.056 | 9/46 (A549, AN3 CA, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.424×** | -3.4 | 0.056 | 5/38 (RKO, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.650×** | -3.3 | 0.078 | 8/31 (J82, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.458× | -3.1 | 0.11 | 11/38 (A498, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.458× | -3.1 | 0.11 | 9/30 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.754× | -3.1 | 0.12 | 8/43 (A498, NCI-H23, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.468× | -3.0 | 0.12 | 5/45 (RKO, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.59 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +9.4) | [[Digitoxin (drug)]] 0.5 µM 0.0505× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 4.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 6.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +10.4) | — |
| [[J82 (line)]] | alt | 3.61 | 0 | 1 | — | [[Torkinib (drug)]] 0.05 µM 0.0546× (z -8.7) |
| [[KATO III (line)]] | alt | 2.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 4.51 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0743× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 5.43 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0791× (z -8.5) |
| [[SW1417 (line)]] | alt | 6.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +10.4) | — |
| [[SW480 (line)]] | alt | 2.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.2) | — |
| [[A-427 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL18]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.77 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[TIGD6]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PATL2]] | +0.74 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[TRIP6]] | +0.72 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD31]] | +0.72 | +0.81 / +0.54 | both halves | 1e-05 |  |
| [[PCLO]] | +0.72 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[ZNF518A]] | +0.72 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZNF441]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[PPCS]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALU]] | -0.66 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[TCF3]] | -0.65 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.63 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RBM14-RBM4]] | -0.63 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[SBNO1]] | -0.63 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[TPST2]] | -0.62 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[SDHAP1]] | -0.62 | -0.77 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SDSL's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ZNF85]] | B | ZNF85 activity raises SDSL's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without ZNF85 | 0.066 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726 |
| [[SLC2A6]] | B | SLC2A6 activity raises SDSL's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without SLC2A6 | 0.067 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[HES7]] | B | HES7 activity raises SDSL's level | lines that do not express HES7 (13) vs lines expressing it (37) | 1.21× lower at baseline in the lines without HES7 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.5, 22.5); signed map (15.3, -17.8). **Vector** length 80.9, 16.4% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +17.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | +0.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | serine dehydratase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,422,380-113,438,276 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDS-RS1, cSDH |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GA7](https://www.uniprot.org/uniprotkb/Q96GA7) (Serine dehydratase-like):

> Catalyzes the pyridoxal-phosphate-dependent dehydrative deamination of L-threonine and L-serine to ammonia and alpha-ketobutyrate and pyruvate, respectively. Also exhibits racemase activity towards L-glutamate and D-glutamate (By similarity).

**Summary**, from NCBI Gene [113675](https://www.ncbi.nlm.nih.gov/gene/113675):

> Enables L-serine ammonia-lyase activity; identical protein binding activity; and threonine deaminase activity. Predicted to be involved in L-serine catabolic process and L-threonine catabolic process. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30404) · Entrez [113675](https://www.ncbi.nlm.nih.gov/gene/113675) · UniProt [Q96GA7](https://www.uniprot.org/uniprotkb/Q96GA7) · Ensembl [ENSG00000139410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139410)

## Data

Gene col 6303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6303); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6303]; `tensor/DDL_lfc|DDL_z.npy` [6303]; `embed/gene_vectors.npy` [6303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6303 or target_col == 6303). Every well: [[SDSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
