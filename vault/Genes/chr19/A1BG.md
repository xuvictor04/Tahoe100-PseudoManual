---
symbol: "A1BG"
type: "gene"
col: 4272
ensembl_id: "ENSG00000121410"
name: "alpha-1-B glycoprotein"
location: "19q13.43"
module: 3
arm: "+"
pooled_cpm: 3.71
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# A1BG

*alpha-1-B glycoprotein* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.13× (z +5.1, q 2e-04, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 2.32× (z +3.4, q 0.091, up in 4 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.379× (z -6.8, q 5e-09, down in 18 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD6]] (+0.73, fdr 1e-05), [[ALKBH7]] (+0.72, fdr 1e-05), [[LIN7B]] (+0.72, fdr 1e-05); moves opposite to [[ZNF300]] (-0.69, fdr 2e-05), [[ZNF655]] (-0.67, fdr 1e-05), [[PSME3]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[A1BG-AS1]] → it (grade C ⚠); 7 go from it, the strongest it → [[VKORC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +5.1 | 2e-04 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +4.1 | 0.010 | 9/14 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +3.7 | 0.038 | 3/13 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.5 | 0.060 | 6/21 (A-172, RPMI-7951, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.32×** | +3.4 | 0.091 | 4/21 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.55× | +3.1 | 0.17 | 9/24 (NCI-H23, A-172, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.55× | +3.1 | 0.17 | 3/21 (SHP-77, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | 1.56× | +3.0 | 0.18 | 6/24 (A549, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.379×** | -6.8 | 5e-09 | 18/22 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -5.8 | 2e-06 | 17/21 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.474×** | -5.3 | 3e-05 | 14/29 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -4.3 | 0.002 | 14/23 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -4.2 | 0.004 | 15/28 (H4, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -3.7 | 0.017 | 11/24 (A-172, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.367×** | -3.7 | 0.019 | 11/22 (A-172, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.600×** | -3.6 | 0.023 | 12/28 (SW 900, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.551×** | -3.4 | 0.047 | 13/28 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.612×** | -3.2 | 0.079 | 4/28 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.644× | -3.1 | 0.10 | 10/24 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.649× | -3.0 | 0.11 | 5/29 (H4, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.8) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.9) |
| [[H4 (line)]] | wt | 6.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0419× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 8.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.9) |
| [[PANC-1 (line)]] | alt | 7.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -8.5) |
| [[A-427 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.961 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.918 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.72 | +0.56 / +0.79 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.72 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.71 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[ATP5MJ]] | +0.70 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[C19orf81]] | +0.70 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.70 | +0.52 / +0.76 | both halves | 1e-05 |  |
| [[CCDC107]] | +0.69 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.69 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[KLHL7]] | +0.69 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MALSU1]] | +0.68 | +0.48 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF300]] | -0.69 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.67 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PSME3]] | -0.65 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[SLC39A10]] | -0.64 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[DARS2]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.63 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[ELK4]] | -0.62 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[TASOR]] | -0.62 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.61 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[RCC2]] | -0.61 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[A1BG-AS1]] | C | A1BG-AS1 activity raises A1BG's level | lines that do not express A1BG-AS1 (18) vs lines expressing it (32) | 3.39× lower at baseline in the lines without A1BG-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: A1BG, DZIP1, RNF150; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VKORC1]] | B | A1BG activity raises VKORC1's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.83× lower at baseline in the lines without A1BG | 0.031 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[GOLGA8N]] | B | A1BG activity raises GOLGA8N's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.55× lower at baseline in the lines without A1BG | 0.053 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[UBE2O]] | B | A1BG activity raises UBE2O's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without A1BG | 0.068 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[ZNF565]] | B | A1BG activity raises ZNF565's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without A1BG | 0.083 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[SHARPIN]] | B | A1BG activity lowers SHARPIN's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.17× higher at baseline in the lines without A1BG | 0.093 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[ZNF655]] | B | A1BG activity weakens ZNF655's drug response | lines that do not express A1BG (11) vs lines expressing it (32) | the lines without A1BG respond 1.11× as strongly (z diff +0.07); strongest at Panobinostat 5 µM: 0.36x vs 0.47x (z diff -1.9) | 0.099 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1; target measured in part of the lines; both ways; artifact flags |
| [[A1BG-AS1]] | C | A1BG activity raises A1BG-AS1's level | lines that do not express A1BG (17) vs lines expressing it (33) | 3.79× lower at baseline in the lines without A1BG | 0.012 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.2, -17.9); signed map (-29.9, 11.9). **Vector** length 44.3, 8.94% of its response variance represented; |z| ≥ 3 in 447 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.9 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +0.7 | -0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.0 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1-B glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,345,178-58,353,492 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Immunoglobulin like domain containing |
| Reactome | 6 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

UniProt [P04217](https://www.uniprot.org/uniprotkb/P04217) carries no function annotation.

**Summary**, from NCBI Gene [1](https://www.ncbi.nlm.nih.gov/gene/1):

> The protein encoded by this gene is a plasma glycoprotein of unknown function. The protein shows sequence similarity to the variable regions of some immunoglobulin supergene family member proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5) · Entrez [1](https://www.ncbi.nlm.nih.gov/gene/1) · UniProt [P04217](https://www.uniprot.org/uniprotkb/P04217) · Ensembl [ENSG00000121410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121410)

## Data

Gene col 4272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4272); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4272]; `tensor/DDL_lfc|DDL_z.npy` [4272]; `embed/gene_vectors.npy` [4272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4272 or target_col == 4272). Every well: [[A1BG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A1BG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
