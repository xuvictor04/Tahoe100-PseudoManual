---
symbol: "IFI27L2"
type: "gene"
col: 4086
ensembl_id: "ENSG00000119632"
name: "interferon alpha inducible protein 27 like 2"
location: "14q32.12"
module: 24
arm: "+"
pooled_cpm: 10.13
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# IFI27L2

*interferon alpha inducible protein 27 like 2* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.21× (z +4.2, q 0.015, up in 22 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.461× (z -4.1, q 0.017, down in 29 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.245×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD5]] (+0.79, fdr 1e-05), [[SMIM26]] (+0.78, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[C4orf48]] (+0.77, fdr 2e-05), [[MIEN1]] (+0.76, fdr 1e-05); moves opposite to [[IPO5]] (-0.72, fdr 1e-05), [[PSME3]] (-0.71, fdr 1e-05), [[ABCF2]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[DCTN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.21×** | +4.2 | 0.015 | 22/28 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.07×** | +3.7 | 0.045 | 10/19 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.7 | 0.045 | 16/30 (SW1417, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.97×** | +3.6 | 0.048 | 22/33 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4086.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.112×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 0.245×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -4.1 | 0.017 | 29/40 (SNU-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.467×** | -4.0 | 0.017 | 25/40 (HS-578T, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.481×** | -3.9 | 0.022 | 19/39 (J82, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.269× | -3.3 | 0.13 | 20/35 (NCI-H1792, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.540× | -3.2 | 0.13 | 21/37 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.639× | -3.2 | 0.13 | 22/38 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.245× (z -8.6) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD5]] | +0.79 | +0.50 / +0.82 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.78 | +0.55 / +0.83 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.77 | +0.47 / +0.86 | both halves | 2e-05 |  |
| [[MIEN1]] | +0.76 | +0.54 / +0.82 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.76 | +0.60 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[KRT10]] ⚠ | +0.75 | +0.57 / +0.82 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB4]] | +0.73 | +0.51 / +0.80 | both halves | 1e-05 |  |
| [[ATP5PD]] | +0.73 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[TRAPPC5]] | +0.73 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.73 | +0.44 / +0.78 | both halves | 3e-05 |  |
| [[COMMD6]] | +0.72 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[WDR83OS]] ⚠ | +0.72 | +0.60 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | +0.72 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[ATP5ME]] | +0.71 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[TCEAL8]] | +0.71 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | +0.71 | +0.54 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.72 | -0.50 / -0.80 | both halves | 1e-05 |  |
| [[PSME3]] | -0.71 | -0.51 / -0.75 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.69 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[FAM120A]] | -0.68 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.68 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[SSU72]] | -0.66 | -0.39 / -0.71 | both halves | 6e-05 |  |
| [[EIF4G1]] | -0.66 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[UBE2G2]] | -0.65 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.65 | -0.39 / -0.76 | both halves | 5e-05 |  |
| [[U2AF2]] | -0.65 | -0.42 / -0.71 | both halves | 4e-05 |  |
| [[SRSF1]] | -0.65 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[CAPRIN1]] | -0.65 | -0.46 / -0.69 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCTN3]] | B | IFI27L2 activity raises DCTN3's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without IFI27L2 | 0.031 | ⚠ within organs, on part of the lines |
| [[TMEM191A-1]] | B | IFI27L2 activity lowers TMEM191A-1's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without IFI27L2 | 0.049 | ⚠ within organs, on part of the lines |
| [[FAM120A]] | B | IFI27L2 activity raises FAM120A's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without IFI27L2 | 0.062 | ⚠ within organs, on part of the lines |
| [[SMIM27]] | B | IFI27L2 activity raises SMIM27's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without IFI27L2 | 0.084 | ⚠ within organs, on part of the lines |
| [[LGALS1]] | B | IFI27L2 activity raises LGALS1's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 4.17× lower at baseline in the lines without IFI27L2 | 0.087 | ⚠ within organs, on part of the lines |
| [[TCEAL3]] | B | IFI27L2 activity raises TCEAL3's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without IFI27L2 | 0.097 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.836). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.0, -16.4); signed map (-13.8, -3.5). **Vector** length 60.1, 15.0% of its response variance represented; |z| ≥ 3 in 459 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.57 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.0 | +3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | interferon alpha inducible protein 27 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:94,127,779-94,130,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TLH29; previously FAM14A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2X8](https://www.uniprot.org/uniprotkb/Q9H2X8) (Interferon alpha-inducible protein 27-like protein 2):

> Plays a role in the apoptotic process and has a pro-apoptotic activity.

**Summary**, from NCBI Gene [83982](https://www.ncbi.nlm.nih.gov/gene/83982):

> Predicted to enable molecular adaptor activity. Involved in apoptotic process. Located in mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19753) · Entrez [83982](https://www.ncbi.nlm.nih.gov/gene/83982) · UniProt [Q9H2X8](https://www.uniprot.org/uniprotkb/Q9H2X8) · Ensembl [ENSG00000119632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119632)

## Data

Gene col 4086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4086); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4086]; `tensor/DDL_lfc|DDL_z.npy` [4086]; `embed/gene_vectors.npy` [4086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4086 or target_col == 4086). Every well: [[IFI27L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI27L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
