---
symbol: "TSFM"
type: "gene"
col: 4422
ensembl_id: "ENSG00000123297"
name: "Ts translation elongation factor, mitochondrial"
location: "12q14.1"
module: 168
arm: "+"
pooled_cpm: 8.26
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# TSFM

*Ts translation elongation factor, mitochondrial* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.64× (z +10.3, q 5e-22, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.571× (z -5.9, q 2e-06, down in 26 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.650× (z -4.5, q 6e-04, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTRR]] (+0.68, fdr 7e-06), [[TIMM23]] (+0.68, fdr 1e-05), [[SDHAP4]] (+0.67, fdr 7e-06); moves opposite to [[ZNF638]] (-0.59, fdr 3e-05), [[LINC02307]] (-0.58, fdr 2e-05), [[KANSL1L]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LARGE1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.64×** | +10.3 | 5e-22 | 42/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.05×** | +9.0 | 1e-16 | 32/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +8.7 | 5e-16 | 39/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +8.5 | 3e-15 | 43/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.16×** | +7.9 | 3e-13 | 39/46 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +4.1 | 0.004 | 15/47 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +3.7 | 0.015 | 9/47 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.14 | 2/47 (HepG2/C3A, NCI-H2030) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.571×** | -5.9 | 2e-06 | 26/47 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.686×** | -5.6 | 3e-06 | 22/44 (NCI-H1792, A498, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.587×** | -5.6 | 3e-06 | 25/44 (A-172, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.598×** | -5.2 | 2e-05 | 24/46 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -4.5 | 6e-04 | 20/46 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -3.7 | 0.023 | 17/46 (C32, RKO, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.641×** | -3.4 | 0.064 | 8/44 (SK-MEL-2, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 3 | — | [[Encorafenib (drug)]] 0.05 µM 0.0605× (z -9.1) |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 2 (2 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.104× (z -9.1) ⚠ toxic |
| [[C32 (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0857× (z -10.0) |
| [[LS 180 (line)]] | wt | 6.64 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0740× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 6.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0744× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 7.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[AsPC-1 (line)]] | alt | 6.08 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[HS-578T (line)]] | alt | 7.09 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0917× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~88% of this change |
| [[LOX-IMVI (line)]] | wt | 5.89 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.107× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 8.85 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0607× (z -12.0) |
| [[SW480 (line)]] | alt | 8.92 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRR]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TIMM23]] | +0.68 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[SDHAP4]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NOMO3]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.65 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[VTI1B]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ZNF17]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF638]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LINC02307]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[KANSL1L]] | -0.57 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ZNF335]] | -0.56 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ANKRD26]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[CUX1]] | -0.56 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[LITAF]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[UST]] | -0.55 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[BAZ2B]] | -0.55 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[CAMK2D]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[KIF21A]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LARGE1]] | B | LARGE1 activity lowers TSFM's level | lines that do not express LARGE1 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without LARGE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000249141; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers TSFM's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK14]] | B | MAPK14 activity lowers TSFM's level | compounds that target MAPK14: 2 of 2 raise it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-9.0, -16.1); signed map (-41.8, -16.7). **Vector** length 74.6, 12.8% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +8.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -4.3 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.3 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Tofacitinib (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.4 | -0.4 |
|  | [[γ-Oryzanol (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Ts translation elongation factor, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,782,761-57,808,071 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EF-Tsmt, EF-TS |
| Reactome | 3 pathways, smallest: Mitochondrial translation elongation; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P43897](https://www.uniprot.org/uniprotkb/P43897) (Elongation factor Ts, mitochondrial):

> Associates with the EF-Tu.GDP complex and induces the exchange of GDP to GTP. It remains bound to the aminoacyl-tRNA.EF-Tu.GTP complex up to the GTP hydrolysis stage on the ribosome. Participates in mitochondrial translation.

**Summary**, from NCBI Gene [10102](https://www.ncbi.nlm.nih.gov/gene/10102):

> This gene encodes a mitochondrial translation elongation factor. The encoded protein is an enzyme that catalyzes the exchange of guanine nucleotides on the translation elongation factor Tu during the elongation step of mitchondrial protein translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-3 syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:12367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12367) · Entrez [10102](https://www.ncbi.nlm.nih.gov/gene/10102) · UniProt [P43897](https://www.uniprot.org/uniprotkb/P43897) · Ensembl [ENSG00000123297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123297)

## Data

Gene col 4422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4422); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4422]; `tensor/DDL_lfc|DDL_z.npy` [4422]; `embed/gene_vectors.npy` [4422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4422 or target_col == 4422). Every well: [[TSFM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSFM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
