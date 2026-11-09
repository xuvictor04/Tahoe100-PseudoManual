---
symbol: "ASRGL1"
type: "gene"
col: 8487
ensembl_id: "ENSG00000162174"
name: "asparaginase and isoaspartyl peptidase 1"
location: "11q12.3"
module: 115
arm: "+"
pooled_cpm: 7.95
n_lines_expressing: 43
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# ASRGL1

*asparaginase and isoaspartyl peptidase 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.89× (z +16.2, q 0e+00, up in 21 of 23 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.78× (z +14.7, q 0e+00, up in 32 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.308×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCML2]] (+0.57, fdr 6e-05), [[SBK1]] (+0.55, fdr 7e-05), [[CEP78]] (+0.55, fdr 1e-05); moves opposite to [[ATP6V1G1]] (-0.45, fdr 3e-04), [[FCF1]] (-0.44, fdr 0.001, ⚠ not reproduced), [[RIMOC1]] (-0.44, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ATP6V0E2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.89×** | +16.2 | 0e+00 | 21/23 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +14.7 | 0e+00 | 32/36 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **4.05×** | +14.3 | 8e-44 | 32/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.97×** | +14.0 | 1e-42 | 34/40 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.19×** | +14.0 | 1e-42 | 10/13 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **3.67×** | +13.2 | 4e-38 | 35/40 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +11.9 | 2e-30 | 31/39 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.12×** | +11.6 | 4e-29 | 33/40 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.41×** | +11.6 | 4e-29 | 12/16 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.38×** | +8.8 | 6e-17 | 25/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.17×** | +7.9 | 1e-13 | 22/34 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **2.15×** | +7.5 | 3e-12 | 20/26 (J82, KATO III, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.67×** | +6.9 | 2e-10 | 23/38 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.87×** | +6.1 | 4e-08 | 18/31 (HT-29, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.79×** | +5.7 | 4e-07 | 22/35 (HT-29, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.002 | 15/38 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 10/39 (A549, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.080 | 8/32 (NCI-H661, HT-29, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.094 | 7/39 (SW480, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.308×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.545× | -3.2 | 0.67 | 4/39 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.83 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.74× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[PANC-1 (line)]] | alt | 19.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.61× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-427 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.308× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 7.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +8.6) | — |
| [[A-172 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCML2]] | +0.57 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[SBK1]] | +0.55 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[CEP78]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.54 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[CDC7]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[HPSE]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[PDS5B]] | +0.52 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[PRKD3]] | +0.52 | +0.25 / +0.43 | both halves | 4e-04 |  |
| [[SYTL4]] | +0.52 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[NMU]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[FRMPD3]] | +0.51 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[TSPAN12]] | +0.51 | +0.43 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.45 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[FCF1]] | -0.44 | -0.18 / -0.36 | ⚠ not reproduced | 0.001 |  |
| [[RIMOC1]] | -0.44 | -0.15 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[AIMP1]] | -0.43 | -0.19 / -0.37 | ⚠ not reproduced | 9e-04 | pathway: Metabolism of amino acids and derivatives |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ASRGL1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.9% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SBK1]] | B | SBK1 activity raises ASRGL1's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 2.64× lower at baseline in the lines without SBK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[YBX2]] | B | YBX2 activity raises ASRGL1's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without YBX2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[TSPAN33]] | B | TSPAN33 activity raises ASRGL1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.56× lower at baseline in the lines without TSPAN33 | 0.026 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SYTL4]] | B | SYTL4 activity lowers ASRGL1's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.46× higher at baseline in the lines without SYTL4 | 0.055 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[CCDC69]] | B | CCDC69 activity lowers ASRGL1's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.09× higher at baseline in the lines without CCDC69 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0E2]] | B | ASRGL1 activity raises ATP6V0E2's level | lines that do not express ASRGL1 (7) vs lines expressing it (43) | 2.57× lower at baseline in the lines without ASRGL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, LINC02026, MYO15B; maybe low, not absent |
| [[MPP2]] | B | ASRGL1 activity lowers MPP2's level | lines that do not express ASRGL1 (7) vs lines expressing it (43) | 1.36× higher at baseline in the lines without ASRGL1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, LINC02026, MYO15B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-29.8, -43.1); signed map (-21.8, 31.8). **Vector** length 52.9, 8.38% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.9 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.6 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.4 | +11.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | asparaginase and isoaspartyl peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,337,448-62,393,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22316, ALP1, ALP |
| Reactome | 3 pathways, smallest: Phenylalanine metabolism; Phenylalanine and tyrosine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L266](https://www.uniprot.org/uniprotkb/Q7L266) (Isoaspartyl peptidase/L-asparaginase):

> Has both L-asparaginase and beta-aspartyl peptidase activity. May be involved in the production of L-aspartate, which can act as an excitatory neurotransmitter in some brain regions. Is highly active with L-Asp beta-methyl ester. Besides, has catalytic activity toward beta-aspartyl dipeptides and their methyl esters, including beta-L-Asp-L-Phe, beta-L-Asp-L-Phe methyl ester (aspartame), beta-L-Asp-L-Ala, beta-L-Asp-L-Leu and beta-L-Asp-L-Lys. Does not have aspartylglucosaminidase activity and …

**Summary**, from NCBI Gene [80150](https://www.ncbi.nlm.nih.gov/gene/80150):

> Enables asparaginase activity and beta-aspartyl-peptidase activity. Involved in obsolete L-asparagine catabolic process via L-aspartate. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16448) · Entrez [80150](https://www.ncbi.nlm.nih.gov/gene/80150) · UniProt [Q7L266](https://www.uniprot.org/uniprotkb/Q7L266) · Ensembl [ENSG00000162174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162174)

## Data

Gene col 8487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8487); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8487]; `tensor/DDL_lfc|DDL_z.npy` [8487]; `embed/gene_vectors.npy` [8487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8487 or target_col == 8487). Every well: [[ASRGL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASRGL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
