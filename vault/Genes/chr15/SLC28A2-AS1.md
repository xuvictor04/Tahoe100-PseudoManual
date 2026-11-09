---
symbol: "SLC28A2-AS1"
type: "gene"
col: 15207
ensembl_id: "ENSG00000259520"
name: "SLC28A2 antisense RNA 1"
location: "15q21.1"
module: 15
arm: "+"
pooled_cpm: 3.29
n_lines_expressing: 41
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SLC28A2-AS1

*SLC28A2 antisense RNA 1* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.18× (z +12.3, q 7e-32, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.319× (z -9.8, q 7e-20, down in 30 of 38 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.545× (z -5.2, q 2e-05, down in 17 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTG1P17]] (+0.62, fdr 7e-06), [[FRG1HP]] (+0.60, fdr 1e-05), [[TAGAP-AS1]] (+0.60, fdr 7e-06); moves opposite to [[NASP]] (-0.50, fdr 4e-05), [[MECOM]] (-0.48, fdr 4e-05), [[MEIS2]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF559-ZNF177]] → it (grade B ⚠); 5 go from it, the strongest it → [[ADAM20]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.18×** | +12.3 | 7e-32 | 35/38 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.79×** | +11.1 | 2e-26 | 31/35 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +9.0 | 5e-17 | 25/35 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +8.6 | 2e-15 | 16/30 (NCI-H23, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +6.0 | 3e-07 | 7/16 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +5.4 | 8e-06 | 11/34 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.85×** | +5.3 | 1e-05 | 17/38 (COLO 205, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +4.8 | 9e-05 | 15/38 (RKO, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +3.9 | 0.006 | 7/34 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.012 | 7/36 (SW480, SHP-77, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.012 | 7/37 (A498, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.5 | 0.022 | 13/37 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.032 | 5/33 (NCI-H1792, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.034 | 3/37 (H4, HOP62, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.05×** | +3.2 | 0.046 | 4/24 (SHP-77, A498, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.079 | 5/28 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.319×** | -9.8 | 7e-20 | 30/38 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.425×** | -7.3 | 7e-11 | 16/24 (SW480, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.445×** | -6.9 | 8e-10 | 21/37 (RKO, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.427×** | -6.0 | 2e-07 | 18/35 (HOP62, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -5.2 | 2e-05 | 17/36 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.541×** | -5.1 | 4e-05 | 14/22 (SW480, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.543×** | -5.0 | 4e-05 | 18/37 (NCI-H2030, A-427, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.571×** | -4.0 | 0.005 | 13/34 (NCI-H23, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.652×** | -3.5 | 0.026 | 9/36 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.664×** | -3.5 | 0.026 | 8/35 (SW1417, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -3.3 | 0.044 | 10/34 (hTERT-HPNE, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -3.3 | 0.044 | 10/29 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.498×** | -3.1 | 0.079 | 13/33 (HOP62, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.07 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0521× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 4.24 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.0441× (z -10.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW480 (line)]] | alt | 3.77 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 3.59 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 15.1× (z +9.9) | — |
| [[A549 (line)]] | wt | 2.94 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 2.65 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.942 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTG1P17]] | +0.62 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[FRG1HP]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[TAGAP-AS1]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 | same gene group |
| [[TMEM30A-DT]] | +0.57 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[C1orf50]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[FAM228B]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[FAM149B1]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ZNF559-ZNF177]] | +0.55 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RENO1]] | +0.54 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[ZNF333]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[LINC02987]] | +0.53 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.53 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NASP]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MECOM]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MEIS2]] | -0.47 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[SLC12A2]] | -0.47 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[OPHN1]] | -0.46 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[INPP4B]] | -0.46 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[CHST11]] | -0.45 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[NQO1]] | -0.45 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[SYNE2]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[CHD4]] | -0.45 | -0.26 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF559-ZNF177]] | B | ZNF559-ZNF177 activity raises SLC28A2-AS1's level | lines that do not express ZNF559-ZNF177 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without ZNF559-ZNF177 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZNF177, ZNF559, GUCY1A2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM20]] | B | SLC28A2-AS1 activity raises ADAM20's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without SLC28A2-AS1 | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C1orf50]] | B | SLC28A2-AS1 activity raises C1orf50's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.22× lower at baseline in the lines without SLC28A2-AS1 | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[THAP6]] | B | SLC28A2-AS1 activity raises THAP6's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without SLC28A2-AS1 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BRI3]] | B | SLC28A2-AS1 activity lowers BRI3's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.35× higher at baseline in the lines without SLC28A2-AS1 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADAM20P1]] | B | SLC28A2-AS1 activity raises ADAM20P1's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without SLC28A2-AS1 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.5, 24.7); signed map (32.3, -6.2). **Vector** length 45.4, 6.44% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +3.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +4.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -6.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.7 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.4 | -5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -0.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SLC28A2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q21.1 — chr15:45,235,930-45,279,251 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC051619.4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55417) · Entrez [101928414](https://www.ncbi.nlm.nih.gov/gene/101928414) · Ensembl [ENSG00000259520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259520)

## Data

Gene col 15207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15207); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15207]; `tensor/DDL_lfc|DDL_z.npy` [15207]; `embed/gene_vectors.npy` [15207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15207 or target_col == 15207). Every well: [[SLC28A2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC28A2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
