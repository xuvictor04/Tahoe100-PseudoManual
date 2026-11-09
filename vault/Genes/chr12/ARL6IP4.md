---
symbol: "ARL6IP4"
type: "gene"
col: 11257
ensembl_id: "ENSG00000182196"
name: "ARF like GTPase 6 interacting protein 4"
location: "12q24.31"
module: 24
arm: "+"
pooled_cpm: 43.31
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ARL6IP4

*ARF like GTPase 6 interacting protein 4* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.00× (z +10.6, q 1e-23, up in 45 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (HOP62 5.65×, COLO 205 7.92×, HEC-1-A 4.95×, A498 5.04×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 7.30×, KATO III 4.28×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.555× (z -4.5, q 0.004, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5IF1]] (+0.66, fdr 7e-06), [[ATP5ME]] (+0.62, fdr 1e-05), [[GADD45GIP1]] (+0.56, fdr 2e-05); moves opposite to [[MMGT1]] (-0.47, fdr 1e-04), [[HSPBP1]] (-0.47, fdr 5e-05), [[MAT2A]] (-0.46, fdr 5e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11257.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (HOP62 5.65×, COLO 205 7.92×, HEC-1-A 4.95×, A498 5.04×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 7.30×, KATO III 4.28×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.00×** | +10.6 | 1e-23 | 45/45 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +8.9 | 2e-16 | 39/39 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +5.8 | 1e-06 | 38/43 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.05×** | +5.5 | 5e-06 | 42/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.555×** | -4.5 | 0.004 | 36/48 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.576×** | -4.2 | 0.007 | 39/48 (C-33 A, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.614×** | -3.7 | 0.036 | 28/48 (C-33 A, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.412×** | -3.5 | 0.065 | 35/48 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.646×** | -3.3 | 0.091 | 31/48 (C-33 A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.434×** | -3.3 | 0.091 | 36/48 (LOX-IMVI, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.708× | -3.2 | 0.10 | 31/47 (SNU-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.634× | -3.2 | 0.11 | 28/47 (SK-MEL-2, LS 180, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.671× | -3.1 | 0.14 | 22/47 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 46.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +10.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 46.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.30× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +8.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.92× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 47.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.3) |
| [[SNU-423 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5IF1]] | +0.66 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[ATP5ME]] | +0.62 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[GADD45GIP1]] | +0.56 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[NDUFC1]] | +0.55 | +0.43 / +0.76 | both halves | 4e-05 |  |
| [[EMC9]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[RPS26]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SUCLG1]] | +0.54 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[NDUFB10]] | +0.54 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[UQCRB]] ⚠ | +0.54 | +0.33 / +0.64 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB24]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[SNHG32]] | +0.52 | +0.29 / +0.55 | both halves | 2e-04 |  |
| [[NDUFB1]] | +0.52 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[CHCHD5]] | +0.52 | +0.28 / +0.60 | both halves | 3e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMGT1]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[HSPBP1]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[MAT2A]] | -0.46 | -0.23 / -0.59 | both halves | 5e-04 |  |
| [[GART]] | -0.46 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[HNRNPAB]] | -0.45 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[VMA21]] | -0.45 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[GCLM]] | -0.44 | -0.31 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARL6IP4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.6, -23.2); signed map (-37.9, 8.7). **Vector** length 43.3, 10.8% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +0.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.9 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | -0.6 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +0.9 | -1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.0 | +10.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -1.8 | +5.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | +0.2 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 6 interacting protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,980,060-122,982,913 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SR-25, SRp25, SFRS20, SRrp37 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q66PJ3](https://www.uniprot.org/uniprotkb/Q66PJ3) (ADP-ribosylation factor-like protein 6-interacting protein 4):

> Involved in modulating alternative pre-mRNA splicing with either 5' distal site activation or preferential use of 3' proximal site. In case of infection by Herpes simplex virus (HSVI), may act as a splicing inhibitor of HSVI pre-mRNA.

**Summary**, from NCBI Gene [51329](https://www.ncbi.nlm.nih.gov/gene/51329):

> Enables identical protein binding activity. Predicted to be involved in RNA splicing. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18076) · Entrez [51329](https://www.ncbi.nlm.nih.gov/gene/51329) · UniProt [Q66PJ3](https://www.uniprot.org/uniprotkb/Q66PJ3) · Ensembl [ENSG00000182196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182196)

## Data

Gene col 11257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11257); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11257]; `tensor/DDL_lfc|DDL_z.npy` [11257]; `embed/gene_vectors.npy` [11257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11257 or target_col == 11257). Every well: [[ARL6IP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL6IP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
