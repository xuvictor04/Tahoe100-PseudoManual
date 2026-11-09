---
symbol: "TAF5L"
type: "gene"
col: 5758
ensembl_id: "ENSG00000135801"
name: "TATA-box binding protein associated factor 5 like"
location: "1q42.13"
module: 77
arm: "+"
pooled_cpm: 33.27
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TAF5L

*TATA-box binding protein associated factor 5 like* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.78× (z +11.4, q 2e-27, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 7.55×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -17.1, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFOD2]] (+0.79, fdr 7e-06), [[MTMR12]] (+0.74, fdr 9e-06), [[POMGNT2]] (+0.74, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.77, fdr 1e-05), [[C11orf58]] (-0.73, fdr 1e-05), [[PLA2G4C]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5758.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 7.55×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +11.4 | 2e-27 | 37/48 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +9.2 | 8e-18 | 32/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.7 | 5e-04 | 12/34 (PANC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +3.2 | 0.20 | 14/48 (NCI-H2030, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -17.1 | 0e+00 | 40/47 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -14.9 | 0e+00 | 40/48 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -12.9 | 5e-36 | 26/37 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -12.4 | 4e-33 | 30/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.580×** | -11.6 | 5e-29 | 37/44 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -9.9 | 6e-21 | 36/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -9.0 | 1e-17 | 31/48 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.654×** | -8.3 | 5e-15 | 27/41 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -8.1 | 3e-14 | 31/47 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -7.8 | 4e-13 | 28/47 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.807×** | -6.4 | 8e-09 | 23/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -6.1 | 4e-08 | 26/48 (HOP62, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -6.0 | 1e-07 | 21/48 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.779×** | -5.3 | 5e-06 | 19/48 (KATO III, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.2 | 9e-06 | 2/48 (CHP-212, SW 1088) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -4.4 | 3e-04 | 17/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.836× | -3.6 | 0.008 | 15/47 (A-172, AsPC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.889× | -3.4 | 0.019 | 10/48 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.0) |
| [[A-172 (line)]] | wt | 38.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.6) |
| [[A498 (line)]] | wt | 39.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.8) |
| [[HS-578T (line)]] | alt | 31.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 49.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 46.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -18.4) |
| [[J82 (line)]] | alt | 37.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.4) |
| [[RKO (line)]] | wt | 39.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -12.7) |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.308× (z -10.4) |
| [[C32 (line)]] | wt | 28.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -15.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.356× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0424× (z -26.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 30.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -8.6) |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -15.5) |
| [[H4 (line)]] | wt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 27.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.8) |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0931× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -9.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.55× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.3) |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -8.6) |
| [[A549 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFOD2]] | +0.79 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MTMR12]] | +0.74 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[POMGNT2]] | +0.74 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[ELP1]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[IQCB1]] | +0.73 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.70 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[TRIM35]] | +0.70 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[SHQ1]] | +0.69 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GTPBP3]] | +0.68 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[BRAT1]] | +0.68 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ESS2]] | +0.68 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MMS19]] | +0.68 | +0.69 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.77 | -0.78 / -0.57 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.73 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[PLA2G4C]] | -0.73 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | -0.72 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[TSGA10]] | -0.71 | -0.73 / -0.51 | both halves | 1e-05 |  |
| [[TIA1]] | -0.70 | -0.76 / -0.50 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.68 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[CCDC90B-AS1]] | -0.67 | -0.74 / -0.30 | both halves | 2e-04 |  |
| [[PATL2]] | -0.67 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[OCIAD1]] | -0.67 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[SGO1-AS1]] | -0.66 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[ARRDC3-AS1]] | -0.66 | -0.63 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TAF5L's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WARS2-AS1]] | C | WARS2-AS1 activity lowers TAF5L's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.43× higher at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.6, 0.0); signed map (-39.9, -12.1). **Vector** length 101, 23.8% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +6.1 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +11.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -17.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:229,593,134-229,626,122 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAF65B |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75529](https://www.uniprot.org/uniprotkb/O75529) (TAF5-like RNA polymerase II p300/CBP-associated factor-associated factor 65 kDa subunit 5L):

> Functions as a component of the PCAF complex. The PCAF complex is capable of efficiently acetylating histones in a nucleosomal context. The PCAF complex could be considered as the human version of the yeast SAGA complex (Probable). With TAF6L, acts as an epigenetic regulator essential for somatic reprogramming. Regulates target genes through H3K9ac deposition and MYC recruitment which trigger MYC regulatory network to orchestrate gene expression programs to control embryonic stem cell state (By …

**Summary**, from NCBI Gene [27097](https://www.ncbi.nlm.nih.gov/gene/27097):

> The product of this gene belongs to the WD-repeat TAF5 family of proteins. This gene encodes a protein that is a component of the PCAF histone acetylase complex. The PCAF histone acetylase complex, which is composed of more than 20 polypeptides some of which are TAFs, is required for myogenic transcription and differentiation. TAFs may participate in basal transcription, serve as coactivators, function in promoter recognition or modify general transcription factors to facilitate complex …

**Accessions** — [HGNC:17304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17304) · Entrez [27097](https://www.ncbi.nlm.nih.gov/gene/27097) · UniProt [O75529](https://www.uniprot.org/uniprotkb/O75529) · Ensembl [ENSG00000135801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135801)

## Data

Gene col 5758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5758); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5758]; `tensor/DDL_lfc|DDL_z.npy` [5758]; `embed/gene_vectors.npy` [5758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5758 or target_col == 5758). Every well: [[TAF5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
