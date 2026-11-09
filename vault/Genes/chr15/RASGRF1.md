---
symbol: "RASGRF1"
type: "gene"
col: 660
ensembl_id: "ENSG00000058335"
name: "Ras protein specific guanine nucleotide releasing factor 1"
location: "15q25.1"
module: 92
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 32
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# RASGRF1

*Ras protein specific guanine nucleotide releasing factor 1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.88× (z +16.4, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.605× (z -4.7, q 0.001, down in 11 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.149×; ⚠ toxic; cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRL4]] (+0.70, fdr 7e-06), [[SERTAD4]] (+0.68, fdr 7e-06), [[CD22]] (+0.66, fdr 1e-05); moves opposite to [[HMBOX1]] (-0.56, fdr 1e-05), [[KLHDC10]] (-0.56, fdr 3e-05), [[RARS2]] (-0.55, fdr 2e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC03042]] → it (grade B ⚠); 4 go from it, the strongest it → [[SDHAP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.88×** | +16.4 | 0e+00 | 16/19 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +13.0 | 5e-36 | 3/6 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +12.6 | 5e-34 | 17/27 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.88×** | +11.6 | 7e-29 | 16/18 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +11.0 | 4e-26 | 9/21 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.33×** | +10.3 | 8e-23 | 5/10 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.91×** | +8.4 | 3e-15 | 4/7 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.55×** | +8.0 | 1e-13 | 16/23 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +7.0 | 2e-10 | 18/25 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +6.9 | 3e-10 | 15/23 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.1 | 6e-08 | 12/27 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.9 | 1e-07 | 2/10 (SK-MEL-2, SNU-423) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +5.5 | 2e-06 | 10/24 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.79×** | +5.0 | 3e-05 | 6/27 (NCI-H1573, A-427, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +4.8 | 8e-05 | 2/10 (NCI-H2347, HOP62) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +4.2 | 8e-04 | 12/27 (NCI-H1573, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.93×** | +4.0 | 0.002 | 1/10 (Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.003 | 8/26 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.018 | 6/24 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.032 | 4/13 (SNU-423, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.034 | 2/27 (NCI-H2347, SW480) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 660.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (J82 0.149×; ⚠ toxic; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.605×** | -4.7 | 0.001 | 11/28 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.600×** | -4.2 | 0.007 | 4/28 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.685× | -3.0 | 0.51 | 6/26 (SW480, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 29.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 7.25 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.6× (z +18.6) | — |
| [[A-172 (line)]] | wt | 3.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.0× (z +12.8) | — |
| [[J82 (line)]] | alt | 16.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 3.67 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 29.2× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 1.18 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 25.0× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 8.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +10.9) | — |
| [[A-427 (line)]] | wt | 0.818 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.799 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.680 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRL4]] | +0.70 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SERTAD4]] | +0.68 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[CD22]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[PPP1R1C]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[LINC00460]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SKIL]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.61 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ZNF702P]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZNF462]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[LTBP2]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[BACH1]] | +0.60 | +0.46 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMBOX1]] | -0.56 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[KLHDC10]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RARS2]] | -0.55 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HTT]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RUFY2]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.54 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[GNB2]] | -0.54 | -0.52 / -0.46 | both halves | 3e-05 | pathway: Neuronal System; STRING 655 |
| [[RAB6A]] | -0.54 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.54 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[EFCAB14]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.53 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[MOSPD3]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03042]] | B | LINC03042 activity raises RASGRF1's level | lines that do not express LINC03042 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without LINC03042 | 0.031 | ⚠ within organs, on part of the lines; also absent: LINC00960, CORO2B, DNAH17; maybe low, not absent |
| [[CD22]] | B | CD22 activity raises RASGRF1's level | lines that do not express CD22 (21) vs lines expressing it (29) | 1.59× lower at baseline in the lines without CD22 | 0.057 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP4]] | B | RASGRF1 activity raises SDHAP4's level | lines that do not express RASGRF1 (18) vs lines expressing it (32) | 1.34× lower at baseline in the lines without RASGRF1 | 0.014 | ⚠ within organs, on part of the lines; also absent: RORC, MIR4280HG, TMEM40; maybe low, not absent |
| [[LINC03042]] | B | RASGRF1 activity raises LINC03042's level | lines that do not express RASGRF1 (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without RASGRF1 | 0.024 | ⚠ within organs, on part of the lines; also absent: RORC, MIR4280HG, TMEM40; maybe low, not absent |
| [[ABCG2]] | B | RASGRF1 activity lowers ABCG2's level | lines that do not express RASGRF1 (18) vs lines expressing it (32) | 1.72× higher at baseline in the lines without RASGRF1 | 0.026 | ⚠ within organs, on part of the lines; also absent: RORC, MIR4280HG, TMEM40; maybe low, not absent |
| [[ZNF620]] | B | RASGRF1 activity raises ZNF620's level | lines that do not express RASGRF1 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without RASGRF1 | 0.087 | ⚠ within organs, on part of the lines; also absent: RORC, MIR4280HG, TMEM40; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, 6.0); signed map (27.2, 6.5). **Vector** length 50.3, 9.24% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Ras protein specific guanine nucleotide releasing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,959,906-79,090,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDC25L, CDC25, GRF55, H-GRF55, GNRP, PP13187; previously GRF1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 10 pathways, smallest: Ras activation upon Ca2+ influx through NMDA receptor; CREB1 phosphorylation through NMDA receptor-mediated activation of RAS signaling; Post NMDA receptor activation events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13972](https://www.uniprot.org/uniprotkb/Q13972) (Ras-specific guanine nucleotide-releasing factor 1):

> Promotes the exchange of Ras-bound GDP by GTP.

**Summary**, from NCBI Gene [5923](https://www.ncbi.nlm.nih.gov/gene/5923):

> The protein encoded by this gene is a guanine nucleotide exchange factor (GEF) similar to the Saccharomyces cerevisiae CDC25 gene product. Functional analysis has demonstrated that this protein stimulates the dissociation of GDP from RAS protein. The studies of the similar gene in mouse suggested that the Ras-GEF activity of this protein in brain can be activated by Ca2+ influx, muscarinic receptors, and G protein beta-gamma subunit. Mouse studies also indicated that the Ras-GEF signaling …

**Accessions** — [HGNC:9875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9875) · Entrez [5923](https://www.ncbi.nlm.nih.gov/gene/5923) · UniProt [Q13972](https://www.uniprot.org/uniprotkb/Q13972) · Ensembl [ENSG00000058335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058335)

## Data

Gene col 660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 660); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 660]; `tensor/DDL_lfc|DDL_z.npy` [660]; `embed/gene_vectors.npy` [660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 660 or target_col == 660). Every well: [[RASGRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
