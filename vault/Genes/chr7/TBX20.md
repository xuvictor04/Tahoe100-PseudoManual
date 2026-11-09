---
symbol: "TBX20"
type: "gene"
col: 8958
ensembl_id: "ENSG00000164532"
name: "T-box transcription factor 20"
location: "7p14.2"
module: 212
arm: "+"
pooled_cpm: 6.05
n_lines_expressing: 18
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# TBX20

*T-box transcription factor 20* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.29× (z +11.6, q 2e-28, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +7.5, q 1e-11, up in 7 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.652× (z -4.2, q 0.016, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GP6-AS1]] (+0.54, fdr 3e-05), [[CUZD1]] (+0.51, fdr 1e-04), [[IQCB1]] (+0.51, fdr 5e-05); moves opposite to [[BDNF-AS]] (-0.50, fdr 2e-04), [[ARID1B]] (-0.49, fdr 1e-04), [[CRPPA]] (-0.49, fdr 7e-05).
> It is in [[Module 212]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[ANKS6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +11.6 | 2e-28 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.5 | 7e-15 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +7.8 | 1e-12 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +7.5 | 1e-11 | 7/16 (SW1417, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +5.6 | 3e-06 | 8/16 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.12×** | +5.4 | 5e-06 | 1/12 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.3 | 0.001 | 0/12 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.9 | 0.007 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.8 | 0.008 | 0/8 | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.8 | 0.009 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.7 | 0.013 | 2/14 (SW480, KATO III) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +3.6 | 0.013 | 4/16 (SW480, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.023 | 0/15 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.023 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.023 | 3/14 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.027 | 3/16 (SW480, HEC-1-A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.048 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.054 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.063 | 0/15 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.652×** | -4.2 | 0.016 | 11/16 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.098 | 11/15 (A549, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -3.4 | 0.098 | 8/16 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.698×** | -3.4 | 0.098 | 0/16 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.05 µM |  | 0.716× | -3.2 | 0.14 | 4/16 (SW1417, SK-MEL-2, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.744× | -3.0 | 0.18 | 0/16 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.727× | -3.0 | 0.18 | 1/16 (A-427) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 9.01 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.112× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -19.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0413× (z -19.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0415× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 6.65 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -11.9) |
| [[A-172 (line)]] | wt | 4.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0362× (z -9.1) |
| [[A-427 (line)]] | wt | 9.80 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 8.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.533 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GP6-AS1]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CUZD1]] | +0.51 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[IQCB1]] | +0.51 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[COL4A4]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[NANS]] | +0.51 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[NT5DC3]] | +0.51 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[GALNT12]] | +0.50 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[GNAI3]] | +0.50 | +0.47 / +0.23 | both halves | 5e-04 |  |
| [[RADX]] | +0.50 | +0.37 / +0.42 | both halves | 7e-05 |  |
| [[STAC]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[GPR89B]] | +0.49 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[LPCAT2]] | +0.49 | +0.42 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDNF-AS]] | -0.50 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[ARID1B]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[CRPPA]] | -0.49 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[ARFGAP2]] | -0.49 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[UFL1-AS1]] | -0.48 | -0.44 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[CASD1]] | -0.48 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[WAC-AS1]] | -0.47 | -0.46 / -0.21 | both halves | 7e-04 |  |
| [[BAZ2B]] | -0.47 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[CCAR1]] | -0.47 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[CFAP418-AS1]] | -0.47 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[EFCAB2]] | -0.47 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[MED12]] | -0.47 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[TIGD6]] | -0.47 | -0.48 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKS6]] | B | TBX20 activity raises ANKS6's level | lines that do not express TBX20 (32) vs lines expressing it (18) | 1.49× lower at baseline in the lines without TBX20 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1 |
| [[WAC-AS1]] | B | TBX20 activity raises WAC-AS1's level | lines that do not express TBX20 (32) vs lines expressing it (18) | 1.37× lower at baseline in the lines without TBX20 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1 |
| [[IQCB1]] | B | TBX20 activity raises IQCB1's level | lines that do not express TBX20 (32) vs lines expressing it (18) | 1.19× lower at baseline in the lines without TBX20 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1 |
| [[IQCB1]] | B | TBX20 activity strengthens IQCB1's drug response | lines that do not express TBX20 (32) vs lines expressing it (17) | the lines without TBX20 respond 0.84× as strongly (z diff +0.80); strongest at Harringtonine 5 µM: 0.71x vs 0.58x (z diff +3.0) | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02335, COX7B2, OLR1; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.5, -24.4); signed map (-50.6, -1.8). **Vector** length 42.7, 10.9% of its response variance represented; |z| ≥ 3 in 366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +11.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.4 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.7 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.6 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:35,202,430-35,254,100 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | T-box transcription factors |
| Reactome | 1 pathways, smallest: Cardiogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMR3](https://www.uniprot.org/uniprotkb/Q9UMR3) (T-box transcription factor TBX20):

> Acts as a transcriptional activator and repressor required for cardiac development and may have key roles in the maintenance of functional and structural phenotypes in adult heart.

**Summary**, from NCBI Gene [57057](https://www.ncbi.nlm.nih.gov/gene/57057):

> This gene encodes a T-box family member. The T-box family members share a common DNA binding domain, termed the T-box, and they are transcription factors involved in the regulation of developmental processes. This gene is essential for heart development. Mutations in this gene are associated with diverse cardiac pathologies, including defects in septation, valvulogenesis and cardiomyopathy. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:11598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11598) · Entrez [57057](https://www.ncbi.nlm.nih.gov/gene/57057) · UniProt [Q9UMR3](https://www.uniprot.org/uniprotkb/Q9UMR3) · Ensembl [ENSG00000164532](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164532)

## Data

Gene col 8958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8958); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8958]; `tensor/DDL_lfc|DDL_z.npy` [8958]; `embed/gene_vectors.npy` [8958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8958 or target_col == 8958). Every well: [[TBX20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
