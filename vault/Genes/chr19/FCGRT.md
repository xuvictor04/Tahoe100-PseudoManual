---
symbol: "FCGRT"
type: "gene"
col: 2511
ensembl_id: "ENSG00000104870"
name: "Fc gamma receptor and transporter"
location: "19q13.33"
module: 27
arm: "+"
pooled_cpm: 5.93
n_lines_expressing: 38
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 15
direction_downstream: 6
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# FCGRT

*Fc gamma receptor and transporter* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.65× (z +11.2, q 3e-26, up in 7 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.21× (z +4.9, q 7e-05, up in 11 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.474× (z -8.9, q 2e-16, down in 19 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEIL1]] (+0.65, fdr 1e-05), [[CES3]] (+0.59, fdr 3e-05), [[PRRT1]] (+0.57, fdr 3e-05); moves opposite to [[ABCC10]] (-0.51, fdr 4e-05), [[EEFSEC]] (-0.50, fdr 3e-05), [[ELOVL1]] (-0.47, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); 6 go from it, the strongest it → [[EPCAM-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +11.2 | 3e-26 | 7/11 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +8.2 | 6e-14 | 11/22 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.1 | 2e-10 | 8/14 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.1 | 6e-05 | 6/35 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +4.9 | 7e-05 | 11/32 (SW 900, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.9 | 7e-05 | 12/27 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.4 | 8e-04 | 12/31 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.002 | 14/35 (AsPC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.003 | 8/33 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.017 | 7/32 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.5 | 0.021 | 5/29 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.044 | 6/35 (PANC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.064 | 6/34 (HepG2/C3A, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2511.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.474×** | -8.9 | 2e-16 | 19/29 (SW 900, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.614×** | -5.8 | 1e-06 | 14/34 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.619×** | -5.7 | 2e-06 | 17/34 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -5.6 | 4e-06 | 13/34 (AN3 CA, SW480, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.668×** | -4.8 | 2e-04 | 13/34 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -4.7 | 3e-04 | 17/33 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -4.4 | 8e-04 | 10/34 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.737×** | -3.5 | 0.032 | 11/33 (COLO 205, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.752×** | -3.4 | 0.038 | 7/32 (MIA PaCa-2, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.753×** | -3.4 | 0.038 | 11/34 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.757×** | -3.3 | 0.043 | 9/33 (NCI-H1792, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.8) |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.271× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.0) | — |
| [[KATO III (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -8.5) |
| [[LoVo (line)]] | wt | 1.64 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 2.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.25× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0833× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -12.2) |
| [[SW 900 (line)]] | alt | 7.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0421× (z -12.6) |
| [[A-172 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEIL1]] | +0.65 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CES3]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PRRT1]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[NAPA-AS1]] | +0.56 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[P4HTM]] | +0.56 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[STK31]] | +0.56 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PDK4-AS1]] | +0.55 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[FXYD2]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[MUC1]] | +0.55 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[FAXDC2]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[HNF1A-AS1]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[NRL]] | +0.55 | +0.58 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC10]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[EEFSEC]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ELOVL1]] | -0.47 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[GNPNAT1]] | -0.46 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[KATNBL1]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises FCGRT's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without WFDC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[EPCAM-DT]] | B | EPCAM-DT activity raises FCGRT's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 2.99× lower at baseline in the lines without EPCAM-DT | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[TSPOAP1]] | B | TSPOAP1 activity raises FCGRT's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without TSPOAP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises FCGRT's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.34× lower at baseline in the lines without HNF1A-AS1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[C11orf52]] | B | C11orf52 activity raises FCGRT's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without C11orf52 | 0.028 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[VIL1]] | B | VIL1 activity raises FCGRT's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 2.64× lower at baseline in the lines without VIL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[PRRG2]] | B | PRRG2 activity raises FCGRT's level | lines that do not express PRRG2 (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without PRRG2 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SCNN1A]] | B | SCNN1A activity raises FCGRT's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.09× lower at baseline in the lines without SCNN1A | 0.049 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises FCGRT's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.17× lower at baseline in the lines without SPINT1-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[WFDC2]] | B | WFDC2 activity strengthens FCGRT's drug response | lines that do not express WFDC2 (25) vs lines expressing it (10) | the lines without WFDC2 respond 0.45× as strongly (z diff +1.37); strongest at Homoharringtonine 0.5 µM: 0.72x vs 0.22x (z diff +5.9) | 0.058 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; target measured in part of the lines; artifact flags |
| [[DPP4]] | B | DPP4 activity raises FCGRT's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without DPP4 | 0.071 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[LINC01091]] | B | LINC01091 activity raises FCGRT's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without LINC01091 | 0.072 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPCAM-DT]] | B | FCGRT activity raises EPCAM-DT's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without FCGRT | 0.009 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[VAMP8]] | B | FCGRT activity raises VAMP8's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without FCGRT | 0.059 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[SCNN1A]] | B | FCGRT activity raises SCNN1A's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 3.61× lower at baseline in the lines without FCGRT | 0.085 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[IST1]] | B | FCGRT activity raises IST1's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 1.16× lower at baseline in the lines without FCGRT | 0.086 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[SPINT1-AS1]] | B | FCGRT activity raises SPINT1-AS1's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without FCGRT | 0.092 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[DPP4]] | B | FCGRT activity raises DPP4's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without FCGRT | 0.094 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.2, 29.5); signed map (38.6, -14.3). **Vector** length 54.0, 8.90% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -5.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Fc gamma receptor and transporter |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,506,816-49,526,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FcgammaRn, FcRn |
| Gene groups (HGNC) | C1-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P55899](https://www.uniprot.org/uniprotkb/P55899) (IgG receptor FcRn large subunit p51):

> Cell surface receptor that transfers passive humoral immunity from the mother to the newborn. Binds to the Fc region of monomeric immunoglobulin gamma and mediates its selective uptake from milk. IgG in the milk is bound at the apical surface of the intestinal epithelium. The resultant FcRn-IgG complexes are transcytosed across the intestinal epithelium and IgG is released from FcRn into blood or tissue fluids. Throughout life, contributes to effective humoral immunity by recycling IgG and …

**Summary**, from NCBI Gene [2217](https://www.ncbi.nlm.nih.gov/gene/2217):

> This gene encodes a receptor that binds the Fc region of monomeric immunoglobulin G. The encoded protein transfers immunoglobulin G antibodies from mother to fetus across the placenta. This protein also binds immunoglobulin G to protect the antibody from degradation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:3621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3621) · Entrez [2217](https://www.ncbi.nlm.nih.gov/gene/2217) · UniProt [P55899](https://www.uniprot.org/uniprotkb/P55899) · Ensembl [ENSG00000104870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104870)

## Data

Gene col 2511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2511); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2511]; `tensor/DDL_lfc|DDL_z.npy` [2511]; `embed/gene_vectors.npy` [2511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2511 or target_col == 2511). Every well: [[FCGRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCGRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
