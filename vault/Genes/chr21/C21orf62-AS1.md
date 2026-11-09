---
symbol: "C21orf62-AS1"
type: "gene"
col: 13024
ensembl_id: "ENSG00000205930"
name: "EPCIP antisense RNA 1"
location: "21q22.11"
module: 23
arm: "+"
pooled_cpm: 7.63
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 16
n_dd_up_clean: 23
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# C21orf62-AS1

*EPCIP antisense RNA 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +8.0, q 6e-13, up in 23 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.365× (z -7.8, q 2e-12, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.333× (z -7.6, q 4e-12, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02482]] (+0.69, fdr 7e-06), [[FAM227B]] (+0.68, fdr 1e-05), [[CFAP43]] (+0.68, fdr 7e-06); moves opposite to [[SLC25A19]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, none with an alert; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +8.0 | 6e-13 | 23/39 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **2.31×** | +6.5 | 2e-08 | 32/45 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +6.3 | 6e-08 | 27/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.97×** | +5.1 | 6e-05 | 25/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.72×** | +4.8 | 2e-04 | 20/45 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.81×** | +4.7 | 3e-04 | 23/47 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.58×** | +4.6 | 4e-04 | 19/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.78×** | +4.5 | 6e-04 | 20/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.55×** | +4.4 | 8e-04 | 19/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.002 | 23/47 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.69×** | +4.1 | 0.003 | 17/46 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.007 | 18/46 (A-172, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.008 | 19/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +3.7 | 0.009 | 14/45 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.65×** | +3.6 | 0.011 | 17/46 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.365×** | -7.8 | 2e-12 | 29/46 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.367×** | -7.8 | 2e-12 | 28/40 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.333×** | -7.6 | 4e-12 | 32/44 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.382×** | -7.5 | 1e-11 | 28/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.403×** | -7.1 | 2e-10 | 35/46 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.380×** | -6.7 | 2e-09 | 26/44 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.461×** | -5.8 | 6e-07 | 24/33 (COLO 205, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.288×** | -4.9 | 6e-05 | 22/44 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.569×** | -4.4 | 8e-04 | 19/46 (SW480, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.479×** | -4.1 | 0.003 | 19/47 (SNU-1, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.555×** | -4.1 | 0.003 | 21/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.366×** | -4.0 | 0.003 | 19/42 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.007 | 19/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.586×** | -3.7 | 0.008 | 19/45 (SW480, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.658×** | -3.3 | 0.043 | 13/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.444×** | -3.2 | 0.046 | 17/41 (NCI-H1573, HCT15, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0172× (z -16.2) |
| [[SW480 (line)]] | alt | 13.9 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0518× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0900× (z -11.5) |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0779× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 7.00 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0822× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 14.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.80× (z +8.8) ⚠ position not correctable | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 8.57 | 0 | 1 | — | [[Piroxicam (drug)]] 0.05 µM 0.0430× (z -8.5) |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0597× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 27.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.195× (z -9.1) |
| [[LoVo (line)]] | wt | 3.02 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.84× (z +8.5) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 5.60 | 0 | 1 | — | [[Posaconazole (drug)]] 0.05 µM 0.0607× (z -8.8) |
| [[SW 900 (line)]] | alt | 8.03 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0544× (z -9.1) |
| [[A-427 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02482]] | +0.69 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[FAM227B]] | +0.68 | +0.80 / +0.57 | both halves | 1e-05 |  |
| [[CFAP43]] | +0.68 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[APOLD1]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.66 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[KLHDC1]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[DMXL1-DT]] | +0.66 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[LRRIQ3]] | +0.64 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.63 | +0.74 / +0.50 | both halves | 1e-05 | same gene group |
| [[EFCAB6]] | +0.63 | +0.77 / +0.46 | both halves | 2e-05 |  |
| [[EPM2A-DT]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ITFG2-AS1]] | +0.62 | +0.72 / +0.62 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A19]] | -0.51 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises C21orf62-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without FSIP2-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers C21orf62-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[ERICH2-DT]] | B | ERICH2-DT activity raises C21orf62-AS1's level | lines that do not express ERICH2-DT (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without ERICH2-DT | 0.071 | ⚠ within organs, on part of the lines; also absent: ERICH2, GAD1, ENSG00000256673; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises C21orf62-AS1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without FAM66C | 0.081 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[CXCL13]] | B | CXCL13 activity raises C21orf62-AS1's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without CXCL13 | 0.082 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[FBXO15]] | B | FBXO15 activity raises C21orf62-AS1's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without FBXO15 | 0.091 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[TNNI3K]] | C | TNNI3K activity raises C21orf62-AS1's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without TNNI3K | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises C21orf62-AS1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without LRRIQ3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.0, 19.4); signed map (30.3, -8.6). **Vector** length 65.4, 12.0% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | EPCIP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q22.11 — chr21:32,772,100-33,019,751 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C21orf49, C21orf62-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q17RA5](https://www.uniprot.org/uniprotkb/Q17RA5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:1290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1290) · Entrez [54067](https://www.ncbi.nlm.nih.gov/gene/54067) · UniProt [Q17RA5](https://www.uniprot.org/uniprotkb/Q17RA5) · Ensembl [ENSG00000205930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205930)

## Data

Gene col 13024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13024); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13024]; `tensor/DDL_lfc|DDL_z.npy` [13024]; `embed/gene_vectors.npy` [13024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13024 or target_col == 13024). Every well: [[C21orf62-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C21orf62-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
