---
symbol: "THBS4-AS1"
type: "gene"
col: 14641
ensembl_id: "ENSG00000249825"
name: "THBS4 antisense RNA 1"
location: "5q14.1"
module: 26
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# THBS4-AS1

*THBS4 antisense RNA 1* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 16.3× (z +28.5, q 0e+00, up in 18 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pravastatin (sodium) (drug)]] 5 µM: 0.577× (z -3.8, q 0.076, down in 8 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (C32 0.0446×; ⚠ cell-cycle shift, explains ~32% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (SW480 0.0222×); [[TAK-901 (drug)]] 5 µM in 1 line (COLO 205 0.0191×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAM]] (+0.75, fdr 7e-06), [[DNAH12]] (+0.69, fdr 1e-05), [[ST8SIA5]] (+0.69, fdr 1e-05); moves opposite to [[NR2C1]] (-0.57, fdr 5e-05), [[TRIM35]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C11orf52]] → it (grade B ⚠); 3 go from it, the strongest it → [[CHODL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **16.3×** | +28.5 | 0e+00 | 18/18 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.97×** | +13.5 | 8e-39 | 12/15 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.46×** | +12.6 | 2e-34 | 11/33 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.15×** | +11.4 | 1e-27 | 14/19 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +10.9 | 8e-26 | 1/2 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +9.3 | 2e-18 | 10/23 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +8.5 | 2e-15 | 1/8 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.05×** | +8.1 | 3e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +5.3 | 6e-06 | 7/24 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.2 | 1e-05 | 2/14 (SW48, HCT15) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +4.9 | 6e-05 | 11/38 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.83×** | +4.3 | 7e-04 | 4/26 (SW480, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +4.3 | 8e-04 | 5/23 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.50×** | +4.1 | 0.002 | 7/34 (SW1417, KATO III, …) | rises with dose | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.007 | 5/31 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.017 | 9/36 (KATO III, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.045 | 9/17 (SW480, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.062 | 2/38 (SW480, AN3 CA) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (C32 0.0446×; ⚠ cell-cycle shift, explains ~32% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (SW480 0.0222×); [[TAK-901 (drug)]] 5 µM in 1 line (COLO 205 0.0191×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.577×** | -3.8 | 0.076 | 8/35 (SW 900, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.624× | -3.4 | 0.18 | 16/30 (C32, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.422× | -3.3 | 0.21 | 6/19 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.441× | -3.1 | 0.28 | 11/26 (COLO 205, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.648× | -3.0 | 0.29 | 7/34 (BT-474, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.38 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0222× (z -8.8) |
| [[A-172 (line)]] | wt | 1.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 39.3× (z +10.9) | — |
| [[A498 (line)]] | wt | 2.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 62.8× (z +8.8) | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0446× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0191× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.5× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +9.3) | — |
| [[A-427 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.656 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.890 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.656 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.590 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.706 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.588 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.719 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.832 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAM]] | +0.75 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.69 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[CXCL13]] | +0.68 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.67 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[HSD17B3]] | +0.67 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[BTG3-AS1]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 | same gene group |
| [[BCAR3-AS1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 | same gene group |
| [[CCDC170]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SLC26A7]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.65 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[NEB]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2C1]] | -0.57 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[TRIM35]] | -0.55 | -0.47 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf52]] | B | C11orf52 activity raises THBS4-AS1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without C11orf52 | 0.024 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[TOP2A]] | B | TOP2A activity lowers THBS4-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLEKHS1]] | B | PLEKHS1 activity raises THBS4-AS1's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.57× lower at baseline in the lines without PLEKHS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers THBS4-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[LRRC17]] | B | LRRC17 activity raises THBS4-AS1's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without LRRC17 | 0.088 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent |
| [[LINC02147]] | B | LINC02147 activity raises THBS4-AS1's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without LINC02147 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |
| [[LINC00992]] | B | LINC00992 activity raises THBS4-AS1's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without LINC00992 | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHODL]] | B | THBS4-AS1 activity raises CHODL's level | lines that do not express THBS4-AS1 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without THBS4-AS1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CFAP70]] | B | THBS4-AS1 activity raises CFAP70's level | lines that do not express THBS4-AS1 (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without THBS4-AS1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ERICH2-DT]] | B | THBS4-AS1 activity raises ERICH2-DT's level | lines that do not express THBS4-AS1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without THBS4-AS1 | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.9, 16.8); signed map (24.4, 1.7). **Vector** length 47.9, 7.51% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +28.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | THBS4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.1 — chr5:80,052,374-80,083,654 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40583) · Entrez [101929215](https://www.ncbi.nlm.nih.gov/gene/101929215) · Ensembl [ENSG00000249825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249825)

## Data

Gene col 14641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14641); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14641]; `tensor/DDL_lfc|DDL_z.npy` [14641]; `embed/gene_vectors.npy` [14641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14641 or target_col == 14641). Every well: [[THBS4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
