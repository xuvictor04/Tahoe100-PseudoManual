---
symbol: "RTN1"
type: "gene"
col: 6358
ensembl_id: "ENSG00000139970"
name: "reticulon 1"
location: "14q23.1"
module: 19
arm: "+"
pooled_cpm: 28.52
n_lines_expressing: 19
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RTN1

*reticulon 1* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.59× (z +13.0, q 1e-35, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.567× (z -5.4, q 3e-05, down in 10 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7A]] (+0.76, fdr 7e-06), [[NRCAM]] (+0.75, fdr 7e-06), [[LINC01035]] (+0.73, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLITRK4]] → it (grade C ⚠); 6 go from it, the strongest it → [[PRSS23-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.59×** | +13.0 | 1e-35 | 13/17 (NCI-H23, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.9 | 2e-16 | 1/15 (AN3 CA) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +8.1 | 2e-13 | 4/12 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.23×** | +7.7 | 2e-12 | 11/15 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +7.6 | 2e-12 | 4/11 (Hs 766T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.2 | 2e-05 | 2/16 (SW 1271, C-33 A) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.64×** | +4.8 | 2e-04 | 7/15 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.5 | 6e-04 | 1/11 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.3 | 0.001 | 7/16 (NCI-H23, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.002 | 11/16 (LOX-IMVI, C32, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.027 | 6/14 (C32, H4, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.052 | 1/17 (C32) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.059 | 4/15 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -5.4 | 3e-05 | 10/15 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.573×** | -5.3 | 3e-05 | 5/15 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -4.5 | 0.002 | 11/15 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -4.0 | 0.010 | 13/16 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.665×** | -3.9 | 0.011 | 7/17 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -3.5 | 0.040 | 8/16 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.703×** | -3.4 | 0.059 | 3/16 (AN3 CA, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -3.2 | 0.094 | 13/15 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.535× | -3.1 | 0.11 | 6/15 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 395 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -16.8) |
| [[NCI-H1792 (line)]] | alt | 42.4 | 1 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 5.54× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 16.4 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.24× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -10.8) |
| [[H4 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.170× (z -10.1) |
| [[SHP-77 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.279× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.19 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7A]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 | same gene group |
| [[NRCAM]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_HEDGEHOG_SIGNALING |
| [[LINC01035]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[DPP10]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[GREM2]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ADGRD1]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 | same gene group |
| [[RHOH]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLITRK4]] | C | SLITRK4 activity raises RTN1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.17× lower at baseline in the lines without SLITRK4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[NRCAM]] | C | NRCAM activity raises RTN1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.84× lower at baseline in the lines without NRCAM | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises RTN1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.38× lower at baseline in the lines without DPP10 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[KCNK2]] | C | KCNK2 activity raises RTN1's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.20× lower at baseline in the lines without KCNK2 | 0.098 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23-AS1]] | B | RTN1 activity raises PRSS23-AS1's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.05× lower at baseline in the lines without RTN1 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530 |
| [[FZD4]] | B | RTN1 activity raises FZD4's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without RTN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530 |
| [[ESM1]] | C | RTN1 activity raises ESM1's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.77× lower at baseline in the lines without RTN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |
| [[CDH11]] | C | RTN1 activity raises CDH11's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.46× lower at baseline in the lines without RTN1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |
| [[NRCAM]] | C | RTN1 activity raises NRCAM's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.39× lower at baseline in the lines without RTN1 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |
| [[SLC7A2]] | C | RTN1 activity raises SLC7A2's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without RTN1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 36.6); signed map (43.4, 44.7). **Vector** length 60.3, 20.6% of its response variance represented; |z| ≥ 3 in 419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -0.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:59,595,976-59,870,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NSP |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Reticulons |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16799](https://www.uniprot.org/uniprotkb/Q16799) (Reticulon-1):

> Inhibits amyloid precursor protein processing, probably by blocking BACE1 activity.

**Summary**, from NCBI Gene [6252](https://www.ncbi.nlm.nih.gov/gene/6252):

> This gene belongs to the family of reticulon encoding genes. Reticulons are associated with the endoplasmic reticulum, and are involved in neuroendocrine secretion or in membrane trafficking in neuroendocrine cells. This gene is considered to be a specific marker for neurological diseases and cancer, and is a potential molecular target for therapy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:10467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10467) · Entrez [6252](https://www.ncbi.nlm.nih.gov/gene/6252) · UniProt [Q16799](https://www.uniprot.org/uniprotkb/Q16799) · Ensembl [ENSG00000139970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139970)

## Data

Gene col 6358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6358); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6358]; `tensor/DDL_lfc|DDL_z.npy` [6358]; `embed/gene_vectors.npy` [6358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6358 or target_col == 6358). Every well: [[RTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
