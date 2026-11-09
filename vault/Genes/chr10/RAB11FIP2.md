---
symbol: "RAB11FIP2"
type: "gene"
col: 2859
ensembl_id: "ENSG00000107560"
name: "RAB11 family interacting protein 2"
location: "10q26.11"
module: 29
arm: "+"
pooled_cpm: 40.84
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# RAB11FIP2

*RAB11 family interacting protein 2* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +7.0, q 2e-09, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.686× (z -6.1, q 5e-07, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.211×, KATO III 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.187×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.280×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (H4 0.266×); [[PH-797804 (drug)]] 5 µM in 1 line (SW48 0.0680×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.70, fdr 7e-06), [[FAIM]] (+0.67, fdr 3e-05), [[ANGEL2]] (+0.66, fdr 2e-05); moves opposite to [[ASMTL]] (-0.68, fdr 2e-05), [[RALY]] (-0.67, fdr 3e-05), [[ASL]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.0 | 2e-09 | 27/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +6.4 | 3e-08 | 32/47 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.6 | 3e-06 | 30/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.0 | 8e-05 | 30/47 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 1e-04 | 25/47 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.6 | 5e-04 | 23/47 (H4, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +4.1 | 0.003 | 18/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.006 | 21/47 (A-427, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.006 | 24/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +3.8 | 0.007 | 19/47 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.008 | 22/47 (H4, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.027 | 16/46 (HOP62, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.4 | 0.032 | 16/41 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.23×** | +3.3 | 0.033 | 16/47 (Hs 766T, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.038 | 17/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.041 | 19/46 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.052 | 18/47 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2859.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.211×, KATO III 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.187×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.280×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (H4 0.266×); [[PH-797804 (drug)]] 5 µM in 1 line (SW48 0.0680×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.686×** | -6.1 | 5e-07 | 31/47 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.763×** | -4.4 | 0.003 | 24/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.774×** | -4.2 | 0.005 | 23/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.711×** | -3.9 | 0.015 | 19/46 (H4, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.750× | -3.3 | 0.12 | 14/47 (SW1417, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.0 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.266× (z -9.3) |
| [[KATO III (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 60.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0950× (z -10.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 59.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 72.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.8) | — |
| [[RKO (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 52.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0680× (z -8.8) |
| [[A-172 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.99 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.70 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FAIM]] | +0.67 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ANGEL2]] | +0.66 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZC3HAV1L]] | +0.66 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[HDDC2]] | +0.65 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[STRADB]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SEPHS1]] | +0.65 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[VPS36]] | +0.63 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[SLC35G1]] | +0.63 | +0.60 / +0.37 | both halves | 7e-05 |  |
| [[MYLK-AS1]] | +0.62 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[MACROH2A2]] | +0.62 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[TSTD3]] | +0.62 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL]] | -0.68 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[RALY]] | -0.67 | -0.72 / -0.46 | both halves | 3e-05 |  |
| [[ASL]] | -0.63 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PPARA]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SLC66A2]] | -0.62 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[FAM89B]] | -0.62 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[TGFB1]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ATG101]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[DUSP5]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MIDN]] | -0.60 | -0.39 / -0.69 | both halves | 5e-05 |  |
| [[SLC27A1]] | -0.60 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[MLXIP]] | -0.58 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity lowers RAB11FIP2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.38× higher at baseline in the lines without TMEM92 | 0.023 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[HDAC6]] | B | HDAC6 activity raises RAB11FIP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers RAB11FIP2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-9.7, 12.8); signed map (-13.1, -40.8). **Vector** length 99.7, 24.0% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.3 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +3.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.7 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.3 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.0 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RAB11 family interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:118,004,916-118,046,941 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0941, nRip11, Rab11-FIP2 |
| Gene groups (HGNC) | C2 domain containing; RAB11 binding domain containing |
| Reactome | 3 pathways, smallest: Vasopressin regulates renal water homeostasis via Aquaporins; Aquaporin-mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L804](https://www.uniprot.org/uniprotkb/Q7L804) (Rab11 family-interacting protein 2):

> A Rab11 effector binding preferentially phosphatidylinositol 3,4,5-trisphosphate (PtdInsP3) and phosphatidic acid (PA) and acting in the regulation of the transport of vesicles from the endosomal recycling compartment (ERC) to the plasma membrane. Involved in insulin granule exocytosis. Also involved in receptor-mediated endocytosis and membrane trafficking of recycling endosomes, probably originating from clathrin-coated vesicles. Required in a complex with MYO5B and RAB11 for the transport of …

**Summary**, from NCBI Gene [22841](https://www.ncbi.nlm.nih.gov/gene/22841):

> Enables protein homodimerization activity and protein kinase binding activity. Involved in several processes, including TRAM-dependent toll-like receptor 4 signaling pathway; phagocytosis; and positive regulation of GTPase activity. Located in endosome and phagocytic cup. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29152) · Entrez [22841](https://www.ncbi.nlm.nih.gov/gene/22841) · UniProt [Q7L804](https://www.uniprot.org/uniprotkb/Q7L804) · Ensembl [ENSG00000107560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107560)

## Data

Gene col 2859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2859); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2859]; `tensor/DDL_lfc|DDL_z.npy` [2859]; `embed/gene_vectors.npy` [2859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2859 or target_col == 2859). Every well: [[RAB11FIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11FIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
