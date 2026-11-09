---
symbol: "CCNK"
type: "gene"
col: 1611
ensembl_id: "ENSG00000090061"
name: "cyclin K"
location: "14q32.2"
module: 41
arm: "+"
pooled_cpm: 117.03
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CCNK

*cyclin K* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.65× (z +12.4, q 2e-32, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.778× (z -6.5, q 5e-08, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNIP1]] (+0.63, fdr 1e-05), [[NDEL1]] (+0.63, fdr 1e-05), [[TOX4]] (+0.61, fdr 1e-05); moves opposite to [[DNAH14]] (-0.54, fdr 3e-05), [[ADGRA3]] (-0.52, fdr 5e-05), [[SLC25A13]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[XAB2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.65×** | +12.4 | 2e-32 | 48/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +11.5 | 5e-28 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +10.8 | 7e-25 | 46/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +10.2 | 3e-22 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +8.6 | 1e-15 | 40/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +8.3 | 8e-15 | 43/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +8.2 | 2e-14 | 45/48 (HT-29, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +7.9 | 2e-13 | 41/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.4 | 1e-11 | 32/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +6.9 | 4e-10 | 40/48 (HT-29, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 4e-09 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.40×** | +6.2 | 3e-08 | 34/48 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.38×** | +5.9 | 2e-07 | 35/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.6 | 7e-07 | 40/45 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +5.6 | 7e-07 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 4e-05 | 37/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.778×** | -6.5 | 5e-08 | 34/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -4.8 | 5e-04 | 30/49 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.815×** | -3.7 | 0.036 | 27/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.815×** | -3.6 | 0.047 | 22/47 (NCI-H1573, A498, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.821×** | -3.4 | 0.063 | 21/44 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **0.830×** | -3.4 | 0.063 | 19/49 (J82, HS-578T, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.834× | -3.3 | 0.066 | 21/48 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.834× | -3.3 | 0.066 | 19/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | 0.837× | -3.3 | 0.072 | 19/48 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.840× | -3.2 | 0.082 | 22/49 (NCI-H2347, Panc 03.27, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.845× | -3.1 | 0.11 | 17/48 (SNU-1, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.6 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 74.9 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +15.9) | — |
| [[SW480 (line)]] | alt | 128 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 84.5 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 88.5 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 214 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[KATO III (line)]] | alt | 123 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 101 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 95.2 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 8.61× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.524× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 166 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 125 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.69× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.8) | — |
| [[C32 (line)]] | wt | 82.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 129 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.15× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 133 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +8.7) | [[Docetaxel (drug)]] 0.05 µM 0.414× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 131 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 189 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 106 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 78.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[RKO (line)]] | wt | 126 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 84.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 120 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 172 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 150 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.4) | — |
| [[A-172 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNIP1]] | +0.63 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[NDEL1]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TOX4]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[XAB2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.60 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[CYB561D2]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SPTY2D1]] | +0.58 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CLK3]] | +0.58 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[AP1G1]] | +0.58 | +0.66 / +0.56 | both halves | 1e-05 | pathway: HIV Infection |
| [[OSBPL2]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PSMC4]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 | pathway: HIV Infection |
| [[TMEM208]] | +0.56 | +0.64 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH14]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[ADGRA3]] | -0.52 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A13]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[CLN6]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[GCFC2]] | -0.51 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[E2F5]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 | pathway: Affinity selection of immunoglobulins |
| [[USP25]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CHN1]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SLC35F2]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[PAXIP1]] | -0.50 | -0.59 / -0.45 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[GPR63]] | -0.48 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[MYEF2]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XAB2]] | C | XAB2's natural level weakens CCNK's drug response | XAB2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.28; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.4, -36.1); signed map (-48.2, 17.5). **Vector** length 87.6, 27.8% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +7.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.1 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +4.0 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.9 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.6 | -0.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.2 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.7 | +4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.3 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | +11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,481,169-99,535,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CPR4 |
| Gene groups (HGNC) | Cyclins; P-TEFb complex subunits |
| Hallmark sets | P53_PATHWAY |
| Reactome | 22 pathways, smallest: HIV elongation arrest and recovery; Pausing and recovery of HIV elongation; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [O75909](https://www.uniprot.org/uniprotkb/O75909) (Cyclin-K):

> Regulatory subunit of cyclin-dependent kinases that mediates activation of target kinases. Plays a role in transcriptional regulation via its role in regulating the phosphorylation of the C-terminal domain (CTD) of the large subunit of RNA polymerase II (POLR2A).

**Summary**, from NCBI Gene [8812](https://www.ncbi.nlm.nih.gov/gene/8812):

> The protein encoded by this gene is a member of the transcription cyclin family. These cyclins may regulate transcription through their association with and activation of cyclin-dependent kinases (CDK) that phosphorylate the C-terminal domain (CTD) of the large subunit of RNA polymerase II. This gene product may play a dual role in regulating CDK and RNA polymerase II activities. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1596) · Entrez [8812](https://www.ncbi.nlm.nih.gov/gene/8812) · UniProt [O75909](https://www.uniprot.org/uniprotkb/O75909) · Ensembl [ENSG00000090061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090061)

## Data

Gene col 1611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1611); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1611]; `tensor/DDL_lfc|DDL_z.npy` [1611]; `embed/gene_vectors.npy` [1611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1611 or target_col == 1611). Every well: [[CCNK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
