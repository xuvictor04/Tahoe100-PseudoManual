---
symbol: "MYO5B"
type: "gene"
col: 9450
ensembl_id: "ENSG00000167306"
name: "myosin VB"
location: "18q21.1"
module: 31
arm: "+"
pooled_cpm: 125.08
n_lines_expressing: 24
n_dd_up: 30
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 59
direction_downstream: 92
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MYO5B

*myosin VB* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +15.5, q 0e+00, up in 7 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.636× (z -8.7, q 2e-15, down in 21 of 22 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.827× (z -5.4, q 2e-05, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC9]] (+0.68, fdr 7e-06), [[CDH1]] (+0.68, fdr 1e-05), [[DAPP1]] (+0.67, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[EPS8L1]] → it (grade B ⚠); 92 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9450.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +15.5 | 0e+00 | 7/22 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.50×** | +11.4 | 1e-27 | 17/23 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.77×** | +11.3 | 3e-27 | 19/22 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +11.1 | 1e-26 | 11/22 (SW480, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.1 | 2e-26 | 3/23 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +10.2 | 3e-22 | 5/22 (NCI-H2030, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +10.1 | 4e-22 | 13/22 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.7 | 3e-20 | 1/23 (A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +9.5 | 8e-20 | 13/22 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +9.2 | 1e-18 | 15/22 (SW480, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.59×** | +9.2 | 1e-18 | 16/22 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +9.1 | 4e-18 | 15/22 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.9 | 3e-17 | 9/22 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.49×** | +7.9 | 1e-13 | 17/22 (COLO 205, LS 180, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +7.8 | 2e-13 | 14/22 (BT-474, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.45×** | +7.0 | 6e-11 | 19/22 (COLO 205, LS 180, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.1 | 1e-05 | 0/24 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +5.0 | 1e-05 | 15/22 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 5e-05 | 13/22 (SW480, SW48, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9450.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -8.7 | 2e-15 | 21/22 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -5.4 | 2e-05 | 14/22 (NCI-H2347, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.829×** | -5.3 | 2e-05 | 13/22 (A498, Panc 03.27, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **0.782×** | -5.1 | 6e-05 | 12/23 (CFPAC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.647×** | -4.5 | 6e-04 | 13/22 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.800×** | -4.1 | 0.003 | 2/22 (C32, SW48) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.868× | -4.0 | 0.004 | 7/22 (A498, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.866× | -4.0 | 0.004 | 9/23 (SW48, CFPAC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.822×** | -3.9 | 0.005 | 12/22 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.9 | 0.005 | 8/22 (A498, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.826×** | -3.8 | 0.007 | 12/22 (NCI-H1573, KATO III, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.837× | -3.6 | 0.016 | 0/23 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.838× | -3.5 | 0.017 | 7/22 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.889× | -3.3 | 0.033 | 3/22 (C32, SW48, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.033 | 1/22 (C32) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.896× | -3.1 | 0.055 | 10/22 (BT-474, HT-29, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.055 | 7/22 (A498, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.058 | 5/22 (LoVo, KATO III, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9450. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 303 | 1 | 9 (7 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.36× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 371 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -16.8) |
| [[LS 180 (line)]] | wt | 413 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 41.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.03× (z +13.4) | — |
| [[NCI-H2347 (line)]] | alt | 381 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -11.3) |
| [[SW48 (line)]] | wt | 536 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.4) |
| [[SW480 (line)]] | alt | 71.5 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.22× (z +11.2) | — |
| [[A498 (line)]] | wt | 73.9 | 0 | 3 | — | [[Triamcinolone (drug)]] 5 µM 0.515× (z -8.9) |
| [[C32 (line)]] | wt | 49.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (drug)]] 5 µM 0.289× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.316× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 36.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.66× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 297 | 1 | 1 | [[Peretinoin (drug)]] 5 µM 3.70× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.8) |
| [[HT-29 (line)]] | alt | 322 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -15.3) |
| [[SW1417 (line)]] | alt | 342 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -15.2) |
| [[A-427 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 363 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 209 | 1 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 3.51× (z +9.8) ⚠ unreliable plate only | — |
| [[KATO III (line)]] | alt | 264 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -8.6) |
| [[LoVo (line)]] | wt | 461 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -10.7) |
| [[A-172 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 20.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 15.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9450), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CDH1]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[DAPP1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L1]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[KPNA7]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CLDN4]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FAM83B]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[C1orf116]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SEMA3B]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 | same gene group |
| [[CRYBG2]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[DSC2]] | +0.60 | +0.61 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 11, C 48. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | EPS8L1 activity raises MYO5B's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 5.16× lower at baseline in the lines without EPS8L1 | 0.007 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises MYO5B's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 4.90× lower at baseline in the lines without MYO1D | 0.008 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises MYO5B's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.70× lower at baseline in the lines without PLEKHG1 | 0.008 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[LMO7]] | B | LMO7 activity raises MYO5B's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 4.24× lower at baseline in the lines without LMO7 | 0.016 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[F2RL1]] | B | F2RL1 activity raises MYO5B's level | lines that do not express F2RL1 (20) vs lines expressing it (30) | 4.35× lower at baseline in the lines without F2RL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRSS22, ENSG00000267748, CDH1 |
| [[SEMA3B]] | B | SEMA3B activity raises MYO5B's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.86× lower at baseline in the lines without SEMA3B | 0.027 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises MYO5B's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.58× lower at baseline in the lines without GRHL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises MYO5B's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 3.83× lower at baseline in the lines without KPNA7 | 0.067 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[SDCBP2]] | B | SDCBP2 activity raises MYO5B's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 4.12× lower at baseline in the lines without SDCBP2 | 0.078 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[ADGRF4]] | B | ADGRF4 activity raises MYO5B's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 3.06× lower at baseline in the lines without ADGRF4 | 0.087 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[RALGPS2]] | B | RALGPS2 activity raises MYO5B's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 3.97× lower at baseline in the lines without RALGPS2 | 0.093 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[CDH1]] | C | CDH1 activity raises MYO5B's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 14.69× lower at baseline in the lines without CDH1 | 4e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |

### Downstream of this gene

*92 arrows, 92 of them with an alert ⚠; grade A 0, B 44, C 48. Shown: the 12 strongest; 80 more arrows (80 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | MYO5B activity raises EPS8L1's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.92× lower at baseline in the lines without MYO5B | 3e-04 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[PATJ]] | B | MYO5B activity raises PATJ's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.50× lower at baseline in the lines without MYO5B | 5e-04 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[DSG2]] | B | MYO5B activity raises DSG2's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[SEMA3B]] | B | MYO5B activity raises SEMA3B's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.33× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[ANXA11]] | B | MYO5B activity raises ANXA11's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[MYO1D]] | B | MYO5B activity raises MYO1D's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.72× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[KPNA7]] | B | MYO5B activity raises KPNA7's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.85× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[CBR3-AS1]] | B | MYO5B activity raises CBR3-AS1's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[EZR]] | B | MYO5B activity raises EZR's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without MYO5B | 0.001 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[LMO7]] | B | MYO5B activity raises LMO7's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.68× lower at baseline in the lines without MYO5B | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[ARHGAP27]] | B | MYO5B activity raises ARHGAP27's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without MYO5B | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[TES]] | B | MYO5B activity raises TES's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without MYO5B | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, 57.3); signed map (55.7, 7.6). **Vector** length 117, 46.8% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +11.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.5 | +11.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +11.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.2 | +7.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.6 | +3.0 |
|  | [[NG25 (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | myosin VB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:49,822,789-50,195,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1119 |
| Gene groups (HGNC) | Myosin heavy chains, class V; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Vasopressin regulates renal water homeostasis via Aquaporins; Aquaporin-mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULV0](https://www.uniprot.org/uniprotkb/Q9ULV0) (Unconventional myosin-Vb):

> May be involved in vesicular trafficking via its association with the CART complex. The CART complex is necessary for efficient transferrin receptor recycling but not for EGFR degradation. Required in a complex with RAB11A and RAB11FIP2 for the transport of NPC1L1 to the plasma membrane. Together with RAB11A participates in CFTR trafficking to the plasma membrane and TF (transferrin) recycling in nonpolarized cells. Together with RAB11A and RAB8A participates in epithelial cell polarization. …

**Summary**, from NCBI Gene [4645](https://www.ncbi.nlm.nih.gov/gene/4645):

> The protein encoded by this gene, together with other proteins, may be involved in plasma membrane recycling. Mutations in this gene are associated with microvillous inclusion disease. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:7603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7603) · Entrez [4645](https://www.ncbi.nlm.nih.gov/gene/4645) · UniProt [Q9ULV0](https://www.uniprot.org/uniprotkb/Q9ULV0) · Ensembl [ENSG00000167306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167306)

## Data

Gene col 9450: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9450); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9450, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9450]; `tensor/DDL_lfc|DDL_z.npy` [9450]; `embed/gene_vectors.npy` [9450]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9450 or target_col == 9450). Every well: [[MYO5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
