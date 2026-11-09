---
symbol: "SLC7A8"
type: "gene"
col: 1686
ensembl_id: "ENSG00000092068"
name: "solute carrier family 7 member 8"
location: "14q11.2"
module: 90
arm: "+"
pooled_cpm: 6.41
n_lines_expressing: 31
n_dd_up: 37
n_dd_down: 1
n_dd_up_clean: 29
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 21
direction_downstream: 13
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# SLC7A8

*solute carrier family 7 member 8* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.51× (z +18.2, q 0e+00, up in 27 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.668× (z -4.0, q 0.035, down in 7 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0459×); [[Digitoxin (drug)]] 0.5 µM in 1 line (COLO 205 0.200×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (COLO 205 0.225×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPEAR]] (+0.63, fdr 7e-06), [[MYRIP]] (+0.62, fdr 1e-05), [[SELENOP]] (+0.59, fdr 1e-05); moves opposite to [[TRAPPC12]] (-0.46, fdr 8e-05), [[PRR14L]] (-0.46, fdr 4e-04), [[ANKMY1]] (-0.45, fdr 5e-04).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[ADGRG1]] → it (grade B ⚠); 13 go from it, the strongest it → [[AMOT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.51×** | +18.2 | 0e+00 | 27/28 (CFPAC-1, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.56×** | +15.5 | 0e+00 | 11/12 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.46×** | +14.7 | 0e+00 | 5/6 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +14.3 | 2e-44 | 15/24 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.87×** | +13.9 | 1e-41 | 24/28 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +13.8 | 2e-41 | 14/22 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.59×** | +13.1 | 3e-37 | 22/27 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.38×** | +12.5 | 9e-34 | 24/27 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +12.2 | 3e-32 | 5/7 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.20×** | +11.9 | 5e-31 | 23/27 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.04×** | +11.4 | 3e-28 | 24/26 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.86×** | +9.0 | 1e-17 | 14/28 (C32, HCT15, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +7.3 | 2e-11 | 4/14 (HCT15, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +6.7 | 1e-09 | 11/23 (C32, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.95×** | +5.8 | 3e-07 | 8/26 (BT-474, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.6 | 8e-07 | 7/19 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.3 | 3e-06 | 4/28 (SW1417, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +4.7 | 1e-04 | 7/23 (SW480, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.6 | 2e-04 | 8/26 (HT-29, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1686.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0459×); [[Digitoxin (drug)]] 0.5 µM in 1 line (COLO 205 0.200×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (COLO 205 0.225×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.668×** | -4.0 | 0.035 | 7/23 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.728× | -3.3 | 0.21 | 8/24 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.721× | -3.3 | 0.21 | 9/24 (SW480, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.200× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 25.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 4.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0459× (z -10.3) |
| [[SNU-423 (line)]] | alt | 1.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.2× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.815 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPEAR]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MYRIP]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SELENOP]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CNTNAP2]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TSPAN12]] | +0.59 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[ADGRV1]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[DCDC2]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[LINC00298]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[LINC00992]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ADGRG1]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[KSR2]] | +0.55 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.54 | +0.40 / +0.73 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC12]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[PRR14L]] | -0.46 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[ANKMY1]] | -0.45 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[NUP50-DT]] | -0.43 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[C1orf109]] | -0.43 | -0.15 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[ATR]] | -0.43 | -0.18 / -0.47 | ⚠ not reproduced | 9e-04 |  |
| [[ATP6V0A2]] | -0.42 | -0.27 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 15, C 6. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG1]] | B | ADGRG1 activity raises SLC7A8's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.00× lower at baseline in the lines without ADGRG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[SERPINF1]] | B | SERPINF1 activity raises SLC7A8's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.64× lower at baseline in the lines without SERPINF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[ENPP5]] | B | ENPP5 activity raises SLC7A8's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without ENPP5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[APOA1]] | B | APOA1 activity raises SLC7A8's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 1.29× lower at baseline in the lines without APOA1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB |
| [[QPRT]] | B | QPRT activity raises SLC7A8's level | lines that do not express QPRT (21) vs lines expressing it (29) | 1.65× lower at baseline in the lines without QPRT | 0.031 | ⚠ within organs, on part of the lines; also absent: OPRD1, FREM2, SERPINF1 |
| [[CNTNAP2]] | B | CNTNAP2 activity raises SLC7A8's level | lines that do not express CNTNAP2 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without CNTNAP2 | 0.032 | ⚠ within organs, on part of the lines; also absent: VENTXP1, CACNA1C, COP1-DT; maybe low, not absent |
| [[PPARGC1A]] | B | PPARGC1A activity raises SLC7A8's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without PPARGC1A | 0.042 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |
| [[SELENOP]] | B | SELENOP activity raises SLC7A8's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without SELENOP | 0.048 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[KCND2]] | B | KCND2 activity raises SLC7A8's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without KCND2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[FREM2]] | B | FREM2 activity raises SLC7A8's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without FREM2 | 0.061 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SLC7A8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ATL1]] | B | ATL1 activity raises SLC7A8's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 2.47× lower at baseline in the lines without ATL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOT]] | B | SLC7A8 activity raises AMOT's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without SLC7A8 | 0.009 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[ATL1]] | B | SLC7A8 activity raises ATL1's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without SLC7A8 | 0.024 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[BMF]] | B | SLC7A8 activity raises BMF's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without SLC7A8 | 0.065 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[PKIB]] | B | SLC7A8 activity raises PKIB's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without SLC7A8 | 0.083 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[KSR2]] | B | SLC7A8 activity raises KSR2's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without SLC7A8 | 0.088 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[SMOC2]] | B | SLC7A8 activity raises SMOC2's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without SLC7A8 | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[LRIG1]] | B | SLC7A8 activity raises LRIG1's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without SLC7A8 | 0.094 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[FGD3]] | B | SLC7A8 activity raises FGD3's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without SLC7A8 | 0.099 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[ADGRV1]] | B | SLC7A8 activity raises ADGRV1's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without SLC7A8 | 0.0997 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[RAB17]] | C | SLC7A8 activity raises RAB17's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 3.76× lower at baseline in the lines without SLC7A8 | 0.005 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6; co-absent with the target |
| [[PKHD1]] | C | SLC7A8 activity raises PKHD1's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without SLC7A8 | 0.058 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6; co-absent with the target |
| [[FGF9]] | C | SLC7A8 activity raises FGF9's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 2.59× lower at baseline in the lines without SLC7A8 | 0.077 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6; co-absent with the target |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, 47.4); signed map (52.7, 1.7). **Vector** length 50.6, 9.06% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +18.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -0.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,125,295-23,183,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPI-PC1, LAT2 |
| Gene groups (HGNC) | Solute carrier family 7 |
| Reactome | 7 pathways, smallest: Basigin interactions; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHI5](https://www.uniprot.org/uniprotkb/Q9UHI5) (Large neutral amino acids transporter small subunit 2):

> Associates with SLC3A2 to form a functional heterodimeric complex that translocates small and large neutral amino acids with broad specificity and a stoichiometry of 1:1. Functions as amino acid antiporter mediating the influx of extracellular essential amino acids mainly in exchange with the efflux of highly concentrated intracellular amino acids. Has relatively symmetrical selectivities but strongly asymmetrical substrate affinities at both the intracellular and extracellular sides of the …

**Summary**, from NCBI Gene [23428](https://www.ncbi.nlm.nih.gov/gene/23428):

> Enables protein heterodimerization activity and transmembrane transporter activity. Involved in L-alanine import across plasma membrane; L-leucine import across plasma membrane; and thyroid hormone transport. Located in basolateral plasma membrane and microvillus membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11066) · Entrez [23428](https://www.ncbi.nlm.nih.gov/gene/23428) · UniProt [Q9UHI5](https://www.uniprot.org/uniprotkb/Q9UHI5) · Ensembl [ENSG00000092068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092068)

## Data

Gene col 1686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1686); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1686]; `tensor/DDL_lfc|DDL_z.npy` [1686]; `embed/gene_vectors.npy` [1686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1686 or target_col == 1686). Every well: [[SLC7A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
