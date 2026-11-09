---
symbol: "FIBCD1"
type: "gene"
col: 5106
ensembl_id: "ENSG00000130720"
name: "fibrinogen C domain containing 1"
location: "9q34.12"
module: 195
arm: "+"
pooled_cpm: 7.15
n_lines_expressing: 39
n_dd_up: 9
n_dd_down: 33
n_dd_up_clean: 6
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# FIBCD1

*fibrinogen C domain containing 1* — 9q34.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.17× (z +12.4, q 3e-32, up in 3 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +7.0, q 3e-10, up in 13 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.405× (z -14.2, q 4e-43, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQSEC1]] (+0.58, fdr 9e-06), [[SLCO4A1]] (+0.57, fdr 1e-05), [[SPRED2]] (+0.57, fdr 1e-05); moves opposite to [[SLC44A3]] (-0.53, fdr 4e-05), [[GOPC]] (-0.50, fdr 6e-05), [[PPP1R9A]] (-0.46, fdr 3e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MGAT5B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +12.4 | 3e-32 | 3/11 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.1 | 3e-17 | 6/17 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.0 | 3e-10 | 13/31 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.8 | 1e-09 | 1/12 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.009 | 2/28 (PANC-1, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.018 | 8/33 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.018 | 9/35 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.067 | 7/28 (LoVo, H4, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.097 | 4/31 (HS-578T, J82, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.47× | +3.0 | 0.13 | 3/21 (LoVo, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 2 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5106.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.405×** | -14.2 | 4e-43 | 26/32 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.297×** | -13.0 | 5e-36 | 28/33 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.374×** | -10.9 | 2e-25 | 26/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.408×** | -10.0 | 3e-21 | 22/35 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.417×** | -9.7 | 3e-20 | 21/35 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -8.9 | 5e-17 | 21/34 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.475×** | -8.3 | 1e-14 | 20/34 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.490×** | -7.9 | 1e-13 | 22/35 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.507×** | -7.6 | 3e-12 | 21/36 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.565×** | -5.6 | 1e-06 | 14/36 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -5.5 | 2e-06 | 17/35 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.707×** | -5.4 | 3e-06 | 18/35 (SNU-423, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.616×** | -5.4 | 3e-06 | 13/35 (SW480, SW 900, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.572×** | -5.0 | 2e-05 | 15/36 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.635×** | -4.8 | 7e-05 | 13/34 (SW480, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.5 | 0 | 14 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0431× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -14.3) |
| [[A-172 (line)]] | wt | 6.79 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0646× (z -16.4) |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -23.1) |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.5) |
| [[HOP62 (line)]] | alt | 9.11 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -13.2) |
| [[J82 (line)]] | alt | 7.30 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.9) |
| [[A498 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.2) |
| [[A549 (line)]] | wt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.60× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0208× (z -13.0) |
| [[H4 (line)]] | wt | 8.91 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0612× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 3.11 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0558× (z -8.9) |
| [[A-427 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQSEC1]] | +0.58 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[SLCO4A1]] | +0.57 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[WT1-AS]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SCUBE1]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[WT1]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TMEM255B]] | +0.53 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ESYT3]] | +0.53 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[WDFY2]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF275]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CPNE5]] | +0.52 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[SHC3]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A3]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GOPC]] | -0.50 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[PPP1R9A]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ALCAM]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GRAMD2B]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[RPS6KA6]] | -0.45 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ZNF260]] | -0.45 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[CD2AP]] | -0.45 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[FIGN]] | -0.45 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SETD2]] | -0.44 | -0.38 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT5B]] | B | MGAT5B activity raises FIBCD1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without MGAT5B | 0.005 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL |
| [[KCNK3]] | B | KCNK3 activity raises FIBCD1's level | lines that do not express KCNK3 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without KCNK3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, IGFN1 |
| [[GABBR2]] | B | GABBR2 activity raises FIBCD1's level | lines that do not express GABBR2 (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without GABBR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, LMX1B; maybe low, not absent |
| [[SDK1]] | B | SDK1 activity raises FIBCD1's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.67× lower at baseline in the lines without SDK1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[KCNK13]] | B | KCNK13 activity raises FIBCD1's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without KCNK13 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity lowers FIBCD1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without SLC44A3 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[SHC3]] | B | SHC3 activity raises FIBCD1's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 1.46× lower at baseline in the lines without SHC3 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[PARVG]] | B | PARVG activity strengthens FIBCD1's drug response | lines that do not express PARVG (11) vs lines expressing it (24) | the lines without PARVG respond 0.48× as strongly (z diff +1.88); strongest at Harringtonine 5 µM: 0.41x vs 0.17x (z diff +3.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8; target measured in part of the lines; artifact flags |
| [[PARVG]] | B | PARVG activity raises FIBCD1's level | lines that do not express PARVG (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without PARVG | 0.093 | ⚠ within organs, on part of the lines; also absent: PARVB, DCLK2, RASSF8 |
| [[MAP2K1]] | B | MAP2K1 activity raises FIBCD1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.4, 4.6); signed map (7.2, 54.8). **Vector** length 72.2, 14.8% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -10.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -13.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -7.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | fibrinogen C domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.12 — chr9:130,902,438-130,939,286 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14810 |
| Gene groups (HGNC) | Fibrinogen C domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N539](https://www.uniprot.org/uniprotkb/Q8N539) (Fibrinogen C domain-containing protein 1):

> Acetyl group-binding receptor which shows a high-affinity and calcium-dependent binding to acetylated structures such as chitin, some N-acetylated carbohydrates, and amino acids, but not to their non-acetylated counterparts. Can facilitate the endocytosis of acetylated components.

**Summary**, from NCBI Gene [84929](https://www.ncbi.nlm.nih.gov/gene/84929):

> FIBCD1 is a conserved type II transmembrane endocytic receptor that binds chitin and is located primarily in the intestinal brush border (Schlosser et al., 2009 [PubMed 19710473]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:25922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25922) · Entrez [84929](https://www.ncbi.nlm.nih.gov/gene/84929) · UniProt [Q8N539](https://www.uniprot.org/uniprotkb/Q8N539) · Ensembl [ENSG00000130720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130720)

## Data

Gene col 5106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5106); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5106]; `tensor/DDL_lfc|DDL_z.npy` [5106]; `embed/gene_vectors.npy` [5106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5106 or target_col == 5106). Every well: [[FIBCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIBCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
