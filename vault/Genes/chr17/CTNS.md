---
symbol: "CTNS"
type: "gene"
col: 469
ensembl_id: "ENSG00000040531"
name: "cystinosin, lysosomal cystine transporter"
location: "17p13.2"
module: 122
arm: "+"
pooled_cpm: 7.9
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# CTNS

*cystinosin, lysosomal cystine transporter* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.75× (z +16.7, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.712× (z -5.6, q 1e-05, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCOLN1]] (+0.69, fdr 7e-06), [[VAC14]] (+0.67, fdr 7e-06), [[PEPD]] (+0.60, fdr 1e-05); moves opposite to [[PDS5B]] (-0.48, fdr 3e-05), [[SMAD5]] (-0.46, fdr 6e-05), [[CAND1]] (-0.46, fdr 1e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +16.7 | 0e+00 | 43/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +14.1 | 7e-43 | 41/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +14.1 | 7e-43 | 43/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +11.6 | 5e-29 | 26/43 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.2 | 2e-14 | 23/43 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +6.5 | 9e-09 | 21/47 (SNU-423, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.8 | 7e-07 | 15/38 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 8e-07 | 16/43 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.7 | 2e-04 | 14/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.6 | 3e-04 | 12/43 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.22×** | +4.5 | 3e-04 | 8/48 (RPMI-7951, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 13/41 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +4.0 | 0.002 | 6/47 (NCI-H2030, A498, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 9/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.008 | 6/47 (SW1417, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.010 | 9/42 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.010 | 10/47 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.012 | 11/47 (NCI-H460, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.712×** | -5.6 | 1e-05 | 16/46 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -5.2 | 6e-05 | 15/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.627×** | -3.6 | 0.060 | 6/41 (HS-578T, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.5 | 0.075 | 4/48 (HepG2/C3A, SNU-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.824× | -3.1 | 0.19 | 9/47 (J82, A549, …) | top dose only |  |
| [[Flutamide (drug)]] 0.5 µM |  | 0.831× | -3.1 | 0.19 | 4/46 (NCI-H2030, SNU-423, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.675× | -3.0 | 0.19 | 4/17 (PANC-1, A-172, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.72 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +17.4) | — |
| [[Hs 766T (line)]] | wt | 6.14 | 0 | 2 (1 ⚠) | — | [[Allantoin (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[SW480 (line)]] | alt | 8.88 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.57× (z +9.5) | — |
| [[A-172 (line)]] | wt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +8.9) | — |
| [[A498 (line)]] | wt | 7.51 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.233× (z -8.8) ⚠ toxic |
| [[C32 (line)]] | wt | 7.09 | 0 | 1 | — | [[Belumosudil (drug)]] 0.05 µM 0.0465× (z -11.1) |
| [[COLO 205 (line)]] | alt | 7.11 | 0 | 1 | — | [[Carbamazepine (drug)]] 5 µM 0.0562× (z -9.8) |
| [[HS-578T (line)]] | alt | 7.90 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0984× (z -11.2) |
| [[J82 (line)]] | alt | 8.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 5.31 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0633× (z -10.4) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCOLN1]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | STRING 485 |
| [[VAC14]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PEPD]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SLC38A7]] | +0.59 | +0.63 / +0.61 | both halves | 7e-06 | STRING 479 |
| [[ZFYVE26]] | +0.58 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[AMDHD2]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MROH1]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ATP6V0D1]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CTSA]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SLC66A1]] | +0.54 | +0.57 / +0.56 | both halves | 1e-05 | same gene group; pathway: Miscellaneous transport and binding events; STRING 837 |
| [[SPNS1]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5B]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SMAD5]] | -0.46 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[CAND1]] | -0.46 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[CSNK1G3]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[KCTD3]] | -0.44 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[ABHD10]] | -0.43 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[PRKAA1]] | -0.42 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[MTF2]] | -0.42 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RYK]] | -0.41 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[MACIR]] | -0.41 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[CDC40]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[DHX15]] | -0.40 | -0.52 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAT]] | B | LAT activity raises CTNS's level | lines that do not express LAT (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without LAT | 0.098 | ⚠ within organs, on part of the lines; also absent: FRG1BP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-45.3, 12.0); signed map (-8.8, -20.5). **Vector** length 58.5, 7.80% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +11.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cystinosin, lysosomal cystine transporter |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,636,459-3,663,103 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTNS-LSB, PQLC4, SLC66A4 |
| Gene groups (HGNC) | Solute carrier family 66 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: SLC-mediated transport of oligopeptides; Miscellaneous transport and binding events; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O60931](https://www.uniprot.org/uniprotkb/O60931) (Cystinosin):

> Cystine/H(+) symporter that mediates export of cystine, the oxidized dimer of cysteine, from lysosomes. Plays an important role in melanin synthesis by catalyzing cystine export from melanosomes, possibly by inhibiting pheomelanin synthesis. In addition to cystine export, also acts as a positive regulator of mTORC1 signaling in kidney proximal tubular cells, via interactions with components of the v-ATPase and Ragulator complexes. Also involved in small GTPase-regulated vesicle trafficking and …

**Summary**, from NCBI Gene [1497](https://www.ncbi.nlm.nih.gov/gene/1497):

> This gene encodes a seven-transmembrane domain protein that functions to transport cystine out of lysosomes. Its activity is driven by the H+ electrochemical gradient of the lysosomal membrane. Mutations in this gene cause cystinosis, a lysosomal storage disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:2518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2518) · Entrez [1497](https://www.ncbi.nlm.nih.gov/gene/1497) · UniProt [O60931](https://www.uniprot.org/uniprotkb/O60931) · Ensembl [ENSG00000040531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040531)

## Data

Gene col 469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 469); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 469]; `tensor/DDL_lfc|DDL_z.npy` [469]; `embed/gene_vectors.npy` [469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 469 or target_col == 469). Every well: [[CTNS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
