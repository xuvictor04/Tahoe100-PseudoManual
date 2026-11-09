---
symbol: "HNF1A-AS1"
type: "gene"
col: 14273
ensembl_id: "ENSG00000241388"
name: "HNF1A antisense RNA 1"
location: "12q24.31"
module: 44
arm: "+"
pooled_cpm: 8.46
n_lines_expressing: 19
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 81
direction_downstream: 101
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# HNF1A-AS1

*HNF1A antisense RNA 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.24× (z +21.9, q 0e+00, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.595× (z -4.4, q 0.006, down in 10 of 16 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0595×, HT-29 0.108×, CFPAC-1 0.0784×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (COLO 205 0.0249×, HT-29 0.0680×); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (HT-29 0.0997×, COLO 205 0.148×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR15L]] (+0.77, fdr 7e-06), [[MGAM2]] (+0.77, fdr 7e-06), [[BCL2L15]] (+0.77, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 81 arrows point to it, the strongest [[MAP2K6]] → it (grade B ⚠); 101 go from it, the strongest it → [[DIP2C-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.24×** | +21.9 | 0e+00 | 8/14 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.54×** | +15.1 | 0e+00 | 2/15 (LoVo, HEC-1-A) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.80×** | +12.8 | 4e-35 | 1/5 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.00×** | +11.7 | 1e-29 | 5/13 (BT-474, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.15×** | +9.7 | 3e-20 | 5/16 (SW480, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +8.2 | 3e-14 | 2/10 (A549, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.7 | 1e-09 | 5/16 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +6.1 | 7e-08 | 3/15 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 9e-04 | 11/15 (KATO III, CFPAC-1, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **2.48×** | +4.0 | 0.003 | 9/13 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.6 | 0.015 | 2/11 (LoVo, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.019 | 2/15 (COLO 205, HepG2/C3A) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.019 | 10/15 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.019 | 6/15 (KATO III, SW480, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.026 | 4/15 (KATO III, HEC-1-A, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.026 | 9/16 (LoVo, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.038 | 3/15 (COLO 205, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.038 | 2/13 (SW480, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.038 | 5/15 (COLO 205, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14273.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (COLO 205 0.0595×, HT-29 0.108×, CFPAC-1 0.0784×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (COLO 205 0.0249×, HT-29 0.0680×); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (HT-29 0.0997×, COLO 205 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.595×** | -4.4 | 0.006 | 10/16 (COLO 205, HT-29, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -4.1 | 0.012 | 11/16 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.633×** | -3.9 | 0.018 | 11/16 (COLO 205, HT-29, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.467× | -3.4 | 0.10 | 5/15 (COLO 205, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.674× | -3.2 | 0.14 | 8/16 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.693× | -3.1 | 0.15 | 11/16 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.694× | -3.1 | 0.15 | 6/16 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.0 | 0.18 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 210 | 0 | 31 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -26.4) |
| [[HT-29 (line)]] | alt | 44.9 | 0 | 28 (12 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.0997× (z -19.7) |
| [[CFPAC-1 (line)]] | alt | 53.6 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -16.6) |
| [[LS 180 (line)]] | wt | 38.1 | 0 | 13 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0401× (z -13.9) |
| [[KATO III (line)]] | alt | 22.8 | 1 | 8 (4 ⚠) | [[Ponatinib (drug)]] 5 µM 6.17× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.0576× (z -14.2) |
| [[LoVo (line)]] | wt | 8.03 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +12.3) | [[Digitoxin (drug)]] 0.5 µM 0.135× (z -9.0) |
| [[SW480 (line)]] | alt | 5.29 | 3 | 0 | [[Cobimetinib (drug)]] 5 µM 7.79× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 6.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0690× (z -8.9) |
| [[A-172 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR15L]] | +0.77 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.77 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.77 | +0.83 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[AGR3]] | +0.77 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TSPAN8]] | +0.74 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RORC]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.73 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[A1CF]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[RNF183]] | +0.72 | +0.79 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ARSL]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[BCAS1]] | +0.71 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[SMIM2-AS1]] | +0.71 | +0.72 / +0.62 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 4, C 77. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K6]] | B | MAP2K6 activity raises HNF1A-AS1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without MAP2K6 | 0.015 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises HNF1A-AS1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.46× lower at baseline in the lines without SPATA6L | 0.078 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[HGD]] | B | HGD activity raises HNF1A-AS1's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without HGD | 0.078 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[LINC01091]] | B | LINC01091 activity raises HNF1A-AS1's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.32× lower at baseline in the lines without LINC01091 | 0.086 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[AGR3]] | C | AGR3 activity raises HNF1A-AS1's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 9.36× lower at baseline in the lines without AGR3 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[RNF183]] | C | RNF183 activity raises HNF1A-AS1's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 5.39× lower at baseline in the lines without RNF183 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises HNF1A-AS1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 4.57× lower at baseline in the lines without SMIM2-AS1 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises HNF1A-AS1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 4.15× lower at baseline in the lines without MUC5B | 8e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises HNF1A-AS1's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 6.62× lower at baseline in the lines without TRIM31 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises HNF1A-AS1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 7.53× lower at baseline in the lines without LYZ | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises HNF1A-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without TOX3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises HNF1A-AS1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.61× lower at baseline in the lines without ARHGEF38 | 0.003 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |

### Downstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 21, C 80. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIP2C-AS1]] | B | HNF1A-AS1 activity raises DIP2C-AS1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without HNF1A-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[SH3BGRL2]] | B | HNF1A-AS1 activity raises SH3BGRL2's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.46× lower at baseline in the lines without HNF1A-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[HGD]] | B | HNF1A-AS1 activity raises HGD's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without HNF1A-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[ZNF703]] | B | HNF1A-AS1 activity raises ZNF703's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.83× lower at baseline in the lines without HNF1A-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[BCL2L15]] | B | HNF1A-AS1 activity raises BCL2L15's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without HNF1A-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[BCAR3-AS1]] | B | HNF1A-AS1 activity raises BCAR3-AS1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without HNF1A-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[PLCH1]] | B | HNF1A-AS1 activity raises PLCH1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.21× lower at baseline in the lines without HNF1A-AS1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[HSD11B2]] | B | HNF1A-AS1 activity raises HSD11B2's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without HNF1A-AS1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[SPATA6L]] | B | HNF1A-AS1 activity raises SPATA6L's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.39× lower at baseline in the lines without HNF1A-AS1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[RSPH1]] | B | HNF1A-AS1 activity raises RSPH1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without HNF1A-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[SNTB1]] | B | HNF1A-AS1 activity raises SNTB1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without HNF1A-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[FCGRT]] | B | HNF1A-AS1 activity raises FCGRT's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.34× lower at baseline in the lines without HNF1A-AS1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 51.8); signed map (60.6, 2.4). **Vector** length 84.4, 31.3% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.52 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.52 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +21.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +9.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.8 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | HNF1A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q24.31 — chr12:120,941,728-120,980,968 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ38690, HAS1, HASTER; previously C12orf27, NCRNA00262 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [283460](https://www.ncbi.nlm.nih.gov/gene/283460):

> Biomarker of colon cancer and stomach cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26785) · Entrez [283460](https://www.ncbi.nlm.nih.gov/gene/283460) · Ensembl [ENSG00000241388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241388)

## Data

Gene col 14273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14273); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14273]; `tensor/DDL_lfc|DDL_z.npy` [14273]; `embed/gene_vectors.npy` [14273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14273 or target_col == 14273). Every well: [[HNF1A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNF1A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
