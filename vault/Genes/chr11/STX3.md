---
symbol: "STX3"
type: "gene"
col: 9383
ensembl_id: "ENSG00000166900"
name: "syntaxin 3"
location: "11q12.1"
module: 68
arm: "+"
pooled_cpm: 68.35
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# STX3

*syntaxin 3* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.50× (z +29.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.775× (z -4.3, q 0.008, down in 23 of 49 measured lines) ⚠ unreliable plate only; position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.0804×, SHP-77 0.154×, HT-29 0.477×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.311×, RKO 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAGC-DT]] (+0.65, fdr 1e-05), [[RNF103-CHMP3]] (+0.60, fdr 3e-05), [[MCOLN3]] (+0.59, fdr 1e-05); moves opposite to [[MYCBP]] (-0.45, fdr 6e-05), [[AQR]] (-0.45, fdr 1e-04), [[ELP1]] (-0.44, fdr 3e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.50×** | +29.9 | 0e+00 | 47/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.17×** | +19.5 | 0e+00 | 41/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +15.5 | 0e+00 | 43/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +15.3 | 0e+00 | 40/49 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +14.8 | 0e+00 | 45/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +14.6 | 0e+00 | 46/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +14.5 | 1e-45 | 41/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.12×** | +12.7 | 4e-35 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.12×** | +12.7 | 4e-35 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +12.3 | 3e-33 | 46/47 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.70×** | +11.5 | 4e-29 | 42/49 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.8 | 4e-10 | 26/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +6.5 | 3e-09 | 31/49 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +6.5 | 4e-09 | 30/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.3 | 6e-06 | 25/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +5.2 | 8e-06 | 26/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.0 | 2e-05 | 20/48 (HOP62, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9383.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.0804×, SHP-77 0.154×, HT-29 0.477×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 0.311×, RKO 0.426×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.775×** | -4.3 | 0.008 | 23/49 (SW 900, SW480, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.880× | -3.1 | 0.58 | 12/48 (SNU-423, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.0 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +23.8) | — |
| [[SW480 (line)]] | alt | 80.5 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +17.7) | — |
| [[BT-474 (line)]] | alt | 126 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.3) | — |
| [[C32 (line)]] | wt | 77.6 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.74× (z +14.3) | — |
| [[KATO III (line)]] | alt | 125 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.0) | — |
| [[LoVo (line)]] | wt | 81.6 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +21.1) | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +18.0) | — |
| [[LS 180 (line)]] | wt | 70.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +16.2) | — |
| [[HT-29 (line)]] | alt | 200 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 60.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 44.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.64× (z +24.4) | — |
| [[NCI-H2347 (line)]] | alt | 64.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +21.6) | — |
| [[PANC-1 (line)]] | alt | 33.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 48.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 45.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +20.2) | — |
| [[J82 (line)]] | alt | 130 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +20.0) | — |
| [[Panc 03.27 (line)]] | alt | 84.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.3) | — |
| [[RKO (line)]] | wt | 153 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0804× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 161 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +18.0) | — |
| [[A-172 (line)]] | wt | 63.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +23.0) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 44.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +17.9) | — |
| [[COLO 205 (line)]] | alt | 114 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +18.1) | — |
| [[HCT15 (line)]] | alt | 62.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 73.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.3) | — |
| [[HepG2_C3A (line)]] | wt | 68.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 51.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +17.1) | — |
| [[RPMI-7951 (line)]] | alt | 76.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.3) | — |
| [[A549 (line)]] | wt | 34.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +18.5) | — |
| [[HS-578T (line)]] | alt | 33.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +17.1) | — |
| [[NCI-H2030 (line)]] | alt | 61.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +16.3) | — |
| [[SW 900 (line)]] | alt | 49.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.0) | — |
| [[A498 (line)]] | wt | 39.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +19.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 69.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +16.8) | — |
| [[SW48 (line)]] | wt | 59.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.9) | — |
| [[A-427 (line)]] | wt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.8) | — |
| [[H4 (line)]] | wt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 203 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC-DT]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[MCOLN3]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MGAT4B]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[MAFG]] | +0.54 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[LINC01090]] | +0.54 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[ABRACL]] | +0.54 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[GULP1]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CRYM]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[COL28A1]] | +0.51 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[PKD1L2]] | +0.51 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[LYST]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYCBP]] | -0.45 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[AQR]] | -0.45 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[ELP1]] | -0.44 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[IMMT]] | -0.44 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[RAD54B]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PIGU]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ATG4C]] | -0.44 | -0.38 / -0.24 | both halves | 5e-04 |  |
| [[SLF1]] | -0.44 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[NCAPD3]] | -0.44 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[EFCAB11]] | -0.43 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[POT1]] | -0.43 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[CEP192]] | -0.43 | -0.37 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STX3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (18.1, 13.6); signed map (40.2, -17.1). **Vector** length 91.5, 26.8% of its response variance represented; |z| ≥ 3 in 1,308 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +14.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +3.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.9 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | +4.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | +5.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Riluzole hydrochloride (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +4.2 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,713,456-59,805,882 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously STX3A |
| Gene groups (HGNC) | Syntaxins |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Other interleukin signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13277](https://www.uniprot.org/uniprotkb/Q13277) (Syntaxin-3):

> Potentially involved in docking of synaptic vesicles at presynaptic active zones. Apical receptor involved in membrane fusion of apical vesicles.; [Isoform B]: Essential for survival of retinal photoreceetors.; [Isoform 3]: Functions as a regulator of gene expression.

**Summary**, from NCBI Gene [6809](https://www.ncbi.nlm.nih.gov/gene/6809):

> The gene is a member of the syntaxin family. The encoded protein is targeted to the apical membrane of epithelial cells where it forms clusters and is important in establishing and maintaining polarity necessary for protein trafficking involving vesicle fusion and exocytosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:11438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11438) · Entrez [6809](https://www.ncbi.nlm.nih.gov/gene/6809) · UniProt [Q13277](https://www.uniprot.org/uniprotkb/Q13277) · Ensembl [ENSG00000166900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166900)

## Data

Gene col 9383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9383); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9383]; `tensor/DDL_lfc|DDL_z.npy` [9383]; `embed/gene_vectors.npy` [9383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9383 or target_col == 9383). Every well: [[STX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
