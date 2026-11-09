---
symbol: "OFCC1"
type: "gene"
col: 11182
ensembl_id: "ENSG00000181355"
name: "orofacial cleft 1 candidate 1 (pseudogene)"
location: "6p24.3"
module: 9
arm: "+"
pooled_cpm: 7.36
n_lines_expressing: 36
n_dd_up: 34
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 26
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# OFCC1

*orofacial cleft 1 candidate 1 (pseudogene)* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.25× (z +26.9, q 0e+00, up in 22 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.719× (z -3.8, q 0.027, down in 8 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTSL1]] (+0.69, fdr 7e-06), [[SCN3A]] (+0.66, fdr 3e-05), [[LINC01695]] (+0.65, fdr 7e-06); moves opposite to [[ZDHHC9]] (-0.54, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[LINC01320]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC01611]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.25×** | +26.9 | 0e+00 | 22/25 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.66×** | +25.0 | 0e+00 | 18/27 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +13.3 | 3e-38 | 27/31 (SNU-423, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.34×** | +13.3 | 3e-38 | 18/28 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +12.5 | 9e-34 | 1/11 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +12.3 | 9e-33 | 7/20 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.75×** | +11.6 | 3e-29 | 19/29 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +9.9 | 2e-21 | 14/27 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +9.0 | 1e-17 | 18/28 (A498, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.05×** | +8.3 | 8e-15 | 15/32 (SNU-423, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.04×** | +8.2 | 2e-14 | 17/29 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.12×** | +8.0 | 8e-14 | 5/13 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.4 | 5e-09 | 13/32 (HOP62, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.64×** | +5.7 | 6e-07 | 11/30 (SNU-423, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +5.2 | 9e-06 | 13/31 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 5e-04 | 14/29 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +4.2 | 7e-04 | 13/29 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.004 | 11/30 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.004 | 6/33 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.007 | 5/28 (SK-MEL-2, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.027 | 8/31 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.722×** | -3.8 | 0.027 | 8/30 (H4, CFPAC-1, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.027 | 5/30 (A-172, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.027 | 8/29 (HCT15, Panc 03.27, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.800×** | -3.7 | 0.027 | 9/29 (H4, SW 900, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.047 | 5/33 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ranolazine (drug)]] 5 µM |  | 0.764× | -3.1 | 0.14 | 2/30 (Panc 03.27, NCI-H23) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 32.3 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 16.2× (z +14.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.71× (z +13.5) | — |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 89.0 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.81× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -12.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[J82 (line)]] | alt | 8.13 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +17.7) | — |
| [[LoVo (line)]] | wt | 4.33 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.3× (z +18.1) | — |
| [[A-172 (line)]] | wt | 15.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 9.02 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 61.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 2.82 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 8.90× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 1.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 5.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.5× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 3.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +9.4) | — |
| [[SW480 (line)]] | alt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +9.5) | — |
| [[A-427 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL1]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SCN3A]] | +0.66 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[LINC01695]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[RALYL]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[BAALC]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[LINC01483]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[IL7R]] | +0.62 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[LINC00871]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[DMD]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 25, C 1. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01320]] | B | LINC01320 activity raises OFCC1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 4.15× lower at baseline in the lines without LINC01320 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[BAALC]] | B | BAALC activity raises OFCC1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without BAALC | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[LINC01611]] | B | LINC01611 activity raises OFCC1's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without LINC01611 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[POU3F2]] | B | POU3F2 activity raises OFCC1's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.87× lower at baseline in the lines without POU3F2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[PDZRN3]] | B | PDZRN3 activity raises OFCC1's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PDZRN3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[SCG2]] | B | SCG2 activity raises OFCC1's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without SCG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG |
| [[PEX5L]] | B | PEX5L activity raises OFCC1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without PEX5L | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent |
| [[LINC01695]] | B | LINC01695 activity raises OFCC1's level | lines that do not express LINC01695 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without LINC01695 | 0.031 | ⚠ within organs, on part of the lines; also absent: VCAN, ITGA4, PTPRN |
| [[CDH6]] | B | CDH6 activity raises OFCC1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without CDH6 | 0.035 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[HGF]] | B | HGF activity raises OFCC1's level | lines that do not express HGF (38) vs lines expressing it (12) | 1.63× lower at baseline in the lines without HGF | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |
| [[SOX11]] | B | SOX11 activity raises OFCC1's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.06× lower at baseline in the lines without SOX11 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1 |
| [[FRMPD4]] | B | FRMPD4 activity raises OFCC1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without FRMPD4 | 0.052 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01611]] | B | OFCC1 activity raises LINC01611's level | lines that do not express OFCC1 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without OFCC1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PDLIM3, CAMK4, GLRB; maybe low, not absent |
| [[SLIT2]] | B | OFCC1 activity raises SLIT2's level | lines that do not express OFCC1 (14) vs lines expressing it (36) | 2.93× lower at baseline in the lines without OFCC1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PDLIM3, CAMK4, GLRB; maybe low, not absent |
| [[SCG2]] | B | OFCC1 activity raises SCG2's level | lines that do not express OFCC1 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without OFCC1 | 0.090 | ⚠ within organs, on part of the lines; also absent: PDLIM3, CAMK4, GLRB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 28.0); signed map (40.0, 29.4). **Vector** length 67.8, 14.8% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +7.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +26.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | orofacial cleft 1 candidate 1 (pseudogene) |
| Locus type | pseudogene |
| Location | 6p24.3 — chr6:9,596,297-9,939,349 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | OFCC1P, MRDS1, Opo |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [Q8IZS5](https://www.uniprot.org/uniprotkb/Q8IZS5) carries no function annotation.

**Summary**, from NCBI Gene [266553](https://www.ncbi.nlm.nih.gov/gene/266553):

> Predicted to be located in several cellular components, including endoplasmic reticulum; microtubule cytoskeleton; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21017) · Entrez [266553](https://www.ncbi.nlm.nih.gov/gene/266553) · UniProt [Q8IZS5](https://www.uniprot.org/uniprotkb/Q8IZS5) · Ensembl [ENSG00000181355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181355)

## Data

Gene col 11182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11182); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11182]; `tensor/DDL_lfc|DDL_z.npy` [11182]; `embed/gene_vectors.npy` [11182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11182 or target_col == 11182). Every well: [[OFCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OFCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
