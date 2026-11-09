---
symbol: "CCDC69"
type: "gene"
col: 12629
ensembl_id: "ENSG00000198624"
name: "coiled-coil domain containing 69"
location: "5q33.1"
module: 115
arm: "+"
pooled_cpm: 4.42
n_lines_expressing: 39
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# CCDC69

*coiled-coil domain containing 69* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.21× (z +19.1, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.680× (z -3.7, q 0.077, down in 12 of 35 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HES2]] (+0.63, fdr 3e-05), [[RGS9]] (+0.56, fdr 3e-04), [[TSPAN33]] (+0.55, fdr 5e-05); moves opposite to [[KRIT1]] (-0.45, fdr 1e-04), [[METTL15]] (-0.45, fdr 1e-04), [[KIAA0753]] (-0.44, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[NPTXR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.21×** | +19.1 | 0e+00 | 32/34 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.94×** | +15.0 | 0e+00 | 29/31 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.45×** | +13.5 | 5e-39 | 4/4 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +13.2 | 1e-37 | 15/16 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.51×** | +11.8 | 5e-30 | 28/34 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +10.3 | 1e-22 | 6/6 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +9.5 | 2e-19 | 18/33 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.61×** | +9.0 | 2e-17 | 23/34 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +8.3 | 5e-15 | 22/33 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.53×** | +6.2 | 4e-08 | 14/29 (NCI-H460, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +6.1 | 6e-08 | 8/33 (RKO, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.88×** | +5.9 | 2e-07 | 15/33 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.83×** | +5.4 | 3e-06 | 7/15 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.9 | 5e-05 | 11/22 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **2.06×** | +4.8 | 5e-05 | 5/33 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.64×** | +4.6 | 1e-04 | 9/33 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 8/33 (A498, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.001 | 8/33 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.56×** | +3.8 | 0.003 | 4/19 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.011 | 6/33 (RKO, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.680×** | -3.7 | 0.077 | 12/35 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -3.5 | 0.077 | 16/32 (KATO III, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -3.5 | 0.077 | 9/34 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.694×** | -3.5 | 0.077 | 11/32 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.705× | -3.2 | 0.16 | 12/30 (NCI-H1792, J82, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 40.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HepG2_C3A (line)]] | wt | 9.50 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0603× (z -9.2) |
| [[LoVo (line)]] | wt | 9.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES2]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[RGS9]] | +0.56 | +0.27 / +0.68 | both halves | 3e-04 |  |
| [[TSPAN33]] | +0.55 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[SLC26A5]] | +0.55 | +0.25 / +0.67 | both halves | 4e-04 |  |
| [[CYFIP2]] | +0.54 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[SMARCD3]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[LYPD5]] | +0.54 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[SBK1]] | +0.53 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[TMEM98]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[KSR1]] | +0.51 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[NPTXR]] | +0.51 | +0.21 / +0.58 | both halves | 6e-04 |  |
| [[ADAMTS7]] | +0.51 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRIT1]] | -0.45 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[METTL15]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[KIAA0753]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ACAD9]] | -0.44 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[LINS1]] | -0.44 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[SPATA17]] | -0.43 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[DNAAF10]] | -0.43 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[MORN1]] | -0.43 | -0.17 / -0.48 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC69's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LCN2]] | B | LCN2 activity raises CCDC69's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without LCN2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CD74]] | B | CD74 activity raises CCDC69's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.61× lower at baseline in the lines without CD74 | 0.069 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPTXR]] | B | CCDC69 activity lowers NPTXR's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.23× higher at baseline in the lines without CCDC69 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BLVRA]] | B | CCDC69 activity lowers BLVRA's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without CCDC69 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GRIP2]] | B | CCDC69 activity lowers GRIP2's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.60× higher at baseline in the lines without CCDC69 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPX3]] | B | CCDC69 activity raises GPX3's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 2.73× lower at baseline in the lines without CCDC69 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ASRGL1]] | B | CCDC69 activity lowers ASRGL1's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.09× higher at baseline in the lines without CCDC69 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TSPAN33]] | B | CCDC69 activity raises TSPAN33's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.06× lower at baseline in the lines without CCDC69 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CCDC88B]] | B | CCDC69 activity lowers CCDC88B's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.25× higher at baseline in the lines without CCDC69 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[USB1]] | B | CCDC69 activity lowers USB1's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.03× higher at baseline in the lines without CCDC69 | 0.086 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.7, 41.2); signed map (22.5, 22.0). **Vector** length 54.0, 9.21% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +19.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.3 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.6 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | +0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,181,052-151,224,093 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13705, DKFZP434C171 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NI79](https://www.uniprot.org/uniprotkb/A6NI79) (Coiled-coil domain-containing protein 69):

> May act as a scaffold to regulate the recruitment and assembly of spindle midzone components. Required for the localization of AURKB and PLK1 to the spindle midzone.

**Summary**, from NCBI Gene [26112](https://www.ncbi.nlm.nih.gov/gene/26112):

> Predicted to enable microtubule binding activity. Involved in spindle midzone assembly. Located in spindle midzone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24487) · Entrez [26112](https://www.ncbi.nlm.nih.gov/gene/26112) · UniProt [A6NI79](https://www.uniprot.org/uniprotkb/A6NI79) · Ensembl [ENSG00000198624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198624)

## Data

Gene col 12629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12629); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12629]; `tensor/DDL_lfc|DDL_z.npy` [12629]; `embed/gene_vectors.npy` [12629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12629 or target_col == 12629). Every well: [[CCDC69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
