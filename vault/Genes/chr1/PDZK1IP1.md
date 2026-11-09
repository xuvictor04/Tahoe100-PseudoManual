---
symbol: "PDZK1IP1"
type: "gene"
col: 8502
ensembl_id: "ENSG00000162366"
name: "PDZK1 interacting protein 1"
location: "1p33"
module: 8
arm: "+"
pooled_cpm: 6.62
n_lines_expressing: 18
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 78
direction_downstream: 100
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PDZK1IP1

*PDZK1 interacting protein 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.69× (z +7.8, q 3e-12, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 2.66× (z +5.2, q 4e-05, up in 15 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.464× (z -4.1, q 0.018, down in 14 of 16 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.476× (z -3.9, q 0.018, down in 12 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (HT-29 0.0764×, COLO 205 0.0230×, KATO III 0.0221×; ⚠ cell-cycle shift, explains ~58% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (COLO 205 0.0375×, KATO III 0.0316×, HT-29 0.163×; ⚠ cell-cycle shift, explains ~52% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (COLO 205 0.0283×, HT-29 0.141×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (COLO 205 0.132×, HT-29 0.258×); [[Auranofin (drug)]] 5 µM in 1 line (COLO 205 0.0291×); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.144×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP7]] (+0.80, fdr 7e-06), [[TRIM31]] (+0.78, fdr 7e-06), [[MUC4]] (+0.76, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 78 arrows point to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); 100 go from it, the strongest it → [[MUC20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.69×** | +7.8 | 3e-12 | 1/7 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +5.9 | 1e-06 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **2.66×** | +5.2 | 4e-05 | 15/16 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +5.1 | 4e-05 | 3/14 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **2.52×** | +4.9 | 1e-04 | 15/16 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.44×** | +4.5 | 6e-04 | 13/16 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **2.28×** | +4.3 | 0.001 | 14/16 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.007 | 12/16 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +3.5 | 0.024 | 8/13 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **3.44×** | +3.5 | 0.024 | 8/13 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.61×** | +3.4 | 0.036 | 9/16 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.94×** | +3.3 | 0.036 | 12/15 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.89×** | +3.3 | 0.036 | 8/16 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.96×** | +3.3 | 0.036 | 11/16 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.80×** | +3.3 | 0.036 | 11/16 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **3.17×** | +3.1 | 0.061 | 10/15 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.98×** | +3.1 | 0.061 | 13/15 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.80×** | +3.1 | 0.065 | 8/16 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (HT-29 0.0764×, COLO 205 0.0230×, KATO III 0.0221×; ⚠ cell-cycle shift, explains ~58% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (COLO 205 0.0375×, KATO III 0.0316×, HT-29 0.163×; ⚠ cell-cycle shift, explains ~52% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (COLO 205 0.0283×, HT-29 0.141×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (COLO 205 0.132×, HT-29 0.258×); [[Auranofin (drug)]] 5 µM in 1 line (COLO 205 0.0291×); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.464×** | -4.1 | 0.018 | 14/16 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.476×** | -3.9 | 0.018 | 12/16 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.484×** | -3.8 | 0.018 | 14/16 (COLO 205, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.486×** | -3.8 | 0.018 | 16/16 (COLO 205, KATO III, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.505×** | -3.6 | 0.033 | 12/15 (COLO 205, NCI-H2347, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.75 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 15.0 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0230× (z -12.6) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0291× (z -11.8) |
| [[HT-29 (line)]] | alt | 42.6 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0764× (z -12.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.5) |
| [[KATO III (line)]] | alt | 5.13 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0221× (z -11.8) ⚠ cell-cycle shift, explains ~58% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.97 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.06× (z +8.6) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.240 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP7]] | +0.80 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 | STRING 441 |
| [[WFDC2]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TNFSF10]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[SLC34A2]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CFB]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[MUC1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LGALS9]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TMC5]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[STEAP4]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.69 | +0.75 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*78 arrows, 78 of them with an alert ⚠; grade A 0, B 12, C 66. Shown: the 12 strongest; 66 more arrows (66 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises PDZK1IP1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.02× lower at baseline in the lines without ELF3-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises PDZK1IP1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.64× lower at baseline in the lines without GBP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[GBP1]] | B | GBP1 activity raises PDZK1IP1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without GBP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[PLCH1]] | B | PLCH1 activity raises PDZK1IP1's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without PLCH1 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises PDZK1IP1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without OAS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises PDZK1IP1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without SPATA6L | 0.046 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PDZK1IP1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[FLRT3]] | B | FLRT3 activity raises PDZK1IP1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.96× lower at baseline in the lines without FLRT3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[HDAC6]] | B | HDAC6 activity raises PDZK1IP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TLR3]] | B | TLR3 activity raises PDZK1IP1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without TLR3 | 0.065 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[PRRG4]] | B | PRRG4 activity raises PDZK1IP1's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without PRRG4 | 0.080 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[MTUS1]] | B | MTUS1 activity raises PDZK1IP1's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without MTUS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |

### Downstream of this gene

*100 arrows, 100 of them with an alert ⚠; grade A 0, B 41, C 59. Shown: the 12 strongest; 88 more arrows (88 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC20]] | B | PDZK1IP1 activity raises MUC20's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 4.46× lower at baseline in the lines without PDZK1IP1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[PRRG4]] | B | PDZK1IP1 activity raises PRRG4's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 3.78× lower at baseline in the lines without PDZK1IP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[CD2AP]] | B | PDZK1IP1 activity raises CD2AP's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without PDZK1IP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[CARD14]] | B | PDZK1IP1 activity raises CARD14's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.89× lower at baseline in the lines without PDZK1IP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[CD2AP]] | B | PDZK1IP1 activity strengthens CD2AP's drug response | lines that do not express PDZK1IP1 (32) vs lines expressing it (17) | the lines without PDZK1IP1 respond 0.71× as strongly (z diff +1.45); strongest at Belinostat 5 µM: 0.82x vs 0.60x (z diff +4.1) | 0.006 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; target measured in part of the lines; artifact flags |
| [[STS]] | B | PDZK1IP1 activity raises STS's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without PDZK1IP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[MVP-DT]] | B | PDZK1IP1 activity raises MVP-DT's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without PDZK1IP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[LINC01504]] | B | PDZK1IP1 activity raises LINC01504's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.84× lower at baseline in the lines without PDZK1IP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[EFNA1]] | B | PDZK1IP1 activity raises EFNA1's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without PDZK1IP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[ELF3-AS1]] | B | PDZK1IP1 activity raises ELF3-AS1's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 3.00× lower at baseline in the lines without PDZK1IP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[LGALS9]] | B | PDZK1IP1 activity raises LGALS9's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without PDZK1IP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[CGN]] | B | PDZK1IP1 activity raises CGN's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 3.67× lower at baseline in the lines without PDZK1IP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, 54.6); signed map (59.6, 2.3). **Vector** length 66.6, 25.9% of its response variance represented; |z| ≥ 3 in 464 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.63 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +4.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PDZK1 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:47,183,582-47,191,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DD96, MAP17, SPAP |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13113](https://www.uniprot.org/uniprotkb/Q13113) (PDZK1-interacting protein 1):

> Auxiliary protein of electrogenic Na(+)-coupled sugar symporter SLC5A2/SGLT2 and SLC5A1/SGLT1. Essential for the transporter activity of SLC5A2/SGLT2 but not SLC5A1/SGLT1.

**Summary**, from NCBI Gene [10158](https://www.ncbi.nlm.nih.gov/gene/10158):

> Involved in D-glucose import across plasma membrane. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16887) · Entrez [10158](https://www.ncbi.nlm.nih.gov/gene/10158) · UniProt [Q13113](https://www.uniprot.org/uniprotkb/Q13113) · Ensembl [ENSG00000162366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162366)

## Data

Gene col 8502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8502); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8502]; `tensor/DDL_lfc|DDL_z.npy` [8502]; `embed/gene_vectors.npy` [8502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8502 or target_col == 8502). Every well: [[PDZK1IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZK1IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
