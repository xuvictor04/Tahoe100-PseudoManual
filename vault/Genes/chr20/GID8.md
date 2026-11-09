---
symbol: "GID8"
type: "gene"
col: 2092
ensembl_id: "ENSG00000101193"
name: "GID complex subunit 8 homolog"
location: "20q13.33"
module: 130
arm: "+"
pooled_cpm: 46.99
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# GID8

*GID complex subunit 8 homolog* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.41× (z +7.0, q 1e-09, up in 32 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.38× (z +6.5, q 2e-08, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.772× (z -7.5, q 3e-11, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.169×, RPMI-7951 0.277×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW1417 0.614×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSM14B]] (+0.64, fdr 7e-06), [[POLDIP3]] (+0.61, fdr 1e-05), [[BAG4]] (+0.59, fdr 7e-06); moves opposite to [[BICD1]] (-0.57, fdr 1e-05), [[HNRNPA2B1]] (-0.54, fdr 1e-05), [[GALNT1]] (-0.54, fdr 4e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ASPH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.0 | 1e-09 | 32/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +6.5 | 2e-08 | 33/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.35×** | +6.1 | 1e-07 | 31/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +5.6 | 3e-06 | 29/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.4 | 8e-06 | 0/49 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.9 | 0.009 | 15/46 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.009 | 20/49 (SK-MEL-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.026 | 12/37 (NCI-H1573, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.3 | 0.057 | 14/43 (SNU-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.11 | 16/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2092.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.169×, RPMI-7951 0.277×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.323×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW1417 0.614×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -7.5 | 3e-11 | 33/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -5.0 | 2e-04 | 24/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.833× | -3.7 | 0.035 | 20/48 (HOP62, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.841× | -3.6 | 0.054 | 17/48 (NCI-H23, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.850× | -3.3 | 0.080 | 17/48 (HepG2/C3A, A-427, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.891× | -3.3 | 0.080 | 8/48 (SK-MEL-2, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.9 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 32.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.6) | — |
| [[SW480 (line)]] | alt | 57.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +11.3) | — |
| [[A-427 (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[NCI-H2030 (line)]] | alt | 59.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 60.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 118 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.614× (z -9.1) |
| [[SW48 (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM14B]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[POLDIP3]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[BAG4]] | +0.59 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[HOXC10]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TMUB1]] | +0.57 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[COPS4]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GLE1]] | +0.56 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[NELFA]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[DUSP11]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.54 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[MKRN1]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TTC9C]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICD1]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GALNT1]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ASPH]] | -0.52 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[BMAL2]] | -0.51 | -0.47 / -0.43 | both halves | 4e-05 |  |
| [[MSN]] | -0.51 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[MTAP]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DST]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TUSC3]] | -0.50 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[BACH1]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[INO80C]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[GALNT10]] | -0.49 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASPH]] | B | ASPH activity lowers GID8's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.42× higher at baseline in the lines without ASPH | 0.072 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.7, -20.1); signed map (-11.2, 2.1). **Vector** length 70.0, 13.0% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | +3.4 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +0.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -0.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | GID complex subunit 8 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,938,147-62,948,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20602, bA305P22.1, TWA1; previously C20orf11 |
| Gene groups (HGNC) | CTLH complex subunits |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWU2](https://www.uniprot.org/uniprotkb/Q9NWU2) (Glucose-induced degradation protein 8 homolog):

> Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. Acts as a positive regulator of Wnt signaling pathway by promoting beta-catenin (CTNNB1) nuclear accumulation.

**Summary**, from NCBI Gene [54994](https://www.ncbi.nlm.nih.gov/gene/54994):

> Predicted to enable protein-macromolecule adaptor activity. Involved in positive regulation of canonical Wnt signaling pathway and positive regulation of cell population proliferation. Located in cell junction; cytosol; and nucleoplasm. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15857) · Entrez [54994](https://www.ncbi.nlm.nih.gov/gene/54994) · UniProt [Q9NWU2](https://www.uniprot.org/uniprotkb/Q9NWU2) · Ensembl [ENSG00000101193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101193)

## Data

Gene col 2092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2092); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2092]; `tensor/DDL_lfc|DDL_z.npy` [2092]; `embed/gene_vectors.npy` [2092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2092 or target_col == 2092). Every well: [[GID8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GID8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
