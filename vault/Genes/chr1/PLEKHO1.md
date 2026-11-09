---
symbol: "PLEKHO1"
type: "gene"
col: 353
ensembl_id: "ENSG00000023902"
name: "pleckstrin homology domain containing O1"
location: "1q21.2"
module: 203
arm: "+"
pooled_cpm: 9.81
n_lines_expressing: 37
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# PLEKHO1

*pleckstrin homology domain containing O1* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +6.2, q 3e-07, up in 14 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.530× (z -8.8, q 9e-16, down in 21 of 33 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.526× (z -4.7, q 5e-04, down in 10 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR161]] (+0.57, fdr 5e-05), [[MSI1]] (+0.55, fdr 5e-05), [[GAB2]] (+0.54, fdr 1e-05); moves opposite to [[ARHGAP18]] (-0.52, fdr 7e-05), [[IGFBP4]] (-0.46, fdr 1e-04), [[ABCC3]] (-0.44, fdr 2e-04).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EBF4]] → it (grade B ⚠); 13 go from it, the strongest it → [[MSX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-07 | 14/31 (A549, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 2e-06 | 17/33 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.34×** | +5.7 | 2e-06 | 18/34 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +5.0 | 7e-05 | 15/34 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.40×** | +4.7 | 3e-04 | 11/33 (NCI-H2347, CFPAC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.003 | 10/33 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +3.8 | 0.014 | 10/34 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.028 | 10/33 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.4 | 0.043 | 5/24 (NCI-H460, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.054 | 4/33 (C32, RPMI-7951, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.27×** | +3.2 | 0.065 | 8/33 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.075 | 7/34 (A-172, NCI-H460, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.092 | 3/32 (LoVo, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.092 | 10/32 (SNU-1, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.0 | 0.093 | 7/29 (A-172, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.530×** | -8.8 | 9e-16 | 21/33 (NCI-H1792, SHP-77, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.638×** | -6.2 | 1e-07 | 22/34 (C32, A-172, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.675×** | -5.4 | 1e-05 | 19/34 (C32, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.526×** | -4.7 | 5e-04 | 10/34 (NCI-H2347, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.6 | 5e-04 | 16/34 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.711×** | -4.5 | 5e-04 | 12/33 (C32, NCI-H2347, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.730×** | -4.4 | 0.001 | 15/34 (SNU-1, NCI-H1792, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.817×** | -3.9 | 0.006 | 13/33 (NCI-H2347, SNU-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.754×** | -3.9 | 0.006 | 12/35 (SNU-1, LOX-IMVI, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.761×** | -3.8 | 0.009 | 14/33 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.760×** | -3.6 | 0.014 | 11/33 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.773×** | -3.6 | 0.018 | 14/34 (SNU-1, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.034 | 11/30 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.066 | 3/34 (SW480, hTERT-HPNE, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 24.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -11.2) |
| [[SNU-1 (line)]] | wt | 40.3 | 0 | 5 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0637× (z -15.5) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.311× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0576× (z -12.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.313× (z -8.5) |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 6.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.25 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR161]] | +0.57 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[MSI1]] | +0.55 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[GAB2]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 | same gene group |
| [[BAHD1]] | +0.53 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[COMMD5]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CDR2L]] | +0.52 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[RHOQ]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ZNF600]] | +0.51 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[ZNF771]] | +0.50 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SPSB1]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NKAIN1]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[RHOQ-AS1]] | +0.50 | +0.31 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP18]] | -0.52 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[IGFBP4]] | -0.46 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ABCC3]] | -0.44 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[ATP5F1A]] | -0.43 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[CBX5]] | -0.43 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[PARK7]] ⚠ | -0.42 | -0.36 / -0.38 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ECT2]] | -0.42 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[PARP4]] | -0.41 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[PPP6R3]] | -0.41 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ZFHX3-AS1]] | -0.40 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[MBNL1]] | -0.40 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[RAB14]] | -0.40 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[TMEM245]] | -0.40 | -0.30 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity raises PLEKHO1's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.87× lower at baseline in the lines without EBF4 | 0.005 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[FGD1]] | B | FGD1 activity raises PLEKHO1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without FGD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[LINC01705]] | B | LINC01705 activity raises PLEKHO1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.36× lower at baseline in the lines without LINC01705 | 0.076 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[ABCC3]] | B | ABCC3 activity lowers PLEKHO1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.68× higher at baseline in the lines without ABCC3 | 0.093 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ZNF611]] | C | ZNF611 activity raises PLEKHO1's level | lines that do not express ZNF611 (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without ZNF611 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF468, ZNF845, ZNF14 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | PLEKHO1 activity raises MSX1's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without PLEKHO1 | 0.032 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[GPR161]] | B | PLEKHO1 activity raises GPR161's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.42× lower at baseline in the lines without PLEKHO1 | 0.037 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[FGD1]] | B | PLEKHO1 activity raises FGD1's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without PLEKHO1 | 0.043 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| cells under [[Daptomycin (drug)]] 5 µM | B | PLEKHO1 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 1.21× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent; cell counts less trustworthy |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | PLEKHO1 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 0.82× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[PPP2R3A]] | B | PLEKHO1 activity raises PPP2R3A's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without PLEKHO1 | 0.075 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[TUBA4A]] | B | PLEKHO1 activity lowers TUBA4A's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.13× higher at baseline in the lines without PLEKHO1 | 0.079 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | PLEKHO1 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 1.24× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[TBKBP1]] | B | PLEKHO1 activity raises TBKBP1's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without PLEKHO1 | 0.083 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[RHOQ]] | B | PLEKHO1 activity raises RHOQ's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PLEKHO1 | 0.083 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[GAB2]] | B | PLEKHO1 activity raises GAB2's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without PLEKHO1 | 0.093 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| cells under [[(S)-Crizotinib (drug)]] 0.5 µM | B | PLEKHO1 activity raises the cells' numbers under (S)-Crizotinib 0.5 µM (protects the cells) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 0.82× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.7, 30.1); signed map (1.7, 10.1). **Vector** length 68.5, 14.1% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +3.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.2 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +5.7 |
| fall | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -1.8 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.4 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -1.3 | -6.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing O1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,149,183-150,164,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CKIP-1, OC120 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GL0](https://www.uniprot.org/uniprotkb/Q53GL0) (Pleckstrin homology domain-containing family O member 1):

> Plays a role in the regulation of the actin cytoskeleton through its interactions with actin capping protein (CP). May function to target CK2 to the plasma membrane thereby serving as an adapter to facilitate the phosphorylation of CP by protein kinase 2 (CK2). Appears to target ATM to the plasma membrane. Appears to also inhibit tumor cell growth by inhibiting AKT-mediated cell-survival. Also implicated in PI3K-regulated muscle differentiation, the regulation of AP-1 activity (plasma membrane …

**Summary**, from NCBI Gene [51177](https://www.ncbi.nlm.nih.gov/gene/51177):

> Predicted to be involved in regulation of myoblast fusion. Predicted to act upstream of or within several processes, including lamellipodium morphogenesis; myoblast fusion; and myoblast migration. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24310) · Entrez [51177](https://www.ncbi.nlm.nih.gov/gene/51177) · UniProt [Q53GL0](https://www.uniprot.org/uniprotkb/Q53GL0) · Ensembl [ENSG00000023902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023902)

## Data

Gene col 353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 353); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 353]; `tensor/DDL_lfc|DDL_z.npy` [353]; `embed/gene_vectors.npy` [353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 353 or target_col == 353). Every well: [[PLEKHO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
