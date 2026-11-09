---
symbol: "PXMP4"
type: "gene"
col: 2134
ensembl_id: "ENSG00000101417"
name: "peroxisomal membrane protein 4"
location: "20q11.22"
module: 209
arm: "+"
pooled_cpm: 5.01
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# PXMP4

*peroxisomal membrane protein 4* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.65× (z +10.2, q 7e-22, up in 10 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.48× (z +9.9, q 9e-21, up in 33 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -11.5, q 8e-28, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP57L1]] (+0.66, fdr 3e-05), [[NUDT21]] (+0.66, fdr 1e-05), [[TBC1D13]] (+0.64, fdr 5e-05); moves opposite to [[LRIF1]] (-0.65, fdr 2e-05), [[SLC22A1]] (-0.64, fdr 1e-05), [[IDI2-AS1]] (-0.64, fdr 4e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[NFATC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +10.2 | 7e-22 | 10/12 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +9.9 | 9e-21 | 33/41 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +9.3 | 3e-18 | 37/41 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +8.6 | 1e-15 | 28/40 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.6 | 1e-15 | 14/22 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.7 | 1e-06 | 17/41 (KATO III, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +4.9 | 8e-05 | 10/41 (J82, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.7 | 2e-04 | 6/15 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 11/40 (KATO III, C-33 A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.7 | 0.011 | 11/25 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.40×** | +3.5 | 0.021 | 10/25 (SW1417, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.021 | 7/41 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.3 | 0.041 | 3/40 (SW480, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.080 | 3/23 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -11.5 | 8e-28 | 31/35 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -8.6 | 2e-15 | 25/41 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.506×** | -7.5 | 1e-11 | 24/41 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.508×** | -7.4 | 2e-11 | 24/34 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.517×** | -7.2 | 6e-11 | 21/40 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.529×** | -6.7 | 2e-09 | 23/37 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -6.0 | 2e-07 | 18/34 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.574×** | -5.7 | 6e-07 | 17/39 (SW1417, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.365×** | -5.7 | 6e-07 | 16/32 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -5.4 | 3e-06 | 20/38 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.659×** | -4.6 | 3e-04 | 18/41 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -4.2 | 0.001 | 16/39 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -4.1 | 0.002 | 15/40 (HT-29, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.681×** | -4.0 | 0.003 | 11/38 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -3.5 | 0.018 | 9/30 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -3.2 | 0.041 | 13/39 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -3.1 | 0.075 | 10/41 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.22 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -10.8) |
| [[HT-29 (line)]] | alt | 7.22 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.108× (z -9.9) |
| [[PANC-1 (line)]] | alt | 5.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -9.4) |
| [[SHP-77 (line)]] | alt | 7.38 | 0 | 2 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0950× (z -9.7) |
| [[A498 (line)]] | wt | 5.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.6) |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0664× (z -9.3) |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 4.32 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0559× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0724× (z -8.5) |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0544× (z -8.8) |
| [[SNU-423 (line)]] | alt | 5.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP57L1]] | +0.66 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[NUDT21]] | +0.66 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D13]] | +0.64 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[SLC9A6]] | +0.62 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[TERF1]] | +0.62 | +0.36 / +0.66 | both halves | 1e-04 |  |
| [[FBXO3]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MPPE1]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NDUFB6]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RPA1]] | +0.61 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ZDHHC12]] | +0.61 | +0.59 / +0.33 | both halves | 1e-04 |  |
| [[MRPS31P5-1]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[BRAT1]] | +0.60 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIF1]] | -0.65 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[SLC22A1]] | -0.64 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | -0.64 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[USP50]] | -0.63 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[PPIEL-1]] | -0.63 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PARD6G-AS1]] | -0.63 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MSH4]] | -0.61 | -0.47 / -0.20 | ⚠ not reproduced | 7e-04 |  |
| [[PPIEL]] | -0.61 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MYOCOS]] | -0.60 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SLC6A13]] | -0.60 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[PLAC8L1]] | -0.60 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[C3orf20]] | -0.60 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[C6orf62]] | -0.60 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC1]] | B | PXMP4 activity lowers NFATC1's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.94× higher at baseline in the lines without PXMP4 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[IDI2-AS1]] | B | PXMP4 activity lowers IDI2-AS1's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.86× higher at baseline in the lines without PXMP4 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[IFT172]] | B | PXMP4 activity strengthens IFT172's drug response | lines that do not express PXMP4 (6) vs lines expressing it (40) | the lines without PXMP4 respond 0.44× as strongly (z diff +3.03); strongest at Homoharringtonine 5 µM: 1.26x vs 0.52x (z diff +8.3) | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF532; target measured in part of the lines; artifact flags |
| [[C3orf20]] | B | PXMP4 activity lowers C3orf20's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 2.05× higher at baseline in the lines without PXMP4 | 0.065 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[PLAC8L1]] | B | PXMP4 activity lowers PLAC8L1's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.29× higher at baseline in the lines without PXMP4 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF532 |
| [[FN3KRP]] | B | PXMP4 activity raises FN3KRP's level | lines that do not express PXMP4 (6) vs lines expressing it (44) | 1.44× lower at baseline in the lines without PXMP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF532 |

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.2, -21.7); signed map (-31.7, -11.0). **Vector** length 49.3, 6.56% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +9.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.0 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal membrane protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:33,702,758-33,720,319 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMP24 |
| Gene groups (HGNC) | Tim17 family |
| Reactome | 2 pathways, smallest: Class I peroxisomal membrane protein import; Protein localization |
| Matched by | ensembl_id |

UniProt [Q9Y6I8](https://www.uniprot.org/uniprotkb/Q9Y6I8) carries no function annotation.

**Summary**, from NCBI Gene [11264](https://www.ncbi.nlm.nih.gov/gene/11264):

> Predicted to act upstream of or within ether lipid metabolic process. Located in peroxisomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15920) · Entrez [11264](https://www.ncbi.nlm.nih.gov/gene/11264) · UniProt [Q9Y6I8](https://www.uniprot.org/uniprotkb/Q9Y6I8) · Ensembl [ENSG00000101417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101417)

## Data

Gene col 2134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2134); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2134]; `tensor/DDL_lfc|DDL_z.npy` [2134]; `embed/gene_vectors.npy` [2134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2134 or target_col == 2134). Every well: [[PXMP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXMP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
