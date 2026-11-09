---
symbol: "SLC3A2"
type: "gene"
col: 9578
ensembl_id: "ENSG00000168003"
name: "solute carrier family 3 member 2"
location: "11q12.3"
module: 133
arm: "+"
pooled_cpm: 81.43
n_lines_expressing: 50
n_dd_up: 52
n_dd_down: 0
n_dd_up_clean: 45
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# SLC3A2

*solute carrier family 3 member 2* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 52 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.13× (z +24.3, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.337×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.449×; ⚠ cell-cycle shift, explains ~15% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBED3]] (+0.72, fdr 7e-06), [[ATF5]] (+0.69, fdr 1e-05), [[BLTP3A]] (+0.69, fdr 7e-06); moves opposite to [[ARPC2]] (-0.55, fdr 3e-05), [[COL13A1]] (-0.55, fdr 2e-05), [[RRM2]] (-0.54, fdr 1e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LURAP1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 52 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.13×** | +24.3 | 0e+00 | 47/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.53×** | +18.3 | 0e+00 | 47/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.80×** | +12.0 | 5e-31 | 46/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +9.6 | 8e-20 | 45/48 (SW480, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.21×** | +9.6 | 8e-20 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +9.5 | 1e-19 | 44/48 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +8.8 | 1e-16 | 41/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +8.2 | 2e-14 | 39/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +7.2 | 5e-11 | 37/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +6.7 | 1e-09 | 43/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +6.4 | 6e-09 | 40/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.70×** | +6.4 | 6e-09 | 39/49 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.69×** | +6.4 | 8e-09 | 40/48 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.69×** | +6.3 | 1e-08 | 44/48 (LoVo, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +5.8 | 2e-07 | 36/48 (SW1417, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 5e-06 | 34/48 (C32, LOX-IMVI, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +5.3 | 5e-06 | 38/49 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.52×** | +5.1 | 1e-05 | 36/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.35×** | +5.1 | 1e-05 | 33/48 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9578.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HT-29 0.337×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.449×; ⚠ cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | 0.765× | -3.3 | 0.60 | 24/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.8 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +22.9) | — |
| [[J82 (line)]] | alt | 107 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +21.2) | — |
| [[SW480 (line)]] | alt | 82.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +16.3) | — |
| [[C32 (line)]] | wt | 53.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +20.0) | — |
| [[HEC-1-A (line)]] | alt | 48.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +18.4) | — |
| [[A549 (line)]] | wt | 64.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.1) | — |
| [[AsPC-1 (line)]] | alt | 39.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +24.0) | — |
| [[LoVo (line)]] | wt | 87.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.449× (z -8.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[LOX-IMVI (line)]] | wt | 36.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +18.5) | — |
| [[A-427 (line)]] | wt | 96.8 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.36× (z +16.9) | — |
| [[A-172 (line)]] | wt | 100 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +21.8) | — |
| [[HT-29 (line)]] | alt | 136 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +19.8) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +22.1) | — |
| [[BT-474 (line)]] | alt | 61.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 88.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +21.3) | — |
| [[HOP62 (line)]] | alt | 40.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +17.9) | — |
| [[Hs 766T (line)]] | wt | 69.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +18.0) | — |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +15.8) | — |
| [[NCI-H23 (line)]] | alt | 40.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +15.9) | — |
| [[NCI-H2347 (line)]] | alt | 90.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +18.2) | — |
| [[Panc 03.27 (line)]] | alt | 80.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +17.8) | — |
| [[RKO (line)]] | wt | 82.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +17.2) | — |
| [[SNU-423 (line)]] | alt | 85.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +18.4) | — |
| [[SW 900 (line)]] | alt | 61.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +15.8) | — |
| [[SW1417 (line)]] | alt | 195 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.5) | — |
| [[A498 (line)]] | wt | 111 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 80.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +16.9) | — |
| [[HCT15 (line)]] | alt | 91.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 100 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +13.9) | — |
| [[KATO III (line)]] | alt | 193 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 98.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 72.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 90.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 99.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 87.1 | 2 | 0 | [[Selinexor (drug)]] 5 µM 3.46× (z +11.9) | — |
| [[SW48 (line)]] | wt | 141 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.47× (z +12.4) | — |
| [[H4 (line)]] | wt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED3]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ATF5]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[BLTP3A]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[NUPR1]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[TMEM268]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PCK2]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DMGDH]] | +0.65 | +0.71 / +0.54 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[NIBAN1]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[LURAP1L-AS1]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HOXD3]] | +0.61 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[LURAP1L]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC2]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[COL13A1]] | -0.55 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[RRM2]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RASA1]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[SLC2A13]] | -0.53 | -0.46 / -0.34 | both halves | 1e-04 | pathway: SLC-mediated transmembrane transport |
| [[MYCBP]] | -0.52 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PHC2]] | -0.51 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[ODF2]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[WWTR1]] | -0.51 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[KHDRBS1]] | -0.51 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[ABTB3]] | -0.51 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ITGB5]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LURAP1L]] | B | LURAP1L activity raises SLC3A2's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.45× lower at baseline in the lines without LURAP1L | 0.030 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[ZNF737]] | B | ZNF737 activity raises SLC3A2's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without ZNF737 | 0.042 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |
| [[HOXB9]] | B | HOXB9 activity raises SLC3A2's level | lines that do not express HOXB9 (17) vs lines expressing it (33) | 1.35× lower at baseline in the lines without HOXB9 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| [[ZBED3]] | C | ZBED3 activity raises SLC3A2's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.7, 46.8); signed map (-12.3, 21.8). **Vector** length 127, 48.8% of its response variance represented; |z| ≥ 3 in 1,501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +12.8 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.9 | +4.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +8.1 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +6.7 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +6.9 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.5 | +5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.5 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +9.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.6 | +4.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.7 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Methotrexate (drug)]] 5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 3 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,856,004-62,888,880 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 4T2HC, 4F2, NACAE, CD98, CD98HC, 4F2HC; previously MDU1 |
| Gene groups (HGNC) | Solute carrier family 3 |
| Hallmark sets | P53_PATHWAY |
| Reactome | 11 pathways, smallest: Tryptophan catabolism; Basigin interactions; Amino acid transport across the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P08195](https://www.uniprot.org/uniprotkb/P08195) (Amino acid transporter heavy chain SLC3A2):

> Acts as a chaperone that facilitates biogenesis and trafficking of functional transporter heterodimers to the plasma membrane. Forms heterodimers with SLC7 family transporters (SLC7A5, SLC7A6, SLC7A7, SLC7A8, SLC7A10 and SLC7A11), a group of amino-acid antiporters. Heterodimers function as amino acid exchangers, the specificity of the substrate depending on the SLC7A subunit. Heterodimers SLC3A2/SLC7A6 or SLC3A2/SLC7A7 mediate the uptake of dibasic amino acids. Heterodimer SLC3A2/SLC7A11 …

**Summary**, from NCBI Gene [6520](https://www.ncbi.nlm.nih.gov/gene/6520):

> This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants, encoding different isoforms, have been characterized. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:11026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11026) · Entrez [6520](https://www.ncbi.nlm.nih.gov/gene/6520) · UniProt [P08195](https://www.uniprot.org/uniprotkb/P08195) · Ensembl [ENSG00000168003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168003)

## Data

Gene col 9578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9578); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9578]; `tensor/DDL_lfc|DDL_z.npy` [9578]; `embed/gene_vectors.npy` [9578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9578 or target_col == 9578). Every well: [[SLC3A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC3A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
