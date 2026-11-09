---
symbol: "LY6K"
type: "gene"
col: 8391
ensembl_id: "ENSG00000160886"
name: "lymphocyte antigen 6 family member K"
location: "8q24.3"
module: 120
arm: "+"
pooled_cpm: 6.84
n_lines_expressing: 18
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# LY6K

*lymphocyte antigen 6 family member K* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.77× (z +10.1, q 3e-21, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.24× (z +5.4, q 7e-06, up in 13 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.456× (z -5.3, q 6e-05, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL7R]] (+0.65, fdr 1e-05), [[SPHK1]] (+0.61, fdr 1e-05), [[FJX1]] (+0.58, fdr 3e-05); moves opposite to [[LPCAT3]] (-0.50, fdr 1e-04), [[SPAST]] (-0.48, fdr 8e-05), [[RPA1]] (-0.47, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 7 go from it, the strongest it → [[SAMD4A-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.77×** | +10.1 | 3e-21 | 4/9 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +7.8 | 1e-12 | 8/14 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.95×** | +6.3 | 5e-08 | 9/15 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +6.2 | 9e-08 | 5/12 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +5.4 | 7e-06 | 13/16 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +5.3 | 1e-05 | 10/14 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.97×** | +4.4 | 0.001 | 3/14 (A498, H4, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.88×** | +4.2 | 0.002 | 9/13 (SW 900, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.88×** | +4.2 | 0.002 | 4/14 (SW 900, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.005 | 2/16 (H4, LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.79×** | +3.9 | 0.005 | 10/16 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +3.4 | 0.033 | 0/9 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.27×** | +3.3 | 0.042 | 2/11 (NCI-H2347, HOP62) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.65×** | +3.2 | 0.050 | 12/16 (HS-578T, NCI-H1573, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.053 | 3/16 (SW 900, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.456×** | -5.3 | 6e-05 | 13/16 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -4.1 | 0.011 | 11/16 (J82, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -3.5 | 0.099 | 12/16 (HS-578T, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.615× | -3.3 | 0.11 | 9/16 (J82, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Encorafenib (drug)]] 5 µM |  | 0.396× | -3.3 | 0.11 | 3/16 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.401× | -3.2 | 0.11 | 10/16 (J82, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.407× | -3.2 | 0.12 | 10/16 (J82, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 28.2 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +13.8) ⚠ cell-cycle shift, explains ~68% of this change | [[Panobinostat (drug)]] 5 µM 0.178× (z -10.0) |
| [[J82 (line)]] | alt | 41.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -11.7) |
| [[A498 (line)]] | wt | 2.81 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +11.2) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.200× (z -8.7) |
| [[SW 900 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.7) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A-172 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.350 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL7R]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SPHK1]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[FJX1]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MSANTD3]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[CFLAR-AS1]] | +0.53 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[FOXD1]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RPAP1]] | +0.51 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[C14orf119]] | +0.51 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[ALOXE3]] | +0.50 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[CCL3]] | +0.50 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[LINC00702]] | +0.50 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[PBDC1]] | +0.50 | +0.39 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT3]] | -0.50 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SPAST]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[RPA1]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[SETD3]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[CS]] | -0.47 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[TKT]] | -0.47 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[HDAC1]] | -0.46 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[TECR]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[CD46]] | -0.46 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[LBR]] | -0.45 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[ADAM15]] | -0.45 | -0.41 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LY6K's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ABCC9]] | C | ABCC9 activity raises LY6K's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 3.32× lower at baseline in the lines without ABCC9 | 0.027 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD4A-AS1]] | B | LY6K activity raises SAMD4A-AS1's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.27× lower at baseline in the lines without LY6K | 0.041 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[SAMD4A]] | B | LY6K activity raises SAMD4A's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without LY6K | 0.064 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[C11orf68]] | B | LY6K activity raises C11orf68's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.16× lower at baseline in the lines without LY6K | 0.069 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[PPIF]] | B | LY6K activity raises PPIF's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.36× lower at baseline in the lines without LY6K | 0.073 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[ABL2]] | B | LY6K activity raises ABL2's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without LY6K | 0.089 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | LY6K activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express LY6K (32) vs lines expressing it (16) | the lines without LY6K: 1.17× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[AJAP1]] | C | LY6K activity raises AJAP1's level | lines that do not express LY6K (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without LY6K | 0.086 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.408). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, -2.6); signed map (20.5, -5.1). **Vector** length 41.0, 11.7% of its response variance represented; |z| ≥ 3 in 323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.8 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.4 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.2 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.1 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | lymphocyte antigen 6 family member K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:142,700,111-142,705,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSJ001348, FLJ35226, CT97 |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RY6](https://www.uniprot.org/uniprotkb/Q17RY6) (Lymphocyte antigen 6K):

> Required for sperm migration into the oviduct and male fertility by controlling binding of sperm to zona pellucida (By similarity). May play a role in cell growth.

**Summary**, from NCBI Gene [54742](https://www.ncbi.nlm.nih.gov/gene/54742):

> Predicted to be involved in binding activity of sperm to zona pellucida. Predicted to act upstream of or within flagellated sperm motility. Predicted to be located in cell surface and plasma membrane. Predicted to be active in acrosomal vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24225) · Entrez [54742](https://www.ncbi.nlm.nih.gov/gene/54742) · UniProt [Q17RY6](https://www.uniprot.org/uniprotkb/Q17RY6) · Ensembl [ENSG00000160886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160886)

## Data

Gene col 8391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8391); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8391]; `tensor/DDL_lfc|DDL_z.npy` [8391]; `embed/gene_vectors.npy` [8391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8391 or target_col == 8391). Every well: [[LY6K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LY6K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
