---
symbol: "UBXN11"
type: "gene"
col: 8128
ensembl_id: "ENSG00000158062"
name: "UBX domain protein 11"
location: "1p36.11"
module: 31
arm: "+"
pooled_cpm: 7.54
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# UBXN11

*UBX domain protein 11* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +16.6, q 0e+00, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.675× (z -5.7, q 7e-06, down in 20 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.711× (z -3.7, q 0.072, down in 13 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (AsPC-1 0.0897×; ⚠ toxic; transcription drop); [[Hesperidin (drug)]] 5 µM in 1 line (SNU-423 0.0822×); [[Allantoin (drug)]] 0.5 µM in 1 line (HCT15 0.107×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (A-427 0.139×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLTB]] (+0.55, fdr 2e-05), [[ARHGAP27]] (+0.54, fdr 1e-05), [[UNC13D]] (+0.52, fdr 4e-05); moves opposite to [[SMAD5]] (-0.47, fdr 5e-05), [[BRWD1]] (-0.46, fdr 6e-05), [[PAPOLG]] (-0.45, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[HS3ST1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +16.6 | 0e+00 | 27/38 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +12.7 | 2e-34 | 7/15 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +11.3 | 4e-27 | 12/20 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +10.9 | 1e-25 | 18/29 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +10.9 | 2e-25 | 35/47 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +10.3 | 6e-23 | 29/44 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +9.4 | 4e-19 | 28/47 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +8.0 | 1e-13 | 24/45 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +6.6 | 2e-09 | 19/47 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.5 | 2e-06 | 16/43 (COLO 205, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.4 | 3e-06 | 11/47 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 6e-05 | 16/43 (COLO 205, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 3e-04 | 13/39 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 15/46 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.003 | 8/47 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.018 | 10/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.082 | 4/41 (HT-29, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8128.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (AsPC-1 0.0897×; ⚠ toxic; transcription drop); [[Hesperidin (drug)]] 5 µM in 1 line (SNU-423 0.0822×); [[Allantoin (drug)]] 0.5 µM in 1 line (HCT15 0.107×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (A-427 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -5.7 | 7e-06 | 20/38 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.072 | 13/40 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +10.0) | — |
| [[A-427 (line)]] | wt | 7.35 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.139× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0897× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.107× (z -9.3) |
| [[HOP62 (line)]] | alt | 6.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 6.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 7.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 4.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 4.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 5.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 6.30 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0822× (z -10.0) |
| [[A498 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLTB]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ARHGAP27]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[UNC13D]] | +0.52 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[CFAP46]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[INF2]] | +0.51 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[LSMEM2]] | +0.50 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PADI1]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[ARHGAP23]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[CRYBG2]] | +0.49 | +0.49 / +0.49 | both halves | 1e-05 | ⚠ same locus (3.3 kb, same strand: neighbours can correlate without regulation) |
| [[COQ8B]] | +0.49 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ADAP1]] | +0.48 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[POLR2J3]] | +0.48 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[ANO1]] | +0.48 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD5]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[BRWD1]] | -0.46 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[PAPOLG]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[HOXA10]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[CNOT6L]] | -0.43 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[HOXA11]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[TMEM129]] | -0.42 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[BCL7A]] | -0.42 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[FCHO2]] | -0.42 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[SLC25A36]] | -0.42 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[FZD3]] | -0.41 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[TBC1D12]] | -0.40 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST1]] | B | HS3ST1 activity raises UBXN11's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 1.60× lower at baseline in the lines without HS3ST1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[CRYBG2]] | B | CRYBG2 activity raises UBXN11's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without CRYBG2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises UBXN11's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 1.62× lower at baseline in the lines without TMPRSS4 | 0.009 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[KIAA0040]] | B | KIAA0040 activity raises UBXN11's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 1.46× lower at baseline in the lines without KIAA0040 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[B3GNT3]] | B | B3GNT3 activity raises UBXN11's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without B3GNT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[C1orf116]] | B | C1orf116 activity raises UBXN11's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without C1orf116 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MYH14]] | B | MYH14 activity raises UBXN11's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without MYH14 | 0.038 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[UNC13D]] | B | UNC13D activity raises UBXN11's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without UNC13D | 0.041 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[PADI1]] | B | PADI1 activity raises UBXN11's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.57× lower at baseline in the lines without PADI1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[IL1RN]] | B | IL1RN activity raises UBXN11's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without IL1RN | 0.085 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[SERPINB5]] | B | SERPINB5 activity raises UBXN11's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 1.47× lower at baseline in the lines without SERPINB5 | 0.096 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.0, 52.9); signed map (1.5, 35.8). **Vector** length 66.8, 9.83% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +16.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.8 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,281,328-26,318,363 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SOC, SOCI; previously UBXD5 |
| Gene groups (HGNC) | UBX domain containing |
| Reactome | 6 pathways, smallest: RND1 GTPase cycle; RND2 GTPase cycle; RND3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T124](https://www.uniprot.org/uniprotkb/Q5T124) (UBX domain-containing protein 11):

> May be involved in the reorganization of actin cytoskeleton mediated by RND1, RND2 and RND3. Promotes RHOA activation mediated by GNA12 and GNA13 (By similarity).

**Summary**, from NCBI Gene [91544](https://www.ncbi.nlm.nih.gov/gene/91544):

> This gene encodes a protein with a divergent C-terminal UBX domain. The homologous protein in the rat interacts with members of the Rnd subfamily of Rho GTPases at the cell periphery through its C-terminal region. It also interacts with several heterotrimeric G proteins through their G-alpha subunits and promotes Rho GTPase activation. It is proposed to serve a bidirectional role in the promotion and inhibition of Rho activity through upstream signaling pathways. The 3' coding sequence of this …

**Accessions** — [HGNC:30600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30600) · Entrez [91544](https://www.ncbi.nlm.nih.gov/gene/91544) · UniProt [Q5T124](https://www.uniprot.org/uniprotkb/Q5T124) · Ensembl [ENSG00000158062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158062)

## Data

Gene col 8128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8128); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8128]; `tensor/DDL_lfc|DDL_z.npy` [8128]; `embed/gene_vectors.npy` [8128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8128 or target_col == 8128). Every well: [[UBXN11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
