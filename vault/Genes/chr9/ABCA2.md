---
symbol: "ABCA2"
type: "gene"
col: 2844
ensembl_id: "ENSG00000107331"
name: "ATP binding cassette subfamily A member 2"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 15.67
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ABCA2

*ATP binding cassette subfamily A member 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +6.0, q 1e-06, up in 17 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.52× (z +5.0, q 1e-04, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.293× (z -20.9, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL18A1]] (+0.79, fdr 7e-06), [[PIK3R2]] (+0.75, fdr 7e-06), [[INTS11]] (+0.73, fdr 7e-06); moves opposite to [[PBDC1]] (-0.68, fdr 1e-05), [[TRIP11]] (-0.65, fdr 1e-05), [[LINC02307]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.0 | 1e-06 | 17/29 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +5.0 | 1e-04 | 25/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +4.6 | 6e-04 | 21/36 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.007 | 19/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.049 | 8/47 (C32, LoVo, …) | rises with dose |  |
| [[Fusidic acid (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.087 | 11/47 (LoVo, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +3.3 | 0.093 | 14/31 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.30× | +3.1 | 0.14 | 7/46 (HT-29, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.293×** | -20.9 | 0e+00 | 39/46 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.286×** | -14.1 | 1e-42 | 38/44 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.343×** | -12.4 | 4e-33 | 38/45 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -6.4 | 2e-08 | 26/45 (HCT15, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -5.9 | 5e-07 | 25/44 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.628×** | -5.6 | 2e-06 | 31/46 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.567×** | -5.4 | 4e-06 | 29/45 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.641×** | -5.4 | 5e-06 | 27/46 (A549, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.674×** | -4.8 | 1e-04 | 22/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -4.2 | 0.001 | 22/46 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -4.2 | 0.001 | 16/39 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -3.9 | 0.004 | 17/46 (RPMI-7951, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -3.8 | 0.006 | 19/41 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.720×** | -3.8 | 0.007 | 12/46 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.724×** | -3.7 | 0.008 | 15/46 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **0.817×** | -3.5 | 0.016 | 18/47 (CHP-212, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.020 | 19/46 (RKO, SW480, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.026 | 18/42 (RPMI-7951, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -3.2 | 0.038 | 16/46 (LS 180, NCI-H23, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.5) |
| [[A549 (line)]] | wt | 20.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.2) |
| [[BT-474 (line)]] | alt | 7.96 | 0 | 3 | — | [[Artemether (drug)]] 0.5 µM 0.0543× (z -11.0) |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0851× (z -14.4) |
| [[J82 (line)]] | alt | 21.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -15.5) |
| [[LoVo (line)]] | wt | 25.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.6) |
| [[LS 180 (line)]] | wt | 39.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -20.6) |
| [[SW480 (line)]] | alt | 12.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.4) |
| [[C32 (line)]] | wt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -12.2) |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.3) |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 9.13 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0822× (z -15.6) |
| [[PANC-1 (line)]] | alt | 9.20 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -9.7) |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.2) |
| [[COLO 205 (line)]] | alt | 6.87 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.121× (z -9.3) |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.5) |
| [[KATO III (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 9.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.5) |
| [[RKO (line)]] | wt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -10.3) |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.3) |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.8) |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.1) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL18A1]] | +0.79 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.75 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[INTS11]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[SBF1]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NPDC1]] | +0.72 | +0.77 / +0.53 | both halves | 1e-05 | ⚠ same locus (10.5 kb, same strand: neighbours can correlate without regulation) |
| [[PLBD2]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PRKCSH]] | +0.70 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[INTS1]] | +0.69 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CEP131]] | +0.69 | +0.63 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.68 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.63 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[C14orf119]] | -0.62 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RPP38]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[EID2]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.60 | -0.67 / -0.58 | both halves | 8e-06 |  |
| [[RPP25L]] | -0.59 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.59 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[ZNF407-AS1]] | -0.59 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[RBBP6]] | -0.58 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAM]] | B | BCAM activity raises ABCA2's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without BCAM | 0.080 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[APLP1]] | B | APLP1 activity raises ABCA2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without APLP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[LAMA5]] | B | LAMA5 activity raises ABCA2's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without LAMA5 | 0.088 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.3, -23.0); signed map (-45.4, -10.9). **Vector** length 88.6, 18.9% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -14.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -20.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,007,234-137,028,915 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ABC2 |
| Gene groups (HGNC) | ATP binding cassette subfamily A |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, BILE_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: ABC transporters in lipid homeostasis; ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZC7](https://www.uniprot.org/uniprotkb/Q9BZC7) (ATP-binding cassette sub-family A member 2):

> Probable lipid transporter that modulates cholesterol sequestration in the late endosome/lysosome by regulating the intracellular sphingolipid metabolism, in turn participates in cholesterol homeostasis (Probable). May alter the transbilayer distribution of ceramide in the intraluminal membrane lipid bilayer, favoring its retention in the outer leaflet that results in increased acid ceramidase activity in the late endosome/lysosome, facilitating ceramide deacylation to sphingosine leading to …

**Summary**, from NCBI Gene [20](https://www.ncbi.nlm.nih.gov/gene/20):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. This protein is highly …

**Accessions** — [HGNC:32](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32) · Entrez [20](https://www.ncbi.nlm.nih.gov/gene/20) · UniProt [Q9BZC7](https://www.uniprot.org/uniprotkb/Q9BZC7) · Ensembl [ENSG00000107331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107331)

## Data

Gene col 2844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2844); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2844]; `tensor/DDL_lfc|DDL_z.npy` [2844]; `embed/gene_vectors.npy` [2844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2844 or target_col == 2844). Every well: [[ABCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
