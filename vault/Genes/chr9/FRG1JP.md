---
symbol: "FRG1JP"
type: "gene"
col: 13268
ensembl_id: "ENSG00000215548"
name: "FSHD region gene 1 family member J, pseudogene"
location: "9q13"
module: 183
arm: "+"
pooled_cpm: 2.8
n_lines_expressing: 27
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# FRG1JP

*FSHD region gene 1 family member J, pseudogene* — 9q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.07× (z +10.6, q 1e-23, up in 16 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.519× (z -6.8, q 6e-09, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1DP]] (+0.60, fdr 3e-05), [[FRG1GP]] (+0.58, fdr 3e-05), [[C2orf74]] (+0.55, fdr 5e-05); moves opposite to [[PKP4]] (-0.60, fdr 1e-05), [[EIF4G3]] (-0.58, fdr 2e-05), [[SMARCA4]] (-0.49, fdr 4e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[FRG1DP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.07×** | +10.6 | 1e-23 | 16/22 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +9.9 | 8e-21 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +8.0 | 3e-13 | 2/7 (NCI-H1573, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.2 | 6e-08 | 1/12 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.2 | 2e-05 | 4/19 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.83×** | +4.4 | 9e-04 | 1/12 (A549) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.3 | 0.001 | 3/14 (C32, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 0.001 | 4/17 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.1 | 0.003 | 2/15 (NCI-H1573, LOX-IMVI) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.004 | 5/21 (HS-578T, C32, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.9 | 0.004 | 0/6 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +3.8 | 0.008 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.011 | 1/23 (H4) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.061 | 4/17 (SNU-423, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.34×** | +3.0 | 0.091 | 7/19 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.092 | 2/22 (SK-MEL-2, SHP-77) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.092 | 1/17 (C32) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -6.8 | 6e-09 | 17/21 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -5.5 | 1e-05 | 10/22 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -5.4 | 1e-05 | 14/22 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -5.2 | 3e-05 | 16/21 (SNU-423, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.647×** | -4.5 | 7e-04 | 4/23 (H4, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.715×** | -3.4 | 0.076 | 8/22 (CHP-212, SNU-423, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0712× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 5.21 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0709× (z -9.3) |
| [[HS-578T (line)]] | alt | 8.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 5.11 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0923× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.718 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.705 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.768 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.800 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1DP]] | +0.60 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[FRG1GP]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[C2orf74]] | +0.55 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[ZNF568]] | +0.53 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[ZSCAN23]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[RAMAC]] | +0.53 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[CCNYL2-1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TMEM183A]] | +0.52 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[DUSP11]] | +0.52 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[ZNF836]] | +0.52 | +0.28 / +0.60 | both halves | 3e-04 |  |
| [[SMPDL3A]] | +0.51 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ZNF727]] | +0.50 | +0.32 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP4]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[EIF4G3]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SMARCA4]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ZCCHC14]] | -0.49 | -0.20 / -0.54 | both halves | 7e-04 |  |
| [[PKD2]] | -0.48 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[R3HDM1]] | -0.47 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[SMC1A]] | -0.46 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ZNF704]] | -0.46 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[RFX3]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CLEC16A]] | -0.44 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DPY19L1P1]] | -0.44 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PSPC1]] | -0.44 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[WWC2]] | -0.44 | -0.25 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1DP]] | B | FRG1JP activity raises FRG1DP's level | lines that do not express FRG1JP (23) vs lines expressing it (27) | 2.53× lower at baseline in the lines without FRG1JP | 0.065 | ⚠ within organs, on part of the lines; also absent: LSAMP, TRPV2, MSC; maybe low, not absent |
| [[FRG1FP]] | C | FRG1JP activity raises FRG1FP's level | lines that do not express FRG1JP (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without FRG1JP | 0.073 | ⚠ within organs, on part of the lines; also absent: LSAMP, TRPV2, MSC; maybe low, not absent; co-absent with the target |
| [[KC6]] | C | FRG1JP activity raises KC6's level | lines that do not express FRG1JP (23) vs lines expressing it (27) | 3.50× lower at baseline in the lines without FRG1JP | 0.086 | ⚠ within organs, on part of the lines; also absent: LSAMP, TRPV2, MSC; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.2, -32.7); signed map (-23.9, -11.0). **Vector** length 25.0, 2.99% of its response variance represented; |z| ≥ 3 in 484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.8 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.6 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.5 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.1 | -6.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.0 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.9 | -5.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.5 | +1.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.5 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | +0.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member J, pseudogene |
| Locus type | pseudogene |
| Location | 9q13 — chr9:63,832,127-63,859,641 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51768) · Entrez [642236](https://www.ncbi.nlm.nih.gov/gene/642236) · Ensembl [ENSG00000215548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215548)

## Data

Gene col 13268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13268); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13268]; `tensor/DDL_lfc|DDL_z.npy` [13268]; `embed/gene_vectors.npy` [13268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13268 or target_col == 13268). Every well: [[FRG1JP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1JP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
