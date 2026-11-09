---
symbol: "PDPK1"
type: "gene"
col: 6475
ensembl_id: "ENSG00000140992"
name: "3-phosphoinositide dependent protein kinase 1"
location: "16p13.3"
module: 18
arm: "-"
pooled_cpm: 30.18
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PDPK1

*3-phosphoinositide dependent protein kinase 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.57× (z +31.1, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 0.178×, NCI-H1573 0.273×, RPMI-7951 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.284×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (C32 0.262×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGB1]] (+0.58, fdr 2e-05), [[ZNF324]] (+0.56, fdr 3e-05), [[PLXNA3]] (+0.54, fdr 3e-05); moves opposite to [[FANCL]] (-0.59, fdr 1e-05), [[ADAT2]] (-0.57, fdr 3e-05), [[LAPTM4B]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASIC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +31.1 | 0e+00 | 45/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +20.5 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +16.9 | 0e+00 | 47/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +14.9 | 0e+00 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +13.9 | 6e-42 | 44/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +8.5 | 2e-15 | 28/48 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +7.6 | 3e-12 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +6.2 | 5e-08 | 25/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +6.1 | 6e-08 | 26/48 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +5.5 | 2e-06 | 23/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.21×** | +4.4 | 7e-04 | 20/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +4.3 | 7e-04 | 16/47 (SW480, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.20× | +4.3 | 9e-04 | 14/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +4.2 | 9e-04 | 16/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 9/47 (A498, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 7/47 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.003 | 6/48 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.027 | 6/48 (NCI-H23, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 0.178×, NCI-H1573 0.273×, RPMI-7951 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.284×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (C32 0.262×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.860× | -3.5 | 0.18 | 14/48 (HepG2/C3A, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.840× | -3.4 | 0.18 | 13/48 (RPMI-7951, HCT15, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.874× | -3.2 | 0.28 | 8/48 (SW 1088, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.911× | -3.1 | 0.28 | 8/48 (LoVo, HCT15, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +35.0) | — |
| [[SW480 (line)]] | alt | 26.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.6) | — |
| [[PANC-1 (line)]] | alt | 25.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +18.7) | — |
| [[Hs 766T (line)]] | wt | 36.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.0) | — |
| [[HS-578T (line)]] | alt | 29.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 31.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +17.2) | — |
| [[NCI-H1573 (line)]] | alt | 40.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2030 (line)]] | alt | 25.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +10.1) | — |
| [[RKO (line)]] | wt | 28.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 28.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +19.7) | — |
| [[A-172 (line)]] | wt | 39.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.2) | — |
| [[A498 (line)]] | wt | 35.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.1) | — |
| [[A549 (line)]] | wt | 28.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[AsPC-1 (line)]] | alt | 47.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +9.7) | — |
| [[C32 (line)]] | wt | 23.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.1) | [[Orlistat (drug)]] 0.05 µM 0.262× (z -8.7) |
| [[COLO 205 (line)]] | alt | 40.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.0) | — |
| [[KATO III (line)]] | alt | 47.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.284× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[RPMI-7951 (line)]] | alt | 29.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 43.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.8) | — |
| [[HT-29 (line)]] | alt | 42.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +12.9) | — |
| [[J82 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +18.3) | — |
| [[LOX-IMVI (line)]] | wt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +15.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +17.9) | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +9.0) | — |
| [[SW48 (line)]] | wt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.9) | — |
| [[A-427 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | +0.58 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[ZNF324]] | +0.56 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[PLXNA3]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R37]] | +0.54 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[CREB3]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[MAPK8IP3]] | +0.53 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[TINCR]] | +0.51 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[BUD31]] | +0.51 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[CPNE9]] | +0.51 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[YIPF3]] | +0.51 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[ACAP3]] | +0.51 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[CCNP]] | +0.51 | +0.68 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCL]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ADAT2]] | -0.57 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[LAPTM4B]] | -0.56 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[UCK2]] | -0.56 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[DTD2]] | -0.54 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[NSUN5P1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[SNRPA1]] | -0.52 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[SLC18B1]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SLC35G1]] | -0.52 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[EEF1E1]] | -0.52 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[SORD]] | -0.51 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[PON2]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASIC1]] | C | ASIC1 activity lowers PDPK1's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 1.56× higher at baseline in the lines without ASIC1 | 0.017 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391 |
| [[ZDHHC11]] | C | ZDHHC11 activity raises PDPK1's level | lines that do not express ZDHHC11 (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without ZDHHC11 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **-** arm (projection on the module's main direction -0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.2, -48.6); signed map (-8.8, -3.8). **Vector** length 79.4, 15.6% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +31.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +20.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.7 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | 3-phosphoinositide dependent protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,537,979-2,603,188 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDK1 |
| Gene groups (HGNC) | 3-phosphoinositide dependent protein kinase 1 family |
| Reactome | 70 pathways, smallest: Activation of AKT2; Estrogen-stimulated signaling through PRKCZ; RSK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15530](https://www.uniprot.org/uniprotkb/O15530) (3-phosphoinositide-dependent protein kinase 1):

> Serine/threonine kinase which acts as a master kinase, phosphorylating and activating a subgroup of the AGC family of protein kinases. Its targets include: protein kinase B (PKB/AKT1, PKB/AKT2, PKB/AKT3), p70 ribosomal protein S6 kinase (RPS6KB1), p90 ribosomal protein S6 kinase (RPS6KA1, RPS6KA2 and RPS6KA3), cyclic AMP-dependent protein kinase (PRKACA), protein kinase C (PRKCD and PRKCZ), serum and glucocorticoid-inducible kinase (SGK1, SGK2 and SGK3), p21-activated kinase-1 (PAK1), TSSK3, …

**Summary**, from NCBI Gene [5170](https://www.ncbi.nlm.nih.gov/gene/5170):

> Enables 3-phosphoinositide-dependent protein kinase activity; phospholipase activator activity; and phospholipase binding activity. Involved in several processes, including cell surface receptor signaling pathway; intracellular signaling cassette; and regulation of signal transduction. Acts upstream of or within intracellular signal transduction. Located in cytosol and plasma membrane. Implicated in prostate cancer. Biomarker of lung non-small cell carcinoma. [provided by Alliance of Genome …

**Accessions** — [HGNC:8816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8816) · Entrez [5170](https://www.ncbi.nlm.nih.gov/gene/5170) · UniProt [O15530](https://www.uniprot.org/uniprotkb/O15530) · Ensembl [ENSG00000140992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140992)

## Data

Gene col 6475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6475); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6475]; `tensor/DDL_lfc|DDL_z.npy` [6475]; `embed/gene_vectors.npy` [6475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6475 or target_col == 6475). Every well: [[PDPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
