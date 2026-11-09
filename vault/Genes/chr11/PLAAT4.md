---
symbol: "PLAAT4"
type: "gene"
col: 5442
ensembl_id: "ENSG00000133321"
name: "phospholipase A and acyltransferase 4"
location: "11q12.3"
module: 70
arm: "+"
pooled_cpm: 6.7
n_lines_expressing: 29
n_dd_up: 32
n_dd_down: 18
n_dd_up_clean: 26
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 37
direction_downstream: 76
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# PLAAT4

*phospholipase A and acyltransferase 4* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +9.8, q 9e-20, up in 18 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.432× (z -6.3, q 1e-07, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFSF10]] (+0.75, fdr 7e-06), [[APOL1]] (+0.75, fdr 7e-06), [[TLR3]] (+0.73, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[IFIT2]] → it (grade B ⚠); 76 go from it, the strongest it → [[OASL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +9.8 | 9e-20 | 18/24 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +9.3 | 4e-18 | 4/11 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +6.9 | 7e-10 | 10/17 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +6.7 | 4e-09 | 4/14 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +6.3 | 4e-08 | 15/22 (CFPAC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.12×** | +5.4 | 6e-06 | 15/24 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.02×** | +5.3 | 1e-05 | 15/25 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.02×** | +5.1 | 3e-05 | 18/23 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.93×** | +5.0 | 4e-05 | 16/26 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.73×** | +4.8 | 8e-05 | 14/25 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +4.6 | 2e-04 | 9/14 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +4.4 | 4e-04 | 16/24 (CFPAC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.001 | 17/25 (AsPC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.51×** | +4.2 | 0.001 | 14/25 (Panc 03.27, Hs 766T, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.43×** | +4.2 | 0.001 | 12/22 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.72×** | +3.8 | 0.004 | 12/24 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.004 | 8/25 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.007 | 11/24 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Capmatinib (drug)]] 5 µM |  | **2.52×** | +3.6 | 0.008 | 7/18 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.432×** | -6.3 | 1e-07 | 16/26 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.484×** | -5.5 | 1e-05 | 17/24 (KATO III, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.618×** | -5.1 | 5e-05 | 18/22 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -4.2 | 0.003 | 13/24 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -4.2 | 0.003 | 15/24 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.576×** | -4.2 | 0.003 | 9/24 (Panc 03.27, A-172, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.680×** | -4.1 | 0.003 | 16/25 (A-172, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -4.0 | 0.004 | 15/24 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.594×** | -3.9 | 0.005 | 11/24 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -3.7 | 0.013 | 12/26 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -3.7 | 0.013 | 13/24 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | **0.631×** | -3.5 | 0.024 | 4/24 (Hs 766T, LS 180, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.644×** | -3.3 | 0.038 | 9/24 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.440×** | -3.2 | 0.049 | 7/25 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.452×** | -3.1 | 0.066 | 12/24 (HT-29, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.669×** | -3.0 | 0.085 | 11/24 (MIA PaCa-2, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.654×** | -3.0 | 0.099 | 3/24 (J82, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.26 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -14.9) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -14.9) |
| [[A498 (line)]] | wt | 5.51 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -10.7) |
| [[KATO III (line)]] | alt | 19.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0788× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.2) |
| [[SW1417 (line)]] | alt | 2.83 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0398× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 65.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 7.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0803× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 9.67 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.6) |
| [[A-427 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.503 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFSF10]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 | STRING 430 |
| [[APOL1]] | +0.75 | +0.76 / +0.66 | both halves | 7e-06 | STRING 437 |
| [[TLR3]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[PSMB10]] | +0.72 | +0.72 / +0.60 | both halves | 7e-06 | STRING 440 |
| [[PSMB9]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | STRING 559 |
| [[PSMB8]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 | STRING 449 |
| [[GBP4]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 | STRING 461 |
| [[APOL6]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 | STRING 541 |
| [[CASP10]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[APOL3]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[CFB]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[IDO1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 18, C 19. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT2]] | B | IFIT2 activity raises PLAAT4's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.15× lower at baseline in the lines without IFIT2 | 0.012 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[PRKCH-AS1]] | B | PRKCH-AS1 activity raises PLAAT4's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without PRKCH-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[OASL]] | B | OASL activity raises PLAAT4's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without OASL | 0.025 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises PLAAT4's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.68× lower at baseline in the lines without IFI44 | 0.025 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CD74]] | B | CD74 activity raises PLAAT4's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without CD74 | 0.028 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[TOP2A]] | B | TOP2A activity lowers PLAAT4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OAS1]] | B | OAS1 activity raises PLAAT4's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without OAS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[ETV7]] | B | ETV7 activity raises PLAAT4's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without ETV7 | 0.054 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[IFIT3]] | B | IFIT3 activity raises PLAAT4's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 2.81× lower at baseline in the lines without IFIT3 | 0.054 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[GBP3]] | B | GBP3 activity raises PLAAT4's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without GBP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IDO1]] | B | IDO1 activity raises PLAAT4's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without IDO1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[IL15RA]] | B | IL15RA activity raises PLAAT4's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.81× lower at baseline in the lines without IL15RA | 0.063 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |

### Downstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 55, C 21. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | PLAAT4 activity raises OASL's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.22× lower at baseline in the lines without PLAAT4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[APOL6]] | B | PLAAT4 activity raises APOL6's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.00× lower at baseline in the lines without PLAAT4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[UBA7]] | B | PLAAT4 activity raises UBA7's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.36× lower at baseline in the lines without PLAAT4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IFI44]] | B | PLAAT4 activity raises IFI44's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.20× lower at baseline in the lines without PLAAT4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[DDX60]] | B | PLAAT4 activity raises DDX60's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without PLAAT4 | 7e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IFIT3]] | B | PLAAT4 activity raises IFIT3's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.18× lower at baseline in the lines without PLAAT4 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[ZC3HAV1]] | B | PLAAT4 activity raises ZC3HAV1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without PLAAT4 | 0.001 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[OAS1]] | B | PLAAT4 activity raises OAS1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.63× lower at baseline in the lines without PLAAT4 | 0.002 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[DHX58]] | B | PLAAT4 activity raises DHX58's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.98× lower at baseline in the lines without PLAAT4 | 0.002 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[B2M]] | B | PLAAT4 activity raises B2M's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without PLAAT4 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[PSMB10]] | B | PLAAT4 activity raises PSMB10's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without PLAAT4 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IFIT1]] | B | PLAAT4 activity raises IFIT1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without PLAAT4 | 0.005 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.5, 51.4); signed map (61.6, 29.4). **Vector** length 69.5, 19.9% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.51 to 25); *Antigen processing-Cross presentation* (reactome, mean cos +0.52 to 14); *ER-Phagosome pathway* (reactome, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +5.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.2 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A and acyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:63,536,808-63,546,462 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIG3, HRASLS4, PLAAT-4, RIG1; previously RARRES3 |
| Gene groups (HGNC) | Phospholipase A and acyltransferase family |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL19](https://www.uniprot.org/uniprotkb/Q9UL19) (Phospholipase A and acyltransferase 4):

> Exhibits both phospholipase A1/2 and acyltransferase activities. Shows phospholipase A1 (PLA1) and A2 (PLA2), catalyzing the calcium-independent release of fatty acids from the sn-1 or sn-2 position of glycerophospholipids. For most substrates, PLA1 activity is much higher than PLA2 activity. Shows O-acyltransferase activity, catalyzing the transfer of a fatty acyl group from glycerophospholipid to the hydroxyl group of lysophospholipid. Shows N-acyltransferase activity, catalyzing the …

**Summary**, from NCBI Gene [5920](https://www.ncbi.nlm.nih.gov/gene/5920):

> Retinoids exert biologic effects such as potent growth inhibitory and cell differentiation activities and are used in the treatment of hyperproliferative dermatological diseases. These effects are mediated by specific nuclear receptor proteins that are members of the steroid and thyroid hormone receptor superfamily of transcriptional regulators. RARRES1, RARRES2, and RARRES3 are genes whose expression is upregulated by the synthetic retinoid tazarotene. RARRES3 is thought act as a tumor …

**Accessions** — [HGNC:9869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9869) · Entrez [5920](https://www.ncbi.nlm.nih.gov/gene/5920) · UniProt [Q9UL19](https://www.uniprot.org/uniprotkb/Q9UL19) · Ensembl [ENSG00000133321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133321)

## Data

Gene col 5442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5442); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5442]; `tensor/DDL_lfc|DDL_z.npy` [5442]; `embed/gene_vectors.npy` [5442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5442 or target_col == 5442). Every well: [[PLAAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAAT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
