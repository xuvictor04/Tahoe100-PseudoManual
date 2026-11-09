---
symbol: "PRECSIT"
type: "gene"
col: 14963
ensembl_id: "ENSG00000255874"
name: "p53 regulated carcinoma associated Stat3 activating long intergenic non-protein coding transcript"
location: "13q34"
module: 10
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 41
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PRECSIT

*p53 regulated carcinoma associated Stat3 activating long intergenic non-protein coding transcript* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.71× (z +14.6, q 1e-45, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.669× (z -4.5, q 0.004, down in 9 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (A-172 0.0892×; ⚠ toxic; transcription drop); [[Captopril (drug)]] 0.05 µM in 1 line (HS-578T 0.0652×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPK2-DT]] (+0.64, fdr 7e-06), [[SYNE1]] (+0.64, fdr 1e-05), [[NANOS3]] (+0.62, fdr 1e-05); moves opposite to [[KLHL8]] (-0.65, fdr 1e-05), [[ARMC10]] (-0.60, fdr 1e-05), [[PRKRA]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CREB5]] → it (grade B ⚠); 3 go from it, the strongest it → [[DIO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.71×** | +14.6 | 1e-45 | 24/28 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.03×** | +11.8 | 1e-29 | 5/6 (MIA PaCa-2, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.54×** | +9.6 | 1e-19 | 23/32 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +8.8 | 3e-16 | 6/12 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.97×** | +8.6 | 9e-16 | 20/26 (SHP-77, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +7.7 | 2e-12 | 3/5 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +7.6 | 3e-12 | 13/36 (HS-578T, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.0 | 2e-07 | 12/36 (A498, HS-578T, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +5.8 | 5e-07 | 12/23 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 12/22 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.8 | 7e-05 | 5/17 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.74×** | +4.4 | 6e-04 | 7/34 (HT-29, KATO III, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +4.3 | 7e-04 | 12/29 (A-172, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.005 | 4/23 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.51×** | +3.8 | 0.006 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.012 | 8/26 (HOP62, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.020 | 8/35 (BT-474, SW480, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.068 | 3/27 (LS 180, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.075 | 10/36 (BT-474, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.093 | 9/37 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14963.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (A-172 0.0892×; ⚠ toxic; transcription drop); [[Captopril (drug)]] 0.05 µM in 1 line (HS-578T 0.0652×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | **0.669×** | -4.5 | 0.004 | 9/37 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.680× | -3.1 | 0.54 | 7/26 (SNU-423, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.10 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.0892× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 0.678 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 5.32 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0652× (z -9.3) |
| [[A-427 (line)]] | wt | 0.148 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.858 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.881 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.646 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.640 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 | same gene group |
| [[SYNE1]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[MYOSLID]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 | same gene group |
| [[LURAP1L-AS1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[HSPB8]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[LINC02901]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[KRT8P12]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FNBP1P1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ATF3]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC01828]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | -0.65 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ARMC10]] | -0.60 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[PRKRA]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[SMYD4]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SRGAP2D]] | -0.55 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[STARD3]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[GLMN]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PDPR2P]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[WDR5]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TCTN3]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[MMS19]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB5]] | B | CREB5 activity raises PRECSIT's level | lines that do not express CREB5 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without CREB5 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01828, ITPR1, ENSG00000230647 |
| [[TRIM16L]] | B | TRIM16L activity raises PRECSIT's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without TRIM16L | 0.013 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[SSPN]] | B | SSPN activity raises PRECSIT's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without SSPN | 0.058 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[CAVIN4]] | C | CAVIN4 activity raises PRECSIT's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without CAVIN4 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIO2]] | B | PRECSIT activity raises DIO2's level | lines that do not express PRECSIT (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without PRECSIT | 0.069 | ⚠ within organs, on part of the lines; also absent: FAM3B, CFAP45, ENSG00000283511; maybe low, not absent |
| [[CREB5]] | B | PRECSIT activity raises CREB5's level | lines that do not express PRECSIT (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without PRECSIT | 0.078 | ⚠ within organs, on part of the lines; also absent: FAM3B, CFAP45, ENSG00000283511; maybe low, not absent |
| [[CAVIN4]] | B | PRECSIT activity raises CAVIN4's level | lines that do not express PRECSIT (9) vs lines expressing it (41) | 1.13× lower at baseline in the lines without PRECSIT | 0.095 | ⚠ within organs, on part of the lines; also absent: FAM3B, CFAP45, ENSG00000283511; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (15.9, 13.1); signed map (24.5, 5.0). **Vector** length 57.5, 11.1% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | p53 regulated carcinoma associated Stat3 activating long intergenic non-protein coding transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q34 — chr13:110,863,987-110,870,330 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C13orf29, NCRNA00346, LINC00346 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27492) · Entrez [283487](https://www.ncbi.nlm.nih.gov/gene/283487) · Ensembl [ENSG00000255874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255874)

## Data

Gene col 14963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14963); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14963]; `tensor/DDL_lfc|DDL_z.npy` [14963]; `embed/gene_vectors.npy` [14963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14963 or target_col == 14963). Every well: [[PRECSIT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRECSIT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
