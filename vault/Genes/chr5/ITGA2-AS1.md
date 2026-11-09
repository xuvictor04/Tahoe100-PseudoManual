---
symbol: "ITGA2-AS1"
type: "gene"
col: 14650
ensembl_id: "ENSG00000249899"
name: "ITGA2 antisense RNA 1"
location: "5q11.2"
module: 101
arm: "+"
pooled_cpm: 4.57
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# ITGA2-AS1

*ITGA2 antisense RNA 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 3.41× (z +16.3, q 0e+00, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.468× (z -7.1, q 5e-10, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCG20]] (+0.69, fdr 2e-05), [[ITGB1-DT]] (+0.69, fdr 7e-06), [[NOP14-AS1]] (+0.68, fdr 1e-05); moves opposite to [[IFT172]] (-0.59, fdr 1e-05), [[CAPN7]] (-0.57, fdr 4e-05), [[HAUS4]] (-0.56, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ITGA2]] → it (grade B ⚠); 10 go from it, the strongest it → [[ITGA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.41×** | +16.3 | 0e+00 | 34/43 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +14.6 | 0e+00 | 32/35 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.7 | 2e-12 | 2/7 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +7.4 | 1e-11 | 19/30 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.9 | 6e-10 | 8/21 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +5.9 | 4e-07 | 2/9 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +5.8 | 6e-07 | 23/41 (CFPAC-1, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.4 | 6e-06 | 16/33 (HepG2/C3A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **2.40×** | +4.3 | 0.001 | 6/23 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.003 | 12/40 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.9 | 0.005 | 8/23 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.007 | 17/40 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.8 | 0.007 | 3/10 (HepG2/C3A, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.010 | 4/38 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.015 | 14/40 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.026 | 10/32 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -7.1 | 5e-10 | 25/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.613×** | -5.0 | 1e-04 | 16/42 (AsPC-1, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.665×** | -4.8 | 4e-04 | 20/39 (HepG2/C3A, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.708×** | -4.6 | 6e-04 | 14/40 (AsPC-1, SW 900, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.622×** | -4.5 | 9e-04 | 18/42 (NCI-H23, SW 900, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.629×** | -4.4 | 0.001 | 19/40 (Hs 766T, SK-MEL-2, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.684×** | -4.3 | 0.001 | 14/42 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.724×** | -4.2 | 0.002 | 16/41 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.677×** | -4.0 | 0.003 | 18/39 (SW48, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.737×** | -4.0 | 0.004 | 9/41 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.656×** | -4.0 | 0.004 | 18/29 (PANC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.662×** | -3.9 | 0.005 | 14/41 (NCI-H1792, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -3.8 | 0.006 | 14/39 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.006 | 14/39 (HepG2/C3A, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.649×** | -3.8 | 0.006 | 13/42 (SW 900, SW48, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -3.6 | 0.012 | 10/41 (C32, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.47 | 2 | 1 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 11.7× (z +12.3) | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0579× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0348× (z -14.5) |
| [[PANC-1 (line)]] | alt | 11.9 | 1 | 2 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.37× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 26.4 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 9.16× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.24 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.66× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 7.96 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0483× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 6.09 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 6.83× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 2.79 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 18.7× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 14.9× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.51× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 8.38× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 5.36 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 6.33× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 6.62 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 5.90× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 8.43 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 5.81× (z +9.2) | — |
| [[A-172 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG20]] | +0.69 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[ITGB1-DT]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 | same gene group |
| [[ANTXR2]] | +0.68 | +0.57 / +0.76 | both halves | 9e-06 |  |
| [[ITGA2]] | +0.66 | +0.62 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[BCL10-AS1]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 | same gene group |
| [[LINC01829]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[UBE2R2-AS1]] | +0.65 | +0.44 / +0.67 | both halves | 3e-05 | same gene group |
| [[ERRFI1-DT]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PNP]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[C6orf141]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GSK3B-DT]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DUSP5-DT]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CAPN7]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[HAUS4]] | -0.56 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[UFSP2]] | -0.55 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[USP2]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[THRA]] | -0.55 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[PPP1R12B]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[EHMT2]] | -0.53 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | B | ITGA2 activity raises ITGA2-AS1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without ITGA2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[TOP2A]] | B | TOP2A activity lowers ITGA2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LUCAT1]] | B | LUCAT1 activity raises ITGA2-AS1's level | lines that do not express LUCAT1 (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without LUCAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: TBILA, C3orf52, SPAG16 |
| [[C11orf91]] | B | C11orf91 activity raises ITGA2-AS1's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without C11orf91 | 0.062 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises ITGA2-AS1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without ITGB1-DT | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ITGA2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NABP1]] | C | NABP1 activity raises ITGA2-AS1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; co-absent with the target; its own permutation p |
| [[KBTBD8]] | C | KBTBD8 activity raises ITGA2-AS1's level | lines that do not express KBTBD8 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without KBTBD8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000289986; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | C | ITGA2-AS1 activity raises ITGA2's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 11.00× lower at baseline in the lines without ITGA2-AS1 | 0.002 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[C11orf91]] | C | ITGA2-AS1 activity raises C11orf91's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 3.47× lower at baseline in the lines without ITGA2-AS1 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[UBASH3B]] | C | ITGA2-AS1 activity raises UBASH3B's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 5.44× lower at baseline in the lines without ITGA2-AS1 | 0.019 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[NABP1]] | C | ITGA2-AS1 activity raises NABP1's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 3.76× lower at baseline in the lines without ITGA2-AS1 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent; co-absent with the target |
| [[MIR31HG]] | C | ITGA2-AS1 activity raises MIR31HG's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 4.92× lower at baseline in the lines without ITGA2-AS1 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[PDK1-AS1]] | C | ITGA2-AS1 activity raises PDK1-AS1's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without ITGA2-AS1 | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[S100A11]] | C | ITGA2-AS1 activity raises S100A11's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without ITGA2-AS1 | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[OSMR-DT]] | C | ITGA2-AS1 activity raises OSMR-DT's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without ITGA2-AS1 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[MAZ]] | C | ITGA2-AS1 activity lowers MAZ's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without ITGA2-AS1 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |
| [[PDLIM1]] | C | ITGA2-AS1 activity raises PDLIM1's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 3.04× lower at baseline in the lines without ITGA2-AS1 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, -4.0); signed map (3.4, 31.6). **Vector** length 82.8, 16.0% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +14.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.1 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +4.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.6 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ITGA2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q11.2 — chr5:52,930,606-52,990,278 (-) |
| Ensembl biotype | lncRNA |
| Also known as | I2ALR |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40306) · Entrez [121232372](https://www.ncbi.nlm.nih.gov/gene/121232372) · Ensembl [ENSG00000249899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249899)

## Data

Gene col 14650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14650); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14650]; `tensor/DDL_lfc|DDL_z.npy` [14650]; `embed/gene_vectors.npy` [14650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14650 or target_col == 14650). Every well: [[ITGA2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
