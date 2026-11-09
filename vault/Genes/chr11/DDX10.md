---
symbol: "DDX10"
type: "gene"
col: 10898
ensembl_id: "ENSG00000178105"
name: "DEAD-box helicase 10"
location: "11q22.3"
module: 1
arm: "+"
pooled_cpm: 78.28
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DDX10

*DEAD-box helicase 10* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.05× (z +19.0, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.390×, LOX-IMVI 0.448×, NCI-H23 0.511×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.456×, SNU-1 0.240×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.535×, HEC-1-A 0.504×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.80, fdr 7e-06), [[BYSL]] (+0.80, fdr 7e-06), [[POLR1A]] (+0.80, fdr 7e-06); moves opposite to [[GNAS]] (-0.68, fdr 7e-06), [[SRP54-AS1]] (-0.67, fdr 7e-06), [[RSRP1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MICE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.05×** | +19.0 | 0e+00 | 48/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.79×** | +17.5 | 0e+00 | 48/48 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.58×** | +16.2 | 0e+00 | 48/48 (AsPC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +15.7 | 0e+00 | 45/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.33×** | +14.4 | 7e-45 | 47/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +13.8 | 3e-41 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +13.3 | 1e-38 | 39/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +11.4 | 4e-28 | 43/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.05×** | +10.0 | 2e-21 | 44/49 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +8.2 | 1e-14 | 35/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.65×** | +8.2 | 1e-14 | 44/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.56×** | +7.5 | 2e-12 | 32/48 (NCI-H1573, HT-29, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **2.21×** | +7.1 | 7e-11 | 41/48 (A498, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.2 | 2e-08 | 33/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.99×** | +6.1 | 3e-08 | 35/48 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.83×** | +5.4 | 2e-06 | 36/48 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +4.7 | 7e-05 | 29/47 (HEC-1-A, AN3 CA, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10898.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.390×, LOX-IMVI 0.448×, NCI-H23 0.511×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.456×, SNU-1 0.240×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 0.535×, HEC-1-A 0.504×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.877× | -3.2 | 0.44 | 11/48 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.832× | -3.2 | 0.44 | 18/47 (A-427, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 144 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 62.6 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 70.7 | 9 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.92× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 75.6 | 7 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.48× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[LOX-IMVI (line)]] | wt | 99.9 | 7 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.21× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 52.0 | 8 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.91× (z +15.4) | — |
| [[A549 (line)]] | wt | 68.5 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 34.3 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.71× (z +11.9) | — |
| [[A-172 (line)]] | wt | 29.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.6) | — |
| [[AsPC-1 (line)]] | alt | 29.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 8.92× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 43.0 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 120 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 51.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +13.4) | — |
| [[SW480 (line)]] | alt | 152 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 46.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 4 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.48× (z +11.7) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 2.61× (z +9.0) | [[Adagrasib (drug)]] 0.05 µM 0.592× (z -17.2) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 79.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 73.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +12.2) | — |
| [[J82 (line)]] | alt | 48.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 62.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 64.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +9.8) | — |
| [[H4 (line)]] | wt | 60.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 68.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 45.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +11.9) | — |
| [[LoVo (line)]] | wt | 82.2 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 3.32× (z +10.4) | — |
| [[A-427 (line)]] | wt | 81.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[A498 (line)]] | wt | 51.3 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.26× (z +12.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 2.43× (z +9.6) | — |
| [[C32 (line)]] | wt | 30.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 42.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 7.71× (z +11.3) | — |
| [[KATO III (line)]] | alt | 140 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 65.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 72.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 102 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 81.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.76× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 59.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 90.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.0) | — |
| [[RKO (line)]] | wt | 150 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.34× (z +8.6) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 128 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.80 | +0.79 / +0.79 | both halves | 7e-06 | STRING 554 |
| [[BYSL]] | +0.80 | +0.80 / +0.81 | both halves | 7e-06 | same gene group; STRING 971 |
| [[POLR1A]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | STRING 719 |
| [[NAA15]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[MAK16]] | +0.76 | +0.74 / +0.82 | both halves | 7e-06 | STRING 782 |
| [[RRP15]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 | STRING 481 |
| [[LTV1]] | +0.76 | +0.76 / +0.81 | both halves | 7e-06 | same gene group; STRING 861 |
| [[DIS3L2]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.76 | +0.75 / +0.78 | both halves | 7e-06 | same gene group; STRING 969 |
| [[PNO1]] | +0.75 | +0.75 / +0.81 | both halves | 7e-06 | STRING 634 |
| [[FARSB]] | +0.75 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[MGA]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.68 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.67 | -0.73 / -0.63 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.66 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.65 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[APTR]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.64 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[NARF]] | -0.64 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[MKRN1]] | -0.64 | -0.63 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICE]] | B | MICE activity lowers DDX10's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.56× higher at baseline in the lines without MICE | 0.062 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |
| [[TSEN2]] | C | TSEN2 activity raises DDX10's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without TSEN2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.4, -37.2); signed map (-0.7, -44.4). **Vector** length 132, 46.9% of its response variance represented; |z| ≥ 3 in 1,471 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.54 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.1 | +14.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +9.5 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +8.2 |
|  | [[EX229 (drug)]] 5 µM |  | +6.1 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.8 | +5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.6 | +6.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.4 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,665,058-108,940,999 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRH-J8, Dbp4 |
| Gene groups (HGNC) | DEAD-box helicases; SSU processome |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13206](https://www.uniprot.org/uniprotkb/Q13206) (Probable ATP-dependent RNA helicase DDX10):

> Putative ATP-dependent RNA helicase that plays various role in innate immunity or inflammation. Plays a role in the enhancement of AIM2-induced inflammasome activation by interacting with AIM2 and stabilizing its protein level. Negatively regulates viral infection by promoting interferon beta production and interferon stimulated genes/ISGs expression.

**Summary**, from NCBI Gene [1662](https://www.ncbi.nlm.nih.gov/gene/1662):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2735) · Entrez [1662](https://www.ncbi.nlm.nih.gov/gene/1662) · UniProt [Q13206](https://www.uniprot.org/uniprotkb/Q13206) · Ensembl [ENSG00000178105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178105)

## Data

Gene col 10898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10898); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10898]; `tensor/DDL_lfc|DDL_z.npy` [10898]; `embed/gene_vectors.npy` [10898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10898 or target_col == 10898). Every well: [[DDX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
