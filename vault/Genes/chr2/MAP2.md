---
symbol: "MAP2"
type: "gene"
col: 1202
ensembl_id: "ENSG00000078018"
name: "microtubule associated protein 2"
location: "2q34"
module: 106
arm: "+"
pooled_cpm: 35.04
n_lines_expressing: 35
n_dd_up: 78
n_dd_down: 5
n_dd_up_clean: 72
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# MAP2

*microtubule associated protein 2* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 78 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.68× (z +26.5, q 0e+00, up in 32 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.561× (z -6.3, q 2e-07, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMTC1]] (+0.71, fdr 7e-06), [[PDLIM1]] (+0.68, fdr 1e-05), [[MAOA]] (+0.61, fdr 9e-06); moves opposite to [[TMEM158]] (-0.55, fdr 1e-05), [[ANTXR2]] (-0.53, fdr 1e-05), [[TMEM51]] (-0.52, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C3orf14]] → it (grade C ⚠); 4 go from it, the strongest it → [[HSD17B4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 80 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 78 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.68×** | +26.5 | 0e+00 | 32/33 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.37×** | +18.2 | 0e+00 | 25/32 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.03×** | +17.4 | 0e+00 | 27/32 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.64×** | +16.6 | 0e+00 | 29/32 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.40×** | +16.0 | 0e+00 | 26/32 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.14×** | +14.7 | 0e+00 | 27/32 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +11.3 | 2e-27 | 19/26 (PANC-1, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.3 | 3e-23 | 19/29 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **5.03×** | +9.1 | 5e-18 | 26/34 (NCI-H23, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.16×** | +8.0 | 8e-14 | 20/32 (NCI-H1792, hTERT-HPNE, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.95×** | +7.2 | 4e-11 | 19/32 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.74×** | +7.0 | 1e-10 | 24/33 (NCI-H1573, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +6.8 | 6e-10 | 16/30 (C32, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.85×** | +6.7 | 8e-10 | 23/34 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.90×** | +6.7 | 1e-09 | 22/32 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.86×** | +6.4 | 5e-09 | 22/32 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.80×** | +6.3 | 1e-08 | 17/33 (NCI-H2347, HEC-1-A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.561×** | -6.3 | 2e-07 | 21/32 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.4 | 2e-05 | 21/31 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.647×** | -4.8 | 4e-04 | 19/32 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.475×** | -4.2 | 0.003 | 16/34 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -4.1 | 0.004 | 15/32 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.570× | -3.2 | 0.13 | 13/30 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 57.5 | 17 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 10.0× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -9.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 16 | 0 | [[Tucidinostat (drug)]] 5 µM 7.78× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 67.1 | 9 (2 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 7.28× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 24.1 | 9 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.83× (z +13.3) | — |
| [[A498 (line)]] | wt | 24.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +13.0) | — |
| [[C32 (line)]] | wt | 34.1 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 9.58× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 5.94× (z +18.2) | — |
| [[J82 (line)]] | alt | 15.5 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 11.9× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 6 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.23× (z +13.1) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 13.0× (z +11.9) | — |
| [[LoVo (line)]] | wt | 10.3 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 13.0× (z +19.0) | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 20.1× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 17.9 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 6.62× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 47.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.18× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 52.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 40.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.66× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 16.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.60× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.38× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 264 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -17.1) |
| [[SW 900 (line)]] | alt | 18.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.03× (z +9.4) | — |
| [[A-427 (line)]] | wt | 9.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.31× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HS-578T (line)]] | alt | 9.73 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.47× (z +10.3) | — |
| [[NCI-H661 (line)]] | alt | 861 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -12.0) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 24.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.40× (z +8.5) | — |
| [[A-172 (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC1]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PDLIM1]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[MAOA]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[TES]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[ADGRG2]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[AKR1C1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ZFAND5]] | +0.57 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[NEBL]] | +0.57 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.56 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CCDC6]] | +0.55 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ENAH]] | +0.55 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ACSL1]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | -0.55 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ANTXR2]] | -0.53 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[TMEM51]] | -0.52 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[C16orf46]] | -0.50 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[NPTX1]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[TPBG]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[SYNJ2]] | -0.48 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[LIF]] | -0.47 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[DZANK1]] | -0.47 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[GLE1]] | -0.47 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ANKRD13D]] | -0.46 | -0.46 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C3orf14]] | C | C3orf14 activity raises MAP2's level | lines that do not express C3orf14 (12) vs lines expressing it (38) | 3.96× lower at baseline in the lines without C3orf14 | 0.050 | ⚠ within organs, on part of the lines; also absent: PTPRG-AS1, EVC, WIPF1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD17B4]] | B | MAP2 activity raises HSD17B4's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 1.09× lower at baseline in the lines without MAP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent |
| [[SEMA3E]] | B | MAP2 activity raises SEMA3E's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without MAP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent |
| [[DSEL]] | C | MAP2 activity raises DSEL's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 3.67× lower at baseline in the lines without MAP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent; co-absent with the target |
| [[SLC16A7]] | C | MAP2 activity raises SLC16A7's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 3.80× lower at baseline in the lines without MAP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 18.2); signed map (18.8, 28.5). **Vector** length 111, 29.6% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.5 | +26.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.0 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.6 | +8.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.6 | +6.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.4 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -0.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Ritonavir (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:209,424,047-209,734,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAP2A, MAP2B, MAP2C |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P11137](https://www.uniprot.org/uniprotkb/P11137) (Microtubule-associated protein 2):

> The exact function of MAP2 is unknown but MAPs may stabilize the microtubules against depolymerization. They also seem to have a stiffening effect on microtubules.

**Summary**, from NCBI Gene [4133](https://www.ncbi.nlm.nih.gov/gene/4133):

> This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The products of similar genes in rat and mouse are neuron-specific cytoskeletal proteins that are enriched in dentrites, implicating a role in determining and stabilizing dentritic shape during neuron development. A number of alternatively spliced variants encoding distinct isoforms have …

**Accessions** — [HGNC:6839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6839) · Entrez [4133](https://www.ncbi.nlm.nih.gov/gene/4133) · UniProt [P11137](https://www.uniprot.org/uniprotkb/P11137) · Ensembl [ENSG00000078018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078018)

## Data

Gene col 1202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1202); `tables/drug_effects.parquet` (86 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1202]; `tensor/DDL_lfc|DDL_z.npy` [1202]; `embed/gene_vectors.npy` [1202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1202 or target_col == 1202). Every well: [[MAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
