---
symbol: "SORL1"
type: "gene"
col: 6042
ensembl_id: "ENSG00000137642"
name: "sortilin related receptor 1"
location: "11q24.1"
module: 27
arm: "+"
pooled_cpm: 61.48
n_lines_expressing: 29
n_dd_up: 25
n_dd_down: 38
n_dd_up_clean: 21
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 79
direction_downstream: 90
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SORL1

*sortilin related receptor 1* — 11q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.11× (z +11.3, q 4e-27, up in 8 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +10.3, q 2e-22, up in 14 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.480× (z -11.7, q 1e-28, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF43]] (+0.76, fdr 7e-06), [[AXIN2]] (+0.74, fdr 7e-06), [[LINC02253]] (+0.70, fdr 7e-06); moves opposite to [[OSMR-DT]] (-0.52, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 79 arrows point to it, the strongest [[CXADR]] → it (grade B ⚠); 90 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +11.3 | 4e-27 | 8/20 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +11.3 | 6e-27 | 11/25 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +10.3 | 2e-22 | 14/27 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +8.4 | 4e-15 | 15/26 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +7.7 | 2e-12 | 8/21 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +7.1 | 1e-10 | 15/27 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +6.9 | 3e-10 | 15/27 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.36×** | +6.8 | 5e-10 | 12/27 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +5.8 | 3e-07 | 13/26 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.8 | 1e-04 | 16/27 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.83×** | +4.7 | 1e-04 | 16/25 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 5e-04 | 14/27 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.003 | 7/27 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.007 | 7/28 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.007 | 11/26 (NCI-H1573, AsPC-1, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.007 | 10/25 (CFPAC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.012 | 7/28 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.014 | 8/27 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.014 | 11/28 (CFPAC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.480×** | -11.7 | 1e-28 | 24/26 (HepG2/C3A, HT-29, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -11.1 | 5e-26 | 21/26 (HepG2/C3A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.500×** | -11.0 | 7e-26 | 24/26 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -10.8 | 3e-25 | 22/27 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.509×** | -10.7 | 7e-25 | 23/26 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.535×** | -9.9 | 3e-21 | 26/26 (HepG2/C3A, HT-29, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.663×** | -9.3 | 2e-18 | 22/28 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.563×** | -9.1 | 5e-18 | 25/26 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.598×** | -8.2 | 2e-14 | 20/27 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.581×** | -8.2 | 2e-14 | 23/27 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -7.4 | 8e-12 | 20/26 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -7.1 | 4e-11 | 21/27 (HepG2/C3A, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.646×** | -6.7 | 1e-09 | 14/26 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.658×** | -6.7 | 1e-09 | 21/26 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.663×** | -6.6 | 2e-09 | 23/27 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 555 | 0 | 27 (13 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.115× (z -22.2) |
| [[LoVo (line)]] | wt | 176 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -24.0) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -19.2) |
| [[SW480 (line)]] | alt | 138 | 0 | 18 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -18.1) |
| [[HT-29 (line)]] | alt | 196 | 0 | 13 (5 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0963× (z -17.7) |
| [[PANC-1 (line)]] | alt | 81.7 | 0 | 10 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -15.3) |
| [[COLO 205 (line)]] | alt | 71.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -14.2) |
| [[LS 180 (line)]] | wt | 192 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 59.9 | 1 | 4 (1 ⚠) | [[Radotinib (drug)]] 5 µM 3.21× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.162× (z -10.5) |
| [[HCT15 (line)]] | alt | 90.0 | 0 | 5 | — | [[Bortezomib (drug)]] 0.05 µM 0.139× (z -12.8) |
| [[KATO III (line)]] | alt | 119 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +13.1) ⚠ cell-cycle shift, explains ~11% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -17.5) |
| [[SW48 (line)]] | wt | 331 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 70.1 | 1 | 3 | [[Tofacitinib (drug)]] 5 µM 2.20× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 190 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 54.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -12.9) |
| [[A-427 (line)]] | wt | 26.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.334× (z -12.3) |
| [[CHP-212 (line)]] | wt | 45.7 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0578× (z -11.4) |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.234× (z -8.8) |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.187× (z -9.2) |
| [[SW1417 (line)]] | alt | 125 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.284× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -11.8) |
| [[A-172 (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF43]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[VIL1]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DLEU1]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[TMEM139]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SEMA4G]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[RORC]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[TOX3]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MAP2K6]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSMR-DT]] | -0.52 | -0.59 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 27, C 52. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXADR]] | B | CXADR activity raises SORL1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 4.54× lower at baseline in the lines without CXADR | 0.001 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[LINC00992]] | B | LINC00992 activity raises SORL1's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 3.79× lower at baseline in the lines without LINC00992 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[RNF128]] | B | RNF128 activity raises SORL1's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 2.78× lower at baseline in the lines without RNF128 | 0.008 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[TJP2]] | B | TJP2 activity raises SORL1's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.57× lower at baseline in the lines without TJP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises SORL1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.10× lower at baseline in the lines without SLC44A3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[ANK3]] | B | ANK3 activity raises SORL1's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 3.01× lower at baseline in the lines without ANK3 | 0.021 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[ARHGAP18]] | B | ARHGAP18 activity raises SORL1's level | lines that do not express ARHGAP18 (6) vs lines expressing it (44) | 3.28× lower at baseline in the lines without ARHGAP18 | 0.024 | ⚠ within organs, on part of the lines; also absent: IER3, SLC2A1, SHB |
| [[ATP8B1]] | B | ATP8B1 activity raises SORL1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.08× lower at baseline in the lines without ATP8B1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[CRACR2B]] | B | CRACR2B activity raises SORL1's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without CRACR2B | 0.028 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[NIHCOLE]] | B | NIHCOLE activity raises SORL1's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without NIHCOLE | 0.038 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[TOP2A]] | B | TOP2A activity raises SORL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAPGEF5]] | B | RAPGEF5 activity raises SORL1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.20× lower at baseline in the lines without RAPGEF5 | 0.044 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |

### Downstream of this gene

*90 arrows, 90 of them with an alert ⚠; grade A 0, B 41, C 49. Shown: the 12 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SORL1 activity raises SLC44A3's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.61× lower at baseline in the lines without SORL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[RNF128]] | B | SORL1 activity raises RNF128's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.64× lower at baseline in the lines without SORL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[LRP5]] | B | SORL1 activity raises LRP5's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without SORL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[KSR2]] | B | SORL1 activity raises KSR2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without SORL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[RAB17]] | B | SORL1 activity raises RAB17's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without SORL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[MANSC1]] | B | SORL1 activity raises MANSC1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without SORL1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[PLAC8]] | B | SORL1 activity raises PLAC8's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.57× lower at baseline in the lines without SORL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[FREM2]] | B | SORL1 activity raises FREM2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without SORL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[COPG2IT1]] | B | SORL1 activity raises COPG2IT1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.44× lower at baseline in the lines without SORL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[MTUS1]] | B | SORL1 activity raises MTUS1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 3.70× lower at baseline in the lines without SORL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[SLAIN1]] | B | SORL1 activity raises SLAIN1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without SORL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[TMEM184A]] | B | SORL1 activity raises TMEM184A's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.29× lower at baseline in the lines without SORL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 47.9); signed map (61.7, 12.2). **Vector** length 121, 38.1% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +5.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.4 | +6.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -5.1 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -11.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -9.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -11.0 |

## What is on record

|  |  |
|---|---|
| Name | sortilin related receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.1 — chr11:121,452,314-121,633,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | gp250, LR11, LRP9, SorLA, SorLA-1; previously C11orf32 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92673](https://www.uniprot.org/uniprotkb/Q92673) (Sortilin-related receptor):

> Sorting receptor that directs several proteins to their correct location within the cell (Probable). Along with AP-1 complex, involved Golgi apparatus - endosome sorting. Sorting receptor for APP, regulating its intracellular trafficking and processing into amyloidogenic-beta peptides. Retains APP in the trans-Golgi network, hence preventing its transit through late endosomes where amyloid beta peptides Abeta40 and Abeta42 are generated. May also sort newly produced amyloid-beta peptides to …

**Summary**, from NCBI Gene [6653](https://www.ncbi.nlm.nih.gov/gene/6653):

> This gene encodes a mosaic protein that belongs to at least two families: the vacuolar protein sorting 10 (VPS10) domain-containing receptor family, and the low density lipoprotein receptor (LDLR) family. The encoded protein also contains fibronectin type III repeats and an epidermal growth factor repeat. The encoded preproprotein is proteolytically processed to generate the mature receptor, which likely plays roles in endocytosis and sorting. Mutations in this gene may be associated with …

**Accessions** — [HGNC:11185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11185) · Entrez [6653](https://www.ncbi.nlm.nih.gov/gene/6653) · UniProt [Q92673](https://www.uniprot.org/uniprotkb/Q92673) · Ensembl [ENSG00000137642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137642)

## Data

Gene col 6042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6042); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6042]; `tensor/DDL_lfc|DDL_z.npy` [6042]; `embed/gene_vectors.npy` [6042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6042 or target_col == 6042). Every well: [[SORL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
