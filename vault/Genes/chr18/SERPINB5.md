---
symbol: "SERPINB5"
type: "gene"
col: 13032
ensembl_id: "ENSG00000206075"
name: "serpin family B member 5"
location: "18q21.33"
module: 73
arm: "+"
pooled_cpm: 31.76
n_lines_expressing: 16
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 69
direction_downstream: 118
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SERPINB5

*serpin family B member 5* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +12.3, q 5e-32, up in 3 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.72× (z +5.6, q 3e-06, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.481× (z -7.9, q 1e-12, down in 11 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSG3]] (+0.78, fdr 7e-06), [[ANO1]] (+0.77, fdr 7e-06), [[KLK10]] (+0.77, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 69 arrows point to it, the strongest [[LYPD3]] → it (grade B ⚠); 118 go from it, the strongest it → [[IL22RA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +12.3 | 5e-32 | 3/14 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +8.4 | 2e-14 | 6/13 (AsPC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +8.2 | 3e-14 | 4/12 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +7.1 | 2e-10 | 7/14 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +5.6 | 3e-06 | 7/14 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 6e-04 | 8/14 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 6/14 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 3/14 (NCI-H460, LS 180, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.24×** | +4.0 | 0.004 | 11/14 (LS 180, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +3.8 | 0.008 | 1/14 (NCI-H460) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.6 | 0.014 | 3/8 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.018 | 5/14 (NCI-H460, SW48, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.56×** | +3.4 | 0.026 | 1/14 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.048 | 2/14 (HT-29, NCI-H1573) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.059 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -7.9 | 1e-12 | 11/14 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.627×** | -7.0 | 7e-10 | 7/14 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.533×** | -6.6 | 1e-08 | 13/14 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.544×** | -6.1 | 1e-07 | 7/14 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -4.8 | 2e-04 | 13/14 (LoVo, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -4.7 | 3e-04 | 10/14 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.649×** | -4.0 | 0.004 | 6/14 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.695×** | -3.7 | 0.017 | 0/14 | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.715×** | -3.6 | 0.017 | 0/14 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.734×** | -3.4 | 0.040 | 0/14 | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.734×** | -3.4 | 0.040 | 9/14 (LoVo, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.048 | 7/14 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.740×** | -3.3 | 0.048 | 9/14 (Hs 766T, SW48, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | **0.745×** | -3.2 | 0.057 | 0/14 | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -3.0 | 0.091 | 1/14 (Hs 766T) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.761×** | -3.0 | 0.099 | 6/14 (CFPAC-1, KATO III, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 321 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0341× (z -33.1) |
| [[Hs 766T (line)]] | wt | 145 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -24.3) |
| [[NCI-H460 (line)]] | wt | 25.5 | 2 (2 ⚠) | 5 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 3.88× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.9) |
| [[LS 180 (line)]] | wt | 162 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.6) |
| [[KATO III (line)]] | alt | 78.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0851× (z -20.9) |
| [[AsPC-1 (line)]] | alt | 47.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.2) |
| [[SW1417 (line)]] | alt | 92.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.1) |
| [[SW48 (line)]] | wt | 145 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 74.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 74.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.5) |
| [[COLO 205 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -9.5) |
| [[HT-29 (line)]] | alt | 9.18 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.64× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.2) |
| [[A-172 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG3]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 | STRING 539 |
| [[ANO1]] | +0.77 | +0.73 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[KLK10]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 | STRING 501 |
| [[HS3ST1]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FERMT1]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 | STRING 478 |
| [[PRSS3]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LINC02582]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KLK11]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[PKP1]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 | STRING 560 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 7, C 62. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD3]] | B | LYPD3 activity raises SERPINB5's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 4.02× lower at baseline in the lines without LYPD3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[LANCL3]] | B | LANCL3 activity raises SERPINB5's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 2.71× lower at baseline in the lines without LANCL3 | 0.025 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[EFNB2]] | B | EFNB2 activity raises SERPINB5's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 3.10× lower at baseline in the lines without EFNB2 | 0.057 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[TGFA]] | B | TGFA activity raises SERPINB5's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.30× lower at baseline in the lines without TGFA | 0.060 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[STON2]] | B | STON2 activity raises SERPINB5's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without STON2 | 0.064 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[SH3TC2-DT]] | B | SH3TC2-DT activity raises SERPINB5's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without SH3TC2-DT | 0.086 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[IGSF9]] | B | IGSF9 activity raises SERPINB5's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.90× lower at baseline in the lines without IGSF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[FGFBP1]] | C | FGFBP1 activity raises SERPINB5's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 13.04× lower at baseline in the lines without FGFBP1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises SERPINB5's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 7.85× lower at baseline in the lines without PKP1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises SERPINB5's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 12.56× lower at baseline in the lines without COL17A1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises SERPINB5's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 12.10× lower at baseline in the lines without KLK10 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises SERPINB5's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 16.95× lower at baseline in the lines without TFF2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |

### Downstream of this gene

*118 arrows, 118 of them with an alert ⚠; grade A 0, B 52, C 66. Shown: the 12 strongest; 106 more arrows (106 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL22RA1]] | B | SERPINB5 activity raises IL22RA1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without SERPINB5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[CD55]] | B | SERPINB5 activity raises CD55's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 4.68× lower at baseline in the lines without SERPINB5 | 8e-04 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[ITGA6]] | B | SERPINB5 activity raises ITGA6's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.76× lower at baseline in the lines without SERPINB5 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[EPS8L1]] | B | SERPINB5 activity raises EPS8L1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 4.08× lower at baseline in the lines without SERPINB5 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[YOD1]] | B | SERPINB5 activity raises YOD1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.40× lower at baseline in the lines without SERPINB5 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[OXSR1]] | B | SERPINB5 activity strengthens OXSR1's drug response | lines that do not express SERPINB5 (34) vs lines expressing it (15) | the lines without SERPINB5 respond 0.69× as strongly (z diff +1.76); strongest at Homoharringtonine 5 µM: 0.88x vs 0.48x (z diff +7.0) | 0.003 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; target measured in part of the lines; artifact flags |
| [[DENND2C]] | B | SERPINB5 activity weakens DENND2C's drug response | lines that do not express SERPINB5 (27) vs lines expressing it (12) | the lines without SERPINB5 respond 3.16× as strongly (z diff -3.84); strongest at Idarubicin (hydrochloride) 5 µM: 1.82x vs 0.54x (z diff -8.8) | 0.004 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; target measured in part of the lines; artifact flags |
| [[LYPD3]] | B | SERPINB5 activity raises LYPD3's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without SERPINB5 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[OXSR1]] | B | SERPINB5 activity raises OXSR1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 1.54× lower at baseline in the lines without SERPINB5 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[IGSF9]] | B | SERPINB5 activity raises IGSF9's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without SERPINB5 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[ARHGAP27]] | B | SERPINB5 activity raises ARHGAP27's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.73× lower at baseline in the lines without SERPINB5 | 0.007 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[ITPK1]] | B | SERPINB5 activity raises ITPK1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without SERPINB5 | 0.007 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.3, 53.3); signed map (2.1, 38.8). **Vector** length 85.2, 38.2% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.6 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,476,958-63,505,085 (+) |
| Ensembl biotype | protein_coding |
| Also known as | maspin; previously PI5 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [P36952](https://www.uniprot.org/uniprotkb/P36952) (Serpin B5):

> Tumor suppressor. It blocks the growth, invasion, and metastatic properties of mammary tumors. As it does not undergo the S (stressed) to R (relaxed) conformational transition characteristic of active serpins, it exhibits no serine protease inhibitory activity.

**Summary**, from NCBI Gene [5268](https://www.ncbi.nlm.nih.gov/gene/5268):

> Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to act upstream of or within several processes, including extracellular matrix organization; prostate gland morphogenesis; and regulation of epithelial cell proliferation. Located in cytoplasm. Biomarker of hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8949) · Entrez [5268](https://www.ncbi.nlm.nih.gov/gene/5268) · UniProt [P36952](https://www.uniprot.org/uniprotkb/P36952) · Ensembl [ENSG00000206075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206075)

## Data

Gene col 13032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13032); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13032]; `tensor/DDL_lfc|DDL_z.npy` [13032]; `embed/gene_vectors.npy` [13032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13032 or target_col == 13032). Every well: [[SERPINB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
