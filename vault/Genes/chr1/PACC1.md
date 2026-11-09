---
symbol: "PACC1"
type: "gene"
col: 795
ensembl_id: "ENSG00000065600"
name: "proton activated chloride channel 1"
location: "1q32.3"
module: 159
arm: "+"
pooled_cpm: 11.3
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 5
n_dd_up_clean: 28
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# PACC1

*proton activated chloride channel 1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.42× (z +21.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.620× (z -11.9, q 1e-29, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEIL2]] (+0.79, fdr 7e-06), [[ANKS6]] (+0.78, fdr 7e-06), [[INPP4A]] (+0.77, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.72, fdr 1e-05), [[PDCL3P4]] (-0.70, fdr 4e-05), [[PCNX4-DT]] (-0.70, fdr 7e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MFAP3L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **3.42×** | +21.6 | 0e+00 | 45/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.34×** | +21.2 | 0e+00 | 45/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.09×** | +19.8 | 0e+00 | 44/47 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.32×** | +14.7 | 0e+00 | 42/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.23×** | +14.1 | 5e-43 | 40/46 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.18×** | +13.7 | 1e-40 | 38/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.22×** | +13.2 | 6e-38 | 40/46 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +10.7 | 6e-25 | 34/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.99×** | +10.0 | 6e-22 | 28/32 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +9.8 | 6e-21 | 34/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +9.7 | 2e-20 | 31/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.69×** | +8.9 | 3e-17 | 19/39 (A-172, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +8.7 | 1e-16 | 26/40 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.46×** | +8.3 | 6e-15 | 31/47 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +7.8 | 2e-13 | 22/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +7.0 | 6e-11 | 25/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.67×** | +6.4 | 6e-09 | 18/47 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +5.4 | 2e-06 | 11/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.4 | 2e-06 | 17/46 (HOP62, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 795.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.620×** | -11.9 | 1e-29 | 25/45 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.645×** | -7.7 | 4e-12 | 25/45 (PANC-1, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.759×** | -4.7 | 6e-04 | 20/47 (NCI-H460, A498, …) | inconsistent across doses | composition shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.772×** | -4.5 | 8e-04 | 10/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.674×** | -3.6 | 0.033 | 11/47 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.18 | 9/47 (SNU-423, J82, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.0 | 2 (1 ⚠) | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.21× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.3) |
| [[PANC-1 (line)]] | alt | 10.3 | 2 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.41× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.0) |
| [[C32 (line)]] | wt | 9.35 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 8.14 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.88× (z +11.0) | — |
| [[A-172 (line)]] | wt | 12.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.93× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 5.86 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -12.2) |
| [[SW48 (line)]] | wt | 29.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.6) |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0634× (z -10.2) |
| [[HOP62 (line)]] | alt | 6.05 | 1 | 0 | [[Belinostat (drug)]] 5 µM 6.51× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.13 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.05 µM 0.0516× (z -8.5) |
| [[LoVo (line)]] | wt | 14.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.19× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0811× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.5) |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 24.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.228× (z -8.7) |
| [[SNU-423 (line)]] | alt | 4.65 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0957× (z -8.5) |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEIL2]] | +0.79 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.78 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[INPP4A]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[TRABD]] | +0.73 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LIMK1]] | +0.73 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[RNF216]] | +0.72 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ST6GALNAC4]] | +0.72 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PIP4K2A]] | +0.72 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[BLVRA]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[GNA12]] | +0.71 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.72 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[PDCL3P4]] | -0.70 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[PCNX4-DT]] | -0.70 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[USP11]] | -0.69 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[EP300]] | -0.68 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[METTL6]] | -0.67 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[HELQ]] | -0.67 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.67 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[UBE3B]] | -0.66 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[THAP9]] | -0.66 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[SGO1-AS1]] | -0.66 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[AK9]] | -0.66 | -0.60 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFAP3L]] | B | MFAP3L activity raises PACC1's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.92× lower at baseline in the lines without MFAP3L | 0.001 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises PACC1's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without ARHGAP44 | 0.005 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[CRACD]] | B | CRACD activity raises PACC1's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.82× lower at baseline in the lines without CRACD | 0.007 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises PACC1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without GNAZ | 0.046 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[CMTM8]] | B | CMTM8 activity raises PACC1's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without CMTM8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[LRRC20]] | B | LRRC20 activity raises PACC1's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without LRRC20 | 0.088 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, 2.8); signed map (-41.8, -8.3). **Vector** length 93.9, 20.4% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +13.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +13.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +14.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +9.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +7.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +5.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.1 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.3 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -6.4 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | proton activated chloride channel 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,363,928-212,414,901 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10874, PAC, ASOR, PAORAC; previously C1orf75, TMEM206 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H813](https://www.uniprot.org/uniprotkb/Q9H813) (Proton-activated chloride channel):

> Chloride channel gated by pH that facilitates the entry of chloride ions into cells upon exposure to extracellular acidic pH. Involved in acidosis-induced cell death by mediating chloride influx and subsequent cell swelling.

**Summary**, from NCBI Gene [55248](https://www.ncbi.nlm.nih.gov/gene/55248):

> Enables pH-gated chloride channel activity. Involved in chloride transport. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25593) · Entrez [55248](https://www.ncbi.nlm.nih.gov/gene/55248) · UniProt [Q9H813](https://www.uniprot.org/uniprotkb/Q9H813) · Ensembl [ENSG00000065600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065600)

## Data

Gene col 795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 795); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 795]; `tensor/DDL_lfc|DDL_z.npy` [795]; `embed/gene_vectors.npy` [795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 795 or target_col == 795). Every well: [[PACC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PACC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
