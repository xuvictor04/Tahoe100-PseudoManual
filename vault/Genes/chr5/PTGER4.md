---
symbol: "PTGER4"
type: "gene"
col: 10126
ensembl_id: "ENSG00000171522"
name: "prostaglandin E receptor 4"
location: "5p13.1"
module: 123
arm: "+"
pooled_cpm: 12.91
n_lines_expressing: 38
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# PTGER4

*prostaglandin E receptor 4* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.04× (z +24.7, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.554× (z -7.4, q 1e-10, down in 23 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEDD9]] (+0.74, fdr 7e-06), [[NFKBIZ]] (+0.66, fdr 7e-06), [[ARL4A]] (+0.59, fdr 1e-05); moves opposite to [[BABAM1]] (-0.56, fdr 1e-05), [[STX16-NPEPL1]] (-0.55, fdr 2e-05), [[NAA50]] (-0.54, fdr 3e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AHR]] → it (grade B ⚠); 8 go from it, the strongest it → [[AHR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.04×** | +24.7 | 0e+00 | 35/35 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.11×** | +13.5 | 7e-39 | 34/36 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +13.4 | 1e-38 | 33/35 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.82×** | +13.0 | 3e-36 | 29/36 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +10.6 | 2e-24 | 29/36 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +10.4 | 3e-23 | 28/36 (SW1417, J82, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +10.3 | 5e-23 | 28/36 (NCI-H1792, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.13×** | +9.3 | 1e-18 | 26/34 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.8 | 5e-10 | 25/36 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +6.7 | 2e-09 | 20/35 (C32, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.64×** | +6.2 | 3e-08 | 18/36 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.58×** | +5.7 | 5e-07 | 16/32 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.7 | 6e-07 | 15/30 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +5.2 | 9e-06 | 15/36 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.48×** | +4.7 | 1e-04 | 16/31 (J82, NCI-H460, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.006 | 10/35 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.017 | 14/35 (HS-578T, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.554×** | -7.4 | 1e-10 | 23/35 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -5.2 | 5e-05 | 17/26 (BT-474, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -4.0 | 0.011 | 13/16 (Hs 766T, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.736×** | -3.6 | 0.037 | 8/34 (LS 180, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.749×** | -3.6 | 0.037 | 9/34 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 0.5 µM |  | **0.755×** | -3.5 | 0.045 | 12/35 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.761×** | -3.4 | 0.058 | 8/36 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.072 | 7/34 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.771×** | -3.2 | 0.078 | 12/36 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.776×** | -3.1 | 0.094 | 8/34 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.86 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +13.3) | — |
| [[A498 (line)]] | wt | 13.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 26.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +19.8) | — |
| [[CFPAC-1 (line)]] | alt | 32.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 52.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -17.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.36 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +13.3) | [[Ciclopirox (drug)]] 0.5 µM 0.0572× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 21.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HOP62 (line)]] | alt | 7.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +12.2) | — |
| [[J82 (line)]] | alt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +14.4) | — |
| [[A-427 (line)]] | wt | 7.50 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0610× (z -12.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 5.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +13.3) | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0449× (z -13.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -9.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[Panc 03.27 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 26.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 4.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEDD9]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[NFKBIZ]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ARL4A]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TNFAIP3]] | +0.55 | +0.54 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[AHR]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[KLF4]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLF2]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNFRSF9]] | +0.55 | +0.46 / +0.54 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[PIM2]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MYLIP]] | +0.54 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[SFR1]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RASSF5]] | +0.54 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[NAA50]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[APTX]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[XPNPEP3]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[DVL3]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ARIH2]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[VPS53]] | -0.52 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[THAP4]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[NDUFA10]] | -0.51 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[STX16]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[AHSA1]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | AHR activity raises PTGER4's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.35× lower at baseline in the lines without AHR | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[TRIB1]] | B | TRIB1 activity raises PTGER4's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.89× lower at baseline in the lines without TRIB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[IER3]] | B | IER3 activity raises PTGER4's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.94× lower at baseline in the lines without IER3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[ETS2]] | B | ETS2 activity raises PTGER4's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without ETS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[TLE4]] | B | TLE4 activity raises PTGER4's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without TLE4 | 0.096 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | PTGER4 activity raises AHR's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 3.22× lower at baseline in the lines without PTGER4 | 0.006 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[ATP2B1]] | B | PTGER4 activity raises ATP2B1's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without PTGER4 | 0.018 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[IER3]] | B | PTGER4 activity raises IER3's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without PTGER4 | 0.025 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[UGCG]] | B | PTGER4 activity raises UGCG's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.95× lower at baseline in the lines without PTGER4 | 0.057 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[BTG1]] | B | PTGER4 activity raises BTG1's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.77× lower at baseline in the lines without PTGER4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[IL18]] | B | PTGER4 activity raises IL18's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without PTGER4 | 0.074 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[NEDD4L]] | B | PTGER4 activity raises NEDD4L's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without PTGER4 | 0.081 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| cells under [[Fulvestrant (drug)]] 5 µM | B | PTGER4 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express PTGER4 (12) vs lines expressing it (36) | the lines without PTGER4: 0.85× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.5, 6.5); signed map (10.0, 28.1). **Vector** length 85.6, 19.9% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +24.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +13.4 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.4 | +2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +0.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.1 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin E receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:40,679,915-40,693,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EP4 |
| Gene groups (HGNC) | Prostaglandin receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 6 pathways, smallest: Eicosanoid ligand-binding receptors; G alpha (s) signalling events; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P35408](https://www.uniprot.org/uniprotkb/P35408) (Prostaglandin E2 receptor EP4 subtype):

> Receptor for prostaglandin E2 (PGE2). The activity of this receptor is mediated by G(s) proteins that stimulate adenylate cyclase. Has a relaxing effect on smooth muscle. May play an important role in regulating renal hemodynamics, intestinal epithelial transport, adrenal aldosterone secretion, and uterine function.

**Summary**, from NCBI Gene [5734](https://www.ncbi.nlm.nih.gov/gene/5734):

> The protein encoded by this gene is a member of the G-protein coupled receptor family. This protein is one of four receptors identified for prostaglandin E2 (PGE2). This receptor can activate T-cell factor signaling. It has been shown to mediate PGE2 induced expression of early growth response 1 (EGR1), regulate the level and stability of cyclooxygenase-2 mRNA, and lead to the phosphorylation of glycogen synthase kinase-3. Knockout studies in mice suggest that this receptor may be involved in …

**Accessions** — [HGNC:9596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9596) · Entrez [5734](https://www.ncbi.nlm.nih.gov/gene/5734) · UniProt [P35408](https://www.uniprot.org/uniprotkb/P35408) · Ensembl [ENSG00000171522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171522)

## Data

Gene col 10126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10126); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10126]; `tensor/DDL_lfc|DDL_z.npy` [10126]; `embed/gene_vectors.npy` [10126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10126 or target_col == 10126). Every well: [[PTGER4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGER4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
