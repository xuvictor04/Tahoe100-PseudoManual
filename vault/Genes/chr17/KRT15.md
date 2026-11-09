---
symbol: "KRT15"
type: "gene"
col: 10095
ensembl_id: "ENSG00000171346"
name: "keratin 15"
location: "17q21.2"
module: 34
arm: "+"
pooled_cpm: 11.43
n_lines_expressing: 35
n_dd_up: 2
n_dd_down: 56
n_dd_up_clean: 2
n_dd_down_clean: 52
in_vector_space: true
direction_upstream: 39
direction_downstream: 36
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# KRT15

*keratin 15* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.78× (z +8.4, q 3e-14, up in 25 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.298× (z -17.3, q 0e+00, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD1]] (+0.69, fdr 1e-05), [[PLAUR]] (+0.67, fdr 7e-06), [[ITGA2]] (+0.67, fdr 7e-06); moves opposite to [[GAS2]] (-0.57, fdr 4e-05), [[ARID1B]] (-0.55, fdr 5e-05), [[RNF146]] (-0.55, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[LEMD1]] → it (grade B ⚠); 36 go from it, the strongest it → [[ITGA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +8.4 | 3e-14 | 25/32 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.7 | 3e-06 | 20/31 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.45 | 6/32 (SW480, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.298×** | -17.3 | 0e+00 | 27/32 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.347×** | -15.1 | 0e+00 | 27/32 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -12.9 | 1e-35 | 26/32 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.337×** | -11.0 | 5e-26 | 27/31 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.340×** | -10.5 | 1e-23 | 25/32 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.368×** | -10.1 | 5e-22 | 29/32 (SW48, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.370×** | -10.1 | 7e-22 | 20/31 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.356×** | -10.0 | 7e-22 | 23/31 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.412×** | -8.9 | 2e-17 | 25/31 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.460×** | -7.8 | 3e-13 | 22/32 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.581×** | -7.7 | 6e-13 | 22/32 (NCI-H1573, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.469×** | -7.6 | 1e-12 | 24/31 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.483×** | -7.3 | 9e-12 | 25/32 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.509×** | -6.8 | 4e-10 | 25/32 (SK-MEL-2, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.492×** | -6.6 | 2e-09 | 20/32 (SK-MEL-2, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -6.3 | 7e-09 | 20/31 (MIA PaCa-2, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 18.1 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 7 | — | [[Trametinib (drug)]] 0.5 µM 0.153× (z -13.2) |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0804× (z -17.7) |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 30.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.6) |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 37.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -14.6) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.5) |
| [[A549 (line)]] | wt | 6.40 | 0 | 3 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0422× (z -10.4) |
| [[H4 (line)]] | wt | 8.76 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0296× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 6.24 | 0 | 3 | — | [[Erythromycin (drug)]] 0.5 µM 0.0718× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -17.4) |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.7) |
| [[SW48 (line)]] | wt | 18.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0267× (z -10.1) |
| [[SW480 (line)]] | alt | 14.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.4) |
| [[A498 (line)]] | wt | 18.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.9) |
| [[LoVo (line)]] | wt | 7.59 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0573× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.6) |
| [[PANC-1 (line)]] | alt | 8.90 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 6.79 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0797× (z -10.5) |
| [[KATO III (line)]] | alt | 15.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 3.06 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0383× (z -9.5) |
| [[LS 180 (line)]] | wt | 5.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.89 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD1]] | +0.69 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.67 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GDPD5]] | +0.67 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SHB]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PPARD]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ITGA6]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 | STRING 519 |
| [[SERPINB1]] | +0.63 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[RAC2]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PTGS1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS2]] | -0.57 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ARID1B]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RNF146]] | -0.55 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 33, C 6. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEMD1]] | B | LEMD1 activity raises KRT15's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 3.03× lower at baseline in the lines without LEMD1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[AREG]] | B | AREG activity raises KRT15's level | lines that do not express AREG (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without AREG | 0.008 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |
| [[PDGFB]] | B | PDGFB activity raises KRT15's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.87× lower at baseline in the lines without PDGFB | 0.009 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[SEMA3B]] | B | SEMA3B activity raises KRT15's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.15× lower at baseline in the lines without SEMA3B | 0.014 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[SULT2B1]] | B | SULT2B1 activity raises KRT15's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without SULT2B1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity raises KRT15's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.26× lower at baseline in the lines without ITGA3 | 0.020 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises KRT15's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 3.00× lower at baseline in the lines without SLCO4A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[KRT19]] | B | KRT19 activity raises KRT15's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without KRT19 | 0.026 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[CARD11]] | B | CARD11 activity raises KRT15's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.16× lower at baseline in the lines without CARD11 | 0.030 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[PRAG1]] | B | PRAG1 activity raises KRT15's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without PRAG1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[CELSR1]] | B | CELSR1 activity raises KRT15's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.12× lower at baseline in the lines without CELSR1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[ANO1]] | B | ANO1 activity raises KRT15's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.28× lower at baseline in the lines without ANO1 | 0.044 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 31, C 5. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA6]] | B | KRT15 activity raises ITGA6's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.84× lower at baseline in the lines without KRT15 | 0.003 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[EPHA2]] | B | KRT15 activity raises EPHA2's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without KRT15 | 0.004 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[KRT19]] | B | KRT15 activity raises KRT19's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 4.92× lower at baseline in the lines without KRT15 | 0.008 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[SLCO4A1]] | B | KRT15 activity raises SLCO4A1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.59× lower at baseline in the lines without KRT15 | 0.012 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[MYEOV]] | B | KRT15 activity raises MYEOV's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.91× lower at baseline in the lines without KRT15 | 0.014 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[PLEK2]] | B | KRT15 activity raises PLEK2's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 3.06× lower at baseline in the lines without KRT15 | 0.014 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[LINC00887]] | B | KRT15 activity raises LINC00887's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without KRT15 | 0.015 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[TMC6]] | B | KRT15 activity raises TMC6's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without KRT15 | 0.016 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[C3orf52]] | B | KRT15 activity raises C3orf52's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without KRT15 | 0.042 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[PTK6]] | B | KRT15 activity raises PTK6's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without KRT15 | 0.044 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[SULT2B1]] | B | KRT15 activity raises SULT2B1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without KRT15 | 0.048 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[SEMA4B]] | B | KRT15 activity raises SEMA4B's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without KRT15 | 0.053 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.9, 0.1); signed map (-0.8, 45.7). **Vector** length 92.8, 24.0% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | -10.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +3.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.1 | -12.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.7 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | keratin 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,513,745-41,522,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | K15, CK15, K1CO |
| Gene groups (HGNC) | Keratins, type I; MicroRNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_DN, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P19012](https://www.uniprot.org/uniprotkb/P19012) (Keratin, type I cytoskeletal 15):

> Structural component of intermediate filaments in the epithelium. Forms heteropolymers with type II keratin KRT5, assembling into keratin intermediate filament network that promotes mechanical resilience of undifferentiated cells, including hair follicle bulge cells, foregut basal progenitors and intestinal crypt cells. Displays an antagonist role with KRT14 in basal epithelial cells, where KRT14 promotes cell differentiation while KRT15 maintains the progenitor state and promotes proliferation …

**Summary**, from NCBI Gene [3866](https://www.ncbi.nlm.nih.gov/gene/3866):

> The protein encoded by this gene is a member of the keratin gene family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. Most of the type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains and are clustered in a region on chromosome 17q21.2. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6421) · Entrez [3866](https://www.ncbi.nlm.nih.gov/gene/3866) · UniProt [P19012](https://www.uniprot.org/uniprotkb/P19012) · Ensembl [ENSG00000171346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171346)

## Data

Gene col 10095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10095); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10095]; `tensor/DDL_lfc|DDL_z.npy` [10095]; `embed/gene_vectors.npy` [10095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10095 or target_col == 10095). Every well: [[KRT15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
