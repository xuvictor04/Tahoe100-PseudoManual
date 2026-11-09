---
symbol: "NCOA4"
type: "gene"
col: 15490
ensembl_id: "ENSG00000266412"
name: "nuclear receptor coactivator 4"
location: "10q11.22"
module: 3
arm: "-"
pooled_cpm: 47.85
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# NCOA4

*nuclear receptor coactivator 4* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +21.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 0.746× (z -3.8, q 0.083, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Isocorydine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.236×); [[Amsacrine (drug)]] 5 µM in 1 line (CHP-212 0.243×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.405×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SNU-1 0.228×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFL2]] (+0.75, fdr 7e-06), [[EIF4G2]] (+0.72, fdr 1e-05), [[IL6ST]] (+0.70, fdr 7e-06); moves opposite to [[UQCRH]] (-0.66, fdr 7e-06), [[TOMM5]] (-0.65, fdr 1e-05), [[MNX1]] (-0.63, fdr 5e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +21.1 | 0e+00 | 46/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.50×** | +16.5 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +14.5 | 3e-45 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +12.7 | 1e-34 | 45/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +11.7 | 9e-30 | 38/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +11.0 | 4e-26 | 43/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.3 | 6e-23 | 29/38 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +8.8 | 1e-16 | 27/42 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.5 | 8e-16 | 33/48 (A-172, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +7.8 | 3e-13 | 37/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +7.2 | 4e-11 | 32/49 (LoVo, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +7.1 | 7e-11 | 40/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.7 | 8e-10 | 38/48 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.9 | 1e-07 | 28/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 28/49 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.3 | 5e-06 | 27/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.1 | 1e-05 | 26/48 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.7 | 8e-05 | 25/47 (A498, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15490.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Isocorydine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.236×); [[Amsacrine (drug)]] 5 µM in 1 line (CHP-212 0.243×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.405×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SNU-1 0.228×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.746×** | -3.8 | 0.083 | 25/47 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.780× | -3.2 | 0.30 | 10/48 (J82, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.784× | -3.2 | 0.30 | 17/48 (SW 1088, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 43.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 46.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +21.2) | — |
| [[PANC-1 (line)]] | alt | 47.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.9) | — |
| [[A-427 (line)]] | wt | 39.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +17.2) | — |
| [[HOP62 (line)]] | alt | 32.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +19.1) | — |
| [[LS 180 (line)]] | wt | 55.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.0) | — |
| [[RKO (line)]] | wt | 101 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 51.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 42.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +19.3) | — |
| [[A-172 (line)]] | wt | 45.5 | 3 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.09× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 46.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 50.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +16.1) | — |
| [[HT-29 (line)]] | alt | 47.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.6) | — |
| [[J82 (line)]] | alt | 39.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.88× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[KATO III (line)]] | alt | 50.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.5 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 54.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 55.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.6) | — |
| [[SW480 (line)]] | alt | 64.1 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[A498 (line)]] | wt | 57.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 57.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 27.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 37.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 44.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.228× (z -8.8) |
| [[C32 (line)]] | wt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.243× (z -9.6) |
| [[H4 (line)]] | wt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 52.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 35.1 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.236× (z -9.7) |
| [[SNU-423 (line)]] | alt | 75.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.72 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[IL6ST]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TAF9]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.68 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PARP3]] | +0.68 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.67 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SCRN1]] | +0.66 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LEPROT]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ARMT1]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CILK1]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TWF1]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.66 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[TOMM5]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[MNX1]] | -0.63 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[ANKS3]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[ATAT1]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.63 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[DRD4]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SNU13]] | -0.62 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ANKRD13D]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.61 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[PTMAP2]] ⚠ | -0.61 | -0.59 / -0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM120B]] | -0.61 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[WRN]] | -0.61 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NCOA4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.2, 1.5); signed map (16.8, -32.5). **Vector** length 102, 27.6% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +16.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +14.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.0 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.9 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.4 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -3.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:46,005,088-46,030,623 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARA70, RFG, ELE1, PTC3, DKFZp762E1112 |
| Hallmark sets | ANDROGEN_RESPONSE, HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13772](https://www.uniprot.org/uniprotkb/Q13772) (Nuclear receptor coactivator 4):

> Cargo receptor for the autophagic turnover of the iron-binding ferritin complex, playing a central role in iron homeostasis. Acts as an adapter for delivery of ferritin to lysosomes and autophagic degradation of ferritin, a process named ferritinophagy. Targets the iron-binding ferritin complex to autolysosomes following starvation or iron depletion. Ensures efficient erythropoiesis, possibly by regulating hemin-induced erythroid differentiation. In some studies, has been shown to enhance the …

**Summary**, from NCBI Gene [8031](https://www.ncbi.nlm.nih.gov/gene/8031):

> This gene encodes an androgen receptor coactivator. The encoded protein interacts with the androgen receptor in a ligand-dependent manner to enhance its transcriptional activity. Chromosomal translocations between this gene and the ret tyrosine kinase gene, also located on chromosome 10, have been associated with papillary thyroid carcinoma. Alternatively spliced transcript variants have been described. Pseudogenes are present on chromosomes 4, 5, 10, and 14. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7671) · Entrez [8031](https://www.ncbi.nlm.nih.gov/gene/8031) · UniProt [Q13772](https://www.uniprot.org/uniprotkb/Q13772) · Ensembl [ENSG00000266412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266412)

## Data

Gene col 15490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15490); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15490]; `tensor/DDL_lfc|DDL_z.npy` [15490]; `embed/gene_vectors.npy` [15490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15490 or target_col == 15490). Every well: [[NCOA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
