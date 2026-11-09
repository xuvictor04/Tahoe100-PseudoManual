---
symbol: "OVOL2"
type: "gene"
col: 4679
ensembl_id: "ENSG00000125850"
name: "ovo like zinc finger 2"
location: "20p11.23"
module: 21
arm: "+"
pooled_cpm: 7.25
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# OVOL2

*ovo like zinc finger 2* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.06× (z +20.9, q 0e+00, up in 33 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW48 0.100×; ⚠ cell-cycle shift, explains ~22% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW48 0.0518×; ⚠ toxic; transcription drop); [[Acetazolamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0520×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPOAP1-AS1]] (+0.65, fdr 1e-05), [[CCNO-DT]] (+0.62, fdr 1e-05), [[PRKCH-AS1]] (+0.60, fdr 2e-05); moves opposite to [[MLX]] (-0.53, fdr 1e-04), [[ALAS1]] (-0.49, fdr 7e-04), [[MKNK1]] (-0.48, fdr 0.001, ⚠ not reproduced), [[SKIC8]] (-0.45, fdr 4e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GRHL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +20.9 | 0e+00 | 33/38 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +14.0 | 6e-42 | 9/14 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +13.2 | 1e-37 | 17/25 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +11.7 | 3e-29 | 11/16 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +10.5 | 8e-24 | 23/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.2 | 2e-18 | 24/39 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +9.0 | 3e-17 | 24/44 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +7.0 | 2e-10 | 23/43 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.7 | 6e-07 | 14/46 (A498, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +5.0 | 3e-05 | 15/45 (COLO 205, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.5 | 4e-04 | 6/28 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 8e-04 | 12/43 (NCI-H1573, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 1e-03 | 11/45 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.001 | 5/34 (SW480, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.1 | 0.002 | 11/42 (KATO III, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 8/47 (NCI-H1573, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.056 | 7/41 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.060 | 2/37 (LS 180, COLO 205) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.071 | 14/46 (KATO III, BT-474, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.076 | 2/39 (NCI-H2347, HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4679.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW48 0.100×; ⚠ cell-cycle shift, explains ~22% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW48 0.0518×; ⚠ toxic; transcription drop); [[Acetazolamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0520×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -4.3 | 0.011 | 9/48 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM |  | 0.691× | -3.5 | 0.14 | 3/47 (HEC-1-A, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Valdecoxib (drug)]] 0.05 µM |  | 0.782× | -3.2 | 0.22 | 8/43 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 46.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -14.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A549 (line)]] | wt | 3.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0520× (z -11.6) |
| [[HT-29 (line)]] | alt | 9.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 2.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 8.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +8.6) | — |
| [[SW480 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.4) | — |
| [[A-172 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPOAP1-AS1]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[CCNO-DT]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PRKCH-AS1]] | +0.60 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[OXR1-AS1]] | +0.59 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[HOXB-AS3]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[CCDC170]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[HOXB7]] | +0.56 | +0.46 / +0.32 | both halves | 1e-04 |  |
| [[HNRNPK-AS1]] | +0.55 | +0.29 / +0.44 | both halves | 2e-04 |  |
| [[ARGLU1]] | +0.55 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[DLEU7]] | +0.54 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[NINJ2]] | +0.54 | +0.47 / +0.29 | both halves | 2e-04 |  |
| [[TAPT1]] | +0.54 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLX]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.49 | -0.32 / -0.21 | both halves | 7e-04 |  |
| [[MKNK1]] | -0.48 | -0.31 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[SKIC8]] | -0.45 | -0.35 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]] | B | GRHL2 activity raises OVOL2's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without GRHL2 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[LINC02331]] | B | LINC02331 activity raises OVOL2's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.51× lower at baseline in the lines without LINC02331 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[TOP2A]] | B | TOP2A activity lowers OVOL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PHACTR3]] | B | PHACTR3 activity raises OVOL2's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without PHACTR3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[BANK1]] | B | BANK1 activity raises OVOL2's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without BANK1 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPR15]] | C | GPR15 activity raises OVOL2's level | lines that do not express GPR15 (46) vs lines expressing it (4) | 2.14× lower at baseline in the lines without GPR15 | 0.029 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GCG, APOB, BMP10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.2, 25.9); signed map (33.8, 1.1). **Vector** length 63.3, 9.45% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +20.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ovo like zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:17,956,979-18,059,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA504H3.3, HOVO2, CHED; previously ZNF339, CHED1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRP0](https://www.uniprot.org/uniprotkb/Q9BRP0) (Transcription factor Ovo-like 2):

> Zinc-finger transcription repressor factor. Plays a critical role in maintaining the identity of epithelial lineages by suppressing epithelial-to mesenchymal transition (EMT) mainly through the repression of ZEB1, an EMT inducer (By similarity). Positively regulates neuronal differentiation (By similarity). Suppresses cell cycling and terminal differentiation of keratinocytes by directly repressing MYC and NOTCH1. Important for the correct development of primordial germ cells in embryos (By …

**Summary**, from NCBI Gene [58495](https://www.ncbi.nlm.nih.gov/gene/58495):

> This gene encodes a member of the evolutionarily conserved ovo-like protein family. Mammalian members of this family contain a single zinc finger domain composed of a tetrad of C2H2 zinc fingers with variable N- and C-terminal extensions that contain intrinsically disordered domains. Members of this family are involved in epithelial development and differentiation. Knockout of this gene in mouse results in early embryonic lethality with phenotypes that include neurectoderm expansion, impaired …

**Accessions** — [HGNC:15804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15804) · Entrez [58495](https://www.ncbi.nlm.nih.gov/gene/58495) · UniProt [Q9BRP0](https://www.uniprot.org/uniprotkb/Q9BRP0) · Ensembl [ENSG00000125850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125850)

## Data

Gene col 4679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4679); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4679]; `tensor/DDL_lfc|DDL_z.npy` [4679]; `embed/gene_vectors.npy` [4679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4679 or target_col == 4679). Every well: [[OVOL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OVOL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
