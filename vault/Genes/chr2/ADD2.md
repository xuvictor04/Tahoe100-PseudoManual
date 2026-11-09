---
symbol: "ADD2"
type: "gene"
col: 1114
ensembl_id: "ENSG00000075340"
name: "adducin 2"
location: "2p13.3"
module: 82
arm: "+"
pooled_cpm: 18.1
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# ADD2

*adducin 2* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +24.2, q 0e+00, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.654× (z -6.4, q 7e-08, down in 10 of 17 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL5]] (+0.60, fdr 1e-05), [[TMEM108]] (+0.58, fdr 1e-05), [[ADCY1]] (+0.57, fdr 1e-05); moves opposite to [[USP49]] (-0.45, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[VASH1]] → it (grade B ⚠); 5 go from it, the strongest it → [[VASH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +24.2 | 0e+00 | 9/16 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +15.2 | 0e+00 | 5/13 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +12.4 | 4e-33 | 7/13 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +10.5 | 2e-23 | 8/17 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +9.4 | 9e-19 | 5/14 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.7 | 3e-16 | 1/15 (H4) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +6.4 | 1e-08 | 2/17 (NCI-H23, C-33 A) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 1e-06 | 8/17 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.4 | 3e-06 | 1/16 (SW 1271) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 3e-04 | 5/15 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.8 | 0.008 | 1/14 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.009 | 0/16 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.009 | 2/16 (C-33 A, H4) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.009 | 0/17 | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.012 | 0/17 | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.029 | 5/15 (NCI-H460, SHP-77, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.050 | 0/17 | top dose only |  |
| [[Hesperidin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.079 | 0/15 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -6.4 | 7e-08 | 10/17 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.687×** | -5.7 | 4e-06 | 16/17 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.730×** | -4.6 | 8e-04 | 12/16 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.749×** | -4.4 | 0.002 | 0/17 | two highest doses | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.792×** | -3.5 | 0.046 | 0/17 | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.785×** | -3.3 | 0.082 | 0/17 | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.795×** | -3.3 | 0.082 | 0/16 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.084 | 7/16 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.12 | 0/17 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.678× | -3.1 | 0.12 | 10/16 (NCI-H460, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 5 µM |  | 0.818× | -3.0 | 0.12 | 2/17 (C-33 A, A549) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 112 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -21.6) |
| [[NCI-H460 (line)]] | wt | 40.1 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.9) |
| [[A-427 (line)]] | wt | 144 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -12.7) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.5) |
| [[H4 (line)]] | wt | 95.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.0) |
| [[A549 (line)]] | wt | 81.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.3) |
| [[SHP-77 (line)]] | alt | 45.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -8.5) |
| [[A498 (line)]] | wt | 35.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 45.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 65.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -18.2) |
| [[SW 900 (line)]] | alt | 38.1 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0626× (z -8.7) |
| [[AN3 CA (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL5]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TMEM108]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ADCY1]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[KIF26A]] | +0.56 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[GPC3]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[RADIL]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ANO5]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SLC6A17]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RET]] | +0.54 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[ELOVL2]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RBM20]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[RNF212]] | +0.52 | +0.55 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP49]] | -0.45 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VASH1]] | B | VASH1 activity raises ADD2's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without VASH1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[ST6GALNAC3]] | B | ST6GALNAC3 activity raises ADD2's level | lines that do not express ST6GALNAC3 (18) vs lines expressing it (32) | 3.38× lower at baseline in the lines without ST6GALNAC3 | 0.097 | ⚠ within organs, on part of the lines; also absent: TRIM9, GHR, OSBPL6; maybe low, not absent |
| [[DCLK2]] | C | DCLK2 activity raises ADD2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 4.45× lower at baseline in the lines without DCLK2 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises ADD2's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 4.01× lower at baseline in the lines without DPYSL5 | 0.084 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[KIF26A]] | C | KIF26A activity raises ADD2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 4.15× lower at baseline in the lines without KIF26A | 0.0999 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VASH1]] | B | ADD2 activity raises VASH1's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 2.68× lower at baseline in the lines without ADD2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1 |
| [[PTPRS]] | B | ADD2 activity raises PTPRS's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without ADD2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1 |
| [[DCLK2]] | C | ADD2 activity raises DCLK2's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 5.30× lower at baseline in the lines without ADD2 | 0.014 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1; co-absent with the target |
| [[KIF26A]] | C | ADD2 activity raises KIF26A's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without ADD2 | 0.028 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1; co-absent with the target |
| [[RASSF2]] | C | ADD2 activity raises RASSF2's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without ADD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.2, 39.0); signed map (27.5, 27.5). **Vector** length 52.5, 15.4% of its response variance represented; |z| ≥ 3 in 424 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +24.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | adducin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,607,618-70,768,225 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADDB |
| Gene groups (HGNC) | Adducin family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P35612](https://www.uniprot.org/uniprotkb/P35612) (Beta-adducin):

> Membrane-cytoskeleton-associated protein that promotes the assembly of the spectrin-actin network. Binds to the erythrocyte membrane receptor SLC2A1/GLUT1 and may therefore provide a link between the spectrin cytoskeleton to the plasma membrane. Binds to calmodulin. Calmodulin binds preferentially to the beta subunit.

**Summary**, from NCBI Gene [119](https://www.ncbi.nlm.nih.gov/gene/119):

> Adducins are heteromeric proteins composed of different subunits referred to as adducin alpha, beta and gamma. The three subunits are encoded by distinct genes and belong to a family of membrane skeletal proteins involved in the assembly of spectrin-actin network in erythrocytes and at sites of cell-cell contact in epithelial tissues. While adducins alpha and gamma are ubiquitously expressed, the expression of adducin beta is restricted to brain and hematopoietic tissues. Adducin, originally …

**Accessions** — [HGNC:244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:244) · Entrez [119](https://www.ncbi.nlm.nih.gov/gene/119) · UniProt [P35612](https://www.uniprot.org/uniprotkb/P35612) · Ensembl [ENSG00000075340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075340)

## Data

Gene col 1114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1114); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1114]; `tensor/DDL_lfc|DDL_z.npy` [1114]; `embed/gene_vectors.npy` [1114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1114 or target_col == 1114). Every well: [[ADD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
