---
symbol: "EDARADD"
type: "gene"
col: 11791
ensembl_id: "ENSG00000186197"
name: "EDAR associated via death domain"
location: "1q42.3-q43"
module: 19
arm: "+"
pooled_cpm: 22.92
n_lines_expressing: 24
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# EDARADD

*EDAR associated via death domain* — 1q42.3-q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +15.8, q 0e+00, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.588× (z -7.6, q 1e-11, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRFN5]] (+0.61, fdr 2e-05), [[RASSF8-AS1]] (+0.58, fdr 3e-05), [[WT1-AS]] (+0.54, fdr 2e-05); moves opposite to [[EPS15]] (-0.42, fdr 1e-04), [[HEBP1]] (-0.42, fdr 7e-04), [[TMCC1]] (-0.41, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 3 go from it, the strongest it → [[FSTL4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +15.8 | 0e+00 | 12/21 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +10.2 | 7e-22 | 1/15 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.0 | 3e-17 | 1/11 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +8.1 | 5e-14 | 7/22 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.5 | 6e-12 | 5/21 (C32, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.2 | 5e-11 | 2/12 (A549, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.023 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.6 | 0.023 | 3/22 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.031 | 1/20 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.031 | 5/20 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.031 | 1/22 (SHP-77) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.068 | 5/19 (HepG2/C3A, C-33 A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.2 | 0.070 | 0/20 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.588×** | -7.6 | 1e-11 | 18/21 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.597×** | -7.4 | 4e-11 | 16/21 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.618×** | -6.9 | 1e-09 | 16/21 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -5.1 | 6e-05 | 12/21 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -4.5 | 9e-04 | 16/20 (A-427, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.732×** | -4.3 | 0.002 | 7/21 (CHP-212, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.568×** | -4.2 | 0.002 | 9/22 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.735×** | -4.1 | 0.003 | 0/21 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -4.1 | 0.003 | 12/21 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.762×** | -3.9 | 0.006 | 7/21 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.7 | 0.011 | 4/22 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.014 | 11/21 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 446 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0479× (z -26.8) |
| [[HOP62 (line)]] | alt | 76.6 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0878× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -10.1) |
| [[PANC-1 (line)]] | alt | 67.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -17.5) |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.220× (z -8.9) |
| [[SW480 (line)]] | alt | 23.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.182× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.4) |
| [[A549 (line)]] | wt | 9.70 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.164× (z -9.2) |
| [[C32 (line)]] | wt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.8× (z +15.5) | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.151× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0992× (z -9.3) |
| [[SW48 (line)]] | wt | 6.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +8.8) | — |
| [[A-172 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRFN5]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[RASSF8-AS1]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[WT1-AS]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[STEAP1B-AS1]] | +0.54 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[GRAMD1B]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC35G2]] | +0.51 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[GABBR2]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TCF4]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CDH13]] | +0.50 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[LINC02454]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[BASP1-AS1]] | +0.49 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[SGIP1]] | +0.49 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS15]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.42 | -0.40 / -0.20 | both halves | 7e-04 |  |
| [[TMCC1]] | -0.41 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[PPP1R12B]] | -0.41 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[PHKB]] | -0.41 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[STX7]] | -0.40 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[EDEM2]] | -0.39 | -0.33 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises EDARADD's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.87× lower at baseline in the lines without ELFN1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[GABBR2]] | C | GABBR2 activity raises EDARADD's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without GABBR2 | 0.026 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent; co-absent with the target |
| [[WT1-AS]] | C | WT1-AS activity raises EDARADD's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 3.22× lower at baseline in the lines without WT1-AS | 0.028 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises EDARADD's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without PLEKHG4B | 0.033 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL4]] | B | EDARADD activity raises FSTL4's level | lines that do not express EDARADD (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without EDARADD | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000239268, NOL4, ASXL3 |
| [[PDE4B]] | B | EDARADD activity raises PDE4B's level | lines that do not express EDARADD (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without EDARADD | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000239268, NOL4, ASXL3 |
| [[FGF14]] | C | EDARADD activity raises FGF14's level | lines that do not express EDARADD (26) vs lines expressing it (24) | 3.07× lower at baseline in the lines without EDARADD | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000239268, NOL4, ASXL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.420). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.3, 17.5); signed map (21.2, 53.2). **Vector** length 59.1, 14.3% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +15.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | -0.9 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.0 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.2 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.7 | -7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | EDAR associated via death domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3-q43 — chr1:236,348,257-236,502,915 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CR |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWZ3](https://www.uniprot.org/uniprotkb/Q8WWZ3) (Ectodysplasin-A receptor-associated adapter protein):

> Adapter protein that interacts with EDAR DEATH domain and couples the receptor to EDA signaling pathway during morphogenesis of ectodermal organs. Mediates the activation of NF-kappa-B.

**Summary**, from NCBI Gene [128178](https://www.ncbi.nlm.nih.gov/gene/128178):

> This gene was identified by its association with ectodermal dysplasia, a genetic disorder characterized by defective development of hair, teeth, and eccrine sweat glands. The protein encoded by this gene is a death domain-containing protein, and is found to interact with EDAR, a death domain receptor known to be required for the development of hair, teeth and other ectodermal derivatives. This protein and EDAR are coexpressed in epithelial cells during the formation of hair follicles and teeth. …

**Accessions** — [HGNC:14341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14341) · Entrez [128178](https://www.ncbi.nlm.nih.gov/gene/128178) · UniProt [Q8WWZ3](https://www.uniprot.org/uniprotkb/Q8WWZ3) · Ensembl [ENSG00000186197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186197)

## Data

Gene col 11791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11791); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11791]; `tensor/DDL_lfc|DDL_z.npy` [11791]; `embed/gene_vectors.npy` [11791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11791 or target_col == 11791). Every well: [[EDARADD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDARADD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
