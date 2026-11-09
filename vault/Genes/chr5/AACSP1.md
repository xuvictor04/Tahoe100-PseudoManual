---
symbol: "AACSP1"
type: "gene"
col: 14694
ensembl_id: "ENSG00000250420"
name: "acetoacetyl-CoA synthetase pseudogene 1"
location: "5q35.3"
module: 177
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 18
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# AACSP1

*acetoacetyl-CoA synthetase pseudogene 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.20× (z +16.8, q 0e+00, up in 6 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.105×, CHP-212 0.0887×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0953×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.169×; ⚠ toxic).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF2P2]] (+0.63, fdr 1e-05), [[ANKRD20A8P]] (+0.56, fdr 1e-05), [[DHRS2]] (+0.54, fdr 3e-05); moves opposite to [[SOS2]] (-0.49, fdr 3e-04), [[SAP30L-AS1]] (-0.48, fdr 0.001, ⚠ not reproduced), [[RAB22A]] (-0.48, fdr 5e-05), [[GHITM]] (-0.47, fdr 2e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PHF2P2]] → it (grade C ⚠); 4 go from it, the strongest it → [[PHF2P2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.20×** | +16.8 | 0e+00 | 6/9 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.36×** | +11.7 | 3e-29 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +9.5 | 3e-19 | 15/15 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.21×** | +8.9 | 6e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +8.9 | 6e-17 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.70×** | +8.2 | 2e-14 | 5/9 (HEC-1-A, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +7.5 | 6e-12 | 14/14 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.24×** | +6.4 | 1e-08 | 8/12 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.66×** | +5.8 | 5e-07 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.38×** | +5.3 | 8e-06 | 0/3 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +4.4 | 6e-04 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.001 | 1/10 (KATO III) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 2/13 (NCI-H1573, SNU-1) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +3.8 | 0.006 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.007 | 0/8 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.018 | 3/13 (CHP-212, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.020 | 8/15 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.77×** | +3.4 | 0.021 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.030 | 0/9 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.044 | 7/15 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.044 | 1/10 (HEC-1-A) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14694.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.105×, CHP-212 0.0887×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 0.0953×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.169×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.631× | -3.5 | 0.22 | 1/14 (SHP-77) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | 0.681× | -3.2 | 0.38 | 1/15 (SK-MEL-2) | two highest doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -9.2) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0887× (z -8.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0953× (z -12.2) |
| [[A-172 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.660 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.918 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.657 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.328 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF2P2]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD20A8P]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[DHRS2]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[FAM95A]] | +0.54 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD20A9P]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RRP9]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[THOP1]] | +0.51 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[FAR2P1]] | +0.50 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[POTEF]] | +0.49 | +0.29 / +0.45 | both halves | 2e-04 |  |
| [[HLF]] | +0.48 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[HSD17B10]] ⚠ | +0.48 | +0.35 / +0.38 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUBPL]] | +0.47 | +0.27 / +0.44 | both halves | 3e-04 |  |
| [[COQ2]] | +0.47 | +0.39 / +0.41 | both halves | 6e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOS2]] | -0.49 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[SAP30L-AS1]] | -0.48 | -0.17 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[RAB22A]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[GHITM]] | -0.47 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[CCNY-AS1]] | -0.45 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[HINT1]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[RNF11]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[GLUD1P3]] | -0.44 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[ZNF460-AS1]] | -0.44 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[TPTEP2-CSNK1E]] | -0.43 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[TM2D1]] | -0.43 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[GARS1-DT]] | -0.43 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[SANBR]] | -0.43 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ELMOD3]] | -0.43 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHF2P2]] | C | PHF2P2 activity raises AACSP1's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.41× lower at baseline in the lines without PHF2P2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises AACSP1's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.10× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC01518]] | C | LINC01518 activity raises AACSP1's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without LINC01518 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[BAGE2]] | C | BAGE2 activity raises AACSP1's level | lines that do not express BAGE2 (36) vs lines expressing it (14) | 2.09× lower at baseline in the lines without BAGE2 | 0.038 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TPTE, ENSG00000260289, LINC01029; co-absent with the target |
| [[ANKRD20A9P]] | C | ANKRD20A9P activity raises AACSP1's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without ANKRD20A9P | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHF2P2]] | C | AACSP1 activity raises PHF2P2's level | lines that do not express AACSP1 (32) vs lines expressing it (18) | 4.06× lower at baseline in the lines without AACSP1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00408, ENSG00000277757, NAA11; co-absent with the target |
| [[POTEF]] | C | AACSP1 activity raises POTEF's level | lines that do not express AACSP1 (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without AACSP1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00408, ENSG00000277757, NAA11; co-absent with the target |
| [[LINC02099]] | C | AACSP1 activity raises LINC02099's level | lines that do not express AACSP1 (32) vs lines expressing it (18) | 1.96× lower at baseline in the lines without AACSP1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00408, ENSG00000277757, NAA11; co-absent with the target |
| [[LINC01518]] | C | AACSP1 activity raises LINC01518's level | lines that do not express AACSP1 (32) vs lines expressing it (18) | 3.53× lower at baseline in the lines without AACSP1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00408, ENSG00000277757, NAA11; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 31.5); signed map (33.5, 36.2). **Vector** length 21.6, 3.45% of its response variance represented; |z| ≥ 3 in 360 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.1 | +16.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.7 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.6 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.6 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -0.7 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | +0.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | -0.4 | -1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -0.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | acetoacetyl-CoA synthetase pseudogene 1 |
| Locus type | pseudogene |
| Location | 5q35.3 — chr5:178,767,204-178,797,611 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously AACSL |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:18226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18226) · Entrez [729522](https://www.ncbi.nlm.nih.gov/gene/729522) · Ensembl [ENSG00000250420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250420)

## Data

Gene col 14694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14694); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14694]; `tensor/DDL_lfc|DDL_z.npy` [14694]; `embed/gene_vectors.npy` [14694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14694 or target_col == 14694). Every well: [[AACSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AACSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
