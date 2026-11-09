---
symbol: "FAM227A"
type: "gene"
col: 11595
ensembl_id: "ENSG00000184949"
name: "family with sequence similarity 227 member A"
location: "22q13.1"
module: 106
arm: "+"
pooled_cpm: 8.57
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# FAM227A

*family with sequence similarity 227 member A* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.75× (z +16.2, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.541× (z -7.5, q 3e-11, down in 25 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.550× (z -7.3, q 6e-11, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB8]] (+0.57, fdr 1e-05), [[PSMC4]] (+0.53, fdr 3e-05), [[ULK4]] (+0.52, fdr 2e-05); moves opposite to [[C3]] (-0.53, fdr 2e-04), [[BIRC3]] (-0.52, fdr 2e-04), [[MT1M]] (-0.49, fdr 3e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ETS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.75×** | +16.2 | 0e+00 | 42/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +15.3 | 0e+00 | 40/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.19×** | +14.2 | 1e-43 | 38/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.00×** | +13.5 | 3e-39 | 39/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.09×** | +9.0 | 2e-17 | 34/44 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +9.0 | 3e-17 | 31/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +8.8 | 1e-16 | 27/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.22×** | +7.5 | 4e-12 | 31/46 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.0 | 1e-10 | 8/12 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +7.0 | 2e-10 | 12/23 (NCI-H2347, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +6.7 | 1e-09 | 24/46 (HOP62, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +5.3 | 5e-06 | 19/42 (LoVo, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.2 | 9e-06 | 18/44 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.9 | 4e-05 | 15/33 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 12/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.004 | 9/46 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.028 | 10/45 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.086 | 5/45 (A549, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -7.5 | 3e-11 | 25/43 (SHP-77, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -7.3 | 6e-11 | 26/46 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.575×** | -6.8 | 2e-09 | 23/45 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -6.5 | 9e-09 | 22/45 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.638×** | -5.5 | 4e-06 | 24/46 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -4.8 | 2e-04 | 18/42 (NCI-H2030, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -4.4 | 1e-03 | 19/45 (NCI-H1573, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.702×** | -4.3 | 0.001 | 11/46 (NCI-H2030, LoVo, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.560×** | -3.7 | 0.013 | 11/41 (LS 180, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.809×** | -3.7 | 0.014 | 18/47 (RPMI-7951, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.037 | 13/45 (A498, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.28 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.2) | [[Digitoxin (drug)]] 0.05 µM 0.113× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.126× (z -11.5) |
| [[SW480 (line)]] | alt | 7.48 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +12.2) | — |
| [[A498 (line)]] | wt | 17.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.194× (z -10.7) |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.2) |
| [[J82 (line)]] | alt | 8.33 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 9.36 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.119× (z -10.5) |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.120× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 6.10 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.23× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 6.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.15× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0641× (z -10.4) |
| [[PANC-1 (line)]] | alt | 7.77 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +8.5) | — |
| [[RKO (line)]] | wt | 9.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB8]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PSMC4]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ULK4]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[VPS53]] | +0.50 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[VCP]] | +0.49 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[FBXO36]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[DCDC1]] | +0.48 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[CCDC40]] | +0.46 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[MOK]] | +0.45 | +0.47 / +0.40 | both halves | 4e-05 |  |
| [[IQCK]] | +0.45 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[GLYR1]] | +0.45 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[NPLOC4]] | +0.45 | +0.32 / +0.47 | both halves | 2e-04 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3]] | -0.53 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[BIRC3]] | -0.52 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[MT1M]] | -0.49 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[ARHGAP40]] | -0.48 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[EPS8]] | -0.47 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[WDR75]] | -0.47 | -0.18 / -0.42 | ⚠ not reproduced | 9e-04 |  |
| [[CSF3]] | -0.46 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[PELI1]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[CEBPB]] | -0.46 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[MIR4527HG]] | -0.45 | -0.29 / -0.34 | both halves | 2e-04 |  |
| [[EBI3]] | -0.45 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[TLR2]] | -0.45 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[SGPP2]] | -0.44 | -0.23 / -0.40 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS2]] | B | ETS2 activity lowers FAM227A's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.69× higher at baseline in the lines without ETS2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[KLF5]] | B | KLF5 activity lowers FAM227A's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.45× higher at baseline in the lines without KLF5 | 0.017 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FAM227A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRAMD2B]] | B | GRAMD2B activity lowers FAM227A's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 1.50× higher at baseline in the lines without GRAMD2B | 0.032 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[SGPP2]] | B | SGPP2 activity lowers FAM227A's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 1.50× higher at baseline in the lines without SGPP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[CCL20]] | B | CCL20 activity lowers FAM227A's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.48× higher at baseline in the lines without CCL20 | 0.035 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TXNIP]] | B | TXNIP activity lowers FAM227A's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.77× higher at baseline in the lines without TXNIP | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[IRS2]] | B | IRS2 activity lowers FAM227A's level | lines that do not express IRS2 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without IRS2 | 0.088 | ⚠ within organs, on part of the lines; also absent: MAP3K5 |
| [[SPATA17]] | C | SPATA17 activity raises FAM227A's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction -0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 37.5); signed map (-28.7, -27.7). **Vector** length 65.0, 11.0% of its response variance represented; |z| ≥ 3 in 1,191 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.8 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +15.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +0.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.1 | +1.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.7 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 227 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,578,118-38,656,629 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [F5H4B4](https://www.uniprot.org/uniprotkb/F5H4B4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44197) · Entrez [646851](https://www.ncbi.nlm.nih.gov/gene/646851) · UniProt [F5H4B4](https://www.uniprot.org/uniprotkb/F5H4B4) · Ensembl [ENSG00000184949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184949)

## Data

Gene col 11595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11595); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11595]; `tensor/DDL_lfc|DDL_z.npy` [11595]; `embed/gene_vectors.npy` [11595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11595 or target_col == 11595). Every well: [[FAM227A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM227A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
