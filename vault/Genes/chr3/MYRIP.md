---
symbol: "MYRIP"
type: "gene"
col: 9893
ensembl_id: "ENSG00000170011"
name: "myosin VIIA and Rab interacting protein"
location: "3p22.1"
module: 27
arm: "+"
pooled_cpm: 11.52
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MYRIP

*myosin VIIA and Rab interacting protein* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.60× (z +19.5, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.726× (z -4.4, q 0.008, down in 15 of 31 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC7A8]] (+0.62, fdr 1e-05), [[MPP7]] (+0.60, fdr 1e-05), [[LINC00992]] (+0.58, fdr 7e-06); moves opposite to [[PRR14L]] (-0.46, fdr 4e-04), [[PSMB5]] (-0.45, fdr 1e-04), [[NPLOC4]] (-0.45, fdr 8e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.60×** | +19.5 | 0e+00 | 30/33 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.52×** | +18.1 | 0e+00 | 29/33 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.91×** | +15.4 | 0e+00 | 29/32 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +11.7 | 2e-29 | 14/29 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.18×** | +11.2 | 3e-27 | 27/32 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +10.8 | 3e-25 | 3/11 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +10.6 | 2e-24 | 15/28 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +9.6 | 4e-20 | 11/25 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +9.4 | 4e-19 | 23/33 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +8.9 | 4e-17 | 20/33 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +7.8 | 4e-13 | 4/18 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.8 | 4e-07 | 12/29 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 2e-06 | 11/32 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +5.0 | 3e-05 | 17/30 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.2 | 8e-04 | 9/30 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.002 | 6/31 (SW480, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.005 | 8/31 (SHP-77, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.013 | 11/32 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.726×** | -4.4 | 0.008 | 15/31 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.9 | 0.021 | 4/34 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -3.9 | 0.021 | 13/31 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.053 | 13/32 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.1 | 4 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.92× (z +11.7) | [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.01× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 40.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.301× (z -9.5) |
| [[SW480 (line)]] | alt | 18.2 | 2 | 1 | [[Cobimetinib (drug)]] 5 µM 4.64× (z +8.9) | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -8.8) |
| [[LoVo (line)]] | wt | 11.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.75× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.140× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 76.4 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0972× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.310× (z -8.5) |
| [[PANC-1 (line)]] | alt | 4.08 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.58× (z +11.1) | — |
| [[RKO (line)]] | wt | 5.16 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 8.37× (z +10.0) | [[Vandetanib (drug)]] 0.05 µM 0.0664× (z -9.0) |
| [[A-172 (line)]] | wt | 2.95 | 0 | 1 | — | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM 0.0543× (z -9.4) |
| [[A-427 (line)]] | wt | 5.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.06× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0659× (z -8.7) |
| [[BT-474 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 2.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 60.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.8) | — |
| [[A498 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC7A8]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MPP7]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[LINC00992]] | +0.58 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SELENOP]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[NRXN3]] | +0.51 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[MAP2K6]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SLC40A1]] | +0.51 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[LINC02147]] | +0.50 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PPFIBP2]] | +0.50 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[DCDC2]] | +0.49 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[KSR2]] | +0.49 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DLEU1]] | +0.49 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR14L]] | -0.46 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[PSMB5]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[NPLOC4]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[KMT2D]] | -0.43 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MRPL18]] | -0.41 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[SERPINH1]] | -0.41 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[IREB2]] | -0.40 | -0.21 / -0.39 | both halves | 7e-04 |  |
| [[PEX6]] | -0.40 | -0.15 / -0.31 | ⚠ not reproduced | 0.001 |  |
| [[MRPS15]] | -0.40 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MEF2B]] | -0.39 | -0.14 / -0.38 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises MYRIP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00992]] | B | LINC00992 activity raises MYRIP's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without LINC00992 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[CHN2]] | B | CHN2 activity raises MYRIP's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without CHN2 | 0.069 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[LINC02147]] | B | LINC02147 activity raises MYRIP's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without LINC02147 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |
| [[SORBS2]] | B | SORBS2 activity raises MYRIP's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without SORBS2 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[MAP2K1]] | B | MAP2K1 activity lowers MYRIP's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, 46.9); signed map (52.7, 2.7). **Vector** length 61.6, 10.8% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +19.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.8 | +0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | myosin VIIA and Rab interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:39,808,914-40,260,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586F1018, exophilin-8, SLAC2-C, SLAC2C |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Reactome | 5 pathways, smallest: Insulin processing; Regulation of MITF-M-dependent genes involved in pigmentation; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFW9](https://www.uniprot.org/uniprotkb/Q8NFW9) (Rab effector MyRIP):

> Rab effector protein involved in melanosome transport. Serves as link between melanosome-bound RAB27A and the motor proteins MYO5A and MYO7A. May link RAB27A-containing vesicles to actin filaments. Functions as a protein kinase A-anchoring protein (AKAP). May act as a scaffolding protein that links PKA to components of the exocytosis machinery, thus facilitating exocytosis, including insulin release (By similarity).

**Summary**, from NCBI Gene [25924](https://www.ncbi.nlm.nih.gov/gene/25924):

> Predicted to enable actin binding activity and myosin binding activity. Predicted to be involved in positive regulation of insulin secretion. Predicted to be located in dense core granule and perinuclear region of cytoplasm. Predicted to be part of exocyst. Predicted to be active in cortical actin cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19156) · Entrez [25924](https://www.ncbi.nlm.nih.gov/gene/25924) · UniProt [Q8NFW9](https://www.uniprot.org/uniprotkb/Q8NFW9) · Ensembl [ENSG00000170011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170011)

## Data

Gene col 9893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9893); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9893]; `tensor/DDL_lfc|DDL_z.npy` [9893]; `embed/gene_vectors.npy` [9893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9893 or target_col == 9893). Every well: [[MYRIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYRIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
