---
symbol: "DPY19L2P2"
type: "gene"
col: 9986
ensembl_id: "ENSG00000170629"
name: "DPY19L2 pseudogene 2"
location: "7q22.1"
module: 80
arm: "+"
pooled_cpm: 5.46
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# DPY19L2P2

*DPY19L2 pseudogene 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.73× (z +24.5, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.05 µM: 0.683× (z -4.2, q 0.012, down in 12 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L2P2-1]] (+0.79, fdr 7e-06, ⚠ same locus), [[DPY19L2]] (+0.73, fdr 7e-06), [[LINC00240]] (+0.71, fdr 7e-06), [[ZFHX2]] (+0.69, fdr 7e-06); moves opposite to [[NTAQ1]] (-0.64, fdr 3e-05), [[ATP7B]] (-0.62, fdr 4e-05), [[CPSF4]] (-0.61, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[DPY19L2P2-1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.73×** | +24.5 | 0e+00 | 39/42 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +15.9 | 0e+00 | 29/37 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.51×** | +14.0 | 3e-42 | 27/38 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.27×** | +12.7 | 1e-34 | 35/43 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.25×** | +9.0 | 2e-17 | 27/47 (SW480, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.29×** | +8.9 | 5e-17 | 3/9 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.16×** | +8.6 | 9e-16 | 15/23 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.8 | 5e-13 | 5/14 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.1 | 6e-11 | 16/35 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +6.9 | 3e-10 | 21/45 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +6.7 | 1e-09 | 17/41 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +5.6 | 1e-06 | 15/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.5 | 1e-06 | 11/45 (HOP62, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.4 | 3e-06 | 20/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +5.2 | 7e-06 | 16/41 (NCI-H23, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 15/46 (A-172, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.6 | 1e-04 | 6/40 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.5 | 2e-04 | 15/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.007 | 8/39 (NCI-H23, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.683×** | -4.2 | 0.012 | 12/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.707×** | -3.9 | 0.019 | 6/41 (NCI-H23, A498, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -3.8 | 0.019 | 14/41 (NCI-H460, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.709×** | -3.8 | 0.019 | 11/45 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.072 | 12/41 (C32, HS-578T, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.739×** | -3.4 | 0.072 | 10/36 (C32, COLO 205, …) | two highest doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.742×** | -3.3 | 0.072 | 7/46 (HepG2/C3A, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.750×** | -3.2 | 0.096 | 15/43 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.760× | -3.1 | 0.14 | 6/45 (SNU-423, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.8 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.6) | [[Digitoxin (drug)]] 0.5 µM 0.183× (z -10.9) |
| [[A-172 (line)]] | wt | 5.93 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +14.6) | [[Finasteride (drug)]] 0.05 µM 0.0921× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 8.72 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +14.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.137× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 3.44 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +12.0) | [[Harringtonine (drug)]] 0.05 µM 0.111× (z -8.6) |
| [[SW480 (line)]] | alt | 5.53 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +14.2) | — |
| [[HEC-1-A (line)]] | alt | 2.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.6× (z +13.5) | — |
| [[A498 (line)]] | wt | 2.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +8.9) | — |
| [[A549 (line)]] | wt | 2.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 5.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +11.0) | — |
| [[KATO III (line)]] | alt | 2.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +10.8) | — |
| [[LoVo (line)]] | wt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.109× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 4.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 6.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | +0.79 | +0.82 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[DPY19L2]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.71 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.69 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[NANOS3]] | +0.68 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CUBN]] | +0.68 | +0.80 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD31]] | +0.66 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[DZIP3]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[SSPN]] | +0.65 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.65 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[ANGPT2]] | +0.65 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | +0.64 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB1]] | +0.64 | +0.61 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAQ1]] | -0.64 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[ATP7B]] | -0.62 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[CPSF4]] | -0.61 | -0.71 / -0.33 | both halves | 1e-04 |  |
| [[WDR5]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[ERI3]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[PDPR2P]] | -0.58 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[HERC2P2]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TMEM120B]] | -0.57 | -0.65 / -0.27 | both halves | 3e-04 |  |
| [[GTF2E2]] | -0.57 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[DCUN1D2]] | -0.57 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[MTFR1]] | -0.57 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[ANKRD27]] | -0.56 | -0.65 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises DPY19L2P2's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 2.27× lower at baseline in the lines without DPY19L2P2-1 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[ZNF385D]] | B | ZNF385D activity raises DPY19L2P2's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without ZNF385D | 0.021 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises DPY19L2P2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without PLS3-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[RBMS3]] | B | RBMS3 activity raises DPY19L2P2's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without RBMS3 | 0.038 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[BHLHE41]] | B | BHLHE41 activity raises DPY19L2P2's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without BHLHE41 | 0.039 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[CUBN]] | B | CUBN activity raises DPY19L2P2's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.79× lower at baseline in the lines without CUBN | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DPY19L2P2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD20A21P]] | B | ANKRD20A21P activity raises DPY19L2P2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.36× lower at baseline in the lines without ANKRD20A21P | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[KATNAL2]] | B | KATNAL2 activity raises DPY19L2P2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without KATNAL2 | 0.065 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[CNTNAP3]] | B | CNTNAP3 activity raises DPY19L2P2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without CNTNAP3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2 |
| [[MAGI2-AS3]] | B | MAGI2-AS3 activity raises DPY19L2P2's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without MAGI2-AS3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC |
| [[CYGB]] | B | CYGB activity raises DPY19L2P2's level | lines that do not express CYGB (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without CYGB | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | DPY19L2P2's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | DPY19L2P2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.082 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.0, 16.4); signed map (27.5, 3.8). **Vector** length 69.6, 11.3% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +24.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +14.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.5 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +5.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.5 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.0 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DPY19L2 pseudogene 2 |
| Locus type | pseudogene |
| Location | 7q22.1 — chr7:103,175,343-103,277,638 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZp434E092, FLJ36166 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN68](https://www.uniprot.org/uniprotkb/Q6ZN68) (Putative C-mannosyltransferase DPY19L2P2):

> Probable C-mannosyltransferase that mediates C-mannosylation of tryptophan residues on target proteins.

**Summary**, from NCBI Gene [349152](https://www.ncbi.nlm.nih.gov/gene/349152):

> Predicted to enable mannosyltransferase activity. Predicted to be involved in spermatid development. Predicted to be located in membrane. Predicted to be active in nuclear inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21764) · Entrez [349152](https://www.ncbi.nlm.nih.gov/gene/349152) · UniProt [Q6ZN68](https://www.uniprot.org/uniprotkb/Q6ZN68) · Ensembl [ENSG00000170629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170629)

## Data

Gene col 9986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9986); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9986]; `tensor/DDL_lfc|DDL_z.npy` [9986]; `embed/gene_vectors.npy` [9986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9986 or target_col == 9986). Every well: [[DPY19L2P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L2P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
