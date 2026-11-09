---
symbol: "MAOA"
type: "gene"
col: 12105
ensembl_id: "ENSG00000189221"
name: "monoamine oxidase A"
location: "Xp11.3"
module: 98
arm: "+"
pooled_cpm: 5.28
n_lines_expressing: 37
n_dd_up: 44
n_dd_down: 6
n_dd_up_clean: 35
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# MAOA

*monoamine oxidase A* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (9 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 3.17× (z +15.9, q 0e+00, up in 22 of 33 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Dexamethasone (drug)]] 5 µM: 2.55× (z +12.9, q 9e-36, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.584× (z -7.4, q 6e-11, down in 13 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACSL1]] (+0.75, fdr 7e-06), [[FKBP5]] (+0.73, fdr 7e-06), [[VSTM2L]] (+0.73, fdr 7e-06); moves opposite to [[MRPS6]] (-0.59, fdr 1e-05), [[RASGRP3]] (-0.55, fdr 1e-05), [[ANXA10]] (-0.54, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FST]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZMYND8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **3.17×** | +15.9 | 0e+00 | 22/33 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | **2.87×** | +14.5 | 1e-45 | 18/33 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **2.55×** | +12.9 | 9e-36 | 19/34 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.45×** | +12.4 | 6e-33 | 17/33 (NCI-H460, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.44×** | +12.3 | 2e-32 | 17/32 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.41×** | +12.1 | 9e-32 | 19/33 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **1.96×** | +12.0 | 2e-31 | 12/28 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.39×** | +12.0 | 2e-31 | 22/32 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +11.8 | 1e-30 | 23/34 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **2.34×** | +11.7 | 6e-30 | 19/34 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.90×** | +11.7 | 9e-30 | 18/34 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +11.4 | 1e-28 | 6/12 (Panc 03.27, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.38×** | +11.1 | 9e-27 | 18/30 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.20×** | +10.9 | 7e-26 | 21/34 (NCI-H2347, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **2.20×** | +10.8 | 8e-26 | 16/33 (NCI-H1792, NCI-H460, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **2.09×** | +10.2 | 1e-22 | 19/34 (NCI-H460, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.07×** | +10.0 | 4e-22 | 17/33 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +9.6 | 2e-20 | 19/34 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +8.9 | 2e-17 | 17/34 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.83×** | +8.3 | 2e-15 | 15/34 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -7.4 | 6e-11 | 13/34 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -5.7 | 4e-06 | 14/26 (CHP-212, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -4.9 | 2e-04 | 14/33 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.5 | 0.001 | 11/26 (SK-MEL-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.744×** | -4.1 | 0.005 | 8/33 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **0.780×** | -3.4 | 0.054 | 2/30 (A-172, C32) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM |  | 0.794× | -3.2 | 0.12 | 4/33 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.647× | -3.1 | 0.12 | 4/32 (Panc 03.27, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.804× | -3.0 | 0.16 | 7/34 (NCI-H1573, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 17.6 | 17 (3 ⚠) | 0 | [[Triamcinolone (drug)]] 0.5 µM 10.6× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 6.93 | 16 (3 ⚠) | 0 | [[Clobetasol propionate (drug)]] 5 µM 8.56× (z +12.6) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 7.37× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 6.04 | 7 (3 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 14.0× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 4.94× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -9.1) ⚠ position correction uncertain |
| [[A498 (line)]] | wt | 3.54 | 3 (2 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 10.4× (z +9.8) ⚠ position correction uncertain · without an alert: [[Phenylephrine (hydrochloride) (drug)]] 5 µM 7.67× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 9.15 | 3 (2 ⚠) | 0 | [[Triamcinolone (drug)]] 0.5 µM 12.7× (z +8.9) | — |
| [[A549 (line)]] | wt | 4.60 | 2 (2 ⚠) | 0 | [[Clobetasol propionate (drug)]] 5 µM 15.1× (z +8.8) ⚠ position correction uncertain | — |
| [[A-172 (line)]] | wt | 2.38 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +9.4) ⚠ position correction uncertain | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 1 | — | [[Fumaric acid (drug)]] 0.05 µM 0.0602× (z -9.7) |
| [[LoVo (line)]] | wt | 3.07 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0729× (z -9.0) |
| [[A-427 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.773 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[FKBP5]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | STRING 542 |
| [[VSTM2L]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.72 | +0.78 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CCND3]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[COPS8]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[TLR2]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADGRG2]] | +0.68 | +0.59 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TSC22D3]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PDLIM1]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[STOM]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[IRAK3]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS6]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RASGRP3]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ANXA10]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SLC5A3]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NHS]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[NPTX1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SYNJ2]] | -0.50 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CYP27C1]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[PTHLH]] | -0.49 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FST]] | B | FST activity strengthens MAOA's drug response | lines that do not express FST (18) vs lines expressing it (16) | the lines without FST respond 0.44× as strongly (z diff +1.33); strongest at Clobetasol propionate 0.5 µM: 1.67x vs 4.28x (z diff +2.4) | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2; target measured in part of the lines; the reference differs |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises MAOA's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.82× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.053 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[MFGE8]] | B | MFGE8 activity lowers MAOA's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 1.69× higher at baseline in the lines without MFGE8 | 0.059 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[F5]] | B | F5 activity raises MAOA's level | lines that do not express F5 (39) vs lines expressing it (11) | 2.07× lower at baseline in the lines without F5 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2 |
| [[MAFB]] | B | MAFB activity raises MAOA's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without MAFB | 0.073 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[NR3C1]] | B | NR3C1 activity raises MAOA's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMYND8]] | B | MAOA activity raises ZMYND8's level | lines that do not express MAOA (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without MAOA | 0.018 | ⚠ within organs, on part of the lines; also absent: OAS1, CKB; maybe low, not absent |
| [[MAFB]] | B | MAOA activity raises MAFB's level | lines that do not express MAOA (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without MAOA | 0.056 | ⚠ within organs, on part of the lines; also absent: OAS1, CKB; maybe low, not absent |
| [[PYGB]] | B | MAOA activity raises PYGB's level | lines that do not express MAOA (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without MAOA | 0.099 | ⚠ within organs, on part of the lines; also absent: OAS1, CKB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.2, 15.6); signed map (17.1, 30.6). **Vector** length 90.6, 19.6% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +11.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.9 | +10.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.7 | +12.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | +4.7 | +14.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | +4.7 | +15.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | +0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.4 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | monoamine oxidase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:43,654,907-43,746,817 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Monoamine oxidase family |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_UP, XENOBIOTIC_METABOLISM |
| Reactome | 13 pathways, smallest: Amine Oxidase reactions; Neurotransmitter clearance; Norepinephrine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P21397](https://www.uniprot.org/uniprotkb/P21397) (Amine oxidase):

> Catalyzes the oxidative deamination of primary and some secondary amine such as neurotransmitters, with concomitant reduction of oxygen to hydrogen peroxide and has important functions in the metabolism of neuroactive and vasoactive amines in the central nervous system and peripheral tissues. Preferentially oxidizes serotonin. Also catalyzes the oxidative deamination of kynuramine to 3-(2-aminophenyl)-3-oxopropanal that can spontaneously condense to 4-hydroxyquinoline (By similarity).

**Summary**, from NCBI Gene [4128](https://www.ncbi.nlm.nih.gov/gene/4128):

> This gene is one of two neighboring gene family members that encode mitochondrial enzymes which catalyze the oxidative deamination of amines, such as dopamine, norepinephrine, and serotonin. Mutation of this gene results in Brunner syndrome. This gene has also been associated with a variety of other psychiatric disorders, including antisocial behavior. Alternatively spliced transcript variants encoding multiple isoforms have been observed. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:6833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6833) · Entrez [4128](https://www.ncbi.nlm.nih.gov/gene/4128) · UniProt [P21397](https://www.uniprot.org/uniprotkb/P21397) · Ensembl [ENSG00000189221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189221)

## Data

Gene col 12105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12105); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12105]; `tensor/DDL_lfc|DDL_z.npy` [12105]; `embed/gene_vectors.npy` [12105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12105 or target_col == 12105). Every well: [[MAOA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAOA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
