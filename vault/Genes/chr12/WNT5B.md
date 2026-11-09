---
symbol: "WNT5B"
type: "gene"
col: 3197
ensembl_id: "ENSG00000111186"
name: "Wnt family member 5B"
location: "12p13.33"
module: 13
arm: "+"
pooled_cpm: 27.94
n_lines_expressing: 28
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 23
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# WNT5B

*Wnt family member 5B* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +16.1, q 0e+00, up in 12 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.485× (z -11.4, q 2e-27, down in 22 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO9-AS1]] (+0.64, fdr 1e-05), [[DENND2A]] (+0.62, fdr 1e-05), [[AK5]] (+0.61, fdr 1e-05); moves opposite to [[ALAD]] (-0.51, fdr 5e-05), [[FRRS1]] (-0.50, fdr 5e-05), [[ORC4]] (-0.49, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[PXDC1]] → it (grade B ⚠); 19 go from it, the strongest it → [[TTC7B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +16.1 | 0e+00 | 12/26 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +9.0 | 9e-17 | 11/26 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.2 | 1e-10 | 2/17 (A-427, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.0 | 3e-10 | 3/22 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.5 | 6e-04 | 11/26 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +4.4 | 9e-04 | 7/26 (H4, HOP62, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 8/26 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.0 | 0.005 | 3/20 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.014 | 5/26 (A549, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.044 | 7/25 (A-172, A-427, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.063 | 3/26 (SNU-423, AN3 CA, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.067 | 13/25 (SK-MEL-2, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.485×** | -11.4 | 2e-27 | 22/26 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.596×** | -7.8 | 1e-12 | 21/25 (LOX-IMVI, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -6.7 | 4e-09 | 21/26 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.688×** | -5.9 | 6e-07 | 16/26 (A-427, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.712×** | -5.3 | 1e-05 | 14/24 (LoVo, NCI-H1792, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -5.3 | 1e-05 | 16/25 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.740×** | -4.7 | 2e-04 | 22/26 (LoVo, J82, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -4.6 | 3e-04 | 21/25 (LoVo, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -4.4 | 6e-04 | 19/26 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.795×** | -3.6 | 0.016 | 18/26 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.795×** | -3.6 | 0.016 | 13/25 (A-427, LoVo, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.851× | -3.6 | 0.016 | 6/26 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.043 | 0/26 | rises with dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.819×** | -3.1 | 0.071 | 4/26 (NCI-H661, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.0 | 1 | 13 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.0874× (z -23.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.135× (z -19.4) |
| [[J82 (line)]] | alt | 258 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0649× (z -16.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0708× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 86.7 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -13.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.132× (z -12.8) |
| [[H4 (line)]] | wt | 65.6 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0700× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 19.5 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +13.2) | [[Harringtonine (drug)]] 0.5 µM 0.205× (z -11.5) |
| [[A-427 (line)]] | wt | 38.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.192× (z -12.4) |
| [[HOP62 (line)]] | alt | 43.5 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.179× (z -11.5) |
| [[HS-578T (line)]] | alt | 82.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.135× (z -12.5) |
| [[PANC-1 (line)]] | alt | 42.6 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 89.2 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.207× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 41.6 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -14.5) |
| [[SNU-423 (line)]] | alt | 75.6 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -16.1) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.128× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.233× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 12.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +11.3) | — |
| [[A549 (line)]] | wt | 7.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.93× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.179× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 88.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 94.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0464× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.89 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9-AS1]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[DENND2A]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[AK5]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[FLI1]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[COL27A1]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[TSHZ3-AS1]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GBX2-AS1]] | +0.57 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[LINC00702]] | +0.56 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[BNC1]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SAMD3]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[FRRS1]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ORC4]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PRSS16]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RHOXF1]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ACACB]] | -0.47 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[FHIP1A]] | -0.47 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[TMEM14A]] | -0.47 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[DMXL2]] | -0.46 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SLC25A40]] | -0.46 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ARHGAP12]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SLC11A2]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 2, C 21. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXDC1]] | B | PXDC1 activity raises WNT5B's level | lines that do not express PXDC1 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without PXDC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TSPAN4, OSMR, VIM |
| [[ARHGAP31]] | B | ARHGAP31 activity raises WNT5B's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without ARHGAP31 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[DENND2A]] | C | DENND2A activity raises WNT5B's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 3.40× lower at baseline in the lines without DENND2A | 0.004 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises WNT5B's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.62× lower at baseline in the lines without EVC2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[MSRB3]] | C | MSRB3 activity raises WNT5B's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 3.58× lower at baseline in the lines without MSRB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises WNT5B's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 4.96× lower at baseline in the lines without TENM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises WNT5B's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.60× lower at baseline in the lines without ADAMTS6 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises WNT5B's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.55× lower at baseline in the lines without HS3ST3A1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises WNT5B's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 4.77× lower at baseline in the lines without PAPPA | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[MRC2]] | C | MRC2 activity raises WNT5B's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without MRC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1; co-absent with the target |
| [[NTM]] | C | NTM activity raises WNT5B's level | lines that do not express NTM (33) vs lines expressing it (17) | 3.93× lower at baseline in the lines without NTM | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[FBN2]] | C | FBN2 activity raises WNT5B's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 3.87× lower at baseline in the lines without FBN2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 9, C 10. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC7B]] | B | WNT5B activity raises TTC7B's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 3.66× lower at baseline in the lines without WNT5B | 7e-04 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[ST3GAL3]] | B | WNT5B activity raises ST3GAL3's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without WNT5B | 0.008 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[POU6F1]] | B | WNT5B activity raises POU6F1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without WNT5B | 0.020 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[FLACC1]] | B | WNT5B activity raises FLACC1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 1.50× lower at baseline in the lines without WNT5B | 0.048 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[TTC7B]] | B | WNT5B activity strengthens TTC7B's drug response | lines that do not express WNT5B (13) vs lines expressing it (26) | the lines without WNT5B respond 0.40× as strongly (z diff +3.67); strongest at Panobinostat 5 µM: 0.84x vs 0.43x (z diff +5.5) | 0.049 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; target measured in part of the lines; artifact flags |
| [[PRPSAP1]] | B | WNT5B activity raises PRPSAP1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without WNT5B | 0.051 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[COL27A1]] | B | WNT5B activity raises COL27A1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without WNT5B | 0.054 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[SCHIP1]] | B | WNT5B activity raises SCHIP1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without WNT5B | 0.064 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[FHIP1A]] | B | WNT5B activity lowers FHIP1A's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.14× higher at baseline in the lines without WNT5B | 0.081 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[MSRB3]] | C | WNT5B activity raises MSRB3's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 4.66× lower at baseline in the lines without WNT5B | 0.004 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |
| [[MRC2]] | C | WNT5B activity raises MRC2's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 5.47× lower at baseline in the lines without WNT5B | 0.013 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |
| [[MIR137HG]] | C | WNT5B activity raises MIR137HG's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 4.24× lower at baseline in the lines without WNT5B | 0.037 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.6, 15.3); signed map (25.1, 49.1). **Vector** length 85.9, 23.6% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +4.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.9 | -7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | +1.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:1,529,891-1,647,212 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Wnt family |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 4 pathways, smallest: WNT ligand biogenesis and trafficking; PCP/CE pathway; Beta-catenin independent WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1J7](https://www.uniprot.org/uniprotkb/Q9H1J7) (Protein Wnt-5b):

> Ligand for members of the frizzled family of seven transmembrane receptors. Probable developmental protein. May be a signaling molecule which affects the development of discrete regions of tissues. Is likely to signal over only few cell diameters (By similarity).

**Summary**, from NCBI Gene [81029](https://www.ncbi.nlm.nih.gov/gene/81029):

> The WNT gene family consists of structurally related genes which encode secreted signaling proteins. These proteins have been implicated in oncogenesis and in several developmental processes, including regulation of cell fate and patterning during embryogenesis. This gene is a member of the WNT gene family. It encodes a protein which shows 94% and 80% amino acid identity to the mouse Wnt5b protein and the human WNT5A protein, respectively. Alternative splicing of this gene generates 2 …

**Accessions** — [HGNC:16265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16265) · Entrez [81029](https://www.ncbi.nlm.nih.gov/gene/81029) · UniProt [Q9H1J7](https://www.uniprot.org/uniprotkb/Q9H1J7) · Ensembl [ENSG00000111186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111186)

## Data

Gene col 3197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3197); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3197]; `tensor/DDL_lfc|DDL_z.npy` [3197]; `embed/gene_vectors.npy` [3197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3197 or target_col == 3197). Every well: [[WNT5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
