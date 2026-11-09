---
symbol: "CARHSP1"
type: "gene"
col: 7684
ensembl_id: "ENSG00000153048"
name: "calcium regulated heat stable protein 1"
location: "16p13.2"
module: 194
arm: "-"
pooled_cpm: 50.54
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# CARHSP1

*calcium regulated heat stable protein 1* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.32× (z +9.3, q 7e-18, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.391× (z -10.4, q 2e-22, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.74, fdr 1e-05), [[CDKN2D]] (+0.73, fdr 3e-05), [[CFD]] (+0.72, fdr 1e-05); moves opposite to [[PSME3IP1]] (-0.73, fdr 7e-06), [[ST7L]] (-0.73, fdr 1e-05), [[ZMYND11]] (-0.71, fdr 1e-05).
> It sits in the **-** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +9.3 | 7e-18 | 41/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +8.5 | 3e-15 | 43/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +8.5 | 3e-15 | 43/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.0 | 1e-04 | 37/48 (A498, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.1 | 0.004 | 27/48 (A549, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.11 | 23/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.23× | +3.2 | 0.11 | 25/49 (LS 180, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.391×** | -10.4 | 2e-22 | 44/48 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -9.3 | 4e-18 | 36/48 (AsPC-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.424×** | -9.1 | 2e-17 | 44/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.659×** | -4.6 | 6e-04 | 33/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -4.5 | 9e-04 | 29/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.4 | 9e-04 | 27/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.784×** | -3.8 | 0.013 | 29/48 (SNU-423, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -3.6 | 0.025 | 23/48 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.056 | 23/48 (HepG2/C3A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.088 | 24/48 (A-172, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 181 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -21.5) |
| [[SK-MEL-2 (line)]] | alt | 68.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.6) |
| [[Hs 766T (line)]] | wt | 54.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.9) |
| [[KATO III (line)]] | alt | 42.7 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.59× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 61.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.1) |
| [[SW480 (line)]] | alt | 37.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.12× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -10.2) |
| [[SNU-423 (line)]] | alt | 85.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.1) |
| [[SW1417 (line)]] | alt | 53.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.22× (z +9.6) | — |
| [[A-172 (line)]] | wt | 92.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -11.7) |
| [[A549 (line)]] | wt | 38.4 | 1 | 1 | [[Belinostat (drug)]] 5 µM 3.95× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 51.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 46.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -11.7) |
| [[PANC-1 (line)]] | alt | 72.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 79.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.1) |
| [[H4 (line)]] | wt | 35.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.178× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 59.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 80.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.9) |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -9.6) |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.1) |
| [[J82 (line)]] | alt | 65.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 36.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0620× (z -10.0) |
| [[RKO (line)]] | wt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.1) |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -10.6) |
| [[A-427 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.74 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.73 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[CFD]] | +0.72 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RALGDS]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CARD19]] | +0.71 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.71 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[TRIM62]] | +0.71 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.71 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TNNI3]] | +0.70 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[TMEM256]] | +0.70 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[RNF24]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PHAF1]] | +0.70 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | -0.73 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[ST7L]] | -0.73 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.71 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.71 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.70 | -0.43 / -0.71 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.70 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[KICS2]] | -0.69 | -0.71 / -0.46 | both halves | 3e-05 |  |
| [[DPH5-DT]] | -0.69 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[ZFP91]] | -0.68 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.68 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.68 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GUF1]] | -0.67 | -0.58 / -0.71 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises CARHSP1's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.30× lower at baseline in the lines without GPRC5A | 0.033 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PRSS8]] | B | PRSS8 activity raises CARHSP1's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.32× lower at baseline in the lines without PRSS8 | 0.041 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CARHSP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CARHSP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP3K9]] | B | MAP3K9 activity raises CARHSP1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without MAP3K9 | 0.055 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[RASSF7]] | B | RASSF7 activity raises CARHSP1's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without RASSF7 | 0.079 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **-** arm (projection on the module's main direction -0.803). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.8, -3.3); signed map (-30.4, 17.7). **Vector** length 131, 42.4% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.9 | +8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.7 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.7 | +9.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.8 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.3 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | calcium regulated heat stable protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:8,852,942-8,869,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRHSP-24, CSDC1 |
| Gene groups (HGNC) | Cold shock domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2V2](https://www.uniprot.org/uniprotkb/Q9Y2V2) (Calcium-regulated heat-stable protein 1):

> Binds mRNA and regulates the stability of target mRNA. Binds single-stranded DNA (in vitro).

**Summary**, from NCBI Gene [23589](https://www.ncbi.nlm.nih.gov/gene/23589):

> Enables mRNA 3'-UTR binding activity. Predicted to be involved in regulation of mRNA stability. Predicted to be located in P granule; cytoplasmic exosome (RNase complex); and cytosol. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17150) · Entrez [23589](https://www.ncbi.nlm.nih.gov/gene/23589) · UniProt [Q9Y2V2](https://www.uniprot.org/uniprotkb/Q9Y2V2) · Ensembl [ENSG00000153048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153048)

## Data

Gene col 7684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7684); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7684]; `tensor/DDL_lfc|DDL_z.npy` [7684]; `embed/gene_vectors.npy` [7684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7684 or target_col == 7684). Every well: [[CARHSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARHSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
