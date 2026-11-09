---
symbol: "TRABD"
type: "gene"
col: 9991
ensembl_id: "ENSG00000170638"
name: "TraB domain containing"
location: "22q13.33"
module: 2
arm: "+"
pooled_cpm: 13.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TRABD

*TraB domain containing* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +9.7, q 2e-19, up in 15 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.64× (z +3.7, q 0.014, up in 9 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.17×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.19×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.351× (z -21.0, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC8]] (+0.75, fdr 7e-06), [[ST6GALNAC6]] (+0.75, fdr 7e-06), [[ST6GALNAC4]] (+0.75, fdr 1e-05); moves opposite to [[PCNX4-DT]] (-0.65, fdr 1e-04), [[ZNF764]] (-0.65, fdr 5e-05), [[PDCL3P4]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9991.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.17×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.19×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +9.7 | 2e-19 | 15/23 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.5 | 2e-11 | 25/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.3 | 2e-05 | 13/30 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.0 | 7e-05 | 18/39 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.6 | 4e-04 | 17/41 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.1 | 0.005 | 19/41 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.7 | 0.014 | 11/47 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.014 | 9/43 (COLO 205, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.026 | 9/44 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.3 | 0.051 | 6/46 (C32, NCI-H1573, …) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.2 | 0.079 | 5/29 (CFPAC-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.49× | +3.0 | 0.12 | 0/46 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.351×** | -21.0 | 0e+00 | 39/46 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.440×** | -11.2 | 1e-26 | 36/46 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.456×** | -11.2 | 1e-26 | 31/43 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -10.9 | 2e-25 | 30/42 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.307×** | -6.9 | 8e-10 | 26/46 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -4.9 | 9e-05 | 19/44 (LoVo, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.745×** | -4.2 | 0.002 | 18/47 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.023 | 5/48 (SHP-77, SNU-423, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.780×** | -3.2 | 0.092 | 4/46 (BT-474, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -3.1 | 0.095 | 17/48 (SNU-423, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.095 | 8/45 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -20.1) |
| [[KATO III (line)]] | alt | 21.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -13.7) |
| [[A498 (line)]] | wt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.8) |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.7) |
| [[LoVo (line)]] | wt | 13.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0668× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 9.82 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.3) |
| [[SW480 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.3) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0711× (z -13.6) |
| [[A549 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.0) |
| [[BT-474 (line)]] | alt | 8.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.8) |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -8.6) |
| [[C32 (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0714× (z -12.0) |
| [[H4 (line)]] | wt | 10.2 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0813× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 7.73 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0704× (z -8.8) |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -17.9) |
| [[J82 (line)]] | alt | 9.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -8.6) |
| [[LS 180 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.1) |
| [[SNU-423 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.101× (z -8.5) ⚠ toxic; unreliable plate only |
| [[SW1417 (line)]] | alt | 9.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.0) |
| [[SW48 (line)]] | wt | 30.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -8.8) |
| [[A-172 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC8]] | +0.75 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ST6GALNAC6]] | +0.75 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ST6GALNAC4]] | +0.75 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[PACC1]] | +0.73 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[BRF1]] | +0.72 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.72 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[FAM118A]] | +0.72 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.71 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ERCC2]] | +0.71 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.70 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TCF3]] | +0.69 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.69 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | -0.65 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[ZNF764]] | -0.65 | -0.67 / -0.39 | both halves | 5e-05 |  |
| [[PDCL3P4]] | -0.64 | -0.67 / -0.36 | both halves | 1e-04 |  |
| [[ZMAT2]] | -0.64 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[ZNF341-AS1]] | -0.64 | -0.65 / -0.27 | both halves | 3e-04 |  |
| [[FAM200A]] | -0.64 | -0.70 / -0.30 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.64 | -0.68 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[THAP9]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.63 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[DZIP3]] | -0.63 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD26]] | -0.63 | -0.71 / -0.36 | both halves | 1e-04 |  |
| [[METTL18]] | -0.62 | -0.68 / -0.37 | both halves | 7e-05 |  |
| [[PPP2R3C]] | -0.62 | -0.63 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNG1]] | B | KCNG1 activity lowers TRABD's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 1.48× higher at baseline in the lines without KCNG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.6, -25.4); signed map (-42.5, -9.2). **Vector** length 75.5, 15.0% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.4 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -21.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -10.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | TraB domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,185,913-50,199,598 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP2447 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4I3](https://www.uniprot.org/uniprotkb/Q9H4I3) (TraB domain-containing protein):

> Along with MFN2, MIGA2 and PLD6 promotes mitochondrial clustering and fusion. May play a role in mitochondrial import of proteins, such as that of SLC25A19.

**Summary**, from NCBI Gene [80305](https://www.ncbi.nlm.nih.gov/gene/80305):

> Enables mitochondrion-mitochondrion outer membrane tether activity. Involved in mitochondrial fusion and protein localization to mitochondrion. Located in mitochondrion. Part of TOM complex. Is active in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28805) · Entrez [80305](https://www.ncbi.nlm.nih.gov/gene/80305) · UniProt [Q9H4I3](https://www.uniprot.org/uniprotkb/Q9H4I3) · Ensembl [ENSG00000170638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170638)

## Data

Gene col 9991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9991); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9991]; `tensor/DDL_lfc|DDL_z.npy` [9991]; `embed/gene_vectors.npy` [9991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9991 or target_col == 9991). Every well: [[TRABD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRABD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
