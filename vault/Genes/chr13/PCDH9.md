---
symbol: "PCDH9"
type: "gene"
col: 11508
ensembl_id: "ENSG00000184226"
name: "protocadherin 9"
location: "13q21.32"
module: 9
arm: "+"
pooled_cpm: 44.71
n_lines_expressing: 28
n_dd_up: 35
n_dd_down: 4
n_dd_up_clean: 31
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 19
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PCDH9

*protocadherin 9* — 13q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.23× (z +36.7, q 0e+00, up in 21 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.800× (z -4.2, q 0.018, down in 7 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAM2]] (+0.71, fdr 7e-06), [[RALYL]] (+0.69, fdr 7e-06), [[EPHA5]] (+0.69, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[LRRTM4]] → it (grade B ⚠); 7 go from it, the strongest it → [[LINC00534]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.23×** | +36.7 | 0e+00 | 21/26 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.73×** | +17.2 | 0e+00 | 22/26 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.50×** | +17.0 | 0e+00 | 18/26 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.20×** | +15.2 | 0e+00 | 22/26 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.72×** | +13.1 | 5e-37 | 20/25 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +13.0 | 1e-36 | 15/27 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +12.5 | 3e-34 | 9/24 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +11.9 | 8e-31 | 16/26 (HEC-1-A, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +11.1 | 1e-26 | 16/24 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +10.2 | 1e-22 | 12/26 (HOP62, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.09×** | +9.7 | 2e-20 | 9/26 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +8.2 | 8e-15 | 10/26 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +7.3 | 1e-11 | 13/25 (HOP62, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.74×** | +7.2 | 2e-11 | 20/26 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.2 | 3e-08 | 8/21 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +5.9 | 2e-07 | 18/24 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +5.2 | 5e-06 | 8/25 (SW480, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.800×** | -4.2 | 0.018 | 7/26 (SHP-77, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.744×** | -3.9 | 0.026 | 9/25 (A-427, SHP-77, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.042 | 10/25 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.760×** | -3.6 | 0.043 | 7/24 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.785× | -3.2 | 0.16 | 9/25 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.797× | -3.0 | 0.24 | 8/24 (LS 180, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 245 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.9) |
| [[LS 180 (line)]] | wt | 157 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.8) |
| [[J82 (line)]] | alt | 22.5 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +20.9) | — |
| [[HOP62 (line)]] | alt | 20.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +18.0) | — |
| [[A-427 (line)]] | wt | 289 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 88.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +19.9) | — |
| [[NCI-H1573 (line)]] | alt | 31.6 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.87× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.2× (z +23.6) | — |
| [[C32 (line)]] | wt | 52.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.7× (z +20.0) | — |
| [[H4 (line)]] | wt | 24.4 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 77.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 24.7× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 28.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 13.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +13.2) | — |
| [[A549 (line)]] | wt | 61.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 491 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +9.8) | — |
| [[A-172 (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 944 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.27 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.24 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM2]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[RALYL]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[EPHA5]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADGRL3]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NKAIN2]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CADM2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 | STRING 456 |
| [[PCDH17]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 | same gene group |
| [[KCNH7]] | +0.64 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[LSAMP]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[LINC01695]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SYT1]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 4, C 15. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRTM4]] | B | LRRTM4 activity raises PCDH9's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without LRRTM4 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[TOP2A]] | B | TOP2A activity lowers PCDH9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RMST]] | B | RMST activity raises PCDH9's level | lines that do not express RMST (35) vs lines expressing it (15) | 3.52× lower at baseline in the lines without RMST | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent |
| [[MIR99AHG]] | B | MIR99AHG activity raises PCDH9's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.44× lower at baseline in the lines without MIR99AHG | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099 |
| [[BCHE]] | C | BCHE activity raises PCDH9's level | lines that do not express BCHE (35) vs lines expressing it (15) | 6.09× lower at baseline in the lines without BCHE | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[LSAMP]] | C | LSAMP activity raises PCDH9's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 3.96× lower at baseline in the lines without LSAMP | 0.007 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent; co-absent with the target |
| [[EPHA5-AS1]] | C | EPHA5-AS1 activity raises PCDH9's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 4.28× lower at baseline in the lines without EPHA5-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises PCDH9's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 4.91× lower at baseline in the lines without LINC02506 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[TNFRSF19]] | C | TNFRSF19 activity raises PCDH9's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 3.90× lower at baseline in the lines without TNFRSF19 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |
| [[ROBO2]] | C | ROBO2 activity raises PCDH9's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 4.72× lower at baseline in the lines without ROBO2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises PCDH9's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.39× lower at baseline in the lines without EPHA5 | 0.038 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises PCDH9's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 4.84× lower at baseline in the lines without CSMD3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00534]] | B | PCDH9 activity raises LINC00534's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without PCDH9 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5 |
| [[GRIK2]] | B | PCDH9 activity raises GRIK2's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 2.99× lower at baseline in the lines without PCDH9 | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5 |
| cells under [[Penfluridol (drug)]] 5 µM | B | PCDH9 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express PCDH9 (22) vs lines expressing it (26) | the lines without PCDH9: 1.12× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5 |
| [[MIR3667HG]] | B | PCDH9 activity raises MIR3667HG's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 1.65× lower at baseline in the lines without PCDH9 | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5 |
| [[LSAMP]] | C | PCDH9 activity raises LSAMP's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without PCDH9 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5; co-absent with the target |
| [[ADAMTS1]] | C | PCDH9 activity raises ADAMTS1's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 3.73× lower at baseline in the lines without PCDH9 | 0.066 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5; co-absent with the target |
| [[LINC01320]] | C | PCDH9 activity raises LINC01320's level | lines that do not express PCDH9 (22) vs lines expressing it (28) | 2.45× lower at baseline in the lines without PCDH9 | 0.097 | ⚠ within organs, on part of the lines; also absent: KCNK2, CNRIP1, EPHA5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.7, 33.8); signed map (41.1, 35.4). **Vector** length 80.4, 21.6% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +36.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +17.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -3.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.1 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.32 — chr13:66,302,834-67,230,445 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Non-clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC56](https://www.uniprot.org/uniprotkb/Q9HC56) (Protocadherin-9):

> Potential calcium-dependent cell-adhesion protein.

**Summary**, from NCBI Gene [5101](https://www.ncbi.nlm.nih.gov/gene/5101):

> This gene encodes a member of the protocadherin family, and cadherin superfamily, of transmembrane proteins containing cadherin domains. These proteins mediate cell adhesion in neural tissues in the presence of calcium. The encoded protein may be involved in signaling at neuronal synaptic junctions. Sharing a characteristic with other protocadherin genes, this gene has a notably large exon that encodes multiple cadherin domains and a transmembrane region. Alternatively spliced transcript …

**Accessions** — [HGNC:8661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8661) · Entrez [5101](https://www.ncbi.nlm.nih.gov/gene/5101) · UniProt [Q9HC56](https://www.uniprot.org/uniprotkb/Q9HC56) · Ensembl [ENSG00000184226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184226)

## Data

Gene col 11508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11508); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11508]; `tensor/DDL_lfc|DDL_z.npy` [11508]; `embed/gene_vectors.npy` [11508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11508 or target_col == 11508). Every well: [[PCDH9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
