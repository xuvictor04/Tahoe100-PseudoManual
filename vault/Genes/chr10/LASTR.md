---
symbol: "LASTR"
type: "gene"
col: 14304
ensembl_id: "ENSG00000242147"
name: "lncRNA associated with SART3 regulation of splicing"
location: "10p15.1"
module: 31
arm: "+"
pooled_cpm: 5.65
n_lines_expressing: 28
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 45
direction_downstream: 56
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# LASTR

*lncRNA associated with SART3 regulation of splicing* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.84× (z +9.8, q 6e-20, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -11.1, q 1e-25, down in 23 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLDC2]] (+0.69, fdr 7e-06), [[B3GNT3]] (+0.66, fdr 1e-05), [[INAVA]] (+0.65, fdr 1e-05); moves opposite to [[TTC28]] (-0.51, fdr 3e-05), [[COL5A2]] (-0.50, fdr 3e-05), [[TBX18]] (-0.48, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 45 arrows point to it, the strongest [[DSCAML1]] → it (grade B ⚠); 56 go from it, the strongest it → [[NGEF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +9.8 | 6e-20 | 2/8 (HT-29, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.8 | 2e-06 | 1/16 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.5 | 0.001 | 1/11 (SNU-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.62× | +3.4 | 0.11 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.40× | +3.3 | 0.11 | 4/26 (SNU-1, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -11.1 | 1e-25 | 23/25 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.398×** | -9.0 | 8e-17 | 21/24 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.438×** | -8.0 | 2e-13 | 23/26 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -7.9 | 6e-13 | 18/25 (SW1417, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.428×** | -7.8 | 7e-13 | 20/25 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -7.3 | 2e-11 | 19/26 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.510×** | -6.6 | 4e-09 | 20/25 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.536×** | -6.1 | 9e-08 | 18/26 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -6.0 | 1e-07 | 14/26 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.354×** | -5.3 | 7e-06 | 18/26 (SNU-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.569×** | -5.3 | 7e-06 | 17/26 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.601×** | -4.9 | 4e-05 | 11/26 (SW480, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.621×** | -4.6 | 2e-04 | 11/26 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.641×** | -4.3 | 6e-04 | 16/26 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -4.0 | 0.002 | 19/24 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.3 | 0 | 15 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0269× (z -21.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.130× (z -17.9) |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -20.9) |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0333× (z -27.3) |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -12.7) |
| [[LoVo (line)]] | wt | 3.41 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -11.0) |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0449× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -8.9) |
| [[A549 (line)]] | wt | 4.76 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0257× (z -11.9) |
| [[Hs 766T (line)]] | wt | 8.33 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0491× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0964× (z -15.3) |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 5.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0329× (z -9.1) |
| [[HT-29 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0846× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0562× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 5.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0231× (z -11.7) |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLDC2]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[INAVA]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SKAP1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NET1]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[LINC03040]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[LINC01814]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[MPZL2]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[PADI1]] | +0.61 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[RNF43]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LEMD1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC28]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[COL5A2]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TBX18]] | -0.48 | -0.46 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 7, C 38. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCAML1]] | B | DSCAML1 activity raises LASTR's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 1.85× lower at baseline in the lines without DSCAML1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[DCLK2]] | B | DCLK2 activity lowers LASTR's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.92× higher at baseline in the lines without DCLK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[FGD5]] | B | FGD5 activity raises LASTR's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.20× lower at baseline in the lines without FGD5 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[CCR3]] | B | CCR3 activity raises LASTR's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without CCR3 | 0.030 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[SHROOM4]] | B | SHROOM4 activity raises LASTR's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without SHROOM4 | 0.051 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises LASTR's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without EVA1A-AS | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[TGFA]] | B | TGFA activity raises LASTR's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without TGFA | 0.077 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[INAVA]], [[MROH3P]] | C | INAVA, MROH3P activity raises LASTR's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 3.08× lower at baseline in the lines without INAVA, MROH3P | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent with the target; co-absent genes |
| [[CARD11]] | C | CARD11 activity raises LASTR's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without CARD11 | 0.004 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises LASTR's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.06× lower at baseline in the lines without CLIC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[GALNT5]] | C | GALNT5 activity raises LASTR's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without GALNT5 | 0.005 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[ANXA3]] | C | ANXA3 activity raises LASTR's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.20× lower at baseline in the lines without ANXA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132; co-absent with the target |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 14, C 42. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGEF]] | B | LASTR activity raises NGEF's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without LASTR | 0.007 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[TLDC2]] | B | LASTR activity raises TLDC2's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.08× lower at baseline in the lines without LASTR | 0.009 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[FBLIM1]] | B | LASTR activity raises FBLIM1's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without LASTR | 0.017 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[NET1]] | B | LASTR activity raises NET1's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without LASTR | 0.026 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[SOX12]] | B | LASTR activity lowers SOX12's level | lines that do not express LASTR (22) vs lines expressing it (28) | 1.91× higher at baseline in the lines without LASTR | 0.027 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[TGFA]] | B | LASTR activity raises TGFA's level | lines that do not express LASTR (22) vs lines expressing it (28) | 3.04× lower at baseline in the lines without LASTR | 0.035 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[TTC28]] | B | LASTR activity lowers TTC28's level | lines that do not express LASTR (22) vs lines expressing it (28) | 3.21× higher at baseline in the lines without LASTR | 0.039 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[ACOT11]] | B | LASTR activity raises ACOT11's level | lines that do not express LASTR (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without LASTR | 0.046 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[MROH7]] | B | LASTR activity raises MROH7's level | lines that do not express LASTR (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without LASTR | 0.056 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[KRT15]] | B | LASTR activity raises KRT15's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without LASTR | 0.067 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[OCLN]] | B | LASTR activity strengthens OCLN's drug response | lines that do not express LASTR (11) vs lines expressing it (19) | the lines without LASTR respond 0.20× as strongly (z diff +3.87); strongest at Homoharringtonine 5 µM: 1.11x vs 0.50x (z diff +6.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AFAP1L2]] | B | LASTR activity raises AFAP1L2's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.63× lower at baseline in the lines without LASTR | 0.089 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.5, 55.8); signed map (60.2, 10.1). **Vector** length 66.4, 15.7% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.8 | +3.3 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.5 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -7.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | +0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA associated with SART3 regulation of splicing |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p15.1 — chr10:5,594,984-5,632,566 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC02657 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54143) · Entrez [105376382](https://www.ncbi.nlm.nih.gov/gene/105376382) · Ensembl [ENSG00000242147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242147)

## Data

Gene col 14304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14304); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14304]; `tensor/DDL_lfc|DDL_z.npy` [14304]; `embed/gene_vectors.npy` [14304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14304 or target_col == 14304). Every well: [[LASTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LASTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
