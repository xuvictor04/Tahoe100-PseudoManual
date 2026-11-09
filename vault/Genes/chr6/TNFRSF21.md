---
symbol: "TNFRSF21"
type: "gene"
col: 7060
ensembl_id: "ENSG00000146072"
name: "TNF receptor superfamily member 21"
location: "6p12.3"
module: 8
arm: "+"
pooled_cpm: 113.82
n_lines_expressing: 35
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 82
direction_downstream: 37
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TNFRSF21

*TNF receptor superfamily member 21* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.35× (z +6.3, q 2e-07, up in 12 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.675× (z -8.1, q 3e-13, down in 27 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB6]] (+0.68, fdr 7e-06), [[SMIM31]] (+0.67, fdr 7e-06), [[ARHGAP42]] (+0.64, fdr 7e-06); moves opposite to [[BLTP3B]] (-0.50, fdr 3e-05), [[FAM228B]] (-0.49, fdr 3e-05), [[DNAAF9]] (-0.48, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[CEACAM1]] → it (grade B ⚠); 37 go from it, the strongest it → [[ARHGAP42]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.3 | 2e-07 | 12/33 (J82, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.2 | 5e-05 | 11/33 (SNU-423, J82, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 1e-04 | 9/33 (SNU-423, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.028 | 12/33 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.065 | 9/34 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.083 | 10/33 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.094 | 11/33 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.094 | 15/33 (COLO 205, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.1 | 0.13 | 7/33 (NCI-H23, RPMI-7951, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.13 | 3/34 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -8.1 | 3e-13 | 27/34 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.748×** | -6.0 | 5e-07 | 24/34 (NCI-H1573, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -5.6 | 3e-06 | 19/32 (KATO III, SHP-77, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -5.3 | 1e-05 | 18/33 (HT-29, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.698×** | -5.3 | 2e-05 | 22/33 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.718×** | -4.8 | 1e-04 | 25/33 (NCI-H1573, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.723×** | -4.5 | 6e-04 | 22/33 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.806×** | -4.5 | 6e-04 | 21/32 (HT-29, COLO 205, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.2 | 0.001 | 20/33 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **0.758×** | -4.0 | 0.003 | 20/32 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.760×** | -4.0 | 0.003 | 21/33 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.764×** | -3.9 | 0.004 | 16/32 (C32, COLO 205, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.783×** | -3.6 | 0.015 | 19/33 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.778×** | -3.5 | 0.017 | 19/29 (SHP-77, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.018 | 19/33 (COLO 205, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -3.4 | 0.020 | 19/33 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.639×** | -3.4 | 0.020 | 14/32 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.850× | -3.3 | 0.026 | 7/33 (C32, NCI-H2347, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.055 | 14/32 (C32, SW 900, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.867× | -2.9 | 0.097 | 14/33 (NCI-H1573, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 718 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -15.9) |
| [[COLO 205 (line)]] | alt | 333 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -14.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.129× (z -12.3) |
| [[KATO III (line)]] | alt | 345 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -12.0) |
| [[BT-474 (line)]] | alt | 86.4 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.300× (z -9.1) |
| [[C32 (line)]] | wt | 123 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -10.3) |
| [[LoVo (line)]] | wt | 283 | 1 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.25× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 554 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -14.0) |
| [[SHP-77 (line)]] | alt | 121 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.3) |
| [[SW1417 (line)]] | alt | 369 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -18.9) |
| [[HepG2_C3A (line)]] | wt | 182 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 249 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -10.0) |
| [[A549 (line)]] | wt | 62.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 189 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.4) |
| [[PANC-1 (line)]] | alt | 59.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.8) |
| [[Hs 766T (line)]] | wt | 93.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.3) |
| [[J82 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.19× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 57.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.369× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 233 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.4) |
| [[SNU-423 (line)]] | alt | 38.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -13.5) |
| [[SW48 (line)]] | wt | 59.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 20.3 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 19.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.74 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 72.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB6]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SMIM31]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP42]] | +0.64 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ST14]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[FHL2]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 | pathway: PPARA activates gene expression |
| [[SLC12A2]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[F2RL1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CEACAM5]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 | same gene group |
| [[FLRT3]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[TMC5]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP3B]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[FAM228B]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DNAAF9]] | -0.48 | -0.42 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 81, C 1. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM1]] | B | CEACAM1 activity raises TNFRSF21's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 4.52× lower at baseline in the lines without CEACAM1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[HS3ST1]] | B | HS3ST1 activity raises TNFRSF21's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 4.77× lower at baseline in the lines without HS3ST1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises TNFRSF21's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 5.67× lower at baseline in the lines without TMPRSS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ADGRF1]] | B | ADGRF1 activity raises TNFRSF21's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 5.37× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[TOX3]] | B | TOX3 activity raises TNFRSF21's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.84× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[CDH1]] | B | CDH1 activity raises TNFRSF21's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 4.67× lower at baseline in the lines without CDH1 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[C1orf116]] | B | C1orf116 activity raises TNFRSF21's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.41× lower at baseline in the lines without C1orf116 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CLIC5]] | B | CLIC5 activity raises TNFRSF21's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.35× lower at baseline in the lines without CLIC5 | 8e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[LINC01559]] | B | LINC01559 activity raises TNFRSF21's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 5.31× lower at baseline in the lines without LINC01559 | 0.001 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[TSPAN1]] | B | TSPAN1 activity raises TNFRSF21's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.90× lower at baseline in the lines without TSPAN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises TNFRSF21's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.49× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TMEM45B]] | B | TMEM45B activity raises TNFRSF21's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.90× lower at baseline in the lines without TMEM45B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 37, C 0. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP42]] | B | TNFRSF21 activity raises ARHGAP42's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.59× lower at baseline in the lines without TNFRSF21 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[MTUS1]] | B | TNFRSF21 activity raises MTUS1's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 4.16× lower at baseline in the lines without TNFRSF21 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[ABHD17C]] | B | TNFRSF21 activity raises ABHD17C's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without TNFRSF21 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[ARHGAP26]] | B | TNFRSF21 activity raises ARHGAP26's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without TNFRSF21 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[AHR]] | B | TNFRSF21 activity raises AHR's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.81× lower at baseline in the lines without TNFRSF21 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[ATP1B1]] | B | TNFRSF21 activity raises ATP1B1's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.40× lower at baseline in the lines without TNFRSF21 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[LIPH]] | B | TNFRSF21 activity raises LIPH's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.97× lower at baseline in the lines without TNFRSF21 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[RIN2]] | B | TNFRSF21 activity raises RIN2's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without TNFRSF21 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[TCIM]] | B | TNFRSF21 activity raises TCIM's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.02× lower at baseline in the lines without TNFRSF21 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[KIAA0040]] | B | TNFRSF21 activity raises KIAA0040's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.42× lower at baseline in the lines without TNFRSF21 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[TMEM45B]] | B | TNFRSF21 activity raises TMEM45B's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 4.70× lower at baseline in the lines without TNFRSF21 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[HNF4A]] | B | TNFRSF21 activity raises HNF4A's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.07× lower at baseline in the lines without TNFRSF21 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.5, 56.1); signed map (55.9, 12.0). **Vector** length 125, 40.9% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +2.1 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -6.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:47,231,532-47,309,905 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DR6, CD358 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Hallmark sets | ANGIOGENESIS, IL6_JAK_STAT3_SIGNALING, IL2_STAT5_SIGNALING |
| Reactome | 10 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75509](https://www.uniprot.org/uniprotkb/O75509) (Tumor necrosis factor receptor superfamily member 21):

> Promotes apoptosis, possibly via a pathway that involves the activation of NF-kappa-B. Can also promote apoptosis mediated by BAX and by the release of cytochrome c from the mitochondria into the cytoplasm. Trophic-factor deprivation triggers the cleavage of surface APP by beta-secretase to release sAPP-beta which is further cleaved to release an N-terminal fragment of APP (N-APP). Negatively regulates oligodendrocyte survival, maturation and myelination. Plays a role in signaling cascades …

**Summary**, from NCBI Gene [27242](https://www.ncbi.nlm.nih.gov/gene/27242):

> This gene encodes a member of the tumor necrosis factor receptor superfamily. The encoded protein activates nuclear factor kappa-B and mitogen-activated protein kinase 8 (also called c-Jun N-terminal kinase 1), and induces cell apoptosis. Through its death domain, the encoded receptor interacts with tumor necrosis factor receptor type 1-associated death domain (TRADD) protein, which is known to mediate signal transduction of tumor necrosis factor receptors. Knockout studies in mice suggest that …

**Accessions** — [HGNC:13469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13469) · Entrez [27242](https://www.ncbi.nlm.nih.gov/gene/27242) · UniProt [O75509](https://www.uniprot.org/uniprotkb/O75509) · Ensembl [ENSG00000146072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146072)

## Data

Gene col 7060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7060); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7060]; `tensor/DDL_lfc|DDL_z.npy` [7060]; `embed/gene_vectors.npy` [7060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7060 or target_col == 7060). Every well: [[TNFRSF21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
