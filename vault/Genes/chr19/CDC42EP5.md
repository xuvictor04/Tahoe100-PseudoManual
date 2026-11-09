---
symbol: "CDC42EP5"
type: "gene"
col: 9501
ensembl_id: "ENSG00000167617"
name: "CDC42 effector protein 5"
location: "19q13.42"
module: 44
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 17
direction_downstream: 5
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CDC42EP5

*CDC42 effector protein 5* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.82× (z +8.2, q 2e-13, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 2.40× (z +7.2, q 2e-10, up in 7 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.544× (z -5.0, q 4e-04, down in 12 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC3A]] (+0.61, fdr 9e-06), [[CBLC]] (+0.57, fdr 3e-05), [[PLAAT3]] (+0.57, fdr 1e-05); moves opposite to [[BPNT2]] (-0.47, fdr 4e-05), [[DYNC1H1]] (-0.47, fdr 3e-05), [[TWF1]] (-0.46, fdr 8e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[FXYD3]] → it (grade B ⚠); 5 go from it, the strongest it → [[PLEKHG6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +8.2 | 2e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.40×** | +7.2 | 2e-10 | 7/23 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +6.3 | 6e-08 | 13/31 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +5.8 | 9e-07 | 2/10 (LS 180, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.5 | 8e-04 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.2 | 0.003 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.9 | 0.007 | 1/11 (AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.8 | 0.009 | 3/18 (KATO III, SW1417, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.5 | 0.025 | 4/22 (A-172, AsPC-1, …) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.031 | 4/21 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.054 | 2/32 (A498, H4) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.073 | 6/17 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.080 | 4/29 (KATO III, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.080 | 7/24 (Hs 766T, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.544×** | -5.0 | 4e-04 | 12/22 (KATO III, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -4.6 | 0.001 | 13/29 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.578×** | -4.4 | 0.002 | 13/33 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 2.06 | 0 | 1 | — | [[Erythromycin (drug)]] 0.05 µM 0.0635× (z -8.8) |
| [[LS 180 (line)]] | wt | 8.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0664× (z -8.6) |
| [[A-172 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.933 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.662 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.818 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.644 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC3A]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[CBLC]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PLAAT3]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[AMN]] | +0.57 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[MUC12]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SLC52A3]] | +0.54 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[CKMT1B]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[MAP3K8]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TJP3]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[DTX2]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[PLLP]] | +0.53 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT2]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[DYNC1H1]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TWF1]] | -0.46 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[WNK1]] | -0.45 | -0.37 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FXYD3]] | B | FXYD3 activity raises CDC42EP5's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without FXYD3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[GPA33]] | B | GPA33 activity raises CDC42EP5's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without GPA33 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[CBLC]] | B | CBLC activity raises CDC42EP5's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without CBLC | 0.048 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[CYP4F12]] | B | CYP4F12 activity raises CDC42EP5's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without CYP4F12 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises CDC42EP5's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without PLEKHG6 | 0.050 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises CDC42EP5's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without TJP3 | 0.052 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[LGALS4]] | B | LGALS4 activity raises CDC42EP5's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without LGALS4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[MYO7B]] | B | MYO7B activity raises CDC42EP5's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.68× lower at baseline in the lines without MYO7B | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[LPAR5]] | B | LPAR5 activity raises CDC42EP5's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without LPAR5 | 0.068 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[ABO]] | B | ABO activity raises CDC42EP5's level | lines that do not express ABO (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without ABO | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[SLC52A3]] | B | SLC52A3 activity raises CDC42EP5's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 1.62× lower at baseline in the lines without SLC52A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[TFF2]] | B | TFF2 activity raises CDC42EP5's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.16× lower at baseline in the lines without TFF2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG6]] | B | CDC42EP5 activity raises PLEKHG6's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 2.78× lower at baseline in the lines without CDC42EP5 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TJP3]] | B | CDC42EP5 activity raises TJP3's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 2.97× lower at baseline in the lines without CDC42EP5 | 0.065 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CBLC]] | B | CDC42EP5 activity raises CBLC's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without CDC42EP5 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MROH7]] | B | CDC42EP5 activity raises MROH7's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 2.35× lower at baseline in the lines without CDC42EP5 | 0.078 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LPAR5]] | B | CDC42EP5 activity raises LPAR5's level | lines that do not express CDC42EP5 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without CDC42EP5 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.3, 53.0); signed map (50.3, 1.8). **Vector** length 41.3, 6.55% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.0 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 effector protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,465,026-54,473,296 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEP5, Borg3 |
| Gene groups (HGNC) | CDC42 effector proteins |
| Reactome | 6 pathways, smallest: MAPK6/MAPK4 signaling; CDC42 GTPase cycle; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NZY7](https://www.uniprot.org/uniprotkb/Q6NZY7) (Cdc42 effector protein 5):

> Probably involved in the organization of the actin cytoskeleton. May act downstream of CDC42 to induce actin filament assembly leading to cell shape changes. Induces pseudopodia formation in fibroblasts. Inhibits MAPK8 independently of CDC42 binding. Controls septin organization and this effect is negatively regulated by CDC42 (By similarity).

**Summary**, from NCBI Gene [148170](https://www.ncbi.nlm.nih.gov/gene/148170):

> Cell division control protein 42 (CDC42), a small Rho GTPase, regulates the formation of F-actin-containing structures through its interaction with the downstream effector proteins. The protein encoded by this gene is a member of the Borg (binder of Rho GTPases) family of CDC42 effector proteins. Borg family proteins contain a CRIB (Cdc42/Rac interactive-binding) domain. They bind to CDC42 and regulate its function negatively. The encoded protein may inhibit c-Jun N-terminal kinase (JNK) …

**Accessions** — [HGNC:17408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17408) · Entrez [148170](https://www.ncbi.nlm.nih.gov/gene/148170) · UniProt [Q6NZY7](https://www.uniprot.org/uniprotkb/Q6NZY7) · Ensembl [ENSG00000167617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167617)

## Data

Gene col 9501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9501); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9501]; `tensor/DDL_lfc|DDL_z.npy` [9501]; `embed/gene_vectors.npy` [9501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9501 or target_col == 9501). Every well: [[CDC42EP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42EP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
