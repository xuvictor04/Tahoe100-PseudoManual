---
symbol: "DOCK3"
type: "gene"
col: 1536
ensembl_id: "ENSG00000088538"
name: "dedicator of cytokinesis 3"
location: "3p21.2"
module: 102
arm: "+"
pooled_cpm: 59.51
n_lines_expressing: 28
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# DOCK3

*dedicator of cytokinesis 3* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.91× (z +28.6, q 0e+00, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.811× (z -4.0, q 0.043, down in 10 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C-33 A 0.165×, NCI-H23 0.147×, AN3 CA 0.0957×, SK-MEL-2 0.225×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (C-33 A 0.428×, NCI-H2030 0.405×, SK-MEL-2 0.415×, HEC-1-A 0.489×); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.155×, A-427 0.165×, NCI-H23 0.249×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW 1271 0.129×, AN3 CA 0.299×, NCI-H2030 0.564×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SK-MEL-2 0.242×, AN3 CA 0.200×, C-33 A 0.441×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRID1]] (+0.63, fdr 1e-05), [[ERC2]] (+0.60, fdr 2e-05), [[RETREG1]] (+0.60, fdr 1e-05); moves opposite to [[SLC25A14]] (-0.54, fdr 2e-05), [[SENP2]] (-0.45, fdr 5e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RASGEF1A]] → it (grade B ⚠); 10 go from it, the strongest it → [[CHN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.91×** | +28.6 | 0e+00 | 23/26 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.83×** | +19.7 | 0e+00 | 22/26 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +16.5 | 0e+00 | 17/25 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +13.9 | 7e-42 | 15/26 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +13.7 | 1e-40 | 10/26 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +12.5 | 1e-33 | 10/26 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +11.9 | 1e-30 | 6/27 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +9.9 | 3e-21 | 9/26 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.4 | 3e-15 | 6/22 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +8.1 | 5e-14 | 9/26 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +7.4 | 8e-12 | 5/26 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.0 | 1e-10 | 9/25 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.1 | 6e-08 | 11/25 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.8 | 3e-07 | 12/27 (NCI-H460, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.7 | 4e-07 | 5/23 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +5.6 | 7e-07 | 20/25 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +5.4 | 2e-06 | 12/26 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.3 | 3e-06 | 10/27 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (C-33 A 0.165×, NCI-H23 0.147×, AN3 CA 0.0957×, SK-MEL-2 0.225×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (C-33 A 0.428×, NCI-H2030 0.405×, SK-MEL-2 0.415×, HEC-1-A 0.489×); [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.155×, A-427 0.165×, NCI-H23 0.249×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SW 1271 0.129×, AN3 CA 0.299×, NCI-H2030 0.564×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SK-MEL-2 0.242×, AN3 CA 0.200×, C-33 A 0.441×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -4.0 | 0.043 | 10/25 (C-33 A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.7 | 0.055 | 1/27 (NCI-H1792) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.825×** | -3.6 | 0.055 | 11/25 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.832×** | -3.5 | 0.076 | 13/25 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.841× | -3.3 | 0.13 | 11/26 (NCI-H2030, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.5 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +19.8) | — |
| [[C-33 A (line)]] | alt | 546 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -20.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.1) |
| [[SNU-1 (line)]] | wt | 436 | 2 (1 ⚠) | 6 (5 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.02× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.416× (z -12.5) |
| [[AN3 CA (line)]] | alt | 371 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0957× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.6) |
| [[A549 (line)]] | wt | 25.3 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 3.40× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 232 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.75× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 255 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -23.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 192 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.82× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -14.0) |
| [[SW480 (line)]] | alt | 68.7 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.43× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 294 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -20.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.97× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +9.2) | — |
| [[LoVo (line)]] | wt | 17.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +19.1) | — |
| [[NCI-H1573 (line)]] | alt | 43.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.14× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 18.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.85× (z +11.4) | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0505× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.2) |
| [[SW48 (line)]] | wt | 31.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +9.5) | [[Naproxen (drug)]] 0.05 µM 0.0941× (z -9.2) |
| [[A-172 (line)]] | wt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -13.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.22× (z +8.6) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 102 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.7) | — |
| [[A498 (line)]] | wt | 8.86 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.95 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRID1]] | +0.63 | +0.56 / +0.75 | both halves | 1e-05 | same gene group |
| [[ERC2]] | +0.60 | +0.47 / +0.67 | both halves | 2e-05 | same gene group; STRING 464 |
| [[RETREG1]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ADAM23]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ANKS1B]] | +0.56 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ADCY1]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SNTG2]] | +0.56 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[CECR2]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[EBF4]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PHF21B]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LINC01203]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[ZNF536]] | +0.53 | +0.40 / +0.62 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A14]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SENP2]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1A]] | B | RASGEF1A activity raises DOCK3's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without RASGEF1A | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[FAM184A]] | B | FAM184A activity raises DOCK3's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.60× lower at baseline in the lines without FAM184A | 0.052 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[GRID1]] | B | GRID1 activity raises DOCK3's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without GRID1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[RIMS2]] | C | RIMS2 activity raises DOCK3's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without RIMS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHN1]] | B | DOCK3 activity raises CHN1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 3.20× lower at baseline in the lines without DOCK3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[DTNB]] | B | DOCK3 activity raises DTNB's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without DOCK3 | 0.043 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[FAM184A]] | B | DOCK3 activity raises FAM184A's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without DOCK3 | 0.051 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[OSBP2]] | B | DOCK3 activity raises OSBP2's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without DOCK3 | 0.055 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[SUGCT]] | B | DOCK3 activity raises SUGCT's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without DOCK3 | 0.061 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[GKAP1]] | B | DOCK3 activity raises GKAP1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without DOCK3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[ANKS1B]] | B | DOCK3 activity raises ANKS1B's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without DOCK3 | 0.072 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[TTC7B]] | B | DOCK3 activity raises TTC7B's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.45× lower at baseline in the lines without DOCK3 | 0.074 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[REEP1]] | B | DOCK3 activity raises REEP1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without DOCK3 | 0.098 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[ADCY1]] | C | DOCK3 activity raises ADCY1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 4.09× lower at baseline in the lines without DOCK3 | 0.094 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.5, 36.3); signed map (27.2, 24.3). **Vector** length 83.4, 22.0% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +28.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +19.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +7.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.5 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.0 | -3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.9 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.7 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | dedicator of cytokinesis 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:50,674,927-51,384,198 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0299, MOCA, PBP |
| Gene groups (HGNC) | Armadillo like helical domain containing; DOCK family Rho GEFs; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 13 pathways, smallest: NTRK2 activates RAC1; Activated NTRK2 signals through FYN; Signaling by NTRK2 (TRKB) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZD9](https://www.uniprot.org/uniprotkb/Q8IZD9) (Dedicator of cytokinesis protein 3):

> Potential guanine nucleotide exchange factor (GEF). GEF proteins activate some small GTPases by exchanging bound GDP for free GTP. Its interaction with presenilin proteins as well as its ability to stimulate Tau/MAPT phosphorylation suggest that it may be involved in Alzheimer disease. Ectopic expression in nerve cells decreases the secretion of amyloid-beta APBA1 protein and lowers the rate of cell-substratum adhesion, suggesting that it may affect the function of some small GTPase involved in …

**Summary**, from NCBI Gene [1795](https://www.ncbi.nlm.nih.gov/gene/1795):

> This gene is specifically expressed in the central nervous system (CNS). It encodes a member of the DOCK (dedicator of cytokinesis) family of guanine nucleotide exchange factors (GEFs). This protein, dedicator of cytokinesis 3 (DOCK3), is also known as modifier of cell adhesion (MOCA) and presenilin-binding protein (PBP). The DOCK3 and DOCK1, -2 and -4 share several conserved amino acids in their DHR-2 (DOCK homology region 2) domains that are required for GEF activity, and bind directly to …

**Accessions** — [HGNC:2989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2989) · Entrez [1795](https://www.ncbi.nlm.nih.gov/gene/1795) · UniProt [Q8IZD9](https://www.uniprot.org/uniprotkb/Q8IZD9) · Ensembl [ENSG00000088538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088538)

## Data

Gene col 1536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1536); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1536]; `tensor/DDL_lfc|DDL_z.npy` [1536]; `embed/gene_vectors.npy` [1536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1536 or target_col == 1536). Every well: [[DOCK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOCK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
