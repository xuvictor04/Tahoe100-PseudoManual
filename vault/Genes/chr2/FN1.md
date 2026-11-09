---
symbol: "FN1"
type: "gene"
col: 3670
ensembl_id: "ENSG00000115414"
name: "fibronectin 1"
location: "2q35"
module: 104
arm: "+"
pooled_cpm: 1005.32
n_lines_expressing: 21
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 25
direction_downstream: 26
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# FN1

*fibronectin 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.84× (z +16.3, q 0e+00, up in 14 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +6.3, q 5e-08, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.467× (z -13.1, q 2e-36, down in 19 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A2]] (+0.67, fdr 7e-06), [[SRPX]] (+0.66, fdr 7e-06), [[COL4A1]] (+0.62, fdr 7e-06); moves opposite to [[SLAMF7]] (-0.53, fdr 3e-05), [[ANKRD30B]] (-0.50, fdr 4e-05), [[PATJ]] (-0.48, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[PLXNA2]] → it (grade B ⚠); 26 go from it, the strongest it → [[COL13A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.84×** | +16.3 | 0e+00 | 14/20 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +13.6 | 1e-39 | 14/18 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +9.1 | 1e-17 | 9/18 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.3 | 5e-08 | 8/19 (Panc 03.27, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.003 | 2/21 (LOX-IMVI, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.005 | 5/20 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.005 | 0/19 | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.008 | 12/19 (A-172, J82, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.008 | 9/19 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.043 | 12/19 (Panc 03.27, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.467×** | -13.1 | 2e-36 | 19/19 (HepG2/C3A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.366×** | -12.2 | 7e-32 | 19/19 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -6.3 | 7e-08 | 15/19 (HepG2/C3A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.736×** | -5.3 | 2e-05 | 14/19 (A-172, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.724×** | -3.9 | 0.008 | 15/19 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.724×** | -3.9 | 0.008 | 12/19 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.011 | 14/19 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.733×** | -3.8 | 0.011 | 4/18 (SW 900, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.744×** | -3.6 | 0.020 | 13/19 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.729×** | -3.6 | 0.021 | 2/19 (SK-MEL-2, A-172) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.753×** | -3.4 | 0.029 | 14/19 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -3.4 | 0.031 | 9/19 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.765×** | -3.3 | 0.049 | 12/19 (C32, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.051 | 18/19 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.051 | 12/19 (SK-MEL-2, J82, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.057 | 0/19 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.057 | 7/19 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.770×** | -3.0 | 0.082 | 1/19 (LOX-IMVI) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 448 | 17 | 2 | [[Dexamethasone (drug)]] 0.5 µM 6.97× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 2,149 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.2) |
| [[C32 (line)]] | wt | 6,872 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 3,372 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -25.8) |
| [[Hs 766T (line)]] | wt | 442 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.8) |
| [[A-172 (line)]] | wt | 343 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.7) |
| [[J82 (line)]] | alt | 1,581 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 2,747 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -17.7) |
| [[H4 (line)]] | wt | 807 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -19.0) |
| [[HOP62 (line)]] | alt | 2,961 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 1,183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 436 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 4,692 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -15.1) |
| [[SNU-423 (line)]] | alt | 1,796 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.2) |
| [[SW 900 (line)]] | alt | 2,280 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -18.4) |
| [[NCI-H2347 (line)]] | alt | 2,519 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.2) |
| [[SW 1088 (line)]] | alt | 1,871 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -11.2) |
| [[A-427 (line)]] | wt | 51.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 217 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 185 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 216 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 66.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 65.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 83.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 74.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 145 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 63.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 70.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 68.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6,689 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 88.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4,708 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 57.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 57.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 60.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 63.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 966 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1,217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 50.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 65.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 118 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 74.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 120 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 80.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 87.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 104 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A2]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 750 |
| [[SRPX]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[COL4A1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 849 |
| [[SDC2]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 | pathway: Cell surface interactions at the vascular wall; STRING 959 |
| [[LOXL3]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 | pathway: Elastic fibre formation; STRING 538 |
| [[PLAT]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 867 |
| [[ITGA8]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 | pathway: ECM proteoglycans; STRING 976 |
| [[DAAM2]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ANPEP]] | +0.58 | +0.57 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 448 |
| [[COL6A3]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 736 |
| [[TGFBI]] | +0.58 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 995 |
| [[AEBP1]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAMF7]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD30B]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[PATJ]] | -0.48 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[KCP]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[EPB41]] | -0.43 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[CPEB1]] | -0.43 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[FUT2]] | -0.43 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[RBCK1]] | -0.43 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[HMOX1]] | -0.43 | -0.46 / -0.32 | both halves | 1e-04 | pathway: Interleukin-4 and Interleukin-13 signaling; STRING 479 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 2, C 23. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | PLXNA2 activity raises FN1's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 3.71× lower at baseline in the lines without PLXNA2 | 0.025 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[FUT2]] | B | FUT2 activity raises FN1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 3.09× lower at baseline in the lines without FUT2 | 0.094 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[IGFBP7]] | C | IGFBP7 activity raises FN1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 12.27× lower at baseline in the lines without IGFBP7 | 0.001 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[PLAT]] | C | PLAT activity raises FN1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 8.61× lower at baseline in the lines without PLAT | 0.003 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises FN1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 8.31× lower at baseline in the lines without PDGFRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[LOX]] | C | LOX activity raises FN1's level | lines that do not express LOX (31) vs lines expressing it (19) | 9.24× lower at baseline in the lines without LOX | 0.007 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[DAAM2]] | C | DAAM2 activity raises FN1's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 7.43× lower at baseline in the lines without DAAM2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[ANKRD30B]] | C | ANKRD30B activity raises FN1's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 8.59× lower at baseline in the lines without ANKRD30B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises FN1's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 8.45× lower at baseline in the lines without C10orf90 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[COL8A1]] | C | COL8A1 activity raises FN1's level | lines that do not express COL8A1 (31) vs lines expressing it (19) | 7.46× lower at baseline in the lines without COL8A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: IL6, LINC01411, NCAM1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises FN1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 6.52× lower at baseline in the lines without FBN1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises FN1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 8.82× lower at baseline in the lines without AEBP1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 7, C 19. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | FN1 activity raises COL13A1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 3.74× lower at baseline in the lines without FN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[PLXNA2]] | B | FN1 activity raises PLXNA2's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without FN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[RBMS1]] | B | FN1 activity raises RBMS1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.46× lower at baseline in the lines without FN1 | 0.034 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[ITGA5]] | B | FN1 activity raises ITGA5's level | lines that do not express FN1 (29) vs lines expressing it (21) | 3.76× lower at baseline in the lines without FN1 | 0.042 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[LTBP1]] | B | FN1 activity raises LTBP1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.43× lower at baseline in the lines without FN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[LTBP3]] | B | FN1 activity raises LTBP3's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without FN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[FUT2]] | B | FN1 activity raises FUT2's level | lines that do not express FN1 (29) vs lines expressing it (21) | 1.00× lower at baseline in the lines without FN1 | 0.080 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[SRPX2]] | C | FN1 activity raises SRPX2's level | lines that do not express FN1 (29) vs lines expressing it (21) | 4.27× lower at baseline in the lines without FN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[PLAT]] | C | FN1 activity raises PLAT's level | lines that do not express FN1 (29) vs lines expressing it (21) | 4.59× lower at baseline in the lines without FN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[COL8A1]] | C | FN1 activity raises COL8A1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 4.96× lower at baseline in the lines without FN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[SRPX]] | C | FN1 activity raises SRPX's level | lines that do not express FN1 (29) vs lines expressing it (21) | 5.29× lower at baseline in the lines without FN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[LOX]] | C | FN1 activity raises LOX's level | lines that do not express FN1 (29) vs lines expressing it (21) | 9.30× lower at baseline in the lines without FN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.1, 23.4); signed map (25.0, 40.3). **Vector** length 99.5, 41.1% of its response variance represented; |z| ≥ 3 in 631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +16.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +4.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.3 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -12.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.8 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:215,360,440-215,436,073 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MSF, CIG, LETS, GFND2, FINC, lnc-ABCA12-8 |
| Gene groups (HGNC) | Receptor ligands; Fibronectin type III domain containing |
| Hallmark sets | COAGULATION, COMPLEMENT, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 60 pathways, smallest: ALK mutants bind TKIs; GRB2:SOS provides linkage to MAPK signaling for Integrins; p130Cas linkage to MAPK signaling for integrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P02751](https://www.uniprot.org/uniprotkb/P02751) (Fibronectin):

> Fibronectins bind cell surfaces and various compounds including collagen, fibrin, heparin, DNA, and actin. Fibronectins are involved in cell adhesion, cell motility, opsonization, wound healing, and maintenance of cell shape. Involved in osteoblast compaction through the fibronectin fibrillogenesis cell-mediated matrix assembly process, essential for osteoblast mineralization (By similarity). Participates in the regulation of type I collagen deposition by osteoblasts (By similarity). Acts as a …

**Summary**, from NCBI Gene [2335](https://www.ncbi.nlm.nih.gov/gene/2335):

> This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense, and metastasis. The gene has three regions subject to alternative splicing, with the potential to …

**Accessions** — [HGNC:3778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3778) · Entrez [2335](https://www.ncbi.nlm.nih.gov/gene/2335) · UniProt [P02751](https://www.uniprot.org/uniprotkb/P02751) · Ensembl [ENSG00000115414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115414)

## Data

Gene col 3670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3670); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3670]; `tensor/DDL_lfc|DDL_z.npy` [3670]; `embed/gene_vectors.npy` [3670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3670 or target_col == 3670). Every well: [[FN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
