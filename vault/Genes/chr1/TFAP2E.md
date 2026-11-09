---
symbol: "TFAP2E"
type: "gene"
col: 3844
ensembl_id: "ENSG00000116819"
name: "transcription factor AP-2 epsilon"
location: "1p34.3"
module: 38
arm: "+"
pooled_cpm: 5.1
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TFAP2E

*transcription factor AP-2 epsilon* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.00× (z +11.9, q 6e-30, up in 26 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.06× (z +8.1, q 1e-13, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.549× (z -6.8, q 6e-09, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP2A1]] (+0.68, fdr 7e-06), [[TINCR]] (+0.68, fdr 7e-06), [[SYCE2]] (+0.68, fdr 7e-06); moves opposite to [[ARMT1]] (-0.53, fdr 3e-04), [[GPD2]] (-0.52, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMEM225B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +11.9 | 6e-30 | 26/29 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +8.1 | 1e-13 | 30/47 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.6 | 9e-09 | 19/41 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +5.7 | 2e-06 | 25/46 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 3e-05 | 13/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.5 | 5e-04 | 14/47 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.015 | 7/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.4 | 0.042 | 8/43 (H4, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.047 | 9/37 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.069 | 6/46 (HEC-1-A, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.069 | 9/47 (LS 180, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -6.8 | 6e-09 | 24/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -6.3 | 1e-07 | 20/44 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -6.0 | 4e-07 | 22/46 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.585×** | -5.8 | 8e-07 | 20/44 (A-427, J82, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -5.5 | 4e-06 | 18/44 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.664×** | -4.6 | 3e-04 | 19/40 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -4.3 | 0.002 | 13/41 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.711×** | -3.9 | 0.007 | 14/43 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.764× | -3.1 | 0.13 | 15/44 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.765× | -3.0 | 0.13 | 12/44 (HOP62, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 6.19 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0697× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[HI-TOPK-032 (drug)]] 0.05 µM 0.0848× (z -9.8) |
| [[A498 (line)]] | wt | 7.61 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.180× (z -8.6) |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 4.82 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -8.6) |
| [[A-172 (line)]] | wt | 3.51 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0763× (z -8.5) |
| [[HT-29 (line)]] | alt | 5.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 4.42 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0854× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 5.38 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0861× (z -8.8) |
| [[SNU-423 (line)]] | alt | 5.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A1]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[TINCR]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.68 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[ST6GALNAC6-1]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[OGG1]] | +0.67 | +0.57 / +0.77 | both halves | 9e-06 |  |
| [[PHKG1]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RAPGEFL1]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TRIM3]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMT1]] | -0.53 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[GPD2]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM225B]] | B | TMEM225B activity raises TFAP2E's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without TMEM225B | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TFAP2E's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TFAP2E's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -20.3); signed map (12.0, 12.0). **Vector** length 65.1, 9.55% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +11.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.4 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.5 | -0.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor AP-2 epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,573,314-35,595,328 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP2E, AP-2epsilon |
| Gene groups (HGNC) | Transcription factor AP-2 family |
| Reactome | 3 pathways, smallest: Activation of the TFAP2 (AP-2) family of transcription factors; Negative regulation of activity of TFAP2 (AP-2) family transcription factors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6VUC0](https://www.uniprot.org/uniprotkb/Q6VUC0) (Transcription factor AP-2-epsilon):

> Sequence-specific DNA-binding protein that interacts with inducible viral and cellular enhancer elements to regulate transcription of selected genes. AP-2 factors bind to the consensus sequence 5'-GCCNNNGGC-3' and activate genes involved in a large spectrum of important biological functions including proper eye, face, body wall, limb and neural tube development. They also suppress a number of genes including MCAM/MUC18, C/EBP alpha and MYC. AP-2-epsilon may play a role in the development of the …

**Summary**, from NCBI Gene [339488](https://www.ncbi.nlm.nih.gov/gene/339488):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in positive regulation of transcription by RNA polymerase II and regulation of cell population proliferation. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30774) · Entrez [339488](https://www.ncbi.nlm.nih.gov/gene/339488) · UniProt [Q6VUC0](https://www.uniprot.org/uniprotkb/Q6VUC0) · Ensembl [ENSG00000116819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116819)

## Data

Gene col 3844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3844); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3844]; `tensor/DDL_lfc|DDL_z.npy` [3844]; `embed/gene_vectors.npy` [3844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3844 or target_col == 3844). Every well: [[TFAP2E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFAP2E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
