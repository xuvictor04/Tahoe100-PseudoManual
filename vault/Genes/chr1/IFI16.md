---
symbol: "IFI16"
type: "gene"
col: 8718
ensembl_id: "ENSG00000163565"
name: "interferon gamma inducible protein 16"
location: "1q23.1"
module: 32
arm: "+"
pooled_cpm: 174.87
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 37
n_dd_up_clean: 12
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 30
direction_downstream: 66
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFI16

*interferon gamma inducible protein 16* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.97× (z +8.5, q 1e-14, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.205× (z -19.7, q 0e+00, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD9L]] (+0.87, fdr 7e-06), [[XAF1]] (+0.86, fdr 7e-06), [[IFI44L]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[IFIT3]] → it (grade B ⚠); 66 go from it, the strongest it → [[TRIM38]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +8.5 | 1e-14 | 25/30 (NCI-H2347, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.1 | 4e-07 | 16/30 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +5.2 | 3e-05 | 22/29 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.008 | 15/30 (NCI-H2347, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.011 | 20/31 (CFPAC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.012 | 17/31 (CFPAC-1, Panc 03.27, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.7 | 0.013 | 1/32 (HOP62) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.013 | 17/30 (CFPAC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +3.7 | 0.014 | 19/32 (CFPAC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.018 | 17/30 (CFPAC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.018 | 15/30 (HOP62, A-172, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.026 | 22/30 (A498, NCI-H1792, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.037 | 15/30 (A549, A498, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.055 | 17/29 (SNU-423, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.205×** | -19.7 | 0e+00 | 30/30 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.257×** | -16.9 | 0e+00 | 29/30 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.276×** | -16.0 | 0e+00 | 29/30 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.422×** | -15.1 | 0e+00 | 26/31 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.519×** | -11.5 | 2e-28 | 23/31 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.440×** | -10.2 | 2e-22 | 26/30 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -9.6 | 9e-20 | 27/31 (RKO, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.482×** | -9.0 | 1e-17 | 27/31 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.489×** | -8.9 | 5e-17 | 23/31 (A549, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.709×** | -6.0 | 1e-07 | 19/30 (CFPAC-1, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -5.8 | 3e-07 | 21/30 (C32, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.631×** | -5.7 | 6e-07 | 25/30 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -5.3 | 4e-06 | 20/30 (C32, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.458×** | -5.1 | 2e-05 | 26/31 (A-172, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.658×** | -5.0 | 2e-05 | 16/26 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib (drug)]] 5 µM |  | **0.484×** | -4.7 | 9e-05 | 22/30 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 414 | 0 | 18 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0789× (z -24.9) |
| [[RKO (line)]] | wt | 704 | 0 | 16 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -21.8) |
| [[A549 (line)]] | wt | 74.2 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.229× (z -13.1) |
| [[A-172 (line)]] | wt | 381 | 4 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.197× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 366 | 2 | 10 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +8.9) | [[Tofacitinib (drug)]] 5 µM 0.268× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 415 | 4 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +13.4) | [[Tofacitinib (drug)]] 5 µM 0.260× (z -20.1) |
| [[RPMI-7951 (line)]] | alt | 448 | 2 | 10 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.37× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.128× (z -21.5) |
| [[C32 (line)]] | wt | 1,250 | 2 | 9 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.35× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.206× (z -16.9) |
| [[HS-578T (line)]] | alt | 206 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.140× (z -19.1) |
| [[J82 (line)]] | alt | 177 | 5 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.56× (z +9.9) | [[Tofacitinib (drug)]] 5 µM 0.443× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 358 | 1 | 9 | [[Harringtonine (drug)]] 0.5 µM 2.20× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -18.3) |
| [[COLO 205 (line)]] | alt | 103 | 0 | 9 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0818× (z -12.5) |
| [[A498 (line)]] | wt | 259 | 0 | 8 | — | [[Tofacitinib (drug)]] 5 µM 0.299× (z -16.0) |
| [[KATO III (line)]] | alt | 94.6 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.0990× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 319 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 182 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 177 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.236× (z -15.1) |
| [[CHP-212 (line)]] | wt | 438 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -15.6) |
| [[Hs 766T (line)]] | wt | 330 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 186 | 3 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.57× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.229× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 5 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 253 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -19.1) |
| [[NCI-H460 (line)]] | wt | 175 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -16.2) |
| [[SW 900 (line)]] | alt | 343 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -17.6) |
| [[H4 (line)]] | wt | 216 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -19.5) |
| [[HOP62 (line)]] | alt | 96.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -13.2) |
| [[LS 180 (line)]] | wt | 76.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -12.3) |
| [[SNU-1 (line)]] | wt | 291 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -8.9) |
| [[A-427 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 37.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 25.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 27.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD9L]] | +0.87 | +0.82 / +0.87 | both halves | 7e-06 | STRING 419 |
| [[XAF1]] | +0.86 | +0.75 / +0.89 | both halves | 7e-06 | STRING 459 |
| [[IFI44L]] | +0.86 | +0.75 / +0.88 | both halves | 7e-06 | STRING 565 |
| [[EPSTI1]] | +0.86 | +0.75 / +0.86 | both halves | 7e-06 |  |
| [[SP110]] | +0.85 | +0.77 / +0.88 | both halves | 7e-06 | STRING 415 |
| [[IFIT3]] | +0.85 | +0.78 / +0.86 | both halves | 7e-06 | STRING 606 |
| [[MX1]] | +0.84 | +0.74 / +0.87 | both halves | 7e-06 | STRING 614 |
| [[IFI44]] | +0.84 | +0.74 / +0.86 | both halves | 7e-06 | STRING 700 |
| [[MX2]] | +0.84 | +0.77 / +0.86 | both halves | 7e-06 | STRING 583 |
| [[RSAD2]] | +0.84 | +0.75 / +0.84 | both halves | 7e-06 | STRING 572 |
| [[IFI35]] | +0.83 | +0.71 / +0.86 | both halves | 7e-06 | STRING 584 |
| [[PARP9]] | +0.83 | +0.71 / +0.86 | both halves | 7e-06 | STRING 597 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 17, C 13. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT3]] | B | IFIT3 activity raises IFI16's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 6.81× lower at baseline in the lines without IFIT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[IFITM1]] | B | IFITM1 activity raises IFI16's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 3.50× lower at baseline in the lines without IFITM1 | 0.011 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[NRIR]] | B | NRIR activity raises IFI16's level | lines that do not express NRIR (14) vs lines expressing it (36) | 3.36× lower at baseline in the lines without NRIR | 0.016 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[DDX60L]] | B | DDX60L activity raises IFI16's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 6.45× lower at baseline in the lines without DDX60L | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises IFI16's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.94× lower at baseline in the lines without EPSTI1 | 0.031 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[OAS2]] | B | OAS2 activity raises IFI16's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 4.32× lower at baseline in the lines without OAS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers IFI16's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[UBA7]] | B | UBA7 activity raises IFI16's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 3.50× lower at baseline in the lines without UBA7 | 0.043 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises IFI16's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.18× lower at baseline in the lines without OAS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[NLRC5]] | B | NLRC5 activity raises IFI16's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 3.91× lower at baseline in the lines without NLRC5 | 0.051 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises IFI16's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without MX1 | 0.052 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SLC15A3]] | B | SLC15A3 activity raises IFI16's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 3.68× lower at baseline in the lines without SLC15A3 | 0.055 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |

### Downstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 53, C 13. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM38]] | B | IFI16 activity raises TRIM38's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.59× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[ALPK1]] | B | IFI16 activity raises ALPK1's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IL7]] | B | IFI16 activity raises IL7's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.50× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[DDX60]] | B | IFI16 activity raises DDX60's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.72× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[GBP3]] | B | IFI16 activity raises GBP3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.68× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[B2M]] | B | IFI16 activity raises B2M's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[SAMD9]] | B | IFI16 activity raises SAMD9's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 4.13× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[CASP4]] | B | IFI16 activity raises CASP4's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without IFI16 | 0.004 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IFIT3]] | B | IFI16 activity raises IFIT3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.28× lower at baseline in the lines without IFI16 | 0.004 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[GBP2]] | B | IFI16 activity raises GBP2's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.69× lower at baseline in the lines without IFI16 | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[GBP1]] | B | IFI16 activity raises GBP1's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 3.80× lower at baseline in the lines without IFI16 | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[SP100]] | B | IFI16 activity raises SP100's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.17× lower at baseline in the lines without IFI16 | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.863). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.1, 53.0); signed map (64.1, 30.8). **Vector** length 144, 49.4% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.72 to 56); *interferon gamma response* (hallmark, mean cos +0.73 to 60); *interferon* (control, mean cos +0.80 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +3.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.3 | -15.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.7 | -11.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.6 | -9.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.4 | -10.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.3 | -8.9 |

## What is on record

|  |  |
|---|---|
| Name | interferon gamma inducible protein 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:158,999,968-159,055,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFNGIP1, PYHIN2 |
| Gene groups (HGNC) | Pyrin domain containing; Pyrin and HIN domain family |
| Reactome | 4 pathways, smallest: IRF3-mediated induction of type I IFN; STING mediated induction of host immune responses; Cytosolic sensors of pathogen-associated DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16666](https://www.uniprot.org/uniprotkb/Q16666) (Gamma-interferon-inducible protein 16):

> Binds double-stranded DNA. Binds preferentially to supercoiled DNA and cruciform DNA structures. Seems to be involved in transcriptional regulation. May function as a transcriptional repressor. Could have a role in the regulation of hematopoietic differentiation through activation of unknown target genes. Controls cellular proliferation by modulating the functions of cell cycle regulatory factors including p53/TP53 and the retinoblastoma protein. May be involved in TP53-mediated transcriptional …

**Summary**, from NCBI Gene [3428](https://www.ncbi.nlm.nih.gov/gene/3428):

> This gene encodes a member of the HIN-200 (hematopoietic interferon-inducible nuclear antigens with 200 amino acid repeats) family of cytokines. The encoded protein contains domains involved in DNA binding, transcriptional regulation, and protein-protein interactions. The protein localizes to the nucleoplasm and nucleoli, and interacts with p53 and retinoblastoma-1. It modulates p53 function, and inhibits cell growth in the Ras/Raf signaling pathway. Alternatively spliced transcript variants …

**Accessions** — [HGNC:5395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5395) · Entrez [3428](https://www.ncbi.nlm.nih.gov/gene/3428) · UniProt [Q16666](https://www.uniprot.org/uniprotkb/Q16666) · Ensembl [ENSG00000163565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163565)

## Data

Gene col 8718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8718); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8718]; `tensor/DDL_lfc|DDL_z.npy` [8718]; `embed/gene_vectors.npy` [8718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8718 or target_col == 8718). Every well: [[IFI16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
