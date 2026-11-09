---
symbol: "CPNE4"
type: "gene"
col: 12182
ensembl_id: "ENSG00000196353"
name: "copine 4"
location: "3q22.1"
module: 140
arm: "+"
pooled_cpm: 12.88
n_lines_expressing: 29
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# CPNE4

*copine 4* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.25× (z +27.0, q 0e+00, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.651× (z -5.7, q 9e-06, down in 15 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0769×, NCI-H1573 0.286×, NCI-H1792 0.368×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.101×, NCI-H1792 0.252×); [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0308×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAX5]] (+0.55, fdr 3e-05), [[STYK1]] (+0.55, fdr 1e-05), [[MUC3A]] (+0.55, fdr 9e-05); moves opposite to [[LINC02987]] (-0.42, fdr 6e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[PRDM6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +27.0 | 0e+00 | 20/23 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.24×** | +22.0 | 0e+00 | 23/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.63×** | +17.0 | 0e+00 | 20/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +14.1 | 4e-43 | 3/11 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +13.6 | 4e-40 | 11/23 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.66×** | +12.9 | 3e-36 | 18/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +12.1 | 6e-32 | 7/15 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.47×** | +12.0 | 3e-31 | 19/25 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.41×** | +11.6 | 2e-29 | 20/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +11.2 | 2e-27 | 18/24 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +10.4 | 2e-23 | 6/13 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +10.2 | 1e-22 | 11/23 (COLO 205, RKO, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +10.1 | 2e-22 | 18/25 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.6 | 4e-16 | 9/19 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.8 | 5e-10 | 8/26 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.37×** | +6.0 | 8e-08 | 17/24 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.004 | 6/23 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.039 | 1/21 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0769×, NCI-H1573 0.286×, NCI-H1792 0.368×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.101×, NCI-H1792 0.252×); [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0308×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -5.7 | 9e-06 | 15/25 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[crizotinib (drug)]] 5 µM |  | **0.726×** | -4.0 | 0.015 | 3/25 (Panc 03.27, A549, …) | top dose only |  |
| [[Malotilate (drug)]] 0.05 µM |  | 0.774× | -3.4 | 0.14 | 4/24 (Panc 03.27, COLO 205, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.637× | -3.1 | 0.22 | 4/21 (A549, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.790× | -3.1 | 0.22 | 10/24 (NCI-H1792, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 0.795× | -3.0 | 0.25 | 3/24 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 105 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -19.5) |
| [[PANC-1 (line)]] | alt | 4.15 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 9.66× (z +15.8) | — |
| [[NCI-H460 (line)]] | wt | 9.95 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 5.24× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 8.63 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 6.36× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 10.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 44.5× (z +18.5) | — |
| [[HS-578T (line)]] | alt | 3.33 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.79× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 151 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.4) |
| [[A549 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.181× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 6.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0936× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 6.82 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0640× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 5.35 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0701× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 5.98 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.98× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX5]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 | same gene group |
| [[STYK1]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.55 | +0.49 / +0.36 | both halves | 9e-05 |  |
| [[TMEFF2]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PDE11A]] | +0.52 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[EBF2]] | +0.52 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[HS6ST3]] | +0.51 | +0.40 / +0.59 | both halves | 5e-05 | same gene group |
| [[FRMPD3]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ARSL]] | +0.51 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[PTPRO]] | +0.50 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PLD5]] | +0.50 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[GABRG3]] | +0.50 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02987]] | -0.42 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPNE4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02987]] | B | LINC02987 activity lowers CPNE4's level | lines that do not express LINC02987 (5) vs lines expressing it (45) | 3.23× higher at baseline in the lines without LINC02987 | 0.037 | ⚠ within organs, on part of the lines; also absent: NME4, ZNF566, SPIRE1 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises CPNE4's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without TMPRSS2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[TACSTD2]] | B | TACSTD2 activity raises CPNE4's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without TACSTD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3 |
| [[KCNQ3]] | C | KCNQ3 activity raises CPNE4's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without KCNQ3 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDM6]] | B | CPNE4 activity lowers PRDM6's level | lines that do not express CPNE4 (21) vs lines expressing it (29) | 1.35× higher at baseline in the lines without CPNE4 | 0.033 | ⚠ within organs, on part of the lines; also absent: MIR646HG, TMEM156, BCL2A1; maybe low, not absent |
| [[CYP2J2]] | B | CPNE4 activity raises CYP2J2's level | lines that do not express CPNE4 (21) vs lines expressing it (29) | 1.85× lower at baseline in the lines without CPNE4 | 0.042 | ⚠ within organs, on part of the lines; also absent: MIR646HG, TMEM156, BCL2A1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.440). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, 39.7); signed map (55.0, 10.9). **Vector** length 55.6, 10.9% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +22.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +27.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | copine 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:131,533,555-132,285,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COPN4, CPN4 |
| Gene groups (HGNC) | Copines; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A23](https://www.uniprot.org/uniprotkb/Q96A23) (Copine-4):

> Probable calcium-dependent phospholipid-binding protein that may play a role in calcium-mediated intracellular processes.

**Summary**, from NCBI Gene [131034](https://www.ncbi.nlm.nih.gov/gene/131034):

> This gene belongs to the highly conserved copine family. It encodes a calcium-dependent, phospholipid-binding protein, which may be involved in membrane trafficking, mitogenesis and development. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:2317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2317) · Entrez [131034](https://www.ncbi.nlm.nih.gov/gene/131034) · UniProt [Q96A23](https://www.uniprot.org/uniprotkb/Q96A23) · Ensembl [ENSG00000196353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196353)

## Data

Gene col 12182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12182); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12182]; `tensor/DDL_lfc|DDL_z.npy` [12182]; `embed/gene_vectors.npy` [12182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12182 or target_col == 12182). Every well: [[CPNE4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
