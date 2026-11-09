---
symbol: "GRHL2"
type: "gene"
col: 1367
ensembl_id: "ENSG00000083307"
name: "grainyhead like transcription factor 2"
location: "8q22.3"
module: 8
arm: "+"
pooled_cpm: 42.73
n_lines_expressing: 16
n_dd_up: 31
n_dd_down: 27
n_dd_up_clean: 21
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 47
direction_downstream: 87
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GRHL2

*grainyhead like transcription factor 2* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.49× (z +19.1, q 0e+00, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.789× (z -4.9, q 4e-04, down in 14 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANK3]] (+0.67, fdr 7e-06), [[PLCH1]] (+0.65, fdr 1e-05), [[CCSER1]] (+0.63, fdr 3e-05); moves opposite to [[PBX4]] (-0.49, fdr 2e-04), [[FCHSD1]] (-0.49, fdr 1e-04), [[GIPR]] (-0.48, fdr 4e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 47 arrows point to it, the strongest [[C4orf19]] → it (grade B ⚠); 87 go from it, the strongest it → [[STX19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +19.1 | 0e+00 | 11/14 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +14.6 | 0e+00 | 1/15 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +12.4 | 5e-33 | 2/13 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +10.6 | 5e-24 | 11/15 (SW48, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +10.1 | 4e-22 | 14/14 (SW48, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +8.6 | 6e-16 | 7/14 (LS 180, NCI-H2347, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +7.7 | 7e-13 | 1/13 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +6.4 | 1e-08 | 0/14 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.0 | 1e-07 | 7/14 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 4e-07 | 3/14 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +5.7 | 5e-07 | 0/14 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.5 | 2e-06 | 3/14 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +4.7 | 1e-04 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 8/14 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 5e-04 | 0/14 | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 0/14 | inconsistent across doses |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 0/15 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 9/14 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.006 | 0/14 | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.015 | 0/15 | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.020 | 11/15 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | **0.789×** | -4.9 | 4e-04 | 14/14 (LS 180, HT-29, …) | top dose only | position effect removed |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.750×** | -4.2 | 0.006 | 0/14 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.746×** | -4.1 | 0.007 | 0/14 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.760×** | -4.0 | 0.007 | 9/14 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.745×** | -4.0 | 0.007 | 0/14 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.634×** | -3.8 | 0.013 | 0/14 | inconsistent across doses | noisy plate (z scaled) |
| [[Drospirenone (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.018 | 0/14 | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.018 | 0/14 | inconsistent across doses |  |
| [[Pimozide (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.018 | 0/14 | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.629×** | -3.6 | 0.019 | 0/15 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.777×** | -3.5 | 0.024 | 0/14 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.776×** | -3.4 | 0.027 | 0/14 | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.042 | 0/14 | inconsistent across doses |  |
| [[Adenine (drug)]] 5 µM |  | 0.854× | -3.3 | 0.043 | 0/14 | top dose only |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.658×** | -3.2 | 0.046 | 0/14 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 210 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -17.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 181 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -10.2) |
| [[LoVo (line)]] | wt | 115 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 189 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0383× (z -28.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 161 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.268× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 80.2 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -12.3) ⚠ cell-cycle shift, explains ~13% of this change |
| [[KATO III (line)]] | alt | 189 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -8.8) |
| [[SW48 (line)]] | wt | 93.2 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0730× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANK3]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CCSER1]] | +0.63 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PRKCH-AS1]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[FAAH2]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PIP5K1B]] | +0.61 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[SAMD12-AS1]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TOX3]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[MTUS1]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HNF4G]] | +0.60 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[TRIM31]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX4]] | -0.49 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[FCHSD1]] | -0.49 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[GIPR]] | -0.48 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[ATG9B]] | -0.48 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[KCTD21]] | -0.48 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[GPSM1]] | -0.47 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.46 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[AP1M1]] | -0.46 | -0.41 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 11, C 36. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf19]] | B | C4orf19 activity raises GRHL2's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 4.14× lower at baseline in the lines without C4orf19 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises GRHL2's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.70× lower at baseline in the lines without SLC44A3-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises GRHL2's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 4.39× lower at baseline in the lines without HNF4G | 0.043 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[GNA14]] | B | GNA14 activity raises GRHL2's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 3.69× lower at baseline in the lines without GNA14 | 0.044 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[NAALADL2]] | B | NAALADL2 activity raises GRHL2's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 3.37× lower at baseline in the lines without NAALADL2 | 0.047 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[SPATA6L]] | B | SPATA6L activity raises GRHL2's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 4.50× lower at baseline in the lines without SPATA6L | 0.050 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GRHL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PCAT1]] | B | PCAT1 activity raises GRHL2's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.72× lower at baseline in the lines without PCAT1 | 0.080 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[MBNL3]] | B | MBNL3 activity raises GRHL2's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 3.44× lower at baseline in the lines without MBNL3 | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[MTUS1]] | B | MTUS1 activity raises GRHL2's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 3.80× lower at baseline in the lines without MTUS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[CADPS2]] | B | CADPS2 activity raises GRHL2's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 3.04× lower at baseline in the lines without CADPS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[TNFSF15]] | C | TNFSF15 activity raises GRHL2's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 14.12× lower at baseline in the lines without TNFSF15 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |

### Downstream of this gene

*87 arrows, 87 of them with an alert ⚠; grade A 0, B 49, C 38. Shown: the 12 strongest; 75 more arrows (75 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STX19]] | B | GRHL2, [[LINC02967]] activity raises STX19's level | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (16) | 2.66× lower at baseline in the lines without GRHL2, LINC02967 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[MARVELD2]] | B | GRHL2, [[LINC02967]] activity raises MARVELD2's level | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (16) | 3.97× lower at baseline in the lines without GRHL2, LINC02967 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[OVOL2]] | B | GRHL2 activity raises OVOL2's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without GRHL2 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[AP1M1]] | B | GRHL2 activity lowers AP1M1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.37× higher at baseline in the lines without GRHL2 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[OCLN]] | B | GRHL2 activity strengthens OCLN's drug response | lines that do not express GRHL2 (15) vs lines expressing it (15) | the lines without GRHL2 respond 0.19× as strongly (z diff +4.98); strongest at Homoharringtonine 5 µM: 1.10x vs 0.40x (z diff +8.3) | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; target measured in part of the lines; artifact flags |
| [[SLC44A3-AS1]] | B | GRHL2 activity raises SLC44A3-AS1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.17× lower at baseline in the lines without GRHL2 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[C4orf19]] | B | GRHL2 activity raises C4orf19's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without GRHL2 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[LINC00857]] | B | GRHL2 activity raises LINC00857's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.09× lower at baseline in the lines without GRHL2 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[PCAT1]] | B | GRHL2 activity raises PCAT1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.92× lower at baseline in the lines without GRHL2 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[MBNL3]] | B | GRHL2 activity raises MBNL3's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without GRHL2 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[GPSM1]] | B | GRHL2 activity lowers GPSM1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 2.04× higher at baseline in the lines without GRHL2 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | GRHL2, [[LINC02967]] activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 50.8); signed map (57.7, 1.6). **Vector** length 67.8, 27.8% of its response variance represented; |z| ≥ 3 in 404 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +19.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +14.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | +2.9 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.5 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.5 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | grainyhead like transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:101,492,439-101,669,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13782, BOM; previously DFNA28, TFCP2L3 |
| Gene groups (HGNC) | Grainyhead like transcription factor family |
| Reactome | 4 pathways, smallest: Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ISB3](https://www.uniprot.org/uniprotkb/Q6ISB3) (Grainyhead-like protein 2 homolog):

> Transcription factor playing an important role in primary neurulation and in epithelial development. Binds directly to the consensus DNA sequence 5'-AACCGGTT-3' acting as an activator and repressor on distinct target genes (By similarity). During embryogenesis, plays unique and cooperative roles with GRHL3 in establishing distinct zones of primary neurulation. Essential for closure 3 (rostral end of the forebrain), functions cooperatively with GRHL3 in closure 2 (forebrain/midbrain boundary) …

**Summary**, from NCBI Gene [79977](https://www.ncbi.nlm.nih.gov/gene/79977):

> The protein encoded by this gene is a transcription factor that can act as a homodimer or as a heterodimer with either GRHL1 or GRHL3. Defects in this gene are a cause of non-syndromic sensorineural deafness autosomal dominant type 28 (DFNA28).[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:2799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2799) · Entrez [79977](https://www.ncbi.nlm.nih.gov/gene/79977) · UniProt [Q6ISB3](https://www.uniprot.org/uniprotkb/Q6ISB3) · Ensembl [ENSG00000083307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083307)

## Data

Gene col 1367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1367); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1367]; `tensor/DDL_lfc|DDL_z.npy` [1367]; `embed/gene_vectors.npy` [1367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1367 or target_col == 1367). Every well: [[GRHL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRHL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
