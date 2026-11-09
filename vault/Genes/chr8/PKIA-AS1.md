---
symbol: "PKIA-AS1"
type: "gene"
col: 14864
ensembl_id: "ENSG00000254266"
name: "PKIA antisense RNA 1"
location: "8q21.13"
module: 166
arm: "+"
pooled_cpm: 8.59
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# PKIA-AS1

*PKIA antisense RNA 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.28× (z +14.4, q 3e-44, up in 25 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.456× (z -9.7, q 3e-19, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL7]] (+0.60, fdr 1e-05), [[ST8SIA1]] (+0.60, fdr 3e-05), [[DCC]] (+0.59, fdr 3e-05); moves opposite to [[TRAK2]] (-0.42, fdr 2e-04), [[PTPN21]] (-0.41, fdr 3e-04), [[ENTPD5]] (-0.41, fdr 0.005, ⚠ not reproduced), [[ACSF3]] (-0.40, fdr 6e-04).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CASC20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +14.4 | 3e-44 | 25/40 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.6 | 8e-12 | 23/44 (SW1417, C-33 A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.7 | 2e-06 | 18/42 (SW1417, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +5.0 | 6e-05 | 17/40 (HOP62, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 7e-05 | 15/43 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.063 | 5/42 (SW 900, LoVo, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.063 | 4/43 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.21×** | +3.3 | 0.063 | 9/44 (LOX-IMVI, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.063 | 7/36 (HS-578T, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.12 | 11/43 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.28× | +3.0 | 0.12 | 1/44 (RPMI-7951) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.456×** | -9.7 | 3e-19 | 30/43 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.490×** | -8.8 | 5e-16 | 22/44 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.661×** | -7.2 | 1e-10 | 22/39 (LoVo, C32, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.560×** | -7.1 | 2e-10 | 23/43 (SHP-77, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -6.8 | 1e-09 | 21/38 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -6.2 | 5e-08 | 18/29 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -5.6 | 1e-06 | 16/43 (C32, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -5.2 | 1e-05 | 16/39 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.644×** | -5.2 | 1e-05 | 19/42 (NCI-H1573, A498, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.742×** | -5.2 | 1e-05 | 16/44 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.662×** | -5.1 | 2e-05 | 14/43 (RKO, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.661×** | -4.9 | 5e-05 | 12/43 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.673×** | -4.7 | 1e-04 | 12/42 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.703×** | -4.3 | 6e-04 | 12/43 (H4, RKO, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -3.9 | 0.003 | 15/38 (SK-MEL-2, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.732×** | -3.8 | 0.005 | 11/43 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.019 | 13/42 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.678×** | -3.4 | 0.021 | 7/39 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.025 | 8/43 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.039 | 12/39 (SW 900, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.764×** | -3.0 | 0.055 | 5/35 (A-172, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 91.5 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -12.5) |
| [[C32 (line)]] | wt | 24.9 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0579× (z -13.9) |
| [[LoVo (line)]] | wt | 12.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0904× (z -11.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -9.5) |
| [[RKO (line)]] | wt | 22.0 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.135× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 5.99 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0730× (z -9.6) |
| [[A498 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.4) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A549 (line)]] | wt | 2.54 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0388× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 6.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[J82 (line)]] | alt | 5.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.243× (z -8.7) ⚠ cell-cycle shift, explains ~96% of this change |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.8) |
| [[A-427 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL7]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[ST8SIA1]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[DCC]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SORCS1]] | +0.53 | +0.32 / +0.58 | both halves | 1e-04 |  |
| [[COL25A1]] | +0.52 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[OBI1-AS1]] | +0.51 | +0.27 / +0.58 | both halves | 3e-04 | same gene group |
| [[CLVS1]] | +0.51 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[ANKRD7]] | +0.51 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[LINC01524]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[GRID2]] | +0.50 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[LINC02055]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[PARP8]] | +0.49 | +0.35 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK2]] | -0.42 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PTPN21]] | -0.41 | -0.26 / -0.51 | both halves | 3e-04 |  |
| [[ENTPD5]] | -0.41 | -0.05 / -0.49 | ⚠ not reproduced | 0.005 |  |
| [[ACSF3]] | -0.40 | -0.22 / -0.39 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises PKIA-AS1's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without CASC20 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[ADGRG7]] | B | ADGRG7 activity raises PKIA-AS1's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 2.38× lower at baseline in the lines without ADGRG7 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[STAT4]] | B | STAT4 activity raises PKIA-AS1's level | lines that do not express STAT4 (7) vs lines expressing it (43) | 2.34× lower at baseline in the lines without STAT4 | 0.067 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent |
| [[RMEL3]] | B | RMEL3 activity raises PKIA-AS1's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without RMEL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[LINC02360]] | B | LINC02360 activity raises PKIA-AS1's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 1.67× lower at baseline in the lines without LINC02360 | 0.082 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1 |
| [[LINC00276]] | C | LINC00276's natural level strengthens PKIA-AS1's drug response | LINC00276's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.73, reverse -0.17; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.1, 28.1); signed map (32.2, 15.5). **Vector** length 62.6, 9.23% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +14.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.3 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | -0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -9.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.7 | -3.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.6 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.7 | -5.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | PKIA antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q21.13 — chr8:78,268,637-78,558,503 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51659) · Entrez [101927003](https://www.ncbi.nlm.nih.gov/gene/101927003) · Ensembl [ENSG00000254266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254266)

## Data

Gene col 14864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14864); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14864]; `tensor/DDL_lfc|DDL_z.npy` [14864]; `embed/gene_vectors.npy` [14864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14864 or target_col == 14864). Every well: [[PKIA-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKIA-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
