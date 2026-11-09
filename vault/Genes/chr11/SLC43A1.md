---
symbol: "SLC43A1"
type: "gene"
col: 7344
ensembl_id: "ENSG00000149150"
name: "solute carrier family 43 member 1"
location: "11q12.1"
module: 176
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# SLC43A1

*solute carrier family 43 member 1* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +9.7, q 1e-19, up in 18 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.555× (z -7.2, q 3e-10, down in 17 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACSS1]] (+0.59, fdr 1e-05), [[TMEM268]] (+0.55, fdr 2e-05), [[DENND11]] (+0.54, fdr 1e-05); moves opposite to [[H3-3B]] (-0.55, fdr 2e-05), [[STK17A]] (-0.55, fdr 1e-05), [[DYNLT1]] (-0.52, fdr 4e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CRACR2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[SNX30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.7 | 1e-19 | 18/31 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.3 | 8e-08 | 14/35 (HT-29, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.9 | 7e-07 | 17/37 (SW480, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.012 | 9/34 (NCI-H2347, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.3 | 0.086 | 10/25 (NCI-H1792, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.086 | 1/35 (SW480) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.14 | 9/37 (SW480, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.20× | +3.1 | 0.14 | 7/36 (NCI-H1792, HOP62, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -7.2 | 3e-10 | 17/35 (SW48, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.640×** | -5.3 | 4e-05 | 16/34 (RKO, SW48, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.634×** | -5.2 | 4e-05 | 13/28 (SNU-423, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 0.004 | 10/35 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.727×** | -3.9 | 0.010 | 11/36 (C32, COLO 205, …) | two highest doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -3.9 | 0.010 | 14/36 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | **0.737×** | -3.8 | 0.014 | 9/36 (BT-474, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.738×** | -3.6 | 0.022 | 7/36 (HT-29, C32, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.752×** | -3.5 | 0.028 | 12/36 (SW480, SNU-423, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -3.3 | 0.050 | 10/35 (H4, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -3.2 | 0.066 | 9/34 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -8.7) |
| [[KATO III (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.203× (z -9.8) |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 6.24 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0813× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.126× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 5.55 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0948× (z -8.5) |
| [[RKO (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -12.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Megestrol (drug)]] 0.05 µM 0.0543× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0539× (z -9.9) |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSS1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TMEM268]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DENND11]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TFAP4]] | +0.53 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RAVER2]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TTPA]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[BDH1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[FOXP4-AS1]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[ASIC1]] | +0.50 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PPARGC1B]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ADGRG5]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[FAM27C]] | +0.49 | +0.42 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.55 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[STK17A]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[DYNLT1]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PAFAH1B1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[OSMR]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[EXT1]] | -0.47 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[STX12]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[SH3BGRL3]] | -0.45 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MRTFA]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[SNX6]] | -0.45 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[DLGAP4]] | -0.45 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[EXOC8]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACR2A]] | B | CRACR2A activity raises SLC43A1's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without CRACR2A | 0.089 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[HOXB9]] | B | HOXB9 activity raises SLC43A1's level | lines that do not express HOXB9 (17) vs lines expressing it (33) | 1.56× lower at baseline in the lines without HOXB9 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX30]] | B | SLC43A1 activity raises SNX30's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 1.84× lower at baseline in the lines without SLC43A1 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[AGAP3]] | B | SLC43A1 activity raises AGAP3's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 1.62× lower at baseline in the lines without SLC43A1 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP3K20]] | B | SLC43A1 activity lowers MAP3K20's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 1.94× higher at baseline in the lines without SLC43A1 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SNX30]] | B | SLC43A1 activity weakens SNX30's drug response | lines that do not express SLC43A1 (8) vs lines expressing it (39) | the lines without SLC43A1 respond 1.69× as strongly (z diff -1.37); strongest at Panobinostat 0.5 µM: 1.91x vs 1.36x (z diff -3.0) | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CRACR2A]] | B | SLC43A1 activity raises CRACR2A's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 2.71× lower at baseline in the lines without SLC43A1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.8, 41.4); signed map (12.1, -2.8). **Vector** length 62.1, 10.5% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.2 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 43 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,484,534-57,515,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | R00504, PB39; previously POV1 |
| Gene groups (HGNC) | Solute carrier family 43 |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75387](https://www.uniprot.org/uniprotkb/O75387) (Large neutral amino acids transporter small subunit 3):

> Uniport that mediates the transport of neutral amino acids such as L-leucine, L-isoleucine, L-valine, and L-phenylalanine. The transport activity is sodium ions-independent, electroneutral and mediated by a facilitated diffusion. Mediates the efflux of 3,3'-diiodo-L-thyronine (3,3'-T2) and 3-iodo-L-tyrosine (MIT).

**Summary**, from NCBI Gene [8501](https://www.ncbi.nlm.nih.gov/gene/8501):

> SLC43A1 belongs to the system L family of plasma membrane carrier proteins that transports large neutral amino acids (Babu et al., 2003 [PubMed 12930836]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:9225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9225) · Entrez [8501](https://www.ncbi.nlm.nih.gov/gene/8501) · UniProt [O75387](https://www.uniprot.org/uniprotkb/O75387) · Ensembl [ENSG00000149150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149150)

## Data

Gene col 7344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7344); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7344]; `tensor/DDL_lfc|DDL_z.npy` [7344]; `embed/gene_vectors.npy` [7344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7344 or target_col == 7344). Every well: [[SLC43A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC43A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
