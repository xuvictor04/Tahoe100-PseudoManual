---
symbol: "TTPA"
type: "gene"
col: 6034
ensembl_id: "ENSG00000137561"
name: "alpha tocopherol transfer protein"
location: "8q12.3"
module: 176
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 26
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# TTPA

*alpha tocopherol transfer protein* — 8q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.92× (z +11.4, q 4e-27, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.32× (z +8.8, q 2e-16, up in 13 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.538× (z -4.4, q 0.005, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMID1]] (+0.69, fdr 7e-06), [[SLC27A2]] (+0.68, fdr 7e-06), [[LARGE2]] (+0.65, fdr 1e-05); moves opposite to [[RSPH3]] (-0.51, fdr 4e-05), [[SMG6]] (-0.47, fdr 5e-05), [[C6orf62]] (-0.47, fdr 6e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00173]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CRACD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.92×** | +11.4 | 4e-27 | 2/2 (NCI-H2030, SW1417) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.60×** | +10.5 | 4e-23 | 2/6 (SW480, SW1417) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +10.3 | 1e-22 | 6/7 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +8.8 | 2e-16 | 13/23 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +8.8 | 2e-16 | 8/14 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +6.8 | 1e-09 | 5/8 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.25×** | +6.0 | 2e-07 | 12/23 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.86×** | +5.6 | 2e-06 | 1/6 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +5.2 | 2e-05 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +4.9 | 5e-05 | 10/17 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +4.7 | 1e-04 | 3/23 (A-427, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.82×** | +4.4 | 4e-04 | 12/23 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.78×** | +4.3 | 9e-04 | 7/23 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.70×** | +3.9 | 0.003 | 1/11 (LS 180) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.68×** | +3.8 | 0.004 | 6/22 (C32, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.004 | 12/23 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.61×** | +3.5 | 0.014 | 2/18 (SW1417, SW48) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.018 | 2/12 (SNU-1, NCI-H460) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.043 | 2/16 (NCI-H460, RKO) | all doses, stronger at high dose |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.055 | 0/12 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.067 | 5/22 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +2.9 | 0.083 | 3/18 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +2.9 | 0.083 | 4/16 (SW480, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -4.4 | 0.005 | 13/21 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -4.2 | 0.006 | 12/23 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -3.9 | 0.015 | 12/22 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.617×** | -3.6 | 0.045 | 3/23 (PANC-1, NCI-H1792, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.649× | -3.1 | 0.16 | 4/23 (HCT15, Hs 766T, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.661× | -3.1 | 0.16 | 8/18 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | 0.747× | -3.1 | 0.16 | 7/23 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.27 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.117× (z -10.2) |
| [[LS 180 (line)]] | wt | 9.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.150× (z -9.3) ⚠ cell-cycle shift, explains ~8% of this change |
| [[PANC-1 (line)]] | alt | 2.07 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0741× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0236× (z -13.0) |
| [[A-172 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.647 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.636 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.775 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.895 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMID1]] | +0.69 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SLC27A2]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[LARGE2]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CHDH]] | +0.61 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ADAM22]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ALDH5A1]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[FGF20]] | +0.59 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[RAVER2]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[XK]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GPC4]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Metabolism of fat-soluble vitamins |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSPH3]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SMG6]] | -0.47 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[C6orf62]] | -0.47 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[CLDN14-AS1]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00173]] | B | LINC00173 activity raises TTPA's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.35× lower at baseline in the lines without LINC00173 | 0.056 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[BMP7]] | B | BMP7 activity raises TTPA's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without BMP7 | 0.079 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[CRACD]] | B | CRACD activity raises TTPA's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without CRACD | 0.092 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACD]] | B | TTPA activity raises CRACD's level | lines that do not express TTPA (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without TTPA | 0.056 | ⚠ within organs, on part of the lines; also absent: MKX, FGF20, ENSG00000238178 |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 43.9); signed map (60.3, 14.2). **Vector** length 41.1, 8.21% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +10.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -3.9 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | alpha tocopherol transfer protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.3 — chr8:63,048,553-63,086,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AVED |
| Gene groups (HGNC) | CRAL-TRIO lipid binding domain containing |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Metabolism of fat-soluble vitamins; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P49638](https://www.uniprot.org/uniprotkb/P49638) (Alpha-tocopherol transfer protein):

> Binds alpha-tocopherol, enhances its transfer between separate membranes, and stimulates its release from liver cells. Binds both phosphatidylinositol 3,4-bisphosphate and phosphatidylinositol 4,5-bisphosphate; the resulting conformation change is important for the release of the bound alpha-tocopherol (By similarity).

**Summary**, from NCBI Gene [7274](https://www.ncbi.nlm.nih.gov/gene/7274):

> This gene encodes a soluble protein that binds alpha-trocopherol, a form of vitamin E, with high selectivity and affinity. This protein plays an important role in regulating vitamin E levels in the body by transporting vitamin E between membrane vesicles and facilitating the secretion of vitamin E from hepatocytes to circulating lipoproteins. Mutations in this gene cause hereditary vitamin E deficiency (ataxia with vitamin E deficiency, AVED) and retinitis pigmentosa. [provided by RefSeq, Nov …

**Accessions** — [HGNC:12404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12404) · Entrez [7274](https://www.ncbi.nlm.nih.gov/gene/7274) · UniProt [P49638](https://www.uniprot.org/uniprotkb/P49638) · Ensembl [ENSG00000137561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137561)

## Data

Gene col 6034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6034); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6034]; `tensor/DDL_lfc|DDL_z.npy` [6034]; `embed/gene_vectors.npy` [6034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6034 or target_col == 6034). Every well: [[TTPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
