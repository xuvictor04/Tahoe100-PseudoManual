---
symbol: "DUSP5-DT"
type: "gene"
col: 15765
ensembl_id: "ENSG00000273143"
name: "DUSP5 divergent transcript"
location: "10q25.2"
module: 116
arm: "+"
pooled_cpm: 12.02
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 24
n_dd_up_clean: 15
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# DUSP5-DT

*DUSP5 divergent transcript* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +12.4, q 2e-32, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.597× (z -6.9, q 3e-09, down in 24 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01204]] (+0.68, fdr 7e-06), [[CLCF1]] (+0.68, fdr 7e-06), [[C11orf91]] (+0.67, fdr 7e-06); moves opposite to [[RHOT1]] (-0.62, fdr 1e-05), [[TNRC6A]] (-0.57, fdr 1e-05), [[MLLT10]] (-0.56, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); 9 go from it, the strongest it → [[C11orf91]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +12.4 | 2e-32 | 27/38 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +11.9 | 3e-30 | 24/36 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +9.2 | 4e-18 | 20/26 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +9.1 | 1e-17 | 25/38 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +8.5 | 2e-15 | 22/35 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.9 | 4e-07 | 22/39 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +5.1 | 4e-05 | 11/29 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 3e-04 | 17/41 (A498, NCI-H2347, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.001 | 9/40 (A498, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.008 | 15/41 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.98×** | +3.7 | 0.010 | 9/33 (Panc 03.27, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.015 | 11/35 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.5 | 0.017 | 1/19 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.040 | 10/40 (SW480, CFPAC-1, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.78×** | +3.2 | 0.059 | 8/33 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.081 | 4/41 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.097 | 12/38 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.72×** | +3.0 | 0.098 | 5/36 (A-172, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15765.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.597×** | -6.9 | 3e-09 | 24/39 (SK-MEL-2, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.669×** | -5.9 | 8e-07 | 24/40 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.563×** | -5.6 | 5e-06 | 18/40 (RKO, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.704×** | -5.2 | 3e-05 | 18/41 (RKO, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.662×** | -5.1 | 3e-05 | 21/41 (AsPC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -5.0 | 5e-05 | 18/38 (Hs 766T, J82, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.403×** | -5.0 | 5e-05 | 17/32 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.411×** | -4.9 | 8e-05 | 18/33 (Hs 766T, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.681×** | -4.8 | 9e-05 | 17/40 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.634×** | -4.8 | 1e-04 | 17/40 (AsPC-1, RKO, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.619×** | -4.7 | 1e-04 | 17/38 (AsPC-1, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.636×** | -4.5 | 3e-04 | 16/38 (RKO, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.742×** | -4.4 | 5e-04 | 15/40 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.680×** | -4.3 | 7e-04 | 18/41 (NCI-H23, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.666×** | -4.0 | 0.002 | 18/38 (SW 900, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 6.75 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +12.7) | — |
| [[RKO (line)]] | wt | 123 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.8) |
| [[A-172 (line)]] | wt | 12.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.55× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.0948× (z -9.8) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 6.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +11.1) | — |
| [[C32 (line)]] | wt | 4.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.24× (z +8.6) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 7.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 7.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 6.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 4.41 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0685× (z -9.1) |
| [[SNU-1 (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01204]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CLCF1]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[GRK4]] | +0.65 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[AGO2]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[LINC00513]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ITGA2-AS1]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 | same gene group |
| [[SSUH2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MCL1]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[UBE2R2-AS1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT1]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.57 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MED25]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TADA1]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CROT]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[UBAC1]] | -0.54 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[EHMT2]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CAT]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[DIXDC1]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PPP1R12B]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity raises DUSP5-DT's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 2.42× lower at baseline in the lines without C11orf91 | 0.032 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[ABL1]] | B | ABL1 activity raises DUSP5-DT's level | compounds that target ABL1: 4 of 6 lower it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.5% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FER1L6]] | B | FER1L6 activity raises DUSP5-DT's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without FER1L6 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises DUSP5-DT's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[KIFC3]] | C | KIFC3 activity raises DUSP5-DT's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | DUSP5-DT activity raises C11orf91's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without DUSP5-DT | 0.022 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[NKAIN1]] | B | DUSP5-DT activity lowers NKAIN1's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.46× higher at baseline in the lines without DUSP5-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[KIFC3]] | B | DUSP5-DT activity raises KIFC3's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without DUSP5-DT | 0.047 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[ASB1]] | B | DUSP5-DT activity raises ASB1's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without DUSP5-DT | 0.051 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[CDKN1A]] | B | DUSP5-DT activity raises CDKN1A's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without DUSP5-DT | 0.055 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[RAP1B]] | B | DUSP5-DT activity raises RAP1B's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without DUSP5-DT | 0.055 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[OSMR-DT]] | B | DUSP5-DT activity raises OSMR-DT's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without DUSP5-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[LUCAT1]] | B | DUSP5-DT activity raises LUCAT1's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without DUSP5-DT | 0.087 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[MAMLD1]] | C | DUSP5-DT activity raises MAMLD1's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 4.12× lower at baseline in the lines without DUSP5-DT | 0.054 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, -4.4); signed map (3.1, 32.3). **Vector** length 111, 28.0% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.8 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.8 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | DUSP5 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q25.2 — chr10:110,428,840-110,496,590 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55154) · Entrez [105378481](https://www.ncbi.nlm.nih.gov/gene/105378481) · Ensembl [ENSG00000273143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273143)

## Data

Gene col 15765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15765); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15765]; `tensor/DDL_lfc|DDL_z.npy` [15765]; `embed/gene_vectors.npy` [15765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15765 or target_col == 15765). Every well: [[DUSP5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
