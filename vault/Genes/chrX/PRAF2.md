---
symbol: "PRAF2"
type: "gene"
col: 14348
ensembl_id: "ENSG00000243279"
name: "PRA1 domain family member 2"
location: "Xp11.23"
module: 50
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PRAF2

*PRA1 domain family member 2* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.21× (z +8.5, q 1e-14, up in 20 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.03× (z +7.5, q 1e-11, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.641× (z -4.8, q 1e-03, down in 25 of 42 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.486× (z -4.0, q 0.015, down in 12 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 0.300×, PANC-1 0.430×, MIA PaCa-2 0.314×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.221×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG9A]] (+0.62, fdr 1e-05), [[GGCX]] (+0.62, fdr 1e-05), [[MEF2D]] (+0.61, fdr 1e-05); moves opposite to [[UTP20]] (-0.54, fdr 9e-05), [[RIF1]] (-0.53, fdr 3e-05), [[AFG1L]] (-0.52, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DKK3]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.5 | 1e-14 | 20/28 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +7.5 | 1e-11 | 33/43 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +7.2 | 1e-10 | 16/19 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +5.7 | 1e-06 | 27/44 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +5.6 | 3e-06 | 27/42 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.1 | 2e-05 | 12/22 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.1 | 2e-05 | 23/41 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.8 | 1e-04 | 18/37 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.1 | 0.002 | 18/42 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.004 | 18/39 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.8 | 0.006 | 13/35 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.012 | 16/44 (CFPAC-1, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.028 | 14/43 (SW480, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RPMI-7951 0.300×, PANC-1 0.430×, MIA PaCa-2 0.314×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -4.8 | 1e-03 | 25/42 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -4.0 | 0.015 | 12/38 (PANC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.686×** | -3.8 | 0.025 | 17/43 (NCI-H2347, BT-474, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.751× | -3.1 | 0.29 | 9/42 (SNU-423, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.747× | -3.0 | 0.29 | 16/42 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.70 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +9.2) | — |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG9A]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[GGCX]] | +0.62 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MEF2D]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CTSF]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ADIPOR1]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SYVN1]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MARF1]] | +0.57 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[GUK1]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CHPF]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[IDS]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CRAT]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[MMP2]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.54 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[RIF1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[AFG1L]] | -0.52 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[U2SURP]] | -0.50 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[GPATCH4]] | -0.49 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[TCERG1]] | -0.49 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[DNAJC11]] | -0.48 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DKK3]] | B | DKK3 activity raises PRAF2's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without DKK3 | 0.053 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[CTSF]] | B | CTSF activity raises PRAF2's level | lines that do not express CTSF (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without CTSF | 0.060 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[APLP1]] | B | APLP1 activity raises PRAF2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without APLP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[CIB1]] | C | CIB1 activity raises PRAF2's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without CIB1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | C | PRAF2 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express PRAF2 (4) vs lines expressing it (44) | the lines without PRAF2: 0.30× the cells of the other lines | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286511, LINC02343, CCDC110; maybe low, not absent |
| [[CLK3]] | C | PRAF2 activity raises CLK3's level | lines that do not express PRAF2 (4) vs lines expressing it (46) | 1.39× lower at baseline in the lines without PRAF2 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286511, LINC02343, CCDC110; maybe low, not absent |
| [[CTSF]] | C | PRAF2 activity raises CTSF's level | lines that do not express PRAF2 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without PRAF2 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286511, LINC02343, CCDC110; maybe low, not absent |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | PRAF2's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | PRAF2's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.352 over the table, 0.048 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.5, -37.2); signed map (-22.3, 9.8). **Vector** length 55.7, 8.62% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +7.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | PRA1 domain family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,071,161-49,074,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JM4, Yip6a |
| Gene groups (HGNC) | YIP superfamily |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [O60831](https://www.uniprot.org/uniprotkb/O60831) (PRA1 family protein 2):

> May be involved in ER/Golgi transport and vesicular traffic. Plays a pro-apoptotic role in cerulenin-induced neuroblastoma apoptosis.

**Summary**, from NCBI Gene [11230](https://www.ncbi.nlm.nih.gov/gene/11230):

> Predicted to be involved in L-glutamate transmembrane transport. Predicted to be located in endosome membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28911) · Entrez [11230](https://www.ncbi.nlm.nih.gov/gene/11230) · UniProt [O60831](https://www.uniprot.org/uniprotkb/O60831) · Ensembl [ENSG00000243279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243279)

## Data

Gene col 14348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14348); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14348]; `tensor/DDL_lfc|DDL_z.npy` [14348]; `embed/gene_vectors.npy` [14348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14348 or target_col == 14348). Every well: [[PRAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
