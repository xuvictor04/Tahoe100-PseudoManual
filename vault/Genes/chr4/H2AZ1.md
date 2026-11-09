---
symbol: "H2AZ1"
type: "gene"
col: 8838
ensembl_id: "ENSG00000164032"
name: "H2A.Z variant histone 1"
location: "4q23"
module: 71
arm: "+"
pooled_cpm: 56.59
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# H2AZ1

*H2A.Z variant histone 1* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +6.7, q 9e-09, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.244×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change); [[Thymol (drug)]] 0.05 µM in 1 line (NCI-H661 0.0629×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASF1B]] (+0.62, fdr 7e-06), [[CDK1]] (+0.60, fdr 7e-06), [[CKS1B]] (+0.60, fdr 1e-05); moves opposite to [[DDX1]] (-0.49, fdr 9e-05), [[PWP1]] (-0.47, fdr 6e-05), [[RNF20]] (-0.47, fdr 3e-04).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.7 | 9e-09 | 39/48 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.65×** | +6.1 | 2e-07 | 38/48 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.25×** | +5.8 | 1e-06 | 46/48 (C32, J82, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.3 | 2e-05 | 42/47 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **2.16×** | +5.0 | 7e-05 | 31/42 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.93×** | +4.7 | 2e-04 | 38/47 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.005 | 29/48 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.66×** | +3.7 | 0.016 | 31/48 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.66×** | +3.6 | 0.016 | 35/48 (C32, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +3.6 | 0.016 | 39/47 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.26×** | +3.4 | 0.032 | 41/48 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.68×** | +3.4 | 0.035 | 32/47 (C32, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.65×** | +3.2 | 0.051 | 27/48 (SNU-423, C32, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.14×** | +3.2 | 0.056 | 38/48 (HOP62, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.64×** | +3.2 | 0.060 | 26/48 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8838.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.244×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change); [[Thymol (drug)]] 0.05 µM in 1 line (NCI-H661 0.0629×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.440× | -3.1 | 0.84 | 31/48 (HS-578T, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 27.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 29.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.7) | — |
| [[C32 (line)]] | wt | 46.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H661 (line)]] | alt | 46.4 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0629× (z -8.7) |
| [[RKO (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[A-172 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 94.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASF1B]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 772 |
| [[CDK1]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 744 |
| [[CKS1B]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 577 |
| [[DLEU2]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CDC25C]] | +0.56 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[NUSAP1]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDCA5]] | +0.53 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[TUBA1B]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 | STRING 449 |
| [[DBF4B]] | +0.52 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NDC80]] | +0.52 | +0.54 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[FAM72A]] | +0.52 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[KIF2C]] | +0.52 | +0.48 / +0.58 | both halves | 2e-05 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX1]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[PWP1]] | -0.47 | -0.47 / -0.39 | both halves | 6e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RNF20]] | -0.47 | -0.53 / -0.27 | both halves | 3e-04 | STRING 828 |
| [[BMS1P20]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[QDPR]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[CCDC124]] | -0.45 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[ASCC2]] | -0.45 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[TTC5]] | -0.45 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises H2AZ1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.65× lower at baseline in the lines without PIMREG | 0.077 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.9, -52.4); signed map (-45.7, -42.6). **Vector** length 90.9, 36.7% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.0 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +3.9 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +3.7 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[OTS514 (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | -5.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | -4.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -4.6 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.2 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | H2A.Z variant histone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:99,948,086-99,950,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H2A.Z; previously H2AZ, H2AFZ |
| Gene groups (HGNC) | H2A histones |
| Hallmark sets | FATTY_ACID_METABOLISM, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 3 pathways, smallest: FXIIa activates plasma kallikrein-kinin system; Amyloid fiber formation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C0S5](https://www.uniprot.org/uniprotkb/P0C0S5) (Histone H2A.Z):

> Variant histone H2A which replaces conventional H2A in a subset of nucleosomes. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling. May be …

**Summary**, from NCBI Gene [3015](https://www.ncbi.nlm.nih.gov/gene/3015):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. This gene encodes a replication-independent …

**Accessions** — [HGNC:4741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4741) · Entrez [3015](https://www.ncbi.nlm.nih.gov/gene/3015) · UniProt [P0C0S5](https://www.uniprot.org/uniprotkb/P0C0S5) · Ensembl [ENSG00000164032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164032)

## Data

Gene col 8838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8838); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8838]; `tensor/DDL_lfc|DDL_z.npy` [8838]; `embed/gene_vectors.npy` [8838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8838 or target_col == 8838). Every well: [[H2AZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2AZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
