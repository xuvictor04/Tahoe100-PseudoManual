---
symbol: "FCHO1"
type: "gene"
col: 5068
ensembl_id: "ENSG00000130475"
name: "FCH and mu domain containing endocytic adaptor 1"
location: "19p13.11"
module: 85
arm: "+"
pooled_cpm: 5.29
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# FCHO1

*FCH and mu domain containing endocytic adaptor 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 12.7× (z +33.2, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.668× (z -5.3, q 7e-05, down in 13 of 40 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.75, fdr 1e-05), [[MAST3]] (+0.74, fdr 1e-05), [[LMTK3]] (+0.72, fdr 1e-05); moves opposite to [[EFCAB2]] (-0.74, fdr 1e-05), [[PBLD]] (-0.72, fdr 2e-05), [[UBE3B]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ENTPD2]] → it (grade B ⚠); 9 go from it, the strongest it → [[ATXN7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **12.7×** | +33.2 | 0e+00 | 41/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **12.0×** | +32.5 | 0e+00 | 41/41 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **9.96×** | +30.1 | 0e+00 | 41/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **5.10×** | +21.3 | 0e+00 | 41/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.03×** | +20.5 | 0e+00 | 39/41 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.83×** | +13.6 | 3e-40 | 31/38 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.97×** | +9.4 | 3e-19 | 19/38 (PANC-1, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.79×** | +7.6 | 2e-12 | 14/30 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.4 | 6e-12 | 6/18 (AsPC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.3 | 2e-08 | 1/11 (A549) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.5 | 4e-04 | 2/5 (CFPAC-1, PANC-1) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.4 | 5e-04 | 11/35 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.2 | 9e-04 | 7/24 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 3/40 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.9 | 0.003 | 2/15 (A-427, CFPAC-1) | rises with dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.009 | 7/41 (A498, NCI-H460, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.049 | 2/37 (A498, SW 900) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -5.3 | 7e-05 | 13/40 (SW48, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -4.5 | 0.002 | 13/31 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.042 | 8/39 (LOX-IMVI, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.775× | -3.2 | 0.20 | 4/38 (NCI-H2030, SW 900, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.793× | -3.0 | 0.27 | 14/41 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.8 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.71× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -20.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 2.28 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 22.3× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 9.80 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.6× (z +11.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0330× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.172× (z -11.7) |
| [[Hs 766T (line)]] | wt | 6.45 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.3× (z +9.3) | — |
| [[LoVo (line)]] | wt | 2.65 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 21.7× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 20.8× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.14 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 12.7× (z +9.1) | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0868× (z -8.8) |
| [[PANC-1 (line)]] | alt | 2.43 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.8× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 6.57 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.85× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 1.92 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 23.8× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 1.89 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 14.3× (z +8.9) | — |
| [[KATO III (line)]] | alt | 7.19 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.04× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 7.64 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.39× (z +8.9) | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -10.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 7.98 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.107× (z -9.8) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -10.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.75 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MAST3]] | +0.74 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LMTK3]] | +0.72 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.71 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.70 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[CADM4]] | +0.70 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ATP1A3]] | +0.69 | +0.28 / +0.70 | both halves | 3e-04 |  |
| [[DNAAF3]] | +0.69 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[FBXL16]] | +0.69 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[PEDS1]] | +0.69 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[YIF1B]] | +0.68 | +0.58 / +0.27 | both halves | 3e-04 |  |
| [[TNNI3]] | +0.68 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.74 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PBLD]] | -0.72 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[UBE3B]] | -0.71 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SPRY3]] | -0.71 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MFF-DT]] | -0.70 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[CREBBP]] | -0.69 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[UBTF]] | -0.69 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.68 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[ZMYND11]] | -0.67 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZNF337-AS1]] | -0.67 | -0.54 / -0.24 | both halves | 4e-04 |  |
| [[ARFGAP2]] | -0.66 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[DDX59]] | -0.66 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENTPD2]] | B | ENTPD2 activity raises FCHO1's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 1.45× lower at baseline in the lines without ENTPD2 | 0.040 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |
| [[PADI2]] | B | PADI2 activity raises FCHO1's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.65× lower at baseline in the lines without PADI2 | 0.058 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[FGFR4]] | B | FGFR4 activity raises FCHO1's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without FGFR4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[TNNI3]] | B | TNNI3 activity raises FCHO1's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without TNNI3 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TESC]] | B | TESC activity raises FCHO1's level | lines that do not express TESC (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without TESC | 0.075 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[MCF2L]] | B | MCF2L activity raises FCHO1's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.44× lower at baseline in the lines without MCF2L | 0.075 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[RASAL1]] | B | RASAL1 activity raises FCHO1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without RASAL1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[RASAL1]] | B | RASAL1 activity weakens FCHO1's drug response | lines that do not express RASAL1 (22) vs lines expressing it (20) | the lines without RASAL1 respond 1.14× as strongly (z diff -1.02); strongest at Dinaciclib 0.05 µM: 1.41x vs 0.82x (z diff -2.5) | 0.076 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1; target measured in part of the lines; artifact flags |
| [[RGS9]] | B | RGS9 activity raises FCHO1's level | lines that do not express RGS9 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without RGS9 | 0.094 | ⚠ within organs, on part of the lines; also absent: TMEM132A, KCNC4, ECE1; maybe low, not absent |
| [[UNC5B]] | B | UNC5B activity strengthens FCHO1's drug response | lines that do not express UNC5B (6) vs lines expressing it (36) | the lines without UNC5B respond 0.81× as strongly (z diff +1.39); strongest at Belinostat 5 µM: 4.25x vs 8.80x (z diff +1.6) | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SYP]] | C | SYP activity raises FCHO1's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN7]] | B | FCHO1 activity raises ATXN7's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without FCHO1 | 0.022 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[DNAAF3]] | B | FCHO1 activity raises DNAAF3's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without FCHO1 | 0.024 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[SEMA3F]] | B | FCHO1 activity raises SEMA3F's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without FCHO1 | 0.028 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[TNFAIP8L1]] | B | FCHO1 activity raises TNFAIP8L1's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without FCHO1 | 0.034 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[BDNF-AS]] | B | FCHO1 activity lowers BDNF-AS's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.38× higher at baseline in the lines without FCHO1 | 0.045 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[TRIP10]] | B | FCHO1 activity raises TRIP10's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without FCHO1 | 0.056 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[PRPF40A]] | B | FCHO1 activity raises PRPF40A's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without FCHO1 | 0.056 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[PAFAH1B3]] | B | FCHO1 activity raises PAFAH1B3's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without FCHO1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |
| [[CADM4]] | B | FCHO1 activity raises CADM4's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without FCHO1 | 0.074 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (10.1, 1.7); signed map (-21.6, 29.2). **Vector** length 77.2, 14.0% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +20.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +13.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +33.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | +32.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | +30.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.0 |
|  | [[Erythromycin (drug)]] 5 µM |  | +1.3 | +3.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.5 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | FCH and mu domain containing endocytic adaptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,747,718-17,788,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0290 |
| Gene groups (HGNC) | F-BAR domain containing |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O14526](https://www.uniprot.org/uniprotkb/O14526) (F-BAR domain only protein 1):

> Functions in an early step of clathrin-mediated endocytosis. Has both a membrane binding/bending activity and the ability to recruit proteins essential to the formation of functional clathrin-coated pits. May regulate Bmp signaling by regulating clathrin-mediated endocytosis of Bmp receptors. Involved in the regulation of T-cell proliferation and activation. Affects TCR clustering upon receptor triggering and modulates its internalization, playing a role in TCR-dependent T-cell activation.

**Summary**, from NCBI Gene [23149](https://www.ncbi.nlm.nih.gov/gene/23149):

> Enables AP-2 adaptor complex binding activity. Involved in several processes, including T cell receptor signaling pathway; clathrin coat assembly; and clathrin-dependent endocytosis. Located in cytosol; nucleoplasm; and plasma membrane. Is active in clathrin-coated pit. Implicated in primary immunodeficiency disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29002) · Entrez [23149](https://www.ncbi.nlm.nih.gov/gene/23149) · UniProt [O14526](https://www.uniprot.org/uniprotkb/O14526) · Ensembl [ENSG00000130475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130475)

## Data

Gene col 5068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5068); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5068]; `tensor/DDL_lfc|DDL_z.npy` [5068]; `embed/gene_vectors.npy` [5068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5068 or target_col == 5068). Every well: [[FCHO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCHO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
