---
symbol: "CHCHD7"
type: "gene"
col: 10005
ensembl_id: "ENSG00000170791"
name: "coiled-coil-helix-coiled-coil-helix domain containing 7"
location: "8q12.1"
module: 93
arm: "+"
pooled_cpm: 21.53
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 7
n_dd_up_clean: 23
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# CHCHD7

*coiled-coil-helix-coiled-coil-helix domain containing 7* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.41× (z +25.9, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.583× (z -7.5, q 3e-11, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2A]] (+0.65, fdr 1e-05), [[GTF2B]] (+0.65, fdr 9e-06), [[HEXIM1]] (+0.64, fdr 7e-06); moves opposite to [[SPATA5]] (-0.64, fdr 5e-05), [[HACD3]] (-0.57, fdr 1e-04), [[HERC2]] (-0.56, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.41×** | +25.9 | 0e+00 | 45/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.53×** | +17.5 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.30×** | +16.6 | 0e+00 | 47/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.87×** | +14.7 | 0e+00 | 44/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +14.0 | 1e-42 | 41/46 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.62×** | +13.4 | 8e-39 | 35/37 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +12.4 | 1e-33 | 40/42 (SW 900, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +12.2 | 3e-32 | 30/33 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +11.0 | 3e-26 | 38/45 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.80×** | +9.4 | 3e-19 | 34/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +9.3 | 1e-18 | 37/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.1 | 2e-14 | 29/45 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +7.7 | 5e-13 | 35/48 (HT-29, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +7.3 | 1e-11 | 35/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +7.1 | 4e-11 | 32/48 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +6.7 | 6e-10 | 28/47 (HOP62, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +6.4 | 6e-09 | 32/48 (HT-29, HOP62, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.93×** | +4.8 | 5e-05 | 27/43 (HT-29, SW1417, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -7.5 | 3e-11 | 37/47 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -6.3 | 1e-07 | 26/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -6.0 | 3e-07 | 28/43 (SW480, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -5.8 | 1e-06 | 30/47 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -5.4 | 9e-06 | 29/47 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -4.7 | 2e-04 | 26/45 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -4.4 | 0.001 | 21/47 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.801× | -3.1 | 0.13 | 17/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 28.2 | 10 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 24.2 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +18.8) | — |
| [[SW480 (line)]] | alt | 40.8 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +19.7) | — |
| [[LoVo (line)]] | wt | 27.3 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 34.2 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.70× (z +16.0) | — |
| [[LS 180 (line)]] | wt | 27.9 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 29.7 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +14.1) | — |
| [[KATO III (line)]] | alt | 47.0 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +16.6) | — |
| [[A549 (line)]] | wt | 13.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 9.48 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.15× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 17.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +13.0) | — |
| [[C32 (line)]] | wt | 17.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.90 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +17.0) | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 27.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.9) | — |
| [[A498 (line)]] | wt | 13.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 32.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 26.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +11.1) | — |
| [[J82 (line)]] | alt | 19.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 9.72 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.43× (z +9.7) | — |
| [[RKO (line)]] | wt | 32.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +14.2) | — |
| [[A-172 (line)]] | wt | 6.40 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0956× (z -9.7) |
| [[A-427 (line)]] | wt | 13.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.54× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.3) | — |
| [[H4 (line)]] | wt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 26.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +16.6) | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.70× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2A]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.65 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[HEXIM1]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[WDR47]] | +0.62 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[MED29]] | +0.62 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[RSRP1]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[LINC00910]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[FAM53C]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SAP18]] | +0.58 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[DIS3]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[FAM177A1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ZNF490]] | +0.57 | +0.70 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA5]] | -0.64 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[HACD3]] | -0.57 | -0.72 / -0.33 | both halves | 1e-04 |  |
| [[HERC2]] | -0.56 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[EXT2]] | -0.55 | -0.66 / -0.32 | both halves | 2e-04 |  |
| [[EXOC2]] | -0.54 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[VWA8]] | -0.54 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[HERC2P9]] | -0.54 | -0.63 / -0.29 | both halves | 2e-04 |  |
| [[LARP1]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TALDO1]] | -0.54 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CHCHD3]] | -0.53 | -0.38 / -0.43 | both halves | 7e-05 | same gene group; pathway: Mitochondrial protein import; STRING 416 |
| [[TRRAP]] | -0.53 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.52 | -0.30 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHCHD7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.9, -26.8); signed map (3.4, 16.1). **Vector** length 70.1, 15.9% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +8.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +9.3 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +7.7 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:56,211,686-56,218,809 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2217, COX23 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins; Mitochondrial respiratory chain complex assembly factors |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

UniProt [Q9BUK0](https://www.uniprot.org/uniprotkb/Q9BUK0) carries no function annotation.

**Summary**, from NCBI Gene [79145](https://www.ncbi.nlm.nih.gov/gene/79145):

> Predicted to be involved in mitochondrial respiratory chain complex assembly. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28314) · Entrez [79145](https://www.ncbi.nlm.nih.gov/gene/79145) · UniProt [Q9BUK0](https://www.uniprot.org/uniprotkb/Q9BUK0) · Ensembl [ENSG00000170791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170791)

## Data

Gene col 10005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10005); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10005]; `tensor/DDL_lfc|DDL_z.npy` [10005]; `embed/gene_vectors.npy` [10005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10005 or target_col == 10005). Every well: [[CHCHD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
