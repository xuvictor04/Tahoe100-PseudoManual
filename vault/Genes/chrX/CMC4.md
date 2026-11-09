---
symbol: "CMC4"
type: "gene"
col: 11317
ensembl_id: "ENSG00000182712"
name: "C-X9-C motif containing 4"
location: "Xq28"
module: 130
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# CMC4

*C-X9-C motif containing 4* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.15× (z +11.4, q 2e-27, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +8.7, q 8e-16, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.538× (z -6.1, q 6e-07, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAPT1]] (+0.69, fdr 7e-06), [[LNX2]] (+0.60, fdr 1e-05), [[ZHX1]] (+0.60, fdr 2e-05); moves opposite to [[NUDC]] (-0.63, fdr 1e-05), [[DFFA]] (-0.59, fdr 1e-05), [[PSMD3]] (-0.54, fdr 1e-04).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +11.4 | 2e-27 | 7/9 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.9 | 1e-20 | 22/26 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +8.7 | 8e-16 | 30/40 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.0 | 3e-10 | 14/18 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.7 | 2e-06 | 21/38 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.9 | 9e-05 | 12/27 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.9 | 9e-05 | 20/41 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.42×** | +3.6 | 0.024 | 10/29 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.031 | 9/30 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.046 | 3/41 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.055 | 9/35 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.538×** | -6.1 | 6e-07 | 20/42 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -4.7 | 8e-04 | 15/45 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.530×** | -3.5 | 0.081 | 9/44 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -3.4 | 0.081 | 11/44 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.539×** | -3.4 | 0.086 | 10/24 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPT1]] | +0.69 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LNX2]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZHX1]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DYRK1A]] | +0.56 | +0.29 / +0.48 | both halves | 2e-04 |  |
| [[UBR5]] | +0.56 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[ACOT2]] | +0.55 | +0.37 / +0.54 | both halves | 9e-05 | pathway: Protein localization |
| [[FBXL3]] | +0.54 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[FAM76B]] | +0.53 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[FMC1]] | +0.53 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[ATP23]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ADAL]] | +0.53 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NFYB]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDC]] | -0.63 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DFFA]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PSMD3]] | -0.54 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[DAP3]] | -0.51 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[HSP90AA1]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[HERC2P9]] | -0.51 | -0.60 / -0.37 | both halves | 9e-05 |  |
| [[FERMT3]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CLPB]] | -0.50 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RRP7BP]] | -0.50 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[PLCXD2]] | -0.49 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[HERC2P2]] | -0.49 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[STIP1]] | -0.49 | -0.30 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CMC4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers CMC4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LHFPL6]] | B | LHFPL6 activity raises CMC4's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without LHFPL6 | 0.079 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CMC4's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | CMC4's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.72 | 0.250 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | CMC4's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | CMC4's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.467 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CMC4's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CMC4's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.483 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | CMC4's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | CMC4's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.493 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.8, -26.7); signed map (13.5, -14.0). **Vector** length 45.6, 5.67% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +9.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.9 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -1.7 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | C-X9-C motif containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:155,061,622-155,071,136 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P8MTCP1, p8; previously MTCP1NB |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

UniProt [P56277](https://www.uniprot.org/uniprotkb/P56277) carries no function annotation.

**Summary**, from NCBI Gene [100272147](https://www.ncbi.nlm.nih.gov/gene/100272147):

> This gene was identified by involvement in some t(X;14) translocations associated with mature T-cell proliferations. This region has a complex gene structure, with a common promoter and 5' exon spliced to two different sets of 3' exons that encode two different proteins. This gene represents the downstream 8 kDa protein that localizes to mitochondria.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:35428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35428) · Entrez [100272147](https://www.ncbi.nlm.nih.gov/gene/100272147) · UniProt [P56277](https://www.uniprot.org/uniprotkb/P56277) · Ensembl [ENSG00000182712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182712)

## Data

Gene col 11317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11317); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11317]; `tensor/DDL_lfc|DDL_z.npy` [11317]; `embed/gene_vectors.npy` [11317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11317 or target_col == 11317). Every well: [[CMC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
