---
symbol: "COL21A1"
type: "gene"
col: 4562
ensembl_id: "ENSG00000124749"
name: "collagen type XXI alpha 1 chain"
location: "6p12.1"
module: 90
arm: "+"
pooled_cpm: 3.12
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# COL21A1

*collagen type XXI alpha 1 chain* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.90× (z +20.4, q 0e+00, up in 26 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.175×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.149×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0760×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02306]] (+0.79, fdr 7e-06), [[FAT3]] (+0.75, fdr 7e-06), [[CLVS1]] (+0.74, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ASCL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.90×** | +20.4 | 0e+00 | 26/30 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.61×** | +19.8 | 0e+00 | 24/28 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.96×** | +14.5 | 1e-45 | 18/26 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.98×** | +13.0 | 9e-37 | 27/33 (A-172, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.36×** | +12.0 | 6e-31 | 7/13 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +10.5 | 1e-23 | 1/2 (SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.85×** | +10.1 | 3e-22 | 2/6 (PANC-1, SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.34×** | +9.8 | 9e-21 | 15/40 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.10×** | +9.2 | 2e-18 | 27/37 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.19×** | +9.0 | 1e-17 | 22/38 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +6.8 | 7e-10 | 11/22 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.38×** | +6.7 | 1e-09 | 14/37 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +5.9 | 2e-07 | 13/30 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +5.2 | 7e-06 | 13/34 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.1 | 0.001 | 12/42 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 7/40 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.002 | 11/44 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 8/41 (HOP62, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.175×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.149×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0760×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.683× | -3.1 | 0.84 | 9/34 (SHP-77, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 2.48 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +11.6) | — |
| [[LoVo (line)]] | wt | 2.44 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.3× (z +16.8) | — |
| [[PANC-1 (line)]] | alt | 2.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -10.4) |
| [[A-172 (line)]] | wt | 1.47 | 1 | 0 | [[Auranofin (drug)]] 5 µM 61.8× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.37× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 1.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.0× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0760× (z -10.0) |
| [[HT-29 (line)]] | alt | 1.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 1.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.84× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.799 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.816 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.913 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02306]] | +0.79 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[FAT3]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[NEB]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[GUCY1A2]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[SYNPO2]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[LINC02268]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[UNC80]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ELAPOR1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[GRM8]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | B | ASCL1 activity raises COL21A1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.33× lower at baseline in the lines without ASCL1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[CDH6]] | B | CDH6 activity raises COL21A1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without CDH6 | 0.030 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[DGKB]] | B | DGKB activity raises COL21A1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without DGKB | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers COL21A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SETD1B]] | B | the direction of SETD1B's effect on COL21A1's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of SETD1B in 8 lines vs 32 not recorded | the SETD1B-altered lines respond 0.41× as strongly (z diff +1.73); strongest at Dinaciclib 0.5 µM: 0.25x vs 2.06x (z diff +8.8) | 0.048 | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A; target measured in part of the lines; artifact flags |
| [[POU6F2]] | B | POU6F2 activity raises COL21A1's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.81× lower at baseline in the lines without POU6F2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[LINC01287]] | B | LINC01287 activity raises COL21A1's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without LINC01287 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.1, 29.5); signed map (34.9, 16.0). **Vector** length 61.9, 9.98% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +19.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +20.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +9.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXI alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:56,056,590-56,394,094 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibril associated collagens with interrupted triple helices |
| Reactome | 4 pathways, smallest: Collagen chain trimerization; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

UniProt [Q96P44](https://www.uniprot.org/uniprotkb/Q96P44) carries no function annotation.

**Summary**, from NCBI Gene [81578](https://www.ncbi.nlm.nih.gov/gene/81578):

> This gene encodes the alpha chain of type XXI collagen, a member of the FACIT (fibril-associated collagens with interrupted helices) collagen family. Type XXI collagen is localized to tissues containing type I collagen and maintains the integrity of the extracellular matrix. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:17025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17025) · Entrez [81578](https://www.ncbi.nlm.nih.gov/gene/81578) · UniProt [Q96P44](https://www.uniprot.org/uniprotkb/Q96P44) · Ensembl [ENSG00000124749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124749)

## Data

Gene col 4562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4562); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4562]; `tensor/DDL_lfc|DDL_z.npy` [4562]; `embed/gene_vectors.npy` [4562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4562 or target_col == 4562). Every well: [[COL21A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL21A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
