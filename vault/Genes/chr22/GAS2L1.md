---
symbol: "GAS2L1"
type: "gene"
col: 11663
ensembl_id: "ENSG00000185340"
name: "growth arrest specific 2 like 1"
location: "22q12.2"
module: 85
arm: "+"
pooled_cpm: 7.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# GAS2L1

*growth arrest specific 2 like 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +7.2, q 3e-10, up in 25 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.32× (z +3.6, q 0.043, up in 13 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.310× (z -14.9, q 0e+00, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIP5K1C]] (+0.68, fdr 4e-05), [[GNAI2]] (+0.65, fdr 3e-05), [[CYTH3]] (+0.65, fdr 1e-05); moves opposite to [[AIMP1]] (-0.57, fdr 3e-05), [[RNF6]] (-0.56, fdr 2e-04), [[KRR1]] (-0.56, fdr 7e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BMP8B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +7.2 | 3e-10 | 25/30 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +6.3 | 9e-08 | 12/16 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +4.4 | 0.002 | 10/20 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +3.8 | 0.023 | 10/47 (PANC-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.043 | 13/47 (SW480, LS 180, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **2.10×** | +3.5 | 0.047 | 5/30 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.43×** | +3.2 | 0.098 | 15/36 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.310×** | -14.9 | 0e+00 | 37/43 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.330×** | -10.0 | 7e-21 | 34/42 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.380×** | -8.7 | 7e-16 | 34/47 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.463×** | -6.6 | 5e-09 | 31/46 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -5.5 | 4e-06 | 26/47 (NCI-H1573, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -5.5 | 4e-06 | 24/41 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -5.2 | 2e-05 | 30/45 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.567×** | -5.0 | 5e-05 | 25/47 (SK-MEL-2, SW 1271, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -4.4 | 6e-04 | 19/46 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -4.4 | 6e-04 | 17/40 (KATO III, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.009 | 18/47 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.643×** | -3.7 | 0.009 | 19/45 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -3.7 | 0.011 | 18/45 (SNU-423, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.759×** | -3.5 | 0.020 | 16/47 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -3.4 | 0.027 | 19/46 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.688×** | -3.4 | 0.029 | 15/45 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.492×** | -3.3 | 0.029 | 9/45 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.036 | 15/42 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0358× (z -21.1) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -17.1) |
| [[AsPC-1 (line)]] | alt | 5.50 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -10.1) |
| [[Hs 766T (line)]] | wt | 9.77 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0552× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 5.18 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -15.3) |
| [[PANC-1 (line)]] | alt | 8.13 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.6) |
| [[SW 900 (line)]] | alt | 8.89 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.1) |
| [[A549 (line)]] | wt | 5.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.5) |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -8.8) |
| [[HT-29 (line)]] | alt | 6.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -10.4) |
| [[J82 (line)]] | alt | 5.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0822× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 4.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0833× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 6.80 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0835× (z -9.8) |
| [[SW480 (line)]] | alt | 3.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.4) |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP5K1C]] | +0.68 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.65 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[CYTH3]] | +0.65 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TECPR1]] | +0.62 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[PCMT1]] | +0.62 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[RTN2]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TNFAIP8L1]] | +0.61 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[RRAS]] | +0.60 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[ANKRD13D]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[FAM89B]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MEX3D]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIMP1]] | -0.57 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RNF6]] | -0.56 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[KRR1]] | -0.56 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[YIPF6]] | -0.54 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PNISR-AS1]] | -0.54 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.53 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[LINC01134]] | -0.52 | -0.31 / -0.23 | both halves | 5e-04 |  |
| [[POLR2M]] | -0.52 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.52 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[BCL2L13]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ZXDA]] | -0.52 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ACTR3C]] | -0.52 | -0.49 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP8B]] | B | BMP8B activity lowers GAS2L1's level | lines that do not express BMP8B (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without BMP8B | 0.067 | ⚠ within organs, on part of the lines; also absent: PBX4, SPECC1, CTSV; maybe low, not absent; its own permutation p |
| [[STX2]] | C | STX2 activity raises GAS2L1's level | lines that do not express STX2 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without STX2 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPW, PALS2, CAPRIN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (3.4, -0.2); signed map (-27.0, 18.3). **Vector** length 56.8, 8.91% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -14.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.7 | -3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest specific 2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,306,618-29,312,787 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAR22 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99501](https://www.uniprot.org/uniprotkb/Q99501) (GAS2-like protein 1):

> Involved in the cross-linking of microtubules and microfilaments. Regulates microtubule dynamics and stability by interacting with microtubule plus-end tracking proteins, such as MAPRE1, to regulate microtubule growth along actin stress fibers.

**Summary**, from NCBI Gene [10634](https://www.ncbi.nlm.nih.gov/gene/10634):

> This gene encodes a member of the growth arrest-specific 2 protein family. This protein binds components of the cytoskeleton and may be involved in mediating interactions between microtubules and microfilaments. This protein localizes to the proximal end of mature centrioles and links centrosomes to both microtubules and actin. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 9. [provided by RefSeq, May 2018]

**Accessions** — [HGNC:16955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16955) · Entrez [10634](https://www.ncbi.nlm.nih.gov/gene/10634) · UniProt [Q99501](https://www.uniprot.org/uniprotkb/Q99501) · Ensembl [ENSG00000185340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185340)

## Data

Gene col 11663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11663); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11663]; `tensor/DDL_lfc|DDL_z.npy` [11663]; `embed/gene_vectors.npy` [11663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11663 or target_col == 11663). Every well: [[GAS2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
