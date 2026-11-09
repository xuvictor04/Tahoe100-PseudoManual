---
symbol: "GAMT"
type: "gene"
col: 5014
ensembl_id: "ENSG00000130005"
name: "guanidinoacetate N-methyltransferase"
location: "19p13.3"
module: 45
arm: "+"
pooled_cpm: 2.52
n_lines_expressing: 39
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# GAMT

*guanidinoacetate N-methyltransferase* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.33× (z +9.9, q 2e-20, up in 4 of 5 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +6.9, q 5e-10, up in 15 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.472× (z -5.3, q 7e-05, down in 16 of 28 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSTM4]] (+0.68, fdr 7e-06), [[ATP6V0E2]] (+0.67, fdr 7e-06), [[PCSK1N]] (+0.65, fdr 1e-05); moves opposite to [[AVEN]] (-0.57, fdr 8e-05), [[ST7L]] (-0.54, fdr 2e-04), [[DESI1]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLEKHH2]] → it (grade B ⚠); 8 go from it, the strongest it → [[SYT11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.33×** | +9.9 | 2e-20 | 4/5 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.99×** | +9.7 | 7e-20 | 10/11 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.61×** | +8.3 | 1e-14 | 4/5 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.22×** | +8.2 | 3e-14 | 29/32 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +6.9 | 5e-10 | 15/24 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.63×** | +6.8 | 1e-09 | 24/33 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.54×** | +6.6 | 5e-09 | 24/33 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +5.0 | 5e-05 | 14/31 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +4.4 | 8e-04 | 10/34 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.004 | 5/33 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.67×** | +3.5 | 0.026 | 5/15 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.039 | 6/23 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.056 | 5/24 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.060 | 5/32 (SW 900, HepG2/C3A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.082 | 4/34 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.96×** | +3.0 | 0.082 | 1/22 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.091 | 7/30 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -5.3 | 7e-05 | 16/28 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.535×** | -4.4 | 0.002 | 12/32 (C32, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -4.3 | 0.002 | 15/26 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.542×** | -4.3 | 0.002 | 14/29 (NCI-H460, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.568×** | -4.0 | 0.008 | 10/32 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -3.9 | 0.010 | 11/34 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -3.8 | 0.010 | 10/23 (Panc 03.27, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.599×** | -3.6 | 0.022 | 9/33 (NCI-H460, AN3 CA, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.419×** | -3.2 | 0.084 | 7/33 (Hs 766T, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.620×** | -3.2 | 0.084 | 5/31 (hTERT-HPNE, A-427, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -3.1 | 0.088 | 14/34 (SNU-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.64 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.875 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTM4]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ATP6V0E2]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PCSK1N]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[CDK5]] | +0.65 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[FHIP1A]] | +0.64 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[LMBRD1]] | +0.63 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[EGFL7]] | +0.63 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[ORC4]] | +0.63 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PPP1R14A]] | +0.61 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[CTSF]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[TMEM266]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[SYNGR1]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.57 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ST7L]] | -0.54 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[DESI1]] | -0.54 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[MIRLET7IHG]] | -0.53 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[AFG3L1P]] | -0.53 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[FBXO30]] | -0.52 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[ELK4]] | -0.52 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[REXO1]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ENOX2]] | -0.51 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[PCBD2]] | -0.50 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[LTO1]] | -0.50 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[RNASEH1]] | -0.50 | -0.29 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHH2]] | B | PLEKHH2 activity raises GAMT's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without PLEKHH2 | 0.018 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[LHX6]] | B | LHX6 activity raises GAMT's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without LHX6 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[SNCG]] | B | SNCG activity raises GAMT's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without SNCG | 0.090 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[RAB6B]] | B | RAB6B activity raises GAMT's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without RAB6B | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT11]] | B | GAMT activity raises SYT11's level | lines that do not express GAMT (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without GAMT | 0.025 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[FAM104B]] | B | GAMT activity raises FAM104B's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without GAMT | 0.035 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[NAT14]] | B | GAMT activity raises NAT14's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without GAMT | 0.042 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[LMTK2]] | B | GAMT activity lowers LMTK2's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.88× higher at baseline in the lines without GAMT | 0.046 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[FAM229B]] | B | GAMT activity raises FAM229B's level | lines that do not express GAMT (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without GAMT | 0.062 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[CYP46A1]] | B | GAMT activity raises CYP46A1's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without GAMT | 0.088 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[SMIM10]] | B | GAMT activity raises SMIM10's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without GAMT | 0.093 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[SYNGR1]] | C | GAMT activity raises SYNGR1's level | lines that do not express GAMT (11) vs lines expressing it (39) | 3.56× lower at baseline in the lines without GAMT | 0.023 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3; co-absent with the target |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.0, -7.4); signed map (-27.0, -3.3). **Vector** length 39.0, 5.84% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.7 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.3 | +8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.3 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.9 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | guanidinoacetate N-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,397,026-1,401,570 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG2, TP53I2 |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Hallmark sets | KRAS_SIGNALING_DN, APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Creatine metabolism; Transcriptional Regulation by MECP2; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14353](https://www.uniprot.org/uniprotkb/Q14353) (Guanidinoacetate N-methyltransferase):

> Converts guanidinoacetate to creatine, using S-adenosylmethionine as the methyl donor. Important in nervous system development.

**Summary**, from NCBI Gene [2593](https://www.ncbi.nlm.nih.gov/gene/2593):

> The protein encoded by this gene is a methyltransferase that converts guanidoacetate to creatine, using S-adenosylmethionine as the methyl donor. Defects in this gene have been implicated in neurologic syndromes and muscular hypotonia, probably due to creatine deficiency and accumulation of guanidinoacetate in the brain of affected individuals. Two transcript variants encoding different isoforms have been described for this gene. Pseudogenes of this gene are found on chromosomes 2 and 13. …

**Accessions** — [HGNC:4136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4136) · Entrez [2593](https://www.ncbi.nlm.nih.gov/gene/2593) · UniProt [Q14353](https://www.uniprot.org/uniprotkb/Q14353) · Ensembl [ENSG00000130005](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130005)

## Data

Gene col 5014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5014); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5014]; `tensor/DDL_lfc|DDL_z.npy` [5014]; `embed/gene_vectors.npy` [5014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5014 or target_col == 5014). Every well: [[GAMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
