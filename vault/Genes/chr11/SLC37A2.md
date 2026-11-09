---
symbol: "SLC37A2"
type: "gene"
col: 5629
ensembl_id: "ENSG00000134955"
name: "solute carrier family 37 member 2"
location: "11q24.2"
module: 92
arm: "+"
pooled_cpm: 3.65
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SLC37A2

*solute carrier family 37 member 2* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +15.5, q 0e+00, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.590× (z -5.5, q 2e-05, down in 10 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRL4]] (+0.58, fdr 3e-05), [[CNIH3]] (+0.57, fdr 1e-05), [[CFAP58]] (+0.57, fdr 3e-05); moves opposite to [[HDHD3]] (-0.49, fdr 4e-05), [[ZNF461]] (-0.49, fdr 4e-05), [[RHOT1]] (-0.49, fdr 6e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CCDC15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +15.5 | 0e+00 | 19/27 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.9 | 6e-30 | 4/7 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +9.4 | 8e-19 | 4/13 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +9.0 | 4e-17 | 5/7 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +8.2 | 4e-14 | 11/23 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +7.6 | 4e-12 | 12/31 (HOP62, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.5 | 5e-09 | 10/27 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.3 | 2e-08 | 9/36 (A-172, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.7 | 2e-04 | 7/24 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.48×** | +4.4 | 7e-04 | 8/35 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.009 | 6/24 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.015 | 4/24 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.027 | 4/20 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.4 | 0.027 | 1/8 (Panc 03.27) | top dose only | noisy plate (z scaled) |
| [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +3.3 | 0.043 | 0/34 | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.046 | 3/32 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.074 | 0/27 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.094 | 1/35 (A-172) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -5.5 | 2e-05 | 10/31 (SW 900, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -5.4 | 2e-05 | 14/35 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.400×** | -5.3 | 2e-05 | 11/23 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -5.0 | 8e-05 | 16/32 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -4.5 | 7e-04 | 11/27 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.695×** | -4.5 | 7e-04 | 11/35 (SW 900, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.011 | 14/35 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.733×** | -3.5 | 0.039 | 7/35 (SW 900, J82, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.736×** | -3.4 | 0.042 | 3/27 (COLO 205, SW480, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.048 | 10/32 (SW 900, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.814×** | -3.1 | 0.099 | 10/32 (MIA PaCa-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 26.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.1) |
| [[A-172 (line)]] | wt | 4.11 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 3.91 | 0 | 1 | — | [[Budesonide (drug)]] 0.05 µM 0.0779× (z -9.3) |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.9) |
| [[PANC-1 (line)]] | alt | 1.14 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0483× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -10.1) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SNU-423 (line)]] | alt | 4.05 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0612× (z -8.7) |
| [[A-427 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRL4]] | +0.58 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CNIH3]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CFAP58]] | +0.57 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ZPLD1]] | +0.57 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[PECAM1]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MYH15]] | +0.54 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[MEI1]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[PLXNA4]] | +0.52 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[LTBP2]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[RGL2]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[LINC02454]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[LETM2]] | +0.51 | +0.45 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD3]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZNF461]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[RHOT1]] | -0.49 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[SRI]] | -0.47 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[CRYZL1]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DIPK1A]] | -0.45 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[RWDD1]] | -0.44 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MRPL16]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC37A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINLYP]] | B | PINLYP activity raises SLC37A2's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PINLYP | 0.038 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity raises SLC37A2's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without ADAM8 | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[MILR1]] | B | MILR1 activity raises SLC37A2's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without MILR1 | 0.054 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC15]] | B | SLC37A2 activity raises CCDC15's level | lines that do not express SLC37A2 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without SLC37A2 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent |
| [[CRYZL1]] | B | SLC37A2 activity raises CRYZL1's level | lines that do not express SLC37A2 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without SLC37A2 | 0.054 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent |
| [[ASGR1]] | B | SLC37A2 activity raises ASGR1's level | lines that do not express SLC37A2 (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without SLC37A2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent |
| [[LMNB1-DT]] | B | SLC37A2 activity strengthens LMNB1-DT's drug response | lines that do not express SLC37A2 (9) vs lines expressing it (30) | the lines without SLC37A2 respond 0.64× as strongly (z diff +1.16); strongest at Homoharringtonine 5 µM: 3.23x vs 5.17x (z diff +1.9) | 0.097 | ⚠ within organs, on part of the lines; also absent: FAM111B; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, -7.8); signed map (12.9, 49.9). **Vector** length 48.1, 6.87% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 37 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,063,302-125,090,516 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00171, SPX2 |
| Gene groups (HGNC) | Solute carrier family 37 |
| Reactome | 3 pathways, smallest: Gluconeogenesis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TED4](https://www.uniprot.org/uniprotkb/Q8TED4) (Glucose-6-phosphate exchanger SLC37A2):

> Inorganic phosphate and glucose-6-phosphate antiporter. May transport cytoplasmic glucose-6-phosphate into the lumen of the endoplasmic reticulum and translocate inorganic phosphate into the opposite direction. Independent of a lumenal glucose-6-phosphatase. May not play a role in homeostatic regulation of blood glucose levels.

**Summary**, from NCBI Gene [219855](https://www.ncbi.nlm.nih.gov/gene/219855):

> Enables glucose 6-phosphate:phosphate antiporter activity. Involved in glucose-6-phosphate transport and phosphate ion transmembrane transport. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20644) · Entrez [219855](https://www.ncbi.nlm.nih.gov/gene/219855) · UniProt [Q8TED4](https://www.uniprot.org/uniprotkb/Q8TED4) · Ensembl [ENSG00000134955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134955)

## Data

Gene col 5629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5629); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5629]; `tensor/DDL_lfc|DDL_z.npy` [5629]; `embed/gene_vectors.npy` [5629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5629 or target_col == 5629). Every well: [[SLC37A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC37A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
