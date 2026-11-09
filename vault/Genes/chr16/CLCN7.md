---
symbol: "CLCN7"
type: "gene"
col: 2342
ensembl_id: "ENSG00000103249"
name: "Cl-/H+ antiporter 7"
location: "16p13.3"
module: 138
arm: "+"
pooled_cpm: 19.37
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# CLCN7

*Cl-/H+ antiporter 7* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.39× (z +22.9, q 0e+00, up in 44 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (SW48 0.145×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLLT6]] (+0.61, fdr 2e-05), [[DUSP3]] (+0.61, fdr 1e-05), [[ZFTRAF1]] (+0.60, fdr 3e-05); moves opposite to [[BOLA3]] (-0.60, fdr 1e-05), [[GNAI3]] (-0.52, fdr 2e-04), [[PREP]] (-0.52, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC26A11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.39×** | +22.9 | 0e+00 | 44/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.58×** | +17.0 | 0e+00 | 46/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.60×** | +12.7 | 8e-35 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.25×** | +10.8 | 7e-25 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +10.6 | 4e-24 | 42/46 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +10.3 | 7e-23 | 43/47 (SNU-423, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +10.2 | 1e-22 | 40/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +9.4 | 5e-19 | 39/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +8.5 | 1e-15 | 34/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.7 | 7e-13 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +6.2 | 3e-08 | 30/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.7 | 6e-07 | 25/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.6 | 8e-07 | 22/43 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +5.4 | 3e-06 | 26/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.3 | 4e-06 | 24/47 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 5e-06 | 29/48 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 9e-06 | 26/45 (NCI-H460, HT-29, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.47×** | +5.1 | 1e-05 | 21/48 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2342.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (SW48 0.145×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.6 | 0.17 | 4/48 (AN3 CA, SW48, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.05 µM |  | 0.830× | -3.3 | 0.19 | 10/48 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.782× | -3.3 | 0.19 | 14/48 (SW 1271, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Flutamide (drug)]] 5 µM |  | 0.797× | -3.0 | 0.34 | 11/47 (KATO III, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +23.6) | — |
| [[SW480 (line)]] | alt | 15.3 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.11× (z +14.4) | — |
| [[KATO III (line)]] | alt | 14.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +15.2) | — |
| [[COLO 205 (line)]] | alt | 14.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +15.9) | — |
| [[Hs 766T (line)]] | wt | 24.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +17.7) | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +15.9) | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +20.1) | — |
| [[SNU-423 (line)]] | alt | 27.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.6) | — |
| [[A-172 (line)]] | wt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +20.4) | — |
| [[A-427 (line)]] | wt | 24.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +14.2) | — |
| [[A498 (line)]] | wt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 9.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 21.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +12.2) | — |
| [[RKO (line)]] | wt | 35.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 30.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.1) | — |
| [[A549 (line)]] | wt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 8.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +13.1) | — |
| [[J82 (line)]] | alt | 29.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +17.2) | — |
| [[LoVo (line)]] | wt | 17.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.20× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.6) | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.145× (z -8.7) |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLLT6]] | +0.61 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[DUSP3]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ZFTRAF1]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[ATP6V1C1]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 | pathway: Ion channel transport |
| [[GIGYF1]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CRTC2]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PEPD]] | +0.58 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[SGSH]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 | STRING 425 |
| [[GNPDA1]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[HSPBAP1]] | +0.56 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[UAP1L1]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOLA3]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[GNAI3]] | -0.52 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[PREP]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[DCUN1D3]] | -0.51 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[RNGTT]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TAF5L]] | -0.48 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[LANCL3]] | -0.47 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[GRB2]] | -0.47 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[SMAP2]] | -0.47 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[DIS3]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TNIK]] | -0.46 | -0.53 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A11]] | B | SLC26A11 activity raises CLCN7's level | lines that do not express SLC26A11 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without SLC26A11 | 0.050 | ⚠ within organs, on part of the lines; also absent: DENND5B, SMAD4, MINAR1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.1, -21.6); signed map (4.7, -8.6). **Vector** length 88.0, 20.5% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +10.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.5 | +12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.5 | +17.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | Cl-/H+ antiporter 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,444,934-1,475,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLC-7, OPTA2, CLC7, ClC-7, PPP1R63 |
| Gene groups (HGNC) | CLC chloride channel and transporter family; Protein phosphatase 1 regulatory subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P51798](https://www.uniprot.org/uniprotkb/P51798) (H(+)/Cl(-) exchange transporter 7):

> Slowly voltage-gated channel mediating the exchange of chloride ions against protons. Functions as antiporter and contributes to the acidification of the lysosome lumen and may be involved in maintaining lysosomal pH. The CLC channel family contains both chloride channels and proton-coupled anion transporters that exchange chloride or another anion for protons (By similarity). The presence of conserved gating glutamate residues is typical for family members that function as antiporters (By …

**Summary**, from NCBI Gene [1186](https://www.ncbi.nlm.nih.gov/gene/1186):

> The product of this gene belongs to the CLC chloride channel family of proteins. Chloride channels play important roles in the plasma membrane and in intracellular organelles. This gene encodes chloride channel 7. Defects in this gene are the cause of osteopetrosis autosomal recessive type 4 (OPTB4), also called infantile malignant osteopetrosis type 2 as well as the cause of autosomal dominant osteopetrosis type 2 (OPTA2), also called autosomal dominant Albers-Schonberg disease or marble …

**Accessions** — [HGNC:2025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2025) · Entrez [1186](https://www.ncbi.nlm.nih.gov/gene/1186) · UniProt [P51798](https://www.uniprot.org/uniprotkb/P51798) · Ensembl [ENSG00000103249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103249)

## Data

Gene col 2342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2342); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2342]; `tensor/DDL_lfc|DDL_z.npy` [2342]; `embed/gene_vectors.npy` [2342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2342 or target_col == 2342). Every well: [[CLCN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
