---
symbol: "GASAL1"
type: "gene"
col: 14829
ensembl_id: "ENSG00000253669"
name: "growth arrest associated lncRNA 1"
location: "8q22.3"
module: 80
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# GASAL1

*growth arrest associated lncRNA 1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.13× (z +9.8, q 8e-20, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.339× (z -6.5, q 4e-08, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF10]] (+0.71, fdr 7e-06), [[LETM2]] (+0.68, fdr 7e-06), [[NANOS3]] (+0.65, fdr 2e-05); moves opposite to [[GET1]] (-0.60, fdr 1e-05), [[WDR5]] (-0.59, fdr 1e-05), [[ACTR5]] (-0.58, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LHFPL6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +9.8 | 8e-20 | 22/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +8.7 | 7e-16 | 20/32 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.16×** | +6.7 | 4e-09 | 2/6 (SW1417, HT-29) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +5.2 | 3e-05 | 20/38 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.51×** | +4.8 | 2e-04 | 6/17 (C32, J82, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.7 | 2e-04 | 17/41 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.18×** | +4.4 | 9e-04 | 2/8 (HepG2/C3A, SW480) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.05×** | +4.4 | 9e-04 | 7/16 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.002 | 17/40 (BT-474, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +3.6 | 0.021 | 12/35 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.043 | 11/39 (SNU-423, KATO III, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.058 | 10/40 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.67×** | +3.1 | 0.078 | 5/39 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.69×** | +3.1 | 0.087 | 6/16 (PANC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.339×** | -6.5 | 4e-08 | 23/38 (A549, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.375×** | -5.9 | 9e-07 | 28/42 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.422×** | -5.2 | 4e-05 | 22/40 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.435×** | -5.0 | 8e-05 | 23/38 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.479×** | -4.2 | 0.003 | 17/36 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.527×** | -3.9 | 0.011 | 14/40 (SHP-77, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.543×** | -3.7 | 0.019 | 19/36 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.568×** | -3.4 | 0.046 | 14/40 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.589×** | -3.2 | 0.082 | 11/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.589×** | -3.2 | 0.082 | 19/38 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.373×** | -3.1 | 0.097 | 7/33 (SHP-77, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0669× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0957× (z -9.3) |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0492× (z -10.4) |
| [[A-427 (line)]] | wt | 7.34 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0767× (z -8.9) |
| [[A549 (line)]] | wt | 3.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0343× (z -9.4) |
| [[HOP62 (line)]] | alt | 7.64 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0671× (z -10.0) |
| [[SW480 (line)]] | alt | 5.09 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0989× (z -9.2) |
| [[A-172 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.996 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF10]] | +0.71 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[LETM2]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.65 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[CCDC148]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[S100A3]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | +0.61 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ENO3]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[HIVEP2-DT]] | +0.60 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[LINC00705]] | +0.59 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CFLAR-AS1]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ANGPT2]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[LPXN]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GET1]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[WDR5]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NAPB]] | -0.57 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[CIZ1]] | -0.56 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[ATP5F1C]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ERI3]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AP2A2]] | -0.55 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DFFB]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[STX7]] | -0.55 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[MTFR1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CA5B]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity lowers GASAL1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.62× higher at baseline in the lines without ZNF341-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHFPL6]] | C | GASAL1 activity raises LHFPL6's level | lines that do not express GASAL1 (3) vs lines expressing it (47) | 4.13× lower at baseline in the lines without GASAL1 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NECAB2, DLG4, CEP112; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.7, 10.6); signed map (25.8, 6.5). **Vector** length 74.5, 15.8% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest associated lncRNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.3 — chr8:102,805,517-102,810,039 (+) |
| Ensembl biotype | lncRNA |
| Also known as | GASL1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53461) · Entrez [401472](https://www.ncbi.nlm.nih.gov/gene/401472) · Ensembl [ENSG00000253669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253669)

## Data

Gene col 14829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14829); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14829]; `tensor/DDL_lfc|DDL_z.npy` [14829]; `embed/gene_vectors.npy` [14829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14829 or target_col == 14829). Every well: [[GASAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GASAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
