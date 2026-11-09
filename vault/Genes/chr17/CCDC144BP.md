---
symbol: "CCDC144BP"
type: "gene"
col: 7849
ensembl_id: "ENSG00000154874"
name: "coiled-coil domain containing 144B, pseudogene"
location: "17p11.2"
module: 12
arm: "+"
pooled_cpm: 17.9
n_lines_expressing: 27
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CCDC144BP

*coiled-coil domain containing 144B, pseudogene* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.32× (z +6.4, q 1e-07, up in 16 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.308× (z -10.0, q 8e-21, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC144A]] (+0.64, fdr 7e-06), [[RAB3GAP2]] (+0.60, fdr 1e-05), [[CEP290]] (+0.55, fdr 3e-05); moves opposite to [[TRAPPC10]] (-0.52, fdr 1e-05), [[RAN]] (-0.51, fdr 4e-05), [[MCM9]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCDC144A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.4 | 1e-07 | 16/25 (SK-MEL-2, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 2e-04 | 12/25 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.020 | 10/25 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.4 | 0.080 | 10/25 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.4 | 0.080 | 9/20 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.3 | 0.086 | 7/25 (HT-29, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -10.0 | 8e-21 | 21/25 (A549, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -9.9 | 8e-21 | 21/25 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.363×** | -8.6 | 2e-15 | 19/25 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -6.3 | 5e-08 | 18/25 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -6.0 | 2e-07 | 18/25 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.693×** | -5.9 | 3e-07 | 16/25 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -5.6 | 1e-06 | 14/25 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -5.4 | 5e-06 | 12/25 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -4.9 | 7e-05 | 13/25 (COLO 205, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.753×** | -4.6 | 3e-04 | 11/23 (HS-578T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -4.5 | 3e-04 | 15/25 (HT-29, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -4.1 | 0.002 | 11/25 (J82, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.791×** | -3.8 | 0.007 | 8/25 (HS-578T, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.798×** | -3.6 | 0.012 | 10/25 (J82, SW48, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.810×** | -3.4 | 0.026 | 8/25 (HEC-1-A, SW 1271, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.3 | 0.029 | 7/25 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.869× | -3.2 | 0.050 | 6/25 (MIA PaCa-2, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 31.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.1) |
| [[A549 (line)]] | wt | 23.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.107× (z -8.8) |
| [[AN3 CA (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.362× (z -8.8) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.355× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.106× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.5) |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0685× (z -10.2) |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.88 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC144A]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[RAB3GAP2]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CEP290]] | +0.55 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[DYNC2H1]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[THOC2]] | +0.54 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[UFSP2]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[MAP9]] | +0.52 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[LINC01473]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TPR]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[RING1]] | +0.51 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[FRA10AC1]] | +0.50 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[CLCN3]] | +0.48 | +0.35 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC10]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RAN]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MCM9]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[RNF4]] | -0.48 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ABHD15]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[PPIA]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ZNF718]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[TRMT12]] | -0.45 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[SLC35C1]] | -0.44 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PSKH1]] | -0.44 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[NUP50]] | -0.44 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[NDOR1]] | -0.44 | -0.36 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CCDC144BP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM106A]] | C | FAM106A activity raises CCDC144BP's level | lines that do not express FAM106A (30) vs lines expressing it (20) | 7.20× lower at baseline in the lines without FAM106A | 3e-04 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, SULF1, POSTN; co-absent with the target |
| [[CCDC144A]] | C | CCDC144A activity raises CCDC144BP's level | lines that do not express CCDC144A (18) vs lines expressing it (32) | 5.56× lower at baseline in the lines without CCDC144A | 0.005 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, MCOLN3, ENSG00000266302; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144A]] | C | CCDC144BP activity raises CCDC144A's level | lines that do not express CCDC144BP (23) vs lines expressing it (27) | 3.34× lower at baseline in the lines without CCDC144BP | 1e-04 | ⚠ within organs, on part of the lines; also absent: FAM106A, ENSG00000266302, CCDC144A; co-absent with the target |
| [[FAM106A]] | C | CCDC144BP activity raises FAM106A's level | lines that do not express CCDC144BP (23) vs lines expressing it (27) | 4.36× lower at baseline in the lines without CCDC144BP | 6e-04 | ⚠ within organs, on part of the lines; also absent: FAM106A, ENSG00000266302, CCDC144A; co-absent with the target |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.335). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.1, 2.9); signed map (-17.6, -11.7). **Vector** length 47.3, 9.07% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +0.9 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.9 | +0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -8.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -1.5 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 144B, pseudogene |
| Locus type | pseudogene |
| Location | 17p11.2 — chr17:18,542,155-18,625,447 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ36492; previously CCDC144B |
| Matched by | ensembl_id |

UniProt [Q3MJ40](https://www.uniprot.org/uniprotkb/Q3MJ40) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26704) · Entrez [284047](https://www.ncbi.nlm.nih.gov/gene/284047) · UniProt [Q3MJ40](https://www.uniprot.org/uniprotkb/Q3MJ40) · Ensembl [ENSG00000154874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154874)

## Data

Gene col 7849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7849); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7849]; `tensor/DDL_lfc|DDL_z.npy` [7849]; `embed/gene_vectors.npy` [7849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7849 or target_col == 7849). Every well: [[CCDC144BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC144BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
