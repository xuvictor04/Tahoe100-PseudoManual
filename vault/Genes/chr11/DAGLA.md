---
symbol: "DAGLA"
type: "gene"
col: 5605
ensembl_id: "ENSG00000134780"
name: "diacylglycerol lipase alpha"
location: "11q12.2"
module: 37
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 7
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DAGLA

*diacylglycerol lipase alpha* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.59× (z +5.4, q 5e-05, up in 15 of 41 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.49× (z +4.6, q 8e-04, up in 11 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.521× (z -10.7, q 4e-24, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF30]] (+0.60, fdr 3e-05), [[SNPH]] (+0.59, fdr 1e-05), [[DGAT2]] (+0.59, fdr 4e-05); moves opposite to [[PXDNL]] (-0.59, fdr 6e-05), [[NPHP3-ACAD11]] (-0.58, fdr 7e-05), [[LINC02955]] (-0.54, fdr 2e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 7 go from it, the strongest it → [[USP49]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +5.4 | 5e-05 | 15/41 (NCI-H1792, HepG2/C3A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.56×** | +5.1 | 8e-05 | 16/42 (PANC-1, hTERT-HPNE, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.6 | 8e-04 | 11/42 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 9e-04 | 10/40 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.40×** | +3.9 | 0.012 | 13/42 (PANC-1, HepG2/C3A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.022 | 7/40 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.022 | 8/41 (SW480, KATO III, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.35×** | +3.3 | 0.067 | 7/40 (SW1417, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.33×** | +3.2 | 0.096 | 5/26 (NCI-H23, SW480, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.096 | 9/31 (A-427, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.098 | 3/39 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.521×** | -10.7 | 4e-24 | 28/37 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -4.3 | 0.004 | 15/35 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.708×** | -4.0 | 0.010 | 11/19 (Panc 03.27, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.058 | 12/41 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.06 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0446× (z -12.4) |
| [[C32 (line)]] | wt | 4.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 4.41 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 3.61 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0793× (z -8.8) |
| [[KATO III (line)]] | alt | 4.34 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0692× (z -9.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.6) |
| [[RKO (line)]] | wt | 7.45 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -8.8) |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0784× (z -9.4) |
| [[SW480 (line)]] | alt | 7.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF30]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[SNPH]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[DGAT2]] | +0.59 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ZFAND4]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GNAZ]] | +0.56 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[C15orf39]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[OSBPL7]] | +0.56 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[AADAT]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[MOCS1]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ZNF592]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PANK4]] | +0.53 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.53 | +0.35 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXDNL]] | -0.59 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[NPHP3-ACAD11]] | -0.58 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[LINC02955]] | -0.54 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[LEPR]] | -0.54 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[RNF217-AS1]] | -0.53 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[HERC4]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[MCF2]] | -0.52 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[TBCE-1]] | -0.52 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[OOEP]] | -0.52 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[LINC02936]] | -0.51 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[WDR49]] | -0.50 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[LINC02680]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP49]] | C | DAGLA activity raises USP49's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without DAGLA | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[DNMT3B]] | C | DAGLA activity raises DNMT3B's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without DAGLA | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[AARS2]] | C | DAGLA activity raises AARS2's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without DAGLA | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[PPP5C]] | C | DAGLA activity raises PPP5C's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without DAGLA | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[HEYL]] | C | DAGLA activity raises HEYL's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.29× lower at baseline in the lines without DAGLA | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[FAAP100]] | C | DAGLA activity raises FAAP100's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without DAGLA | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |
| [[SAAL1]] | C | DAGLA activity raises SAAL1's level | lines that do not express DAGLA (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without DAGLA | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PLEKHF1, NBEAP2, C2orf27A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction -0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, 30.2); signed map (-37.5, -17.3). **Vector** length 58.7, 8.68% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.9 | +4.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol lipase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,680,391-61,747,001 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0659, NSDDR, DAGLALPHA; previously C11orf11 |
| Gene groups (HGNC) | Lipases |
| Reactome | 7 pathways, smallest: Arachidonate production from DAG; Effects of PIP2 hydrolysis; G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4D2](https://www.uniprot.org/uniprotkb/Q9Y4D2) (Diacylglycerol lipase-alpha):

> Serine hydrolase that hydrolyzes arachidonic acid-esterified diacylglycerols (DAGs) to produce the principal endocannabinoid, 2-arachidonoylglycerol (2-AG). Preferentially hydrolyzes sn-1 fatty acids from diacylglycerols (DAG) that contain arachidonic acid (AA) esterified at the sn-2 position to biosynthesize 2-AG. Has negligible activity against other lipids including monoacylglycerols and phospholipids. Plays a key role in regulating 2-AG signaling in the central nervous system (CNS). …

**Summary**, from NCBI Gene [747](https://www.ncbi.nlm.nih.gov/gene/747):

> This gene encodes a diacylglycerol lipase. The encoded enzyme is involved in the biosynthesis of the endocannabinoid 2-arachidonoyl-glycerol.[provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:1165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1165) · Entrez [747](https://www.ncbi.nlm.nih.gov/gene/747) · UniProt [Q9Y4D2](https://www.uniprot.org/uniprotkb/Q9Y4D2) · Ensembl [ENSG00000134780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134780)

## Data

Gene col 5605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5605); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5605]; `tensor/DDL_lfc|DDL_z.npy` [5605]; `embed/gene_vectors.npy` [5605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5605 or target_col == 5605). Every well: [[DAGLA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAGLA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
