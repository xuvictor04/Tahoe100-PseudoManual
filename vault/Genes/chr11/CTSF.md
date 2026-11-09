---
symbol: "CTSF"
type: "gene"
col: 10458
ensembl_id: "ENSG00000174080"
name: "cathepsin F"
location: "11q13.2"
module: 50
arm: "+"
pooled_cpm: 3.33
n_lines_expressing: 34
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CTSF

*cathepsin F* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.85× (z +10.5, q 7e-23, up in 14 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.63× (z +5.4, q 1e-05, up in 9 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.329× (z -8.6, q 4e-15, down in 21 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM59]] (+0.67, fdr 7e-06), [[FKBP7]] (+0.65, fdr 9e-06), [[GM2A]] (+0.63, fdr 1e-05); moves opposite to [[GTF2H3]] (-0.50, fdr 4e-05), [[DDX21]] (-0.49, fdr 3e-05), [[EIF3J]] (-0.49, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MMP2]] → it (grade B ⚠); 5 go from it, the strongest it → [[P4HTM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +10.5 | 7e-23 | 14/15 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +8.9 | 1e-16 | 7/8 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +6.6 | 6e-09 | 10/10 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +5.4 | 1e-05 | 9/31 (Panc 03.27, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.0 | 7e-05 | 11/25 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +3.9 | 0.008 | 4/17 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +3.6 | 0.022 | 3/27 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +3.6 | 0.023 | 6/17 (HS-578T, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +3.5 | 0.026 | 11/30 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.82×** | +3.3 | 0.049 | 8/22 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.057 | 4/30 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.057 | 9/27 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.74×** | +3.1 | 0.088 | 3/23 (NCI-H2347, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.329×** | -8.6 | 4e-15 | 21/24 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.502×** | -7.5 | 1e-11 | 21/25 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.404×** | -7.0 | 5e-10 | 23/30 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.582×** | -4.0 | 0.008 | 13/23 (A549, HOP62, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.721×** | -3.6 | 0.041 | 13/29 (C-33 A, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.655× | -3.3 | 0.10 | 7/30 (Panc 03.27, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.665× | -3.1 | 0.13 | 9/28 (C32, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 6.80 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0478× (z -12.2) |
| [[SHP-77 (line)]] | alt | 6.51 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0639× (z -10.0) |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 0.953 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.148 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.188 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.839 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.172 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FKBP7]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[GM2A]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[BEX3]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[GLMP]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MMP2]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 | same gene group |
| [[DNASE2]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PRAF2]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[GRN]] | +0.60 | +0.65 / +0.49 | both halves | 2e-05 | STRING 599 |
| [[PAN3]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[NPC2]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GAMT]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DDX21]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP2]] | B | MMP2 activity raises CTSF's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.24× lower at baseline in the lines without MMP2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[FKBP7]] | B | FKBP7 activity raises CTSF's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 2.74× lower at baseline in the lines without FKBP7 | 0.097 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[SMIM10]] | C | SMIM10 activity raises CTSF's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.80× lower at baseline in the lines without SMIM10 | 0.002 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365; co-absent with the target |
| [[PRAF2]] | C | PRAF2 activity raises CTSF's level | lines that do not express PRAF2 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without PRAF2 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286511, LINC02343, CCDC110; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P4HTM]] | B | CTSF activity lowers P4HTM's level | lines that do not express CTSF (16) vs lines expressing it (34) | 1.17× higher at baseline in the lines without CTSF | 0.048 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[PRAF2]] | B | CTSF activity raises PRAF2's level | lines that do not express CTSF (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without CTSF | 0.060 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[GLMP]] | B | CTSF activity raises GLMP's level | lines that do not express CTSF (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without CTSF | 0.066 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[SIAE]] | B | CTSF activity raises SIAE's level | lines that do not express CTSF (16) vs lines expressing it (34) | 1.19× lower at baseline in the lines without CTSF | 0.087 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES |
| [[SMIM10]] | C | CTSF activity raises SMIM10's level | lines that do not express CTSF (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without CTSF | 0.015 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES; co-absent with the target |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, -37.1); signed map (-24.7, -2.9). **Vector** length 43.0, 7.34% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycosphingolipid catabolism* (reactome, mean cos +0.50 to 5); *Glycosphingolipid metabolism* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,563,464-66,568,879 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CATSF, CLN13 |
| Gene groups (HGNC) | Cathepsins; Elastases; Cysteine endopeptidases |
| Hallmark sets | P53_PATHWAY |
| Reactome | 5 pathways, smallest: Processing of antigen in germinal center B cells; MHC class II antigen presentation; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBX1](https://www.uniprot.org/uniprotkb/Q9UBX1) (Cathepsin F):

> Thiol protease which is believed to participate in intracellular degradation and turnover of proteins. Has also been implicated in tumor invasion and metastasis.

**Summary**, from NCBI Gene [8722](https://www.ncbi.nlm.nih.gov/gene/8722):

> Cathepsins are papain family cysteine proteinases that represent a major component of the lysosomal proteolytic system. Cathepsins generally contain a signal sequence, followed by a propeptide and then a catalytically active mature region. The very long (251 amino acid residues) proregion of the cathepsin F precursor contains a C-terminal domain similar to the pro-segment of cathepsin L-like enzymes, a 50-residue flexible linker peptide, and an N-terminal domain predicted to adopt a …

**Accessions** — [HGNC:2531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2531) · Entrez [8722](https://www.ncbi.nlm.nih.gov/gene/8722) · UniProt [Q9UBX1](https://www.uniprot.org/uniprotkb/Q9UBX1) · Ensembl [ENSG00000174080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174080)

## Data

Gene col 10458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10458); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10458]; `tensor/DDL_lfc|DDL_z.npy` [10458]; `embed/gene_vectors.npy` [10458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10458 or target_col == 10458). Every well: [[CTSF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
