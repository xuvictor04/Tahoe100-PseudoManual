---
symbol: "LETM2"
type: "gene"
col: 9057
ensembl_id: "ENSG00000165046"
name: "leucine zipper and EF-hand containing transmembrane protein 2"
location: "8p11.23"
module: 80
arm: "+"
pooled_cpm: 3.65
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# LETM2

*leucine zipper and EF-hand containing transmembrane protein 2* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.24× (z +30.2, q 0e+00, up in 37 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0827×; ⚠ cell-cycle shift, would explain all of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (COLO 205 0.0683×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.77, fdr 7e-06), [[NOP14-AS1]] (+0.72, fdr 7e-06), [[CFLAR-AS1]] (+0.71, fdr 1e-05); moves opposite to [[NUDT21]] (-0.68, fdr 1e-05), [[RAB4A]] (-0.63, fdr 3e-05), [[ACTR5]] (-0.62, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ICAM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.24×** | +30.2 | 0e+00 | 37/37 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.99×** | +18.1 | 0e+00 | 27/33 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +12.7 | 1e-34 | 25/31 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.94×** | +12.6 | 3e-34 | 24/34 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.84×** | +11.7 | 1e-29 | 30/40 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +11.7 | 1e-29 | 23/33 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.54×** | +10.1 | 5e-22 | 6/11 (SW480, CFPAC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.25×** | +9.1 | 5e-18 | 1/6 (HOP62) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.13×** | +8.8 | 7e-17 | 27/42 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.4 | 1e-11 | 15/44 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.87×** | +7.3 | 2e-11 | 24/44 (A498, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.80×** | +6.9 | 3e-10 | 21/44 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.76×** | +6.6 | 2e-09 | 16/43 (KATO III, HCT15, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.78×** | +6.5 | 3e-09 | 8/19 (A-172, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.64×** | +5.8 | 2e-07 | 5/17 (A549, NCI-H2347, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +5.3 | 5e-06 | 17/44 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 8e-06 | 7/41 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.1 | 9e-06 | 15/42 (KATO III, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 1e-05 | 9/33 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 4e-04 | 11/40 (A-427, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.3 | 5e-04 | 8/39 (SW480, A-172, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.002 | 1/23 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0827×; ⚠ cell-cycle shift, would explain all of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (COLO 205 0.0683×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.738× | -3.4 | 0.39 | 10/31 (A498, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.17 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 3.97 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0827× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 2.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +12.6) | — |
| [[A-172 (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +10.7) | — |
| [[A498 (line)]] | wt | 2.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.16× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 7.83 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0683× (z -8.5) |
| [[Hs 766T (line)]] | wt | 8.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 3.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +9.2) | — |
| [[J82 (line)]] | alt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +10.3) | — |
| [[KATO III (line)]] | alt | 2.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +8.7) | — |
| [[LoVo (line)]] | wt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.7× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 3.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +12.6) | — |
| [[SW480 (line)]] | alt | 5.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +12.2) | — |
| [[A-427 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.77 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.72 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[CFLAR-AS1]] | +0.71 | +0.79 / +0.57 | both halves | 1e-05 |  |
| [[ENO3]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[LPXN]] | +0.71 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.69 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[GASAL1]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ACTR3-AS1]] | +0.67 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[MMRN2]] | +0.67 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[CDK6-AS1]] | +0.65 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ERRFI1-DT]] | +0.65 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LINC00393]] | +0.65 | +0.62 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | -0.68 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[RAB4A]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[ACTR5]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[PRUNE1]] | -0.59 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[MRPS31P5-1]] | -0.59 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ATP5F1C]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CROT]] | -0.58 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[SDHAP1]] | -0.58 | -0.72 / -0.38 | both halves | 6e-05 |  |
| [[EEF1AKMT2]] | -0.57 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[RPA1]] | -0.57 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[RAB40B]] | -0.57 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[WDR5]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM2]] | B | ICAM2 activity raises LETM2's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.28× lower at baseline in the lines without ICAM2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LETM2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01426]] | B | LINC01426 activity raises LETM2's level | lines that do not express LINC01426 (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without LINC01426 | 0.069 | ⚠ within organs, on part of the lines; also absent: MIR3142HG, ADAMTS3, CTHRC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.808). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, 10.7); signed map (25.8, 6.5). **Vector** length 57.0, 7.89% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +30.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +18.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -2.1 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.0 | +6.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.9 | +7.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper and EF-hand containing transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,386,207-38,409,527 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25409, SLC55A2 |
| Gene groups (HGNC) | EF-hand domain containing; Solute carrier family 55, LETM mitochondrial cation/proton exchangers |
| Matched by | ensembl_id |

UniProt [Q2VYF4](https://www.uniprot.org/uniprotkb/Q2VYF4) carries no function annotation.

**Summary**, from NCBI Gene [137994](https://www.ncbi.nlm.nih.gov/gene/137994):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in mitochondrial calcium ion transmembrane transport and mitochondrion organization. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14648) · Entrez [137994](https://www.ncbi.nlm.nih.gov/gene/137994) · UniProt [Q2VYF4](https://www.uniprot.org/uniprotkb/Q2VYF4) · Ensembl [ENSG00000165046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165046)

## Data

Gene col 9057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9057); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9057]; `tensor/DDL_lfc|DDL_z.npy` [9057]; `embed/gene_vectors.npy` [9057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9057 or target_col == 9057). Every well: [[LETM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LETM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
