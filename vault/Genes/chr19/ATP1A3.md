---
symbol: "ATP1A3"
type: "gene"
col: 2600
ensembl_id: "ENSG00000105409"
name: "ATPase Na+/K+ transporting subunit alpha 3"
location: "19q13.2"
module: 176
arm: "+"
pooled_cpm: 3.51
n_lines_expressing: 38
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# ATP1A3

*ATPase Na+/K+ transporting subunit alpha 3* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 34.4× (z +33.2, q 0e+00, up in 34 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0514×; ⚠ cell-cycle shift, explains ~51% of this change).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHO1]] (+0.69, fdr 3e-04), [[GDF11]] (+0.67, fdr 1e-05), [[FOXO6]] (+0.67, fdr 1e-05); moves opposite to [[TRAPPC13]] (-0.63, fdr 3e-05), [[NMNAT1]] (-0.62, fdr 2e-04), [[SPRY3]] (-0.60, fdr 0.001, ⚠ one half only (not replicated)), [[DDX59]] (-0.60, fdr 2e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 7 go from it, the strongest it → [[NRXN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **34.4×** | +33.2 | 0e+00 | 34/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **31.3×** | +32.3 | 0e+00 | 30/30 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **8.74×** | +28.8 | 0e+00 | 21/22 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **16.6×** | +26.4 | 0e+00 | 30/30 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **5.48×** | +22.6 | 0e+00 | 31/32 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **7.09×** | +18.4 | 0e+00 | 32/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +12.2 | 1e-32 | 3/4 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.58×** | +12.0 | 3e-31 | 14/21 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.41×** | +11.5 | 7e-29 | 11/14 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.86×** | +9.9 | 3e-21 | 19/28 (LoVo, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.76×** | +9.5 | 8e-20 | 21/23 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.67×** | +9.2 | 1e-18 | 17/28 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **5.32×** | +8.2 | 9e-15 | 18/27 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +7.5 | 3e-12 | 12/26 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.3 | 1e-11 | 9/23 (A498, A549, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.005 | 6/34 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.020 | 1/32 (A498) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2600.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0514×; ⚠ cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.767× | -3.5 | 0.13 | 2/29 (NCI-H2347, SHP-77) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.769× | -3.5 | 0.13 | 7/31 (C-33 A, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.704× | -3.3 | 0.18 | 2/29 (C32, PANC-1) | inconsistent across doses | position effect removed |
| [[Tucatinib (drug)]] 0.05 µM |  | 0.705× | -3.1 | 0.27 | 2/31 (SW 900, HCT15) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.21 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +15.4) | — |
| [[SW480 (line)]] | alt | 4.56 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 31.2× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 1.49 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 108× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.28 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 3.38 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 20.0× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 1.24 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.4× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 2.40 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 27.0× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 8.45 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 14.8× (z +11.8) | — |
| [[A-427 (line)]] | wt | 7.32 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.6× (z +10.5) | — |
| [[A498 (line)]] | wt | 1.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.9) | — |
| [[A549 (line)]] | wt | 2.00 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 125× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 1.45 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 30.4× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 1.65 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 85.3× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 3.44 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 66.1× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.33 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 22.4× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 6.12 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 18.3× (z +9.5) | — |
| [[C32 (line)]] | wt | 1.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.9× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 1.60 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 56.0× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 1.10 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 69.0× (z +8.5) | — |
| [[RKO (line)]] | wt | 5.42 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0514× (z -9.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | +0.69 | +0.28 / +0.70 | both halves | 3e-04 |  |
| [[GDF11]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.67 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SYN1]] | +0.66 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SUSD4]] | +0.65 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[CADM4]] | +0.65 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[MAST1]] | +0.65 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[KIF5C]] | +0.62 | +0.36 / +0.72 | both halves | 1e-04 |  |
| [[HPSE]] | +0.61 | +0.30 / +0.67 | both halves | 2e-04 |  |
| [[APBA1]] | +0.60 | +0.24 / +0.71 | both halves | 4e-04 |  |
| [[GDPD5]] | +0.60 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[SHF]] | +0.60 | +0.24 / +0.64 | both halves | 4e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.63 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NMNAT1]] | -0.62 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[SPRY3]] | -0.60 | -0.17 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[DDX59]] | -0.60 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[C2orf42]] | -0.59 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.59 | -0.21 / -0.60 | both halves | 7e-04 |  |
| [[ANGEL2]] | -0.59 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[PBLD]] | -0.59 | -0.08 / -0.49 | ⚠ not reproduced | 0.004 |  |
| [[ATAD2B]] | -0.59 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[PDHX]] | -0.59 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[STARD7-AS1]] | -0.58 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[RABL2B]] | -0.58 | -0.18 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[POC1B-AS1]] | -0.56 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[CNPY2]] | -0.56 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PUS10]] | -0.55 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises ATP1A3's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without SEMA6B | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[SRRM3]] | B | SRRM3 activity raises ATP1A3's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without SRRM3 | 0.013 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[GALNT12]] | B | GALNT12 activity lowers ATP1A3's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.01× higher at baseline in the lines without GALNT12 | 0.026 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[ADGRB2]] | B | ADGRB2 activity raises ATP1A3's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without ADGRB2 | 0.048 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[NFASC]] | B | NFASC activity raises ATP1A3's level | lines that do not express NFASC (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without NFASC | 0.056 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[NPTXR]] | B | NPTXR activity raises ATP1A3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without NPTXR | 0.068 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN3]] | B | ATP1A3 activity lowers NRXN3's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.57× higher at baseline in the lines without ATP1A3 | 0.057 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[GDF11]] | B | ATP1A3 activity raises GDF11's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without ATP1A3 | 0.074 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[KCTD17]] | B | ATP1A3 activity raises KCTD17's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without ATP1A3 | 0.081 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[ADGRB2]] | B | ATP1A3 activity raises ADGRB2's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without ATP1A3 | 0.083 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[GJA3]] | B | ATP1A3 activity raises GJA3's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 2.28× lower at baseline in the lines without ATP1A3 | 0.086 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[DPF1]] | B | ATP1A3 activity raises DPF1's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without ATP1A3 | 0.094 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[ARRB2]] | B | ATP1A3 activity raises ARRB2's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without ATP1A3 | 0.096 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.4, 35.7); signed map (-22.2, 29.6). **Vector** length 52.4, 8.39% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +22.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.1 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ATPase Na+/K+ transporting subunit alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,966,582-41,997,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DYT12 |
| Gene groups (HGNC) | ATPase Na+/K+ transporting subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 9 pathways, smallest: Ion homeostasis; Ion transport by P-type ATPases; Potential therapeutics for SARS |
| Matched by | ensembl_id |

**Function**, from UniProt [P13637](https://www.uniprot.org/uniprotkb/P13637) (Sodium/potassium-transporting ATPase subunit alpha-3):

> Neuron-specific alpha catalytic component of the Na(+)/K(+)-transporting ATPase, which catalyzes the hydrolysis of ATP coupled with the exchange of Na(+) and K(+) ions across the plasma membrane. Transports 3 Na(+) ions out of the cell and 2 K(+) ions into the cell for each ATP hydrolyze against their electrochemical gradients to maintain ion concentration gradients across the membranes (By similarity). In the brain, ATP1A3 is critical for neuronal cell signaling and for maintenance of …

**Summary**, from NCBI Gene [478](https://www.ncbi.nlm.nih.gov/gene/478):

> The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organic and inorganic molecules, and for electrical excitability of nerve and muscle. This enzyme is …

**Accessions** — [HGNC:801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:801) · Entrez [478](https://www.ncbi.nlm.nih.gov/gene/478) · UniProt [P13637](https://www.uniprot.org/uniprotkb/P13637) · Ensembl [ENSG00000105409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105409)

## Data

Gene col 2600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2600); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2600]; `tensor/DDL_lfc|DDL_z.npy` [2600]; `embed/gene_vectors.npy` [2600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2600 or target_col == 2600). Every well: [[ATP1A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP1A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
