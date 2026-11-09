---
symbol: "AGPAT2"
type: "gene"
col: 9838
ensembl_id: "ENSG00000169692"
name: "1-acylglycerol-3-phosphate O-acyltransferase 2"
location: "9q34.3"
module: 192
arm: "+"
pooled_cpm: 25.41
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# AGPAT2

*1-acylglycerol-3-phosphate O-acyltransferase 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.54× (z +4.8, q 0.001, up in 25 of 41 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 4.12×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.452× (z -12.3, q 4e-32, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASSF7]] (+0.73, fdr 9e-06), [[PLA2G15]] (+0.68, fdr 2e-05), [[FA2H]] (+0.68, fdr 1e-05); moves opposite to [[FUBP1]] (-0.63, fdr 1e-04), [[MRRF]] (-0.59, fdr 2e-05), [[ENOSF1]] (-0.58, fdr 5e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SERPINB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9838.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 4.12×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.54×** | +4.8 | 0.001 | 25/41 (A-172, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.43×** | +3.9 | 0.024 | 21/38 (A498, NCI-H1792, …) | two highest doses | composition shift |
| [[Rosiglitazone (drug)]] 5 µM |  | 1.35× | +3.2 | 0.27 | 15/45 (LoVo, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.452×** | -12.3 | 4e-32 | 34/44 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -8.0 | 3e-13 | 30/44 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -6.9 | 1e-09 | 30/45 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -6.3 | 4e-08 | 31/46 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.291×** | -6.3 | 4e-08 | 35/46 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.335×** | -5.6 | 3e-06 | 34/43 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -4.7 | 2e-04 | 24/45 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.748×** | -4.5 | 5e-04 | 24/46 (Hs 766T, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.668×** | -4.4 | 6e-04 | 25/45 (LoVo, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -4.4 | 7e-04 | 24/45 (Hs 766T, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -3.6 | 0.016 | 23/44 (NCI-H2030, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.688×** | -3.6 | 0.018 | 21/45 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.726×** | -3.5 | 0.019 | 18/45 (Hs 766T, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -3.4 | 0.023 | 22/45 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.066 | 19/45 (A498, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.762×** | -3.0 | 0.099 | 19/45 (H4, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **0.763×** | -3.0 | 0.099 | 11/45 (SW 1271, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 43.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -21.0) |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.9) |
| [[Hs 766T (line)]] | wt | 46.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -9.3) |
| [[SW480 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.2) |
| [[A549 (line)]] | wt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 42.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.2) |
| [[HT-29 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.8) |
| [[J82 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.7) |
| [[LoVo (line)]] | wt | 42.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -8.6) |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 9.69 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.124× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0769× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.1) |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -10.7) |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.7) |
| [[A-427 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF7]] | +0.73 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[PLA2G15]] | +0.68 | +0.62 / +0.47 | both halves | 2e-05 | pathway: Glycerophospholipid biosynthesis |
| [[FA2H]] | +0.68 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CORO2A]] | +0.67 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CARD19]] | +0.64 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[DOK4]] | +0.64 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[FAM89B]] | +0.63 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TMEM92]] | +0.63 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[RTN2]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SNAPC2]] | +0.62 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LRRC8A]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[RRAS]] | +0.62 | +0.58 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.63 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[MRRF]] | -0.59 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[ENOSF1]] | -0.58 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[EWSR1]] | -0.58 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[MCCC2]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[TXNRD2]] | -0.57 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ECHDC1]] | -0.57 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[CC2D2A]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF280D]] | -0.56 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[QTRT1]] | -0.54 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[FZD6]] | -0.53 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RMDN2]] | -0.53 | -0.43 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB1]] | B | SERPINB1 activity raises AGPAT2's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without SERPINB1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[PTK6]] | B | PTK6 activity raises AGPAT2's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.92× lower at baseline in the lines without PTK6 | 0.046 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises AGPAT2's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without TINAGL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PCDH1]] | B | PCDH1 activity raises AGPAT2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without PCDH1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[FA2H]] | B | FA2H activity raises AGPAT2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 1.83× lower at baseline in the lines without FA2H | 0.065 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[IRF6]] | B | IRF6 activity raises AGPAT2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.09× lower at baseline in the lines without IRF6 | 0.073 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[SLC16A3]] | B | SLC16A3 activity raises AGPAT2's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without SLC16A3 | 0.084 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, 3.9); signed map (-14.1, 39.4). **Vector** length 74.6, 16.5% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.3 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -6.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.2 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | 1-acylglycerol-3-phosphate O-acyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,673,143-136,687,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPAAT-beta, LPLAT2; previously BSCL |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Lysophospholipid acyltransferases |
| Reactome | 11 pathways, smallest: Synthesis of PA; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes; Epigenetic regulation of gene expression by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15120](https://www.uniprot.org/uniprotkb/O15120) (1-acyl-sn-glycerol-3-phosphate acyltransferase beta):

> Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone.

**Summary**, from NCBI Gene [10555](https://www.ncbi.nlm.nih.gov/gene/10555):

> This gene encodes a member of the 1-acylglycerol-3-phosphate O-acyltransferase family. The protein is located within the endoplasmic reticulum membrane and converts lysophosphatidic acid to phosphatidic acid, the second step in de novo phospholipid biosynthesis. Mutations in this gene have been associated with congenital generalized lipodystrophy (CGL), or Berardinelli-Seip syndrome, a disease characterized by a near absence of adipose tissue and severe insulin resistance. Alternate …

**Accessions** — [HGNC:325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:325) · Entrez [10555](https://www.ncbi.nlm.nih.gov/gene/10555) · UniProt [O15120](https://www.uniprot.org/uniprotkb/O15120) · Ensembl [ENSG00000169692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169692)

## Data

Gene col 9838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9838); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9838]; `tensor/DDL_lfc|DDL_z.npy` [9838]; `embed/gene_vectors.npy` [9838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9838 or target_col == 9838). Every well: [[AGPAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGPAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
