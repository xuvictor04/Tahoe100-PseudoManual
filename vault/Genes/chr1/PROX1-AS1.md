---
symbol: "PROX1-AS1"
type: "gene"
col: 13752
ensembl_id: "ENSG00000230461"
name: "PROX1 antisense RNA 1"
location: "1q32.3"
module: 27
arm: "+"
pooled_cpm: 14.95
n_lines_expressing: 21
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 37
direction_downstream: 30
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PROX1-AS1

*PROX1 antisense RNA 1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.82× (z +15.7, q 0e+00, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.430× (z -6.7, q 1e-08, down in 16 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PROX1]] (+0.81, fdr 7e-06, ⚠ same locus), [[NKD1]] (+0.77, fdr 7e-06), [[VWA2]] (+0.77, fdr 7e-06), [[APCDD1]] (+0.77, fdr 7e-06); moves opposite to [[PASD1]] (-0.50, fdr 3e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[HS3ST5]] → it (grade B ⚠); 30 go from it, the strongest it → [[FHDC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +15.7 | 0e+00 | 12/15 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +7.9 | 6e-13 | 1/6 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +6.6 | 8e-09 | 3/11 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +6.6 | 8e-09 | 11/18 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +6.0 | 2e-07 | 10/17 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.3 | 0.002 | 5/14 (SW 900, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.3 | 0.002 | 7/16 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.078 | 5/17 (SHP-77, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.2 | 0.096 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.46× | +3.1 | 0.11 | 6/18 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.430×** | -6.7 | 1e-08 | 16/18 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.576×** | -4.6 | 0.001 | 8/17 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -4.5 | 0.001 | 15/18 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -4.3 | 0.002 | 14/17 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.605×** | -4.0 | 0.006 | 6/17 (LS 180, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -3.8 | 0.012 | 4/17 (SW480, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.8 | 0.013 | 8/17 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.030 | 10/18 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -3.3 | 0.062 | 12/14 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.676×** | -3.3 | 0.062 | 5/17 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.680×** | -3.2 | 0.068 | 12/18 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.683×** | -3.2 | 0.069 | 8/18 (SW480, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -3.1 | 0.094 | 10/16 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.677× | -3.0 | 0.10 | 2/18 (SW48, RKO) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 189 | 0 | 24 (12 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0384× (z -20.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0416× (z -19.7) |
| [[LoVo (line)]] | wt | 6.64 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.40× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.0221× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.1) | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0203× (z -19.0) |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0851× (z -9.8) |
| [[SHP-77 (line)]] | alt | 7.47 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0833× (z -9.4) |
| [[A-172 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROX1]] | +0.81 | +0.76 / +0.79 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NKD1]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ST18]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[IGFL4]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC02254]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[GJB1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[JAKMIP2-AS1]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 | same gene group |
| [[ADGRG5]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LINC01622]] | +0.69 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[FGD5]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PASD1]] | -0.50 | -0.53 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 7, C 30. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST5]] | B | HS3ST5 activity raises PROX1-AS1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without HS3ST5 | 0.013 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PROX1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01091]] | B | LINC01091 activity raises PROX1-AS1's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without LINC01091 | 0.050 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[SLCO6A1]] | B | SLCO6A1 activity raises PROX1-AS1's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without SLCO6A1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |
| [[NCALD]] | B | NCALD activity raises PROX1-AS1's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without NCALD | 0.083 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[TRPV4]] | B | TRPV4 activity raises PROX1-AS1's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without TRPV4 | 0.083 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises PROX1-AS1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without FKBP9P1-1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[PROX1]] | C | PROX1 activity raises PROX1-AS1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without PROX1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises PROX1-AS1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.56× lower at baseline in the lines without TSHZ2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[ST18]] | C | ST18 activity raises PROX1-AS1's level | lines that do not express ST18 (39) vs lines expressing it (11) | 4.12× lower at baseline in the lines without ST18 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | RIMBP2 activity raises PROX1-AS1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without RIMBP2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises PROX1-AS1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.55× lower at baseline in the lines without TFF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 7, C 23. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHDC1]] | B | PROX1-AS1 activity raises FHDC1's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without PROX1-AS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[IL19]] | B | PROX1-AS1 activity raises IL19's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without PROX1-AS1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[LINC01091]] | B | PROX1-AS1 activity raises LINC01091's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without PROX1-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[KIF26B]] | B | PROX1-AS1 activity raises KIF26B's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.09× lower at baseline in the lines without PROX1-AS1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[NCALD]] | B | PROX1-AS1 activity raises NCALD's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 2.43× lower at baseline in the lines without PROX1-AS1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[ZNF703]] | B | PROX1-AS1 activity raises ZNF703's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 2.02× lower at baseline in the lines without PROX1-AS1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | B | PROX1-AS1 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (makes them more sensitive) | lines that do not express PROX1-AS1 (29) vs lines expressing it (19) | the lines without PROX1-AS1: 1.16× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1 |
| [[PROX1]] | C | PROX1-AS1 activity raises PROX1's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 5.58× lower at baseline in the lines without PROX1-AS1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[TSHZ2]] | C | PROX1-AS1 activity raises TSHZ2's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without PROX1-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[RIMBP2]] | C | PROX1-AS1 activity raises RIMBP2's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 2.99× lower at baseline in the lines without PROX1-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[ZBTB7C]] | C | PROX1-AS1 activity raises ZBTB7C's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.05× lower at baseline in the lines without PROX1-AS1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[TFF3]] | C | PROX1-AS1 activity raises TFF3's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.00× lower at baseline in the lines without PROX1-AS1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, 44.2); signed map (63.1, 15.0). **Vector** length 54.3, 16.0% of its response variance represented; |z| ≥ 3 in 417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +15.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.7 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.3 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +0.7 | +1.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.7 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -3.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.3 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.2 | -4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PROX1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.3 — chr1:213,817,751-213,988,508 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43656](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43656) · Entrez [100505832](https://www.ncbi.nlm.nih.gov/gene/100505832) · Ensembl [ENSG00000230461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230461)

## Data

Gene col 13752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13752); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13752]; `tensor/DDL_lfc|DDL_z.npy` [13752]; `embed/gene_vectors.npy` [13752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13752 or target_col == 13752). Every well: [[PROX1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROX1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
