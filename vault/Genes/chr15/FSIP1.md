---
symbol: "FSIP1"
type: "gene"
col: 7451
ensembl_id: "ENSG00000150667"
name: "fibrous sheath interacting protein 1"
location: "15q14"
module: 75
arm: "+"
pooled_cpm: 8.06
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# FSIP1

*fibrous sheath interacting protein 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.83× (z +22.3, q 0e+00, up in 39 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0829×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0792×; ⚠ cell-cycle shift, explains ~43% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0966×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUBN]] (+0.64, fdr 1e-05), [[RBMS3-AS3]] (+0.64, fdr 1e-05), [[DGKI]] (+0.64, fdr 3e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GPR176]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +22.3 | 0e+00 | 39/44 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +16.2 | 0e+00 | 27/32 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +15.2 | 0e+00 | 13/15 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +14.7 | 0e+00 | 33/43 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +12.6 | 2e-34 | 15/22 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +11.6 | 3e-29 | 37/47 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +11.0 | 2e-26 | 28/46 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +9.2 | 2e-18 | 23/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.1 | 9e-18 | 22/40 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +8.4 | 4e-15 | 27/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +7.6 | 1e-12 | 19/47 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.4 | 7e-09 | 19/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.7 | 6e-07 | 17/48 (HOP62, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.6 | 7e-07 | 10/36 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.2 | 1e-05 | 11/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 3e-04 | 8/46 (SW480, A549, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.3 | 4e-04 | 15/46 (hTERT-HPNE, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.011 | 10/46 (HOP62, J82, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.17× | +3.4 | 0.015 | 4/46 (NCI-H1573, C-33 A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7451.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0829×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0792×; ⚠ cell-cycle shift, explains ~43% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0966×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.796× | -3.5 | 0.22 | 14/46 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Phenytoin (sodium) (drug)]] 0.05 µM |  | 0.787× | -3.4 | 0.22 | 8/46 (AN3 CA, NCI-H1573, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 5 µM |  | 0.814× | -3.1 | 0.22 | 8/47 (J82, AsPC-1, …) | top dose only |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.815× | -3.1 | 0.22 | 6/47 (NCI-H460, BT-474, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.805× | -3.0 | 0.22 | 8/39 (A-172, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.819× | -3.0 | 0.22 | 6/47 (SW 900, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 10.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +22.8) | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +13.9) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0792× (z -9.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 11.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +11.6) | — |
| [[A-172 (line)]] | wt | 5.73 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.36× (z +9.6) | — |
| [[A498 (line)]] | wt | 6.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +12.1) | — |
| [[H4 (line)]] | wt | 13.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +16.7) | — |
| [[HS-578T (line)]] | alt | 10.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 6.65 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +10.0) | [[Thymol (drug)]] 0.5 µM 0.0966× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +17.3) | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.09× (z +8.7) | — |
| [[C32 (line)]] | wt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 6.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 7.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +14.7) | — |
| [[J82 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0829× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 9.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +8.9) | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUBN]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[RBMS3-AS3]] | +0.64 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[DGKI]] | +0.64 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[CSMD1]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MYO16]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[CFAP54]] | +0.62 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[COL21A1]] | +0.62 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.61 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[MYOSLID]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP15]] | +0.61 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[BTD]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR176]] | B | GPR176 activity raises FSIP1's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without GPR176 | 0.019 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1 |
| [[THBS1]] | B | THBS1 activity raises FSIP1's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without THBS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[DPYS]] | B | DPYS activity raises FSIP1's level | lines that do not express DPYS (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without DPYS | 0.084 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent |
| [[PAPLN]] | B | PAPLN activity raises FSIP1's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without PAPLN | 0.092 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.2, 24.2); signed map (34.2, 11.6). **Vector** length 61.3, 8.75% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +22.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | +1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | fibrous sheath interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:39,588,357-39,782,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35989 |
| Matched by | ensembl_id |

UniProt [Q8NA03](https://www.uniprot.org/uniprotkb/Q8NA03) carries no function annotation.

**Summary**, from NCBI Gene [161835](https://www.ncbi.nlm.nih.gov/gene/161835):

> Predicted to act upstream of or within several processes, including axoneme assembly; homeostasis of number of cells within a tissue; and vesicle organization. Predicted to be active in acrosomal vesicle; nucleus; and sperm head. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21674) · Entrez [161835](https://www.ncbi.nlm.nih.gov/gene/161835) · UniProt [Q8NA03](https://www.uniprot.org/uniprotkb/Q8NA03) · Ensembl [ENSG00000150667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150667)

## Data

Gene col 7451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7451); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7451]; `tensor/DDL_lfc|DDL_z.npy` [7451]; `embed/gene_vectors.npy` [7451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7451 or target_col == 7451). Every well: [[FSIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
