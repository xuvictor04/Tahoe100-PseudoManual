---
symbol: "TBRG4"
type: "gene"
col: 5847
ensembl_id: "ENSG00000136270"
name: "FASTK mitochondrial RNA regulator 4"
location: "7p13"
module: 5
arm: "+"
pooled_cpm: 17.13
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TBRG4

*FASTK mitochondrial RNA regulator 4* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.71× (z +8.1, q 4e-13, up in 33 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.14× (z +6.0, q 4e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.689× (z -5.5, q 3e-05, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP2]] (+0.81, fdr 7e-06), [[WDR4]] (+0.79, fdr 7e-06), [[NOP16]] (+0.78, fdr 7e-06); moves opposite to [[OPTN]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +8.1 | 4e-13 | 33/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.52×** | +6.0 | 4e-07 | 26/43 (AsPC-1, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +6.0 | 4e-07 | 26/48 (NCI-H2347, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +5.8 | 9e-07 | 27/44 (RKO, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.9 | 1e-04 | 22/43 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.8 | 2e-04 | 22/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +4.3 | 0.001 | 11/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.36×** | +4.2 | 0.002 | 15/36 (KATO III, NCI-H460, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.003 | 13/44 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.003 | 12/45 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.026 | 14/47 (A498, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.043 | 7/45 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.043 | 9/47 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.22× | +3.0 | 0.10 | 9/48 (Hs 766T, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.689×** | -5.5 | 3e-05 | 23/46 (SW480, SW48, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 4e-04 | 21/48 (LoVo, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.778×** | -4.7 | 4e-04 | 20/48 (A-427, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.727×** | -4.7 | 4e-04 | 21/46 (HepG2/C3A, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.817×** | -4.4 | 0.001 | 22/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.794×** | -3.9 | 0.009 | 14/48 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.810×** | -3.9 | 0.009 | 17/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.787×** | -3.7 | 0.018 | 15/48 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.026 | 15/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.049 | 18/46 (A-427, NCI-H1573, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.859× | -3.3 | 0.056 | 11/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.795×** | -3.2 | 0.056 | 16/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.808×** | -3.1 | 0.089 | 12/48 (Hs 766T, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[SBI-0640756 (drug)]] 5 µM 0.0564× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.8) |
| [[SW48 (line)]] | wt | 38.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0980× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 9.76 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0879× (z -8.6) |
| [[RKO (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.6) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP2]] | +0.81 | +0.76 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 590 |
| [[WDR4]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[NOP16]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[GEMIN4]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[BYSL]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[EXOSC2]] | +0.74 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[TWNK]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[URB2]] | +0.73 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.72 | +0.81 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[PUS1]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPTN]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TBRG4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[LTBR]] | B | LTBR activity lowers TBRG4's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.38× higher at baseline in the lines without LTBR | 0.072 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[MAP2K2]] | B | MAP2K2 activity raises TBRG4's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.6, -37.2); signed map (-2.6, -47.2). **Vector** length 94.7, 19.8% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.58 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.58 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.61 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.1 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.7 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -4.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.3 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | FASTK mitochondrial RNA regulator 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:45,100,100-45,112,047 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cpr2, KIAA0948, H_TD2522F11.8, FASTKD4; previously TBRG4 |
| Gene groups (HGNC) | FASTK mitochondrial RNA binding family; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2, E2F_TARGETS |
| Reactome | 3 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969Z0](https://www.uniprot.org/uniprotkb/Q969Z0) (FAST kinase domain-containing protein 4):

> Plays a role in processing of mitochondrial RNA precursors and in stabilization of a subset of mature mitochondrial RNA species, such as MT-CO1, MT-CO2, MT-CYB, MT-CO3, MT-ND3, MT-ND5 and MT-ATP8/6. May play a role in cell cycle progression.

**Summary**, from NCBI Gene [9238](https://www.ncbi.nlm.nih.gov/gene/9238):

> Enables RNA binding activity. Involved in mitochondrial mRNA processing and regulation of mitochondrial mRNA stability. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17443) · Entrez [9238](https://www.ncbi.nlm.nih.gov/gene/9238) · UniProt [Q969Z0](https://www.uniprot.org/uniprotkb/Q969Z0) · Ensembl [ENSG00000136270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136270)

## Data

Gene col 5847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5847); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5847]; `tensor/DDL_lfc|DDL_z.npy` [5847]; `embed/gene_vectors.npy` [5847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5847 or target_col == 5847). Every well: [[TBRG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBRG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
