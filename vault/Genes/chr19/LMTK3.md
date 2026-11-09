---
symbol: "LMTK3"
type: "gene"
col: 6612
ensembl_id: "ENSG00000142235"
name: "lemur tail kinase 3"
location: "19q13.33"
module: 161
arm: "+"
pooled_cpm: 10.21
n_lines_expressing: 35
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 42
direction_downstream: 38
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# LMTK3

*lemur tail kinase 3* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.37× (z +20.2, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.510× (z -9.2, q 2e-17, down in 22 of 30 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM92]] (+0.76, fdr 1e-05), [[FCHO1]] (+0.72, fdr 1e-05), [[TNNI3]] (+0.70, fdr 2e-05); moves opposite to [[UBTF]] (-0.65, fdr 2e-05), [[ZNF689]] (-0.64, fdr 6e-05), [[KLHL42]] (-0.63, fdr 1e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[CBLC]] → it (grade B ⚠); 38 go from it, the strongest it → [[MARVELD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.37×** | +20.2 | 0e+00 | 31/32 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.12×** | +19.4 | 0e+00 | 31/32 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.66×** | +17.7 | 0e+00 | 30/32 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +15.8 | 0e+00 | 29/32 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.56×** | +12.9 | 6e-36 | 30/32 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +12.2 | 2e-32 | 9/15 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +11.8 | 5e-30 | 10/24 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +10.3 | 4e-23 | 25/32 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +7.9 | 2e-13 | 22/30 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +4.8 | 9e-05 | 16/32 (KATO III, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +4.7 | 1e-04 | 4/19 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.024 | 5/32 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.062 | 5/32 (BT-474, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.0 | 0.096 | 5/32 (LS 180, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.510×** | -9.2 | 2e-17 | 22/30 (LS 180, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.550×** | -8.1 | 1e-13 | 22/32 (A549, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -7.4 | 2e-11 | 20/32 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -7.2 | 7e-11 | 20/32 (KATO III, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.621×** | -6.5 | 1e-08 | 22/32 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -6.4 | 2e-08 | 19/32 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.741×** | -5.8 | 6e-07 | 22/30 (CFPAC-1, HT-29, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -5.3 | 8e-06 | 14/32 (A549, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.716×** | -4.5 | 4e-04 | 14/32 (NCI-H23, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.006 | 13/33 (CFPAC-1, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.7 | 0.012 | 9/32 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.774×** | -3.5 | 0.024 | 7/32 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.055 | 16/29 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.070 | 5/32 (NCI-H23, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 28.7 | 5 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.76× (z +14.3) | [[Harringtonine (drug)]] 5 µM 0.101× (z -16.5) |
| [[A549 (line)]] | wt | 18.2 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.130× (z -11.6) |
| [[LS 180 (line)]] | wt | 23.1 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.47× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -13.1) |
| [[HT-29 (line)]] | alt | 27.3 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.28× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -11.0) |
| [[PANC-1 (line)]] | alt | 9.16 | 5 | 0 | [[Belinostat (drug)]] 5 µM 3.98× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -17.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 23.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.03× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -12.7) |
| [[SW480 (line)]] | alt | 13.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.32× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 31.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -9.4) |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0603× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -9.2) |
| [[SHP-77 (line)]] | alt | 6.91 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0600× (z -9.3) |
| [[A-172 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM92]] | +0.76 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.72 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.70 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[SHF]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.69 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[FA2H]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.68 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CFD]] | +0.66 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NCMAP]] | +0.65 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CCDC88B]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.64 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[RASAL1]] | +0.64 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBTF]] | -0.65 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZNF689]] | -0.64 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[KLHL42]] | -0.63 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[RPAP2]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[LATS1]] | -0.61 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ANGEL2]] | -0.61 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[RNF146]] | -0.61 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SPRY3]] | -0.60 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[ZMYND11]] | -0.60 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PPP1R8]] | -0.59 | -0.50 / -0.45 | both halves | 3e-05 | same gene group |
| [[FAIM]] | -0.59 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[MCCC2]] | -0.59 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 35, C 7. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBLC]] | B | CBLC activity raises LMTK3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without CBLC | 4e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[PTAFR]] | B | PTAFR activity raises LMTK3's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without PTAFR | 8e-04 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[CDH1]] | B | CDH1 activity raises LMTK3's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.41× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[PRSS8]] | B | PRSS8 activity raises LMTK3's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.51× lower at baseline in the lines without PRSS8 | 0.002 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[S100A14]] | B | S100A14 activity raises LMTK3's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 3.18× lower at baseline in the lines without S100A14 | 0.003 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[TESC]] | B | TESC activity raises LMTK3's level | lines that do not express TESC (23) vs lines expressing it (27) | 2.95× lower at baseline in the lines without TESC | 0.005 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[ENPP5]] | B | ENPP5 activity raises LMTK3's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without ENPP5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[JUP]] | B | JUP activity raises LMTK3's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without JUP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[EPHA1]] | B | EPHA1 activity raises LMTK3's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without EPHA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[P2RY2]] | B | P2RY2 activity raises LMTK3's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 2.66× lower at baseline in the lines without P2RY2 | 0.007 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[IRF6]] | B | IRF6 activity raises LMTK3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without IRF6 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[VAV1]] | B | VAV1 activity raises LMTK3's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without VAV1 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 32, C 6. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARVELD2]] | B | LMTK3 activity raises MARVELD2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.86× lower at baseline in the lines without LMTK3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[CDH1]] | B | LMTK3 activity raises CDH1's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 5.96× lower at baseline in the lines without LMTK3 | 0.006 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[LLGL2]] | B | LMTK3 activity raises LLGL2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.33× lower at baseline in the lines without LMTK3 | 0.007 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[ACOT11]] | B | LMTK3 activity raises ACOT11's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without LMTK3 | 0.011 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[CBLC]] | B | LMTK3 activity raises CBLC's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without LMTK3 | 0.014 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[CAPN12]] | B | LMTK3 activity raises CAPN12's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.66× lower at baseline in the lines without LMTK3 | 0.018 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[F11R]] | B | LMTK3 activity raises F11R's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.81× lower at baseline in the lines without LMTK3 | 0.022 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[JUP]] | B | LMTK3 activity raises JUP's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.05× lower at baseline in the lines without LMTK3 | 0.023 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[MLXIPL]] | B | LMTK3 activity raises MLXIPL's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without LMTK3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[ATP2C2]] | B | LMTK3 activity raises ATP2C2's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without LMTK3 | 0.027 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[S100A14]] | B | LMTK3 activity raises S100A14's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.30× lower at baseline in the lines without LMTK3 | 0.029 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[AHDC1]] | B | LMTK3 activity raises AHDC1's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.29× lower at baseline in the lines without LMTK3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.0, 1.7); signed map (-21.5, 29.1). **Vector** length 86.9, 22.3% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +19.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +20.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | lemur tail kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,485,271-48,513,935 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1883, LMR3, AATYK3, TYKLM3, PPP1R101 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Lemur tail kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q04](https://www.uniprot.org/uniprotkb/Q96Q04) (Serine/threonine-protein kinase LMTK3):

> Protein kinase which phosphorylates ESR1 (in vitro) and protects it against proteasomal degradation. May also regulate ESR1 levels indirectly via a PKC-AKT-FOXO3 pathway where it decreases the activity of PKC and the phosphorylation of AKT, thereby increasing binding of transcriptional activator FOXO3 to the ESR1 promoter and increasing ESR1 transcription. Involved in endocytic trafficking of N-methyl-D-aspartate receptors (NMDAR) in neurons (By similarity).

**Summary**, from NCBI Gene [114783](https://www.ncbi.nlm.nih.gov/gene/114783):

> Predicted to enable protein kinase activity. Predicted to be located in Golgi membrane; axon; and dendrite. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19295) · Entrez [114783](https://www.ncbi.nlm.nih.gov/gene/114783) · UniProt [Q96Q04](https://www.uniprot.org/uniprotkb/Q96Q04) · Ensembl [ENSG00000142235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142235)

## Data

Gene col 6612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6612); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6612]; `tensor/DDL_lfc|DDL_z.npy` [6612]; `embed/gene_vectors.npy` [6612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6612 or target_col == 6612). Every well: [[LMTK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMTK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
