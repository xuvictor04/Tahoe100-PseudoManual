---
symbol: "LYPD6"
type: "gene"
col: 11891
ensembl_id: "ENSG00000187123"
name: "LY6/PLAUR domain containing 6"
location: "2q23.2"
module: 6
arm: "+"
pooled_cpm: 11.59
n_lines_expressing: 35
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# LYPD6

*LY6/PLAUR domain containing 6* — 2q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.06× (z +10.9, q 5e-25, up in 29 of 33 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 2.95× (z +10.6, q 1e-23, up in 32 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -12.6, q 2e-33, down in 26 of 32 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.356× (z -10.1, q 2e-21, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP1]] (+0.71, fdr 7e-06), [[CDC7]] (+0.69, fdr 7e-06), [[WDR76]] (+0.67, fdr 7e-06); moves opposite to [[ZNF490]] (-0.60, fdr 4e-05), [[ATP6V1G1]] (-0.55, fdr 5e-05), [[CCDC59]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZNF490]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **3.06×** | +10.9 | 5e-25 | 29/33 (A498, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.95×** | +10.6 | 1e-23 | 32/33 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.78×** | +10.0 | 4e-21 | 27/32 (HOP62, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.53×** | +9.1 | 2e-17 | 26/32 (HT-29, NCI-H1792, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +8.8 | 2e-16 | 27/33 (SW480, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.07×** | +7.1 | 1e-10 | 23/32 (HEC-1-A, SW1417, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **3.71×** | +6.7 | 2e-09 | 26/33 (NCI-H460, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +6.4 | 8e-09 | 20/30 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +5.7 | 7e-07 | 20/30 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.42×** | +3.3 | 0.061 | 7/27 (HOP62, A-172, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.401×** | -12.6 | 2e-33 | 26/32 (SW48, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.356×** | -10.1 | 2e-21 | 27/33 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.360×** | -9.6 | 2e-19 | 23/31 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.441×** | -8.0 | 2e-13 | 22/31 (C-33 A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.442×** | -8.0 | 2e-13 | 20/32 (SW48, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -7.2 | 7e-11 | 22/31 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.641×** | -6.1 | 8e-08 | 25/33 (AN3 CA, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.571×** | -5.5 | 3e-06 | 17/32 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.571×** | -5.5 | 3e-06 | 19/31 (A-427, RKO, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -5.2 | 1e-05 | 17/32 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -5.2 | 1e-05 | 19/31 (LS 180, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.581×** | -5.0 | 3e-05 | 17/31 (SW48, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -4.8 | 8e-05 | 18/32 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -4.7 | 1e-04 | 18/31 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -4.0 | 0.002 | 14/31 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.683×** | -3.7 | 0.007 | 14/33 (A-172, AN3 CA, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.507×** | -3.5 | 0.017 | 9/25 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.810×** | -2.9 | 0.100 | 4/33 (BT-474, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.91 per unit of S-phase module lfc, -0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 22.1 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0696× (z -15.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.170× (z -10.9) |
| [[LoVo (line)]] | wt | 17.1 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0648× (z -16.3) |
| [[AN3 CA (line)]] | alt | 131 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.107× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -17.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.142× (z -11.9) |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0271× (z -17.8) |
| [[SW48 (line)]] | wt | 23.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0384× (z -19.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0555× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -11.9) |
| [[RKO (line)]] | wt | 20.2 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0477× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0868× (z -11.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.119× (z -9.6) |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0481× (z -12.6) |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0794× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.128× (z -8.5) |
| [[SW480 (line)]] | alt | 5.94 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0486× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -10.7) |
| [[A498 (line)]] | wt | 6.05 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 7.06 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0509× (z -8.6) |
| [[Hs 766T (line)]] | wt | 7.37 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0760× (z -9.2) |
| [[KATO III (line)]] | alt | 6.95 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.103× (z -8.5) |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0631× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP1]] | +0.71 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CDC7]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[WDR76]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FANCA]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MMS22L]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[DSCC1]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[FANCB]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[EXO1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[BLM]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[UHRF1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | -0.60 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ATP6V1G1]] | -0.55 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CCDC59]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[METTL6]] | -0.54 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[CHMP4A]] | -0.54 | -0.39 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers LYPD6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers LYPD6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PODXL2]] | B | PODXL2 activity raises LYPD6's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without PODXL2 | 0.085 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF490]] | B | LYPD6 activity raises ZNF490's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.26× lower at baseline in the lines without LYPD6 | 0.049 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[SYTL4]] | B | LYPD6 activity raises SYTL4's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without LYPD6 | 0.053 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[C9orf85]] | B | LYPD6 activity raises C9orf85's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without LYPD6 | 0.069 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[DDX11-AS1]] | B | LYPD6 activity raises DDX11-AS1's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without LYPD6 | 0.071 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[DDX12P]] | B | LYPD6 activity raises DDX12P's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.75× lower at baseline in the lines without LYPD6 | 0.091 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[STXBP6]] | B | LYPD6 activity raises STXBP6's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 2.69× lower at baseline in the lines without LYPD6 | 0.092 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.7, -44.1); signed map (-36.6, -44.0). **Vector** length 83.0, 20.9% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.52 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.51 to 22); *Mitotic G1 phase and G1/S transition* (reactome, mean cos +0.52 to 34).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.9 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.7 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -9.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -3.2 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.0 | -12.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | LY6/PLAUR domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.2 — chr2:149,329,985-149,474,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC52057 |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y78](https://www.uniprot.org/uniprotkb/Q86Y78) (Ly6/PLAUR domain-containing protein 6):

> Acts as a modulator of nicotinic acetylcholine receptors (nAChRs) function in the brain. Inhibits nicotine-induced Ca(2+) influx through nAChRs. In vitro, specifically inhibits alpha-3:beta-4 and alpha-7 nAChR currents in an allosteric manner. Acts as a positive regulator of Wnt/beta-catenin signaling (By similarity).

**Summary**, from NCBI Gene [130574](https://www.ncbi.nlm.nih.gov/gene/130574):

> Members of the LY6 protein family (see SLURP1; MIM 606119), such as LYPD6, have at least one 80-amino acid LU domain that contains 10 conserved cysteines with a defined disulfide-bonding pattern (Zhang et al., 2010 [PubMed 19653121]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:28751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28751) · Entrez [130574](https://www.ncbi.nlm.nih.gov/gene/130574) · UniProt [Q86Y78](https://www.uniprot.org/uniprotkb/Q86Y78) · Ensembl [ENSG00000187123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187123)

## Data

Gene col 11891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11891); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11891]; `tensor/DDL_lfc|DDL_z.npy` [11891]; `embed/gene_vectors.npy` [11891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11891 or target_col == 11891). Every well: [[LYPD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
