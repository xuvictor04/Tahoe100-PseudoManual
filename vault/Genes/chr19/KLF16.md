---
symbol: "KLF16"
type: "gene"
col: 5005
ensembl_id: "ENSG00000129911"
name: "KLF transcription factor 16"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 9.1
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KLF16

*KLF transcription factor 16* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +6.7, q 1e-08, up in 25 of 44 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.77× (z +5.4, q 9e-06, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.730× (z -4.2, q 0.018, down in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~45% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0735×); [[Penfluridol (drug)]] 5 µM in 1 line (KATO III 0.0834×); [[Vilanterol (drug)]] 0.05 µM in 1 line (Hs 766T 0.103×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA2L]] (+0.66, fdr 7e-06), [[ZNF598]] (+0.65, fdr 7e-06), [[HAGHL]] (+0.65, fdr 1e-05); moves opposite to [[SRP14]] (-0.60, fdr 4e-05), [[MINDY1]] (-0.55, fdr 2e-05), [[TSPAN6]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SH3BGRL]] → it (grade C ⚠); 1 goes from it, the strongest it → [[R3HDM4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.65×** | +6.7 | 1e-08 | 25/44 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.94×** | +6.0 | 6e-07 | 6/15 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.82×** | +5.6 | 3e-06 | 19/32 (LoVo, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +5.4 | 9e-06 | 27/43 (NCI-H1573, SNU-423, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.69×** | +5.0 | 7e-05 | 22/37 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.8 | 1e-04 | 20/36 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.16×** | +4.7 | 2e-04 | 21/39 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.003 | 19/47 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +4.0 | 0.005 | 5/21 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.85×** | +3.8 | 0.009 | 19/46 (PANC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.79×** | +3.6 | 0.017 | 12/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.6 | 0.017 | 15/43 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +3.4 | 0.034 | 14/47 (SW480, NCI-H1792, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +3.3 | 0.044 | 16/47 (SW480, NCI-H1792, …) | two highest doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.046 | 9/46 (SW1417, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.063 | 13/40 (A549, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5005.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0735×); [[Penfluridol (drug)]] 5 µM in 1 line (KATO III 0.0834×); [[Vilanterol (drug)]] 0.05 µM in 1 line (Hs 766T 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.730×** | -4.2 | 0.018 | 19/47 (NCI-H1573, AsPC-1, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 8.87 | 0 | 2 | — | [[Vilanterol (drug)]] 0.05 µM 0.103× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 5.51 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +12.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.13× (z +9.3) | — |
| [[KATO III (line)]] | alt | 5.13 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0834× (z -9.3) |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0767× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.151× (z -8.5) |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0735× (z -9.5) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA2L]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF598]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | same gene group; STRING 536 |
| [[HAGHL]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF276]] | +0.63 | +0.58 / +0.68 | both halves | 7e-06 | same gene group |
| [[FBXL6]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GPSM1]] | +0.60 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZNF316]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 | same gene group |
| [[MIDN]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DVL1]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MNT]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ESRRA]] | +0.58 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[AXIN1]] | +0.56 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP14]] | -0.60 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[MINDY1]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TSPAN6]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC13]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[AP3M1]] | -0.52 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TMX1]] | -0.52 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[FKBP3]] | -0.52 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[FUCA2]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[VBP1]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[DERA]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[NXT2]] | -0.49 | -0.37 / -0.44 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3BGRL]] | C | SH3BGRL activity lowers KLF16's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 1.50× higher at baseline in the lines without SH3BGRL | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[R3HDM4]] | C | KLF16's natural level weakens R3HDM4's drug response | KLF16's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.07; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-4.2, -25.8); signed map (-29.5, 3.7). **Vector** length 78.1, 16.3% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.5 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,852,399-1,863,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSLP2, BTEB4, DRRF |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Reactome | 3 pathways, smallest: TGFBR3 expression; Signaling by TGFBR3; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXK1](https://www.uniprot.org/uniprotkb/Q9BXK1) (Krueppel-like factor 16):

> Transcription factor that binds GC and GT boxes and displaces Sp1 and Sp3 from these sequences. Modulates dopaminergic transmission in the brain (By similarity).

**Summary**, from NCBI Gene [83855](https://www.ncbi.nlm.nih.gov/gene/83855):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within G protein-coupled dopamine receptor signaling pathway. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16857) · Entrez [83855](https://www.ncbi.nlm.nih.gov/gene/83855) · UniProt [Q9BXK1](https://www.uniprot.org/uniprotkb/Q9BXK1) · Ensembl [ENSG00000129911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129911)

## Data

Gene col 5005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5005); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5005]; `tensor/DDL_lfc|DDL_z.npy` [5005]; `embed/gene_vectors.npy` [5005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5005 or target_col == 5005). Every well: [[KLF16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
