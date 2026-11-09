---
symbol: "PARP3"
type: "gene"
col: 478
ensembl_id: "ENSG00000041880"
name: "poly(ADP-ribose) polymerase family member 3"
location: "3p21.2"
module: 7
arm: "+"
pooled_cpm: 4.93
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PARP3

*poly(ADP-ribose) polymerase family member 3* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +8.4, q 2e-14, up in 9 of 11 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.390× (z -10.2, q 1e-21, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C7orf25]] (+0.69, fdr 1e-05), [[NCOA4]] (+0.68, fdr 1e-05), [[EIF4G2]] (+0.67, fdr 1e-05); moves opposite to [[SRGAP2D]] (-0.61, fdr 1e-05), [[UQCRH]] (-0.61, fdr 3e-05), [[KIAA1958]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MRAS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 478.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +8.4 | 2e-14 | 9/11 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +7.8 | 1e-12 | 11/20 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +6.7 | 5e-09 | 5/13 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +4.3 | 0.002 | 10/44 (C32, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.45× | +3.2 | 0.16 | 8/42 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.34× | +3.1 | 0.21 | 7/39 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 478.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.390×** | -10.2 | 1e-21 | 34/44 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -10.0 | 4e-21 | 32/42 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.423×** | -9.3 | 2e-18 | 31/43 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.480×** | -7.9 | 3e-13 | 29/44 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.531×** | -6.9 | 8e-10 | 27/44 (SW480, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.536×** | -6.8 | 1e-09 | 22/34 (LoVo, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -6.6 | 3e-09 | 24/42 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.577×** | -6.0 | 2e-07 | 20/36 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.642×** | -4.8 | 1e-04 | 20/40 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.644×** | -4.8 | 1e-04 | 14/45 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -4.4 | 6e-04 | 18/44 (A-427, NCI-H2030, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.487×** | -4.1 | 0.002 | 7/41 (NCI-H2030, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.698×** | -3.9 | 0.004 | 17/43 (H4, CFPAC-1, …) | top dose only |  |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.9 | 0.004 | 3/43 (SW 1088, RPMI-7951, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.783×** | -3.7 | 0.007 | 17/35 (HOP62, CFPAC-1, …) | top dose only | composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.695×** | -3.7 | 0.007 | 8/42 (C32, A-172, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.729×** | -3.4 | 0.021 | 12/38 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **0.734×** | -3.2 | 0.039 | 8/41 (NCI-H23, NCI-H2030, …) | top dose only | position effect removed |
| [[Clotrimazole (drug)]] 0.5 µM |  | **0.758×** | -3.0 | 0.076 | 9/39 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 478. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.46 | 0 | 2 (1 ⚠) | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0575× (z -12.2) |
| [[A-172 (line)]] | wt | 15.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -9.2) |
| [[A549 (line)]] | wt | 4.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0787× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 7.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0863× (z -9.6) |
| [[A-427 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 478), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf25]] | +0.69 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.68 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.67 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ACP2]] | +0.67 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNF564]] | +0.66 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[ACTR8]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TAF9]] | +0.65 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZXDB]] | +0.64 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[RNF6]] | +0.64 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SF3B4]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[MRPL9]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MED12]] | +0.62 | +0.41 / +0.72 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2D]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.61 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[KIAA1958]] | -0.61 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SLC25A5]] | -0.59 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[COX6A1]] | -0.59 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TOMM20]] | -0.58 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[COX6C]] | -0.58 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ANAPC11]] | -0.57 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MNX1]] | -0.57 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[SBNO1]] | -0.57 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PIBF1]] | -0.56 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PRKRIP1]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRAS]] | B | MRAS activity raises PARP3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without MRAS | 0.063 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[ZNF532]] | B | ZNF532 activity lowers PARP3's level | lines that do not express ZNF532 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without ZNF532 | 0.064 | ⚠ within organs, on part of the lines; also absent: PXMP4, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.8, 1.9); signed map (5.0, -30.6). **Vector** length 56.9, 8.30% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.5 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.8 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -9.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.5 | -6.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,942,345-51,948,867 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADPRT3, IRT1, hPARP-3, pADPRT-3, ARTD3; previously ADPRTL3 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6F1](https://www.uniprot.org/uniprotkb/Q9Y6F1) (Protein mono-ADP-ribosyltransferase PARP3):

> Mono-ADP-ribosyltransferase that mediates mono-ADP-ribosylation of target proteins and plays a key role in the response to DNA damage. Mediates mono-ADP-ribosylation of glutamate, aspartate or lysine residues on target proteins. In contrast to PARP1 and PARP2, it is not able to mediate poly-ADP-ribosylation. Involved in DNA repair by mediating mono-ADP-ribosylation of a limited number of acceptor proteins involved in chromatin architecture and in DNA metabolism, such as histone H2B, XRCC5 and …

**Summary**, from NCBI Gene [10039](https://www.ncbi.nlm.nih.gov/gene/10039):

> The protein encoded by this gene belongs to the PARP family. These enzymes modify nuclear proteins by poly-ADP-ribosylation, which is required for DNA repair, regulation of apoptosis, and maintenance of genomic stability. This gene encodes the poly(ADP-ribosyl)transferase 3, which is preferentially localized to the daughter centriole throughout the cell cycle. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:273) · Entrez [10039](https://www.ncbi.nlm.nih.gov/gene/10039) · UniProt [Q9Y6F1](https://www.uniprot.org/uniprotkb/Q9Y6F1) · Ensembl [ENSG00000041880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000041880)

## Data

Gene col 478: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 478); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 478, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 478]; `tensor/DDL_lfc|DDL_z.npy` [478]; `embed/gene_vectors.npy` [478]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 478 or target_col == 478). Every well: [[PARP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
