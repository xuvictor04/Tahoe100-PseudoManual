---
symbol: "HOXA10"
type: "gene"
col: 14795
ensembl_id: "ENSG00000253293"
name: "homeobox A10"
location: "7p15.2"
module: 201
arm: "+"
pooled_cpm: 7.75
n_lines_expressing: 30
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXA10

*homeobox A10* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +8.8, q 8e-16, up in 15 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.451× (z -7.9, q 1e-12, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA9]] (+0.74, fdr 7e-06, ⚠ same locus), [[HOXA11]] (+0.71, fdr 7e-06, ⚠ same locus), [[HOXA5]] (+0.68, fdr 7e-06, ⚠ same locus), [[HOXB5]] (+0.63, fdr 1e-05), [[ACOT2]] (+0.60, fdr 2e-04), [[HOXB7]] (+0.60, fdr 3e-05); moves opposite to [[CDC37]] (-0.55, fdr 2e-05), [[ADAMTSL5]] (-0.53, fdr 4e-05), [[CORO1C]] (-0.52, fdr 9e-05).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HOXA3]] → it (grade B ⚠); 7 go from it, the strongest it → [[HOXA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.8 | 8e-16 | 15/27 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +8.0 | 3e-13 | 17/24 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.3 | 2e-05 | 10/20 (A-172, SW1417, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.0 | 8e-05 | 12/22 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.0 | 8e-05 | 11/26 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +4.4 | 0.001 | 11/27 (LS 180, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.008 | 13/26 (Hs 766T, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.016 | 12/27 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.6 | 0.021 | 6/26 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.033 | 9/26 (LoVo, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.3 | 0.056 | 5/15 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.091 | 9/27 (AsPC-1, SW48, …) | top dose only | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.11 | 6/26 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.451×** | -7.9 | 1e-12 | 19/26 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.458×** | -7.8 | 2e-12 | 21/27 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.586×** | -7.5 | 1e-11 | 20/25 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.605×** | -5.0 | 9e-05 | 16/27 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.669×** | -3.8 | 0.018 | 12/26 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -3.7 | 0.024 | 9/27 (HT-29, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 25.4 | 8 (4 ⚠) | 3 | [[Selinexor (drug)]] 5 µM 4.10× (z +13.4) | [[Bortezomib (drug)]] 0.05 µM 0.223× (z -9.5) |
| [[A498 (line)]] | wt | 17.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.4) |
| [[LoVo (line)]] | wt | 22.3 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.85× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +10.0) | — |
| [[A-172 (line)]] | wt | 7.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.2) |
| [[HOP62 (line)]] | alt | 3.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.8) |
| [[HS-578T (line)]] | alt | 6.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0507× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.298× (z -9.1) |
| [[J82 (line)]] | alt | 7.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 4.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 4.92 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0336× (z -11.4) |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -17.4) |
| [[SW1417 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.7) | — |
| [[SW48 (line)]] | wt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.0) | — |
| [[SW480 (line)]] | alt | 16.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -8.9) |
| [[A-427 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 8 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA9]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | same gene group; STRING 931; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA11]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | same gene group; STRING 866; ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA5]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 | same gene group; STRING 883; ⚠ same locus (26.9 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA6]] | +0.66 | +0.45 / +0.67 | both halves | 3e-05 | same gene group; STRING 553; ⚠ same locus (20.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXB5]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 | same gene group |
| [[HOXA3]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 | same gene group; STRING 732; ⚠ same locus (18.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA10-AS]] | +0.61 | +0.39 / +0.66 | both halves | 5e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ACOT2]] | +0.60 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[HOXB7]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 | same gene group; STRING 494 |
| [[PANK1]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[HOXB4]] | +0.58 | +0.36 / +0.59 | both halves | 9e-05 | same gene group |
| [[SLC35D1]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[NDUFB2]] | +0.56 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[SLC16A14]] | +0.56 | +0.26 / +0.59 | both halves | 4e-04 |  |
| [[ACBD5]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PAPOLG]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RNF135]] | +0.55 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[KIF9-AS1]] | +0.55 | +0.45 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC37]] | -0.55 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ADAMTSL5]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.52 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[R3HDM4]] | -0.49 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[ANXA5]] | -0.49 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[MICAL2]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[ANO1]] | -0.47 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[ABLIM2]] | -0.46 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[SLC35C2]] | -0.46 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[MEGF6]] | -0.46 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[FLNC]] | -0.46 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity raises HOXA10's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.50× lower at baseline in the lines without HOXA3 | 0.052 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HOXA10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HOXA9]] | C | HOXA9 activity raises HOXA10's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 5.29× lower at baseline in the lines without HOXA9 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33; co-absent with the target |
| [[HOXA10-AS]] | C | HOXA10-AS activity raises HOXA10's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 3.95× lower at baseline in the lines without HOXA10-AS | 0.002 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent; co-absent with the target |
| [[HOXA11]] | C | HOXA11 activity raises HOXA10's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 4.23× lower at baseline in the lines without HOXA11 | 0.003 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA10 activity raises HOXA3's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without HOXA10 | 0.011 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[CDC37]] | B | HOXA10 activity lowers CDC37's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 1.12× higher at baseline in the lines without HOXA10 | 0.031 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[HOXA5]] | B | HOXA10 activity raises HOXA5's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without HOXA10 | 0.054 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[NLRX1]] | B | HOXA10 activity lowers NLRX1's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 1.14× higher at baseline in the lines without HOXA10 | 0.066 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[HOXA11]] | C | HOXA10 activity raises HOXA11's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 2.84× lower at baseline in the lines without HOXA10 | 0.022 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11; co-absent with the target |
| [[HOXA9]] | C | HOXA10 activity raises HOXA9's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 3.94× lower at baseline in the lines without HOXA10 | 0.023 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11; co-absent with the target |
| [[HOXA10-AS]] | C | HOXA10 activity raises HOXA10-AS's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without HOXA10 | 0.042 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.1, 27.6); signed map (-5.1, 6.7). **Vector** length 54.1, 11.9% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Kidney development* (reactome, mean cos +0.65 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | -7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,170,605-27,180,261 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1H, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P31260](https://www.uniprot.org/uniprotkb/P31260) (Homeobox protein Hox-A10):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis. Binds to the DNA sequence 5'-AA[AT]TTTTATTAC-3'.

**Summary**, from NCBI Gene [3206](https://www.ncbi.nlm.nih.gov/gene/3206):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor that may regulate gene expression, morphogenesis, and differentiation. More specifically, it may function in fertility, embryo viability, …

**Accessions** — [HGNC:5100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5100) · Entrez [3206](https://www.ncbi.nlm.nih.gov/gene/3206) · UniProt [P31260](https://www.uniprot.org/uniprotkb/P31260) · Ensembl [ENSG00000253293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253293)

## Data

Gene col 14795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14795); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14795]; `tensor/DDL_lfc|DDL_z.npy` [14795]; `embed/gene_vectors.npy` [14795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14795 or target_col == 14795). Every well: [[HOXA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
