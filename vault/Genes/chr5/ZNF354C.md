---
symbol: "ZNF354C"
type: "gene"
col: 10877
ensembl_id: "ENSG00000177932"
name: "zinc finger protein 354C"
location: "5q35.3"
module: 16
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 27
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF354C

*zinc finger protein 354C* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.58× (z +6.8, q 4e-09, up in 15 of 25 measured lines) ⚠ cell-cycle shift, explains ~43% of this change.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.270× (z -13.9, q 2e-41, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF287]] (+0.62, fdr 1e-05), [[ZNF813]] (+0.61, fdr 1e-05), [[TSPYL5]] (+0.60, fdr 1e-05); moves opposite to [[PPP1R15B-AS1]] (-0.54, fdr 3e-05), [[BCL2L14]] (-0.50, fdr 4e-05), [[DENND4A]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF559]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.58×** | +6.8 | 4e-09 | 15/25 (SW 900, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.37× | +3.4 | 0.20 | 7/24 (SW 900, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.50 | 6/24 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.270×** | -13.9 | 2e-41 | 21/25 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.420×** | -13.1 | 2e-36 | 21/22 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.525×** | -9.7 | 6e-20 | 18/24 (SK-MEL-2, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.435×** | -8.9 | 1e-16 | 20/24 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.429×** | -8.7 | 5e-16 | 17/22 (SW 900, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.454×** | -8.4 | 4e-15 | 13/24 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.458×** | -8.0 | 1e-13 | 19/22 (AN3 CA, SW 900, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.571×** | -6.0 | 2e-07 | 18/24 (NCI-H23, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.588×** | -5.4 | 3e-06 | 13/20 (SW 1271, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.648×** | -4.4 | 5e-04 | 12/25 (NCI-H460, NCI-H23, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -4.3 | 0.001 | 10/25 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.695×** | -3.9 | 0.005 | 6/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.507×** | -3.8 | 0.006 | 10/23 (HOP62, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.507×** | -3.8 | 0.006 | 8/24 (AN3 CA, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.520×** | -3.6 | 0.010 | 9/23 (hTERT-HPNE, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.735×** | -3.3 | 0.036 | 6/24 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 27.3 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -19.4) |
| [[NCI-H23 (line)]] | alt | 8.19 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0550× (z -12.4) |
| [[HOP62 (line)]] | alt | 6.85 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.131× (z -10.2) |
| [[J82 (line)]] | alt | 22.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0657× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 7.54 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0765× (z -9.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0761× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0753× (z -23.2) |
| [[C32 (line)]] | wt | 12.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -11.2) |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0514× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 9.97 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -14.5) |
| [[PANC-1 (line)]] | alt | 5.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 9.52 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -11.2) |
| [[A-172 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.966 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.403 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF287]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[ZNF813]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 | same gene group |
| [[TSPYL5]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZNF677]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZSCAN23]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 | same gene group |
| [[ZC4H2]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[MOCS1]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZNF790-AS1]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[ZNF229]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |
| [[CHST10]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ZNF232]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 | same gene group |
| [[SAAL1]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R15B-AS1]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[BCL2L14]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[DENND4A]] | -0.48 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DLEU7]] | -0.48 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[ERO1B]] | -0.46 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[KLF3-AS1]] | -0.45 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CD9]] | -0.45 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[KCNQ1]] | -0.45 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[TOM1L2]] | -0.45 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[NFKBID]] | -0.44 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZNF354C's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF439]] | B | ZNF439 activity raises ZNF354C's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without ZNF439 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[CPQ]] | B | CPQ activity raises ZNF354C's level | lines that do not express CPQ (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without CPQ | 0.090 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[EHD3]] | C | EHD3 activity raises ZNF354C's level | lines that do not express EHD3 (14) vs lines expressing it (36) | 3.46× lower at baseline in the lines without EHD3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MAP9, EVC, AKR1B1; co-absent with the target |
| [[WIPF1]] | C | WIPF1 activity raises ZNF354C's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without WIPF1 | 0.071 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF559]] | B | ZNF354C activity raises ZNF559's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without ZNF354C | 0.056 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[ZNF439]] | B | ZNF354C activity raises ZNF439's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 2.56× lower at baseline in the lines without ZNF354C | 0.067 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[CPQ]] | B | ZNF354C activity raises CPQ's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without ZNF354C | 0.067 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[PCDHGA2]] | B | ZNF354C activity raises PCDHGA2's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 2.27× lower at baseline in the lines without ZNF354C | 0.085 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[ZNF177]] | B | ZNF354C activity raises ZNF177's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without ZNF354C | 0.093 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN |
| [[ZNF790-AS1]] | C | ZNF354C activity raises ZNF790-AS1's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 3.62× lower at baseline in the lines without ZNF354C | 0.036 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |
| [[WIPF1]] | C | ZNF354C activity raises WIPF1's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 4.08× lower at baseline in the lines without ZNF354C | 0.039 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |
| [[MICU3]] | C | ZNF354C activity raises MICU3's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 4.59× lower at baseline in the lines without ZNF354C | 0.049 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |
| [[ZFP82]] | C | ZNF354C activity raises ZFP82's level | lines that do not express ZNF354C (23) vs lines expressing it (27) | 4.67× lower at baseline in the lines without ZNF354C | 0.095 | ⚠ within organs, on part of the lines; also absent: CPEB1, MPDZ, NALCN; co-absent with the target |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.4, 22.3); signed map (-5.3, -31.7). **Vector** length 53.0, 11.4% of its response variance represented; |z| ≥ 3 in 559 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.5 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +0.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.0 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -13.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -0.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 354C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,060,373-179,083,977 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KID3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y25](https://www.uniprot.org/uniprotkb/Q86Y25) (Zinc finger protein 354C):

> Transcriptional repressor that inhibits endothelial angiogenic sprouting. Suppresses osteogenic effects of RUNX2 and may be involved in osteoblastic differentiation (By similarity). Plays a role in postnatal myogenesis, may be involved in the regulation of satellite cells self-renewal (By similarity).

**Summary**, from NCBI Gene [30832](https://www.ncbi.nlm.nih.gov/gene/30832):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific. Involved in negative regulation of sprouting angiogenesis. Located in cytoplasm; nuclear membrane; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16736) · Entrez [30832](https://www.ncbi.nlm.nih.gov/gene/30832) · UniProt [Q86Y25](https://www.uniprot.org/uniprotkb/Q86Y25) · Ensembl [ENSG00000177932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177932)

## Data

Gene col 10877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10877); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10877]; `tensor/DDL_lfc|DDL_z.npy` [10877]; `embed/gene_vectors.npy` [10877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10877 or target_col == 10877). Every well: [[ZNF354C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF354C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
