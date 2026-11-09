---
symbol: "CFLAR-AS1"
type: "gene"
col: 13526
ensembl_id: "ENSG00000226312"
name: "CFLAR antisense RNA 1"
location: "2q33.1"
module: 80
arm: "+"
pooled_cpm: 5.55
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# CFLAR-AS1

*CFLAR antisense RNA 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.29× (z +26.7, q 0e+00, up in 29 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.565× (z -6.5, q 6e-08, down in 21 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LETM2]] (+0.71, fdr 1e-05), [[ZNF341-AS1]] (+0.71, fdr 1e-05), [[LINC00705]] (+0.70, fdr 1e-05); moves opposite to [[STRN]] (-0.67, fdr 4e-05), [[SDHAP4]] (-0.65, fdr 1e-05), [[RPA1]] (-0.64, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EDN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.29×** | +26.7 | 0e+00 | 29/35 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.73×** | +14.9 | 0e+00 | 28/34 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.31×** | +13.0 | 1e-36 | 28/39 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +10.3 | 1e-22 | 10/14 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +8.2 | 3e-14 | 10/22 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.9 | 5e-10 | 19/45 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +6.5 | 8e-09 | 2/10 (LOX-IMVI, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +5.4 | 6e-06 | 16/37 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 6e-06 | 19/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.2 | 1e-05 | 7/25 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 3e-05 | 12/34 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.2 | 0.001 | 3/11 (NCI-H2030, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.002 | 13/45 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.002 | 8/41 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.005 | 8/34 (HT-29, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.007 | 10/38 (KATO III, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.024 | 4/34 (A498, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.064 | 9/40 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.097 | 9/42 (HT-29, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -6.5 | 6e-08 | 21/46 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -5.6 | 5e-06 | 20/45 (SW1417, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.655×** | -4.8 | 3e-04 | 17/44 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.0 | 0.009 | 10/48 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.696×** | -3.9 | 0.009 | 11/38 (NCI-H1792, A549, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.720×** | -3.7 | 0.019 | 7/47 (SW1417, Panc 03.27, …) | top dose only |  |
| [[Ivabradine (hydrochloride) (drug)]] 0.5 µM | ⚠ transcription drop; unreliable plate only | 0.760× | -3.1 | 0.15 | 11/40 (HepG2/C3A, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.10 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0479× (z -14.4) |
| [[A-172 (line)]] | wt | 5.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 6.80 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +11.4) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0837× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 30.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +13.7) | — |
| [[A498 (line)]] | wt | 4.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +10.0) | — |
| [[A549 (line)]] | wt | 7.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 9.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 6.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +15.8) | — |
| [[HepG2_C3A (line)]] | wt | 8.51 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0460× (z -9.5) |
| [[HOP62 (line)]] | alt | 3.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +16.1) | — |
| [[HS-578T (line)]] | alt | 2.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +9.5) | — |
| [[J82 (line)]] | alt | 8.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +12.0) | — |
| [[LoVo (line)]] | wt | 4.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 5.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 5.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 3.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.7× (z +13.5) | — |
| [[A-427 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM2]] | +0.71 | +0.79 / +0.57 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.71 | +0.75 / +0.55 | both halves | 1e-05 | same gene group |
| [[LINC00705]] | +0.70 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PIGV]] | +0.69 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[WAKMAR2]] | +0.69 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[LINC01186]] | +0.69 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.68 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[LAMA2]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ABL2]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.66 | +0.72 / +0.42 | both halves | 4e-05 | same gene group |
| [[LPXN]] | +0.64 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[LACC1]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRN]] | -0.67 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[SDHAP4]] | -0.65 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[RPA1]] | -0.64 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.64 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[SDHA]] | -0.64 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[UBAC1]] | -0.63 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.63 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[PMS2P3-1]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.62 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[SEC11A]] | -0.61 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[GET1]] | -0.60 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[SERAC1]] | -0.59 | -0.64 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDN1]] | B | EDN1 activity raises CFLAR-AS1's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.58× lower at baseline in the lines without EDN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[ZNF829]] | B | ZNF829 activity lowers CFLAR-AS1's level | lines that do not express ZNF829 (20) vs lines expressing it (30) | 1.44× higher at baseline in the lines without ZNF829 | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF568, ZNF880, ZNF625 |
| [[HDAC6]] | B | HDAC6 activity raises CFLAR-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSORS1C1]] | B | PSORS1C1 activity raises CFLAR-AS1's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.59× lower at baseline in the lines without PSORS1C1 | 0.081 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.0, 11.1); signed map (26.0, 5.8). **Vector** length 73.0, 12.7% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +26.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +14.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +13.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.2 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | CFLAR antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q33.1 — chr2:201,140,278-201,157,823 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously ALS2CR10 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:14437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14437) · Entrez [65072](https://www.ncbi.nlm.nih.gov/gene/65072) · Ensembl [ENSG00000226312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226312)

## Data

Gene col 13526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13526); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13526]; `tensor/DDL_lfc|DDL_z.npy` [13526]; `embed/gene_vectors.npy` [13526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13526 or target_col == 13526). Every well: [[CFLAR-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFLAR-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
