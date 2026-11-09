---
symbol: "IRF6"
type: "gene"
col: 3929
ensembl_id: "ENSG00000117595"
name: "interferon regulatory factor 6"
location: "1q32.2"
module: 31
arm: "+"
pooled_cpm: 34.38
n_lines_expressing: 19
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 25
direction_downstream: 92
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# IRF6

*interferon regulatory factor 6* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.09× (z +10.8, q 1e-24, up in 0 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.89× (z +9.3, q 3e-18, up in 14 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Darinaparsin (drug)]] 5 µM: 0.812× (z -4.3, q 0.008, down in 8 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.144×, CFPAC-1 0.150×, COLO 205 0.212×, LS 180 0.322×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.224×, CFPAC-1 0.153×, SW48 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.254×, CFPAC-1 0.174×, LS 180 0.282×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.473×, Hs 766T 0.349×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH1]] (+0.66, fdr 2e-05), [[ATG9B]] (+0.61, fdr 1e-05), [[FA2H]] (+0.60, fdr 1e-05); moves opposite to [[ECHDC1]] (-0.49, fdr 2e-04), [[SNX5]] (-0.47, fdr 5e-04), [[GPHN]] (-0.47, fdr 3e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[TMCC3]] → it (grade B ⚠); 92 go from it, the strongest it → [[PTK2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +10.8 | 1e-24 | 0/18 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +9.3 | 3e-18 | 14/17 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.6 | 5e-12 | 2/18 (HEC-1-A, SW48) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +7.4 | 2e-11 | 14/17 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +6.4 | 2e-08 | 15/17 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +6.2 | 5e-08 | 6/17 (HEC-1-A, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.6 | 1e-06 | 4/17 (SW480, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.5 | 2e-06 | 4/17 (SW48, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 2/18 (SW48, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 9e-05 | 0/16 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 8/17 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 6/17 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.002 | 1/17 (Hs 766T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 7/18 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.7 | 0.008 | 4/17 (AsPC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.008 | 2/18 (SW480, Hs 766T) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.011 | 2/17 (NCI-H1573, CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.029 | 5/17 (HCT15, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3929.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.144×, CFPAC-1 0.150×, COLO 205 0.212×, LS 180 0.322×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2347 0.224×, CFPAC-1 0.153×, SW48 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.254×, CFPAC-1 0.174×, LS 180 0.282×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.473×, Hs 766T 0.349×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Darinaparsin (drug)]] 5 µM |  | **0.812×** | -4.3 | 0.008 | 8/17 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.839× | -3.6 | 0.076 | 15/17 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.850× | -3.4 | 0.14 | 1/17 (SW480) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.35× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 297 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -16.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 66.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 54.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 35.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 54.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -8.6) |
| [[HT-29 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.136× (z -8.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 76.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.8) |
| [[SW48 (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH1]] | +0.66 | +0.48 / +0.78 | both halves | 2e-05 | STRING 418 |
| [[ATG9B]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[FA2H]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MPZL3]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[MYO5B]] | +0.57 | +0.30 / +0.72 | both halves | 2e-04 |  |
| [[JUP]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[RAB11FIP1]] | +0.55 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[NECTIN4]] | +0.54 | +0.32 / +0.67 | both halves | 2e-04 |  |
| [[MXD1]] | +0.54 | +0.47 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[MICE]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[NET1]] | +0.54 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[PTK2B]] | +0.54 | +0.37 / +0.58 | both halves | 9e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHDC1]] | -0.49 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[SNX5]] | -0.47 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[GPHN]] | -0.47 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[ATXN10]] | -0.46 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[NINJ2]] | -0.46 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[IGF2BP3]] | -0.45 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[ABCE1]] | -0.45 | -0.40 / -0.30 | both halves | 2e-04 | pathway: Interferon Signaling |
| [[ALG8]] | -0.45 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[PCNX4]] | -0.45 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[E2F3]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[DNAJB14]] | -0.44 | -0.41 / -0.21 | both halves | 6e-04 |  |
| [[ERCC6L2]] | -0.44 | -0.41 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 7, C 18. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC3]] | B | TMCC3 activity raises IRF6's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.92× lower at baseline in the lines without TMCC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[SEMA3B]] | B | SEMA3B activity raises IRF6's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.47× lower at baseline in the lines without SEMA3B | 0.029 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[F11R]] | B | F11R activity raises IRF6's level | lines that do not express F11R (10) vs lines expressing it (40) | 3.78× lower at baseline in the lines without F11R | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[LMTK3]] | B | LMTK3 activity raises IRF6's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.82× lower at baseline in the lines without LMTK3 | 0.053 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[FGD6]] | B | FGD6 activity raises IRF6's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 4.44× lower at baseline in the lines without FGD6 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[FHIP1A]] | B | FHIP1A activity raises IRF6's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 3.41× lower at baseline in the lines without FHIP1A | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises IRF6's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without KPNA7 | 0.083 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[ST14]] | C | ST14 activity raises IRF6's level | lines that do not express ST14 (32) vs lines expressing it (18) | 14.35× lower at baseline in the lines without ST14 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises IRF6's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 12.25× lower at baseline in the lines without CDH1 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[RNF39]] | C | RNF39 activity raises IRF6's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 9.75× lower at baseline in the lines without RNF39 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises IRF6's level | lines that do not express INAVA (29) vs lines expressing it (21) | 7.35× lower at baseline in the lines without INAVA | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[MYO5B]] | C | MYO5B activity raises IRF6's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 7.41× lower at baseline in the lines without MYO5B | 3e-04 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3; co-absent with the target |

### Downstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 72, C 20. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTK2B]] | B | IRF6 activity raises PTK2B's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.96× lower at baseline in the lines without IRF6 | 6e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[KPNA7]] | B | IRF6 activity raises KPNA7's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.14× lower at baseline in the lines without IRF6 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[F11R]] | B | IRF6 activity raises F11R's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.89× lower at baseline in the lines without IRF6 | 4e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TUFT1]] | B | IRF6 activity raises TUFT1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without IRF6 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[RND1]] | B | IRF6 activity raises RND1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without IRF6 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[FHIP1A]] | B | IRF6 activity raises FHIP1A's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.33× lower at baseline in the lines without IRF6 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TLDC2]] | B | [[C1orf116]], IRF6 activity raises TLDC2's level | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (19) | 2.49× lower at baseline in the lines without C1orf116, IRF6 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[MICE]] | B | IRF6 activity raises MICE's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without IRF6 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[SLC25A25]] | B | IRF6 activity raises SLC25A25's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without IRF6 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[RAB11FIP1]] | B | IRF6 activity raises RAB11FIP1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without IRF6 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MXD1]] | B | IRF6 activity raises MXD1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without IRF6 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[SEMA3B]] | B | [[C1orf116]], IRF6 activity raises SEMA3B's level | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (19) | 3.82× lower at baseline in the lines without C1orf116, IRF6 | 0.006 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, 60.0); signed map (54.1, 9.0). **Vector** length 66.1, 25.2% of its response variance represented; |z| ≥ 3 in 382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.6 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | +4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | +2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:209,785,617-209,806,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OFC6, VWS1; previously VWS, LPS |
| Gene groups (HGNC) | Interferon regulatory factors |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 4 pathways, smallest: Interferon alpha/beta signaling; Interferon gamma signaling; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14896](https://www.uniprot.org/uniprotkb/O14896) (Interferon regulatory factor 6):

> Probable DNA-binding transcriptional activator. Key determinant of the keratinocyte proliferation-differentiation switch involved in appropriate epidermal development (By similarity). Plays a role in regulating mammary epithelial cell proliferation (By similarity). May regulate WDR65 transcription (By similarity).

**Summary**, from NCBI Gene [3664](https://www.ncbi.nlm.nih.gov/gene/3664):

> This gene encodes a member of the interferon regulatory transcription factor (IRF) family. Family members share a highly-conserved N-terminal helix-turn-helix DNA-binding domain and a less conserved C-terminal protein-binding domain. The encoded protein may be a transcriptional activator. Mutations in this gene can cause van der Woude syndrome and popliteal pterygium syndrome. Mutations in this gene are also associated with non-syndromic orofacial cleft type 6. Alternate splicing results in …

**Accessions** — [HGNC:6121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6121) · Entrez [3664](https://www.ncbi.nlm.nih.gov/gene/3664) · UniProt [O14896](https://www.uniprot.org/uniprotkb/O14896) · Ensembl [ENSG00000117595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117595)

## Data

Gene col 3929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3929); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3929]; `tensor/DDL_lfc|DDL_z.npy` [3929]; `embed/gene_vectors.npy` [3929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3929 or target_col == 3929). Every well: [[IRF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
