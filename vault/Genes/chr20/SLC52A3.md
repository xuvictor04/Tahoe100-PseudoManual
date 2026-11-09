---
symbol: "SLC52A3"
type: "gene"
col: 2108
ensembl_id: "ENSG00000101276"
name: "solute carrier family 52 member 3"
location: "20p13"
module: 55
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 24
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 111
direction_downstream: 104
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SLC52A3

*solute carrier family 52 member 3* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.13× (z +10.5, q 6e-23, up in 1 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +9.4, q 1e-18, up in 7 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.639× (z -4.1, q 0.012, down in 5 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.0886×, LoVo 0.132×, COLO 205 0.139×, SW480 0.253×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.0989×, HT-29 0.174×, COLO 205 0.233×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0974×, LoVo 0.112×; ⚠ cell-cycle shift, explains ~50% of this change); [[Ponatinib (drug)]] 0.5 µM in 1 line (KATO III 0.202×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01819]] (+0.78, fdr 7e-06), [[AFAP1L2]] (+0.77, fdr 7e-06), [[HNF4A]] (+0.76, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 111 arrows point to it, the strongest [[LINC00589]] → it (grade B ⚠); 104 go from it, the strongest it → [[ARHGEF16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +10.5 | 6e-23 | 1/10 (PANC-1) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +9.4 | 1e-18 | 7/19 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.59×** | +9.1 | 2e-17 | 10/20 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +7.9 | 4e-13 | 1/6 (SW1417) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.1 | 1e-10 | 3/19 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.1 | 2e-10 | 12/22 (LS 180, SW480, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.41×** | +6.2 | 4e-08 | 1/14 (Hs 766T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +6.0 | 1e-07 | 1/16 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +5.1 | 2e-05 | 3/22 (HCT15, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +5.0 | 3e-05 | 6/21 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +5.0 | 3e-05 | 12/22 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.55×** | +4.4 | 6e-04 | 4/22 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.1 | 0.002 | 0/16 | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.49×** | +3.9 | 0.004 | 0/13 | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.006 | 3/20 (Panc 03.27, A-427, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.007 | 3/18 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Clofarabine (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.015 | 0/21 | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +3.5 | 0.017 | 9/19 (BT-474, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.021 | 1/18 (PANC-1) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.026 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.036 | 0/19 | inconsistent across doses | low cells (technical?) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.050 | 0/18 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2108.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.0886×, LoVo 0.132×, COLO 205 0.139×, SW480 0.253×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.0989×, HT-29 0.174×, COLO 205 0.233×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.0974×, LoVo 0.112×; ⚠ cell-cycle shift, explains ~50% of this change); [[Ponatinib (drug)]] 0.5 µM in 1 line (KATO III 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.639×** | -4.1 | 0.012 | 5/22 (SW480, SW1417, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -4.1 | 0.012 | 8/22 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.717× | -3.3 | 0.16 | 9/22 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 20.7 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0353× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -10.2) |
| [[KATO III (line)]] | alt | 28.4 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -21.4) |
| [[LoVo (line)]] | wt | 8.27 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.8) |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -11.6) |
| [[Hs 766T (line)]] | wt | 9.18 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0762× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.0686× (z -9.0) |
| [[PANC-1 (line)]] | alt | 1.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +13.9) | — |
| [[SW480 (line)]] | alt | 4.09 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.170× (z -9.2) |
| [[BT-474 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 4.82 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0767× (z -8.6) |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.237× (z -9.1) |
| [[A-172 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01819]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[AFAP1L2]] | +0.77 | +0.76 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.76 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[EDAR]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[GPX2]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PLEKHG6]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[KCNH8]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[IGSF9]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*111 arrows, 111 of them with an alert ⚠; grade A 0, B 11, C 100. Shown: the 12 strongest; 99 more arrows (99 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00589]] | B | LINC00589 activity raises SLC52A3's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without LINC00589 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[PCDH1]] | B | PCDH1 activity raises SLC52A3's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without PCDH1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[B3GALT5]] | B | B3GALT5 activity raises SLC52A3's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without B3GALT5 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[SULF2]] | B | SULF2 activity raises SLC52A3's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.38× lower at baseline in the lines without SULF2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[RAPGEF5]] | B | RAPGEF5 activity raises SLC52A3's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without RAPGEF5 | 0.042 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises SLC52A3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.97× lower at baseline in the lines without TJP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[NECTIN1]] | B | NECTIN1 activity raises SLC52A3's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without NECTIN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[HR]] | B | HR activity raises SLC52A3's level | lines that do not express HR (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without HR | 0.078 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises SLC52A3's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without SEPTIN9-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity raises SLC52A3's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.08× lower at baseline in the lines without IGSF9 | 0.087 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[MCF2L]] | B | MCF2L activity raises SLC52A3's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without MCF2L | 0.099 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[C1orf116]] | C | C1orf116 activity raises SLC52A3's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.48× lower at baseline in the lines without C1orf116 | 8e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |

### Downstream of this gene

*104 arrows, 104 of them with an alert ⚠; grade A 0, B 28, C 76. Shown: the 12 strongest; 92 more arrows (92 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF16]] | B | SLC52A3 activity raises ARHGEF16's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without SLC52A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[ACOT11]] | B | SLC52A3 activity raises ACOT11's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.93× lower at baseline in the lines without SLC52A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[MROH7]] | B | SLC52A3 activity raises MROH7's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without SLC52A3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[PIK3C2B]] | B | SLC52A3 activity raises PIK3C2B's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without SLC52A3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TCF7L2]] | B | SLC52A3 activity raises TCF7L2's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without SLC52A3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[ABHD11]] | B | SLC52A3 activity raises ABHD11's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without SLC52A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[ITPKC]] | B | SLC52A3 activity raises ITPKC's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.80× lower at baseline in the lines without SLC52A3 | 0.020 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TICAM1]] | B | SLC52A3 activity raises TICAM1's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without SLC52A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[LINC01290]] | B | SLC52A3 activity raises LINC01290's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 1.75× lower at baseline in the lines without SLC52A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[RTKN]] | B | SLC52A3 activity raises RTKN's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without SLC52A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[SEPTIN9-DT]] | B | SLC52A3 activity raises SEPTIN9-DT's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without SLC52A3 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[SYNGR2]] | B | SLC52A3 activity raises SYNGR2's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 1.65× lower at baseline in the lines without SLC52A3 | 0.029 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, 49.0); signed map (63.8, 10.1). **Vector** length 69.0, 20.1% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +3.3 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.4 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +0.9 | +0.3 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 52 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:760,080-776,015 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA371L19.1, hRFT2, RFVT3, RFT2; previously C20orf54 |
| Gene groups (HGNC) | Solute carrier family 52; Flavoproteins |
| Reactome | 3 pathways, smallest: Vitamin B2 (riboflavin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ40](https://www.uniprot.org/uniprotkb/Q9NQ40) (Solute carrier family 52, riboflavin transporter, member 3):

> Plasma membrane transporter mediating the uptake by cells of the water soluble vitamin B2/riboflavin that plays a key role in biochemical oxidation-reduction reactions of the carbohydrate, lipid, and amino acid metabolism. Humans are unable to synthesize vitamin B2/riboflavin and must obtain it via intestinal absorption.

**Summary**, from NCBI Gene [113278](https://www.ncbi.nlm.nih.gov/gene/113278):

> This gene encodes a riboflavin transporter protein that is strongly expressed in the intestine and likely plays a role in intestinal absorption of riboflavin. The protein is predicted to have eleven transmembrane domains and a cell surface localization signal in the C-terminus. Mutations at this locus have been associated with Brown-Vialetto-Van Laere syndrome and Fazio-Londe disease. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:16187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16187) · Entrez [113278](https://www.ncbi.nlm.nih.gov/gene/113278) · UniProt [Q9NQ40](https://www.uniprot.org/uniprotkb/Q9NQ40) · Ensembl [ENSG00000101276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101276)

## Data

Gene col 2108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2108); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2108]; `tensor/DDL_lfc|DDL_z.npy` [2108]; `embed/gene_vectors.npy` [2108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2108 or target_col == 2108). Every well: [[SLC52A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC52A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
