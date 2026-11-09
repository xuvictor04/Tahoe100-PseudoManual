---
symbol: "ARRDC3-AS1"
type: "gene"
col: 15981
ensembl_id: "ENSG00000281357"
name: "ARRDC3 antisense RNA 1"
location: "5q14.3"
module: 10
arm: "+"
pooled_cpm: 11.41
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 37
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ARRDC3-AS1

*ARRDC3 antisense RNA 1* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.7× (z +43.2, q 0e+00, up in 44 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.216×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (SHP-77 0.0856×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.237×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (C-33 A 0.103×).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMADHC-DT]] (+0.83, fdr 8e-06), [[CCDC90B-AS1]] (+0.83, fdr 1e-05), [[PKN2-AS1]] (+0.80, fdr 6e-05); moves opposite to [[L2HGDH]] (-0.73, fdr 2e-05), [[CEP131]] (-0.71, fdr 3e-04), [[PHKA2]] (-0.71, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02398]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.7×** | +43.2 | 0e+00 | 44/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.84×** | +36.2 | 0e+00 | 44/45 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.52×** | +25.1 | 0e+00 | 43/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.29×** | +20.9 | 0e+00 | 44/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **4.77×** | +18.7 | 0e+00 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.56×** | +18.1 | 0e+00 | 43/46 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.05×** | +16.7 | 0e+00 | 40/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.82×** | +16.6 | 0e+00 | 40/47 (SW480, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.75×** | +12.6 | 2e-34 | 39/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.24×** | +10.0 | 7e-22 | 37/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.66×** | +10.0 | 9e-22 | 36/47 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +9.3 | 7e-19 | 24/28 (SK-MEL-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +9.3 | 7e-19 | 30/47 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.99×** | +8.5 | 6e-16 | 29/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +7.8 | 3e-13 | 29/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **1.79×** | +7.2 | 2e-11 | 31/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15981.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.216×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (SHP-77 0.0856×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.237×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 0.05 µM in 1 line (C-33 A 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | 0.756× | -3.5 | 0.27 | 17/43 (A-427, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | 0.616× | -3.2 | 0.45 | 14/42 (NCI-H1573, Hs 766T, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.80 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +26.2) | — |
| [[A-172 (line)]] | wt | 19.3 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.4× (z +25.2) | — |
| [[C32 (line)]] | wt | 12.1 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.0× (z +18.8) | — |
| [[HOP62 (line)]] | alt | 9.11 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +18.6) | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +16.8) | — |
| [[SW480 (line)]] | alt | 7.35 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +21.2) | — |
| [[LoVo (line)]] | wt | 19.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +23.4) | — |
| [[NCI-H2347 (line)]] | alt | 8.69 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +19.3) | — |
| [[A498 (line)]] | wt | 9.47 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +15.1) | — |
| [[HS-578T (line)]] | alt | 10.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +15.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +16.3) | — |
| [[NCI-H1573 (line)]] | alt | 34.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +19.8) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +24.5) | — |
| [[HEC-1-A (line)]] | alt | 7.25 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +16.5) | — |
| [[Hs 766T (line)]] | wt | 19.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.1) | — |
| [[HT-29 (line)]] | alt | 8.27 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +11.9) | — |
| [[KATO III (line)]] | alt | 9.25 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 6.40 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +20.0) | — |
| [[HCT15 (line)]] | alt | 8.65 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +14.0) | — |
| [[RKO (line)]] | wt | 7.57 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.58× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 10.7 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +11.0) | [[Docetaxel (drug)]] 0.05 µM 0.0856× (z -10.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 7.93 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 8.91 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +14.1) | — |
| [[SW48 (line)]] | wt | 8.21 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.5× (z +13.2) | — |
| [[A549 (line)]] | wt | 5.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 5.08 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 49.5× (z +18.8) | — |
| [[BT-474 (line)]] | alt | 9.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 22.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.6) | [[Canagliflozin (drug)]] 0.05 µM 0.103× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 7.05 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 5.00 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.6× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +11.4) | — |
| [[J82 (line)]] | alt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +16.7) | — |
| [[LS 180 (line)]] | wt | 9.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +15.5) | — |
| [[RPMI-7951 (line)]] | alt | 9.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 3.37 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +12.4) | — |
| [[A-427 (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +12.0) | — |
| [[H4 (line)]] | wt | 7.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +11.6) | — |
| [[SW 1271 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | +0.83 | +0.81 / +0.58 | both halves | 8e-06 |  |
| [[CCDC90B-AS1]] | +0.83 | +0.84 / +0.52 | both halves | 1e-05 | same gene group |
| [[PKN2-AS1]] | +0.80 | +0.83 / +0.39 | both halves | 6e-05 | same gene group |
| [[PCNX4-DT]] | +0.79 | +0.84 / +0.39 | both halves | 6e-05 |  |
| [[TMEM202-AS1]] | +0.78 | +0.83 / +0.27 | both halves | 3e-04 | same gene group |
| [[PPP1R12A-AS2]] | +0.76 | +0.83 / +0.28 | both halves | 3e-04 | same gene group |
| [[PATL2]] | +0.75 | +0.83 / +0.34 | both halves | 1e-04 |  |
| [[NEB]] | +0.75 | +0.77 / +0.45 | both halves | 3e-05 |  |
| [[CFAP418-AS1]] | +0.75 | +0.72 / +0.45 | both halves | 3e-05 | same gene group |
| [[WARS2-AS1]] | +0.75 | +0.77 / +0.42 | both halves | 4e-05 | same gene group |
| [[MAD2L1-DT]] | +0.74 | +0.79 / +0.21 | both halves | 6e-04 |  |
| [[RFX3-DT]] | +0.74 | +0.78 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.73 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CEP131]] | -0.71 | -0.68 / -0.27 | both halves | 3e-04 |  |
| [[PHKA2]] | -0.71 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[MYPOP]] | -0.70 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[HACE1]] | -0.70 | -0.75 / -0.35 | both halves | 1e-04 |  |
| [[BRAT1]] | -0.69 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SLC27A1]] | -0.69 | -0.73 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[SUFU]] | -0.69 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[NBPF3]] | -0.68 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[WRAP73]] | -0.68 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[LCMT1]] | -0.67 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[HEATR5B]] | -0.67 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CAMK2G]] | -0.67 | -0.60 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02398]] | B | LINC02398 activity raises ARRDC3-AS1's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without LINC02398 | 0.023 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[NPAS3]] | B | NPAS3 activity raises ARRDC3-AS1's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without NPAS3 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ARRDC3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.0, 13.6); signed map (24.7, -6.8). **Vector** length 106, 27.0% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +16.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +36.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.4 | +20.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.2 | +25.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.9 | +10.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ARRDC3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:91,380,349-91,616,105 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.168 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44145) · Entrez [100129716](https://www.ncbi.nlm.nih.gov/gene/100129716) · Ensembl [ENSG00000281357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281357)

## Data

Gene col 15981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15981); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15981]; `tensor/DDL_lfc|DDL_z.npy` [15981]; `embed/gene_vectors.npy` [15981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15981 or target_col == 15981). Every well: [[ARRDC3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRDC3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
