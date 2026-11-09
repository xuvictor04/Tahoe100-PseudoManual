---
symbol: "SLC9A5"
type: "gene"
col: 5749
ensembl_id: "ENSG00000135740"
name: "solute carrier family 9 member A5"
location: "16q22.1"
module: 38
arm: "+"
pooled_cpm: 9.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SLC9A5

*solute carrier family 9 member A5* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +22.8, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.755× (z -3.7, q 0.046, down in 11 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISY1-RAB43]] (+0.77, fdr 7e-06), [[IDI2-AS1]] (+0.77, fdr 7e-06), [[NUP210L]] (+0.76, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +22.8 | 0e+00 | 43/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.38×** | +16.2 | 0e+00 | 42/45 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +14.1 | 4e-43 | 31/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +9.5 | 2e-19 | 27/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.5 | 1e-15 | 24/47 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +8.5 | 2e-15 | 27/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.5 | 8e-09 | 23/44 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.4 | 8e-09 | 24/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +5.9 | 2e-07 | 20/47 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.51×** | +5.3 | 7e-06 | 20/39 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +5.1 | 2e-05 | 16/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 5e-04 | 15/45 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.007 | 13/48 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.27×** | +3.2 | 0.065 | 17/48 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Naproxen (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.081 | 9/43 (hTERT-HPNE, BT-474, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.081 | 5/48 (NCI-H23, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -3.7 | 0.046 | 11/46 (SNU-1, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -3.7 | 0.046 | 11/46 (A-172, SK-MEL-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.590×** | -3.7 | 0.046 | 11/40 (SK-MEL-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.607×** | -3.5 | 0.073 | 9/40 (HCT15, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.793× | -3.1 | 0.21 | 10/45 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.794× | -3.1 | 0.21 | 2/48 (CFPAC-1, HOP62) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.4 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 9.48 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +15.6) | — |
| [[LoVo (line)]] | wt | 11.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +11.4) | — |
| [[A-172 (line)]] | wt | 4.35 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 5.46 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +9.0) | [[Radotinib (drug)]] 0.5 µM 0.0581× (z -10.9) |
| [[HCT15 (line)]] | alt | 18.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +8.8) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.108× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 6.95 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 6.75 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 10.4× (z +9.1) | [[Nimesulide (drug)]] 5 µM 0.0890× (z -9.5) ⚠ toxic; unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 25.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.6) | — |
| [[A549 (line)]] | wt | 7.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 9.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.7) | — |
| [[C32 (line)]] | wt | 7.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 10.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.92× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 7.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 3.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 5 µM 0.0429× (z -9.9) |
| [[PANC-1 (line)]] | alt | 5.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +11.1) | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0792× (z -8.8) |
| [[SW 900 (line)]] | alt | 9.13 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.00× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 4.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +8.8) | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISY1-RAB43]] | +0.77 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.76 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.75 | +0.82 / +0.52 | both halves | 1e-05 |  |
| [[VWCE]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[COL20A1]] | +0.74 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[THUMPD3-AS1]] | +0.74 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.74 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[ARL9]] | +0.74 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[PYY]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[GPR137]] | +0.73 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.73 | +0.75 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC9A5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC26A4]] | B | SLC26A4 activity raises SLC9A5's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without SLC26A4 | 0.087 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[FER1L4]] | B | FER1L4 activity raises SLC9A5's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without FER1L4 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[DLG4]] | C | DLG4 activity raises SLC9A5's level | lines that do not express DLG4 (3) vs lines expressing it (46) | 1.71× lower at baseline in the lines without DLG4 | 0.072 | ⚠ few lines (3 vs 46); within organs, on part of the lines; also absent: CHST14, NECAB2, DMXL2; maybe low, not absent |
| [[MMP25]] | C | MMP25 activity raises SLC9A5's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.32× lower at baseline in the lines without MMP25 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |
| [[TRIM72]] | C | TRIM72 activity raises SLC9A5's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without TRIM72 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.6, -18.5); signed map (13.3, 11.4). **Vector** length 83.2, 15.8% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +22.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +9.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.5 | +3.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.1 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,237,683-67,272,191 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NHE5 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 4 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14940](https://www.uniprot.org/uniprotkb/Q14940) (Sodium/hydrogen exchanger 5):

> Plasma membrane Na(+)/H(+) antiporter. Mediates the electroneutral exchange of intracellular H(+) ions for extracellular Na(+) in 1:1 stoichiometry, thus regulating intracellular pH homeostasis, in particular in neural tissues. Acts as a negative regulator of dendritic spine growth. Plays a role in postsynaptic remodeling and signaling. Can also contribute to organellar pH regulation, with consequences for receptor tyrosine kinase trafficking.

**Summary**, from NCBI Gene [6553](https://www.ncbi.nlm.nih.gov/gene/6553):

> Enables arrestin family protein binding activity and sodium:proton antiporter activity. Involved in regulation of intracellular pH and sodium ion transmembrane transport. Located in several cellular components, including focal adhesion; neuron spine; and recycling endosome membrane. Implicated in end stage renal disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11078) · Entrez [6553](https://www.ncbi.nlm.nih.gov/gene/6553) · UniProt [Q14940](https://www.uniprot.org/uniprotkb/Q14940) · Ensembl [ENSG00000135740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135740)

## Data

Gene col 5749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5749); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5749]; `tensor/DDL_lfc|DDL_z.npy` [5749]; `embed/gene_vectors.npy` [5749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5749 or target_col == 5749). Every well: [[SLC9A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
