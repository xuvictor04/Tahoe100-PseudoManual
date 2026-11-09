---
symbol: "ANKRD20A9P"
type: "gene"
col: 13037
ensembl_id: "ENSG00000206192"
name: "ankyrin repeat domain 20 family member A9, pseudogene"
location: "13q11"
module: 177
arm: "+"
pooled_cpm: 5.11
n_lines_expressing: 10
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# ANKRD20A9P

*ankyrin repeat domain 20 family member A9, pseudogene* — 13q11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.10× (z +14.3, q 9e-44, up in 8 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Lucanthone (drug)]] 0.05 µM: 0.570× (z -3.8, q 0.094, down in 1 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.228×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.273×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.136×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00408]] (+0.73, fdr 7e-06, ⚠ same locus), [[MT1G]] (+0.60, fdr 3e-05), [[DHRS2]] (+0.59, fdr 1e-05), [[PHF2P2]] (+0.58, fdr 2e-05); moves opposite to [[RBBP4]] (-0.54, fdr 1e-04), [[DIDO1]] (-0.54, fdr 7e-05), [[RPUSD4]] (-0.52, fdr 4e-05).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKRD20A8P]] → it (grade C ⚠); 7 go from it, the strongest it → [[RPUSD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.10×** | +14.3 | 9e-44 | 8/8 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.59×** | +10.9 | 2e-25 | 0/5 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +9.7 | 4e-20 | 0/3 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.09×** | +9.4 | 1e-18 | 0/4 | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +8.7 | 3e-16 | 3/8 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.22×** | +8.1 | 6e-14 | 5/8 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.67×** | +7.1 | 1e-10 | 6/8 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +6.3 | 2e-08 | 7/8 (H4, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +5.9 | 2e-07 | 7/8 (H4, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +5.7 | 7e-07 | 2/8 (RKO, NCI-H23) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +5.7 | 7e-07 | 6/8 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.70×** | +5.1 | 2e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +4.3 | 8e-04 | 5/8 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.2 | 1e-03 | 0/6 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.002 | 5/8 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.81×** | +3.9 | 0.003 | 1/8 (H4) | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.08×** | +3.8 | 0.005 | 1/7 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +3.6 | 0.008 | 5/8 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.66×** | +3.6 | 0.008 | 1/8 (RKO) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.011 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13037.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.228×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 0.273×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | **0.570×** | -3.8 | 0.094 | 1/8 (KATO III) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.600× | -3.4 | 0.18 | 0/8 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 55.6 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.7) | [[Auranofin (drug)]] 5 µM 0.228× (z -10.8) |
| [[H4 (line)]] | wt | 124 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.0) | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -8.9) |
| [[SW480 (line)]] | alt | 1.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +9.0) | — |
| [[A-172 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.644 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.758 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00408]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | ⚠ same locus (33.5 kb: neighbours can correlate without regulation) |
| [[MT1G]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[DHRS2]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PHF2P2]] | +0.58 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[LENG1]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD20A8P]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[AACSP1]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TMEM132D]] | +0.52 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[EMC9]] | +0.52 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[SNAPIN]] | +0.52 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[IRF2BP2]] | +0.51 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[POTEF]] | +0.51 | +0.38 / +0.39 | both halves | 6e-05 |  |
| [[CREB3]] | +0.50 | +0.47 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP4]] | -0.54 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[DIDO1]] | -0.54 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[RPUSD4]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NAXD]] | -0.52 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SAP30L-AS1]] | -0.51 | -0.19 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[MCM9]] | -0.51 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[UBE2V1]] | -0.50 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[TMEM248]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MED28]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PEX26]] | -0.49 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[LAMTOR5-AS1]] | -0.49 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[PPP2R1B]] | -0.49 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SENP3]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A8P]] | C | ANKRD20A8P activity raises ANKRD20A9P's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 4.01× lower at baseline in the lines without ANKRD20A8P | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[LINC00408]] | C | LINC00408 activity raises ANKRD20A9P's level | lines that do not express LINC00408 (38) vs lines expressing it (12) | 3.97× lower at baseline in the lines without LINC00408 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000287861, ANKRD20A9P, PHF2P2; co-absent with the target |
| [[PHF2P2]] | C | PHF2P2 activity raises ANKRD20A9P's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.63× lower at baseline in the lines without PHF2P2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPUSD4]] | B | ANKRD20A9P activity raises RPUSD4's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 1.32× lower at baseline in the lines without ANKRD20A9P | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408 |
| [[NBPF14]] | B | ANKRD20A9P activity weakens NBPF14's drug response | lines that do not express ANKRD20A9P (38) vs lines expressing it (9) | the lines without ANKRD20A9P respond 1.40× as strongly (z diff -1.44); rises at some drug-doses, falls at others (29% from rises): Dinaciclib 5 µM: 0.28x vs 0.62x (z diff -6.2); Dinaciclib 0.5 µM: 0.30x vs 0.78x (z diff -5.7); Homoharringtonine 0.5 µM: 1.58x vs 1.28x (z diff -1.5) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[LINC00408]] | C | ANKRD20A9P activity raises LINC00408's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 4.31× lower at baseline in the lines without ANKRD20A9P | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |
| [[PHF2P2]] | C | ANKRD20A9P activity raises PHF2P2's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 5.96× lower at baseline in the lines without ANKRD20A9P | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |
| [[AACSP1]] | C | ANKRD20A9P activity raises AACSP1's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without ANKRD20A9P | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |
| [[ANKRD20A8P]] | C | ANKRD20A9P activity raises ANKRD20A8P's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 3.86× lower at baseline in the lines without ANKRD20A9P | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |
| [[PASD1]] | C | ANKRD20A9P activity raises PASD1's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 1.81× lower at baseline in the lines without ANKRD20A9P | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.0, 24.3); signed map (33.3, 36.0). **Vector** length 21.3, 5.18% of its response variance represented; |z| ≥ 3 in 173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.6 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.5 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.5 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -0.8 | +2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -3.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.5 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.4 | -1.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.4 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A9, pseudogene |
| Locus type | pseudogene |
| Location | 13q11 — chr13:18,816,718-18,871,967 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42023) · Entrez [284232](https://www.ncbi.nlm.nih.gov/gene/284232) · Ensembl [ENSG00000206192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206192)

## Data

Gene col 13037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13037); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13037]; `tensor/DDL_lfc|DDL_z.npy` [13037]; `embed/gene_vectors.npy` [13037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13037 or target_col == 13037). Every well: [[ANKRD20A9P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A9P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
