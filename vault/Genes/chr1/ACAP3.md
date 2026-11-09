---
symbol: "ACAP3"
type: "gene"
col: 5224
ensembl_id: "ENSG00000131584"
name: "ArfGAP with coiled-coil, ankyrin repeat and PH domains 3"
location: "1p36.33"
module: 189
arm: "+"
pooled_cpm: 11.95
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# ACAP3

*ArfGAP with coiled-coil, ankyrin repeat and PH domains 3* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.01× (z +20.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.645× (z -8.1, q 4e-13, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAI2]] (+0.61, fdr 1e-04), [[CDC42BPG]] (+0.60, fdr 1e-05), [[TBC1D10A]] (+0.58, fdr 5e-05); moves opposite to [[PGAP4]] (-0.52, fdr 9e-05), [[CIAO2A]] (-0.52, fdr 2e-04), [[NAE1]] (-0.51, fdr 2e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.01×** | +20.9 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.43×** | +19.3 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +17.2 | 0e+00 | 40/45 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.58×** | +16.6 | 0e+00 | 47/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +9.6 | 8e-20 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.95×** | +8.6 | 5e-16 | 25/36 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.4 | 2e-15 | 26/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.8 | 6e-13 | 29/44 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.74×** | +6.9 | 3e-10 | 16/25 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +6.5 | 4e-09 | 29/47 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.96×** | +6.2 | 2e-08 | 29/43 (HS-578T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.9 | 1e-07 | 25/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.35×** | +5.8 | 3e-07 | 31/47 (Hs 766T, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.57×** | +5.4 | 3e-06 | 16/32 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +5.3 | 4e-06 | 24/47 (SW480, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 19/44 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.005 | 8/47 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.005 | 11/48 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.645×** | -8.1 | 4e-13 | 29/48 (CFPAC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -4.3 | 0.005 | 18/47 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.723×** | -4.2 | 0.005 | 17/46 (HS-578T, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -4.1 | 0.005 | 16/48 (C32, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -4.0 | 0.008 | 16/48 (NCI-H460, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.742×** | -3.9 | 0.010 | 20/46 (BT-474, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.759×** | -3.4 | 0.052 | 16/46 (HS-578T, H4, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.052 | 13/47 (SNU-1, RPMI-7951, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.071 | 17/48 (HS-578T, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 14.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 22.2 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.06× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.210× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.353× (z -9.6) |
| [[KATO III (line)]] | alt | 7.40 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 12.4× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.217× (z -8.9) |
| [[SW480 (line)]] | alt | 13.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.45× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 6.35× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.251× (z -11.1) |
| [[LoVo (line)]] | wt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +14.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.86 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.5× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 4.72 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 8.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 19.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.43× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 13.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.49× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 5.20 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.9× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.45× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.9) | — |
| [[RKO (line)]] | wt | 8.11 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 9.72× (z +9.0) | [[Glycyrrhizic acid (drug)]] 5 µM 0.0749× (z -9.8) |
| [[SNU-423 (line)]] | alt | 6.76 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.85× (z +9.8) | — |
| [[A-172 (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +11.2) | — |
| [[A-427 (line)]] | wt | 7.86 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.30× (z +9.0) | — |
| [[A549 (line)]] | wt | 5.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 7.90 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.27× (z +8.5) | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.283× (z -9.3) |
| [[H4 (line)]] | wt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.146× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.151× (z -9.5) |
| [[J82 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 6.75 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.81× (z +9.0) | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | +0.61 | +0.35 / +0.56 | both halves | 1e-04 | same gene group |
| [[CDC42BPG]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D10A]] | +0.58 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[ARHGAP45]] | +0.58 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ANO8]] | +0.58 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[PLXNA3]] | +0.57 | +0.53 / +0.37 | both halves | 9e-05 |  |
| [[MAPK8IP3]] | +0.57 | +0.37 / +0.49 | both halves | 8e-05 | same gene group |
| [[PORCN]] | +0.57 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ARHGEF10]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[FOXO6]] | +0.57 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ACTR1B]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PPFIA3]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAP4]] | -0.52 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[CIAO2A]] | -0.52 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[NAE1]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[YARS2]] | -0.50 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[ANGEL2]] | -0.49 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[NAF1]] | -0.49 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[EPM2A]] | -0.49 | -0.26 / -0.29 | both halves | 3e-04 |  |
| [[QRSL1]] | -0.49 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[HNF4G]] | -0.49 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[NSMAF]] | -0.48 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[TOR1A]] | -0.48 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[MRPS15]] | -0.48 | -0.53 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ACAP3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CADM4]] | B | CADM4 activity raises ACAP3's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without CADM4 | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BMP1]] | C | BMP1 activity raises ACAP3's level | lines that do not express BMP1 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without BMP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NPEPPSP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -2.8); signed map (-22.5, 26.1). **Vector** length 83.3, 17.1% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.0 | +8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +20.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.4 | +6.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.5 | -8.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.4 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.5 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with coiled-coil, ankyrin repeat and PH domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,292,390-1,309,609 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1716; previously CENTB5 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P50](https://www.uniprot.org/uniprotkb/Q96P50) (Arf-GAP with coiled-coil, ANK repeat and PH domain-containing protein 3):

> GTPase-activating protein for the ADP ribosylation factor family.

**Summary**, from NCBI Gene [116983](https://www.ncbi.nlm.nih.gov/gene/116983):

> Predicted to enable GTPase activator activity and zinc ion binding activity. Predicted to act upstream of or within neuron migration and regulation of neuron projection development. Predicted to be located in endosome membrane and growth cone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16754) · Entrez [116983](https://www.ncbi.nlm.nih.gov/gene/116983) · UniProt [Q96P50](https://www.uniprot.org/uniprotkb/Q96P50) · Ensembl [ENSG00000131584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131584)

## Data

Gene col 5224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5224); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5224]; `tensor/DDL_lfc|DDL_z.npy` [5224]; `embed/gene_vectors.npy` [5224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5224 or target_col == 5224). Every well: [[ACAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
