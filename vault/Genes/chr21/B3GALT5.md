---
symbol: "B3GALT5"
type: "gene"
col: 11454
ensembl_id: "ENSG00000183778"
name: "beta-1,3-galactosyltransferase 5"
location: "21q22.2"
module: 8
arm: "+"
pooled_cpm: 11.71
n_lines_expressing: 24
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 39
direction_downstream: 24
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# B3GALT5

*beta-1,3-galactosyltransferase 5* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.45× (z +9.8, q 5e-20, up in 1 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +6.9, q 9e-10, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.428× (z -9.7, q 1e-19, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRB]] (+0.67, fdr 1e-05), [[PTPRR]] (+0.61, fdr 1e-05), [[SLCO1B3]] (+0.60, fdr 1e-05); moves opposite to [[HIPK3]] (-0.47, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[STYK1]] → it (grade B ⚠); 24 go from it, the strongest it → [[SLC52A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +9.8 | 5e-20 | 1/10 (NCI-H1792) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +9.2 | 1e-17 | 1/12 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.6 | 8e-12 | 6/18 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.9 | 9e-10 | 10/21 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.5 | 1e-08 | 3/21 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.6 | 2e-06 | 8/20 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.009 | 3/20 (SNU-423, A-172, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.015 | 2/20 (Hs 766T, LOX-IMVI) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.428×** | -9.7 | 1e-19 | 18/20 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -8.5 | 7e-15 | 16/21 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -7.9 | 6e-13 | 14/21 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -5.7 | 1e-06 | 15/20 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.008 | 8/21 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -3.6 | 0.032 | 10/20 (H4, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.044 | 4/20 (SW48, HT-29, …) | top dose only |  |
| [[Resveratrol (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.046 | 9/21 (LS 180, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.746×** | -3.4 | 0.048 | 11/20 (HEC-1-A, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.751×** | -3.3 | 0.058 | 9/21 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -3.2 | 0.063 | 10/21 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -3.2 | 0.063 | 14/19 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.063 | 11/18 (HEC-1-A, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.763×** | -3.1 | 0.078 | 7/21 (H4, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 210 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0816× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 26.6 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -12.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.6) |
| [[LoVo (line)]] | wt | 81.3 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0911× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -17.3) |
| [[H4 (line)]] | wt | 20.0 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0341× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 57.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 3 (2 ⚠) | — | [[Budesonide (drug)]] 0.05 µM 0.158× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 8.28 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0805× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.06 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.56× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.141× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 4.97 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0654× (z -9.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H2030 (line)]] | alt | 4.93 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0696× (z -9.8) |
| [[SNU-423 (line)]] | alt | 7.83 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.102× (z -9.2) |
| [[A-172 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRB]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[PTPRR]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SLCO1B3]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[ANKRD22]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ST14]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[AOAH]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ADGRF1]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MECOM]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[PRSS12]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[LINC02474]] | +0.55 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[GCNT3]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 | STRING 571 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIPK3]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 5, C 34. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STYK1]] | B | STYK1 activity raises B3GALT5's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without STYK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[PRSS12]] | B | PRSS12 activity raises B3GALT5's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without PRSS12 | 0.053 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[TMPRSS3]] | B | TMPRSS3 activity raises B3GALT5's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.58× lower at baseline in the lines without TMPRSS3 | 0.057 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[AMIGO2]] | B | AMIGO2 activity raises B3GALT5's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.71× lower at baseline in the lines without AMIGO2 | 0.089 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[MECOM]] | B | MECOM activity raises B3GALT5's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without MECOM | 0.098 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[DSG3]] | C | DSG3 activity raises B3GALT5's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 6.06× lower at baseline in the lines without DSG3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises B3GALT5's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 4.13× lower at baseline in the lines without PADI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[PTPRB]] | C | PTPRB activity raises B3GALT5's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.79× lower at baseline in the lines without PTPRB | 0.012 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises B3GALT5's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.20× lower at baseline in the lines without SLC14A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises B3GALT5's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.47× lower at baseline in the lines without EPS8L3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises B3GALT5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.13× lower at baseline in the lines without ADGRF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises B3GALT5's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.41× lower at baseline in the lines without GCNT3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 5, C 19. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC52A3]] | B | B3GALT5 activity raises SLC52A3's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without B3GALT5 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[MECOM]] | B | B3GALT5 activity raises MECOM's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without B3GALT5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[AMIGO2]] | B | B3GALT5 activity raises AMIGO2's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without B3GALT5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[GPR39]] | B | B3GALT5 activity raises GPR39's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without B3GALT5 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[CNGA1]] | B | B3GALT5 activity raises CNGA1's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without B3GALT5 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |
| [[PTPRB]] | C | B3GALT5 activity raises PTPRB's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 3.03× lower at baseline in the lines without B3GALT5 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[PTPRR]] | C | B3GALT5 activity raises PTPRR's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 3.06× lower at baseline in the lines without B3GALT5 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[USH1C]] | C | B3GALT5 activity raises USH1C's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 3.18× lower at baseline in the lines without B3GALT5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[SLC14A1]] | C | B3GALT5 activity raises SLC14A1's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without B3GALT5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[MYO7B]] | C | B3GALT5 activity raises MYO7B's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without B3GALT5 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[HKDC1]] | C | B3GALT5 activity raises HKDC1's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 3.29× lower at baseline in the lines without B3GALT5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |
| [[UGT1A6]] | C | B3GALT5 activity raises UGT1A6's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without B3GALT5 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.2, 54.5); signed map (64.3, 3.4). **Vector** length 65.1, 16.9% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -9.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-galactosyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,556,442-39,673,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta3Gal-T5, B3GalT-V, GLCT5, B3T5 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 3 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2C3](https://www.uniprot.org/uniprotkb/Q9Y2C3) (Beta-1,3-galactosyltransferase 5):

> Catalyzes the transfer of Gal to GlcNAc-based acceptors with a preference for the core3 O-linked glycan GlcNAc(beta1,3)GalNAc structure. Can use glycolipid LC3Cer as an efficient acceptor.

**Summary**, from NCBI Gene [10317](https://www.ncbi.nlm.nih.gov/gene/10317):

> This gene encodes a member of a family of membrane-bound glycoproteins. The encoded protein may synthesize type 1 Lewis antigens, which are elevated in gastrointestinal and pancreatic cancers. Alternatively spliced transcript variants using multiple alternate promoters have been observed for this gene. [provided by RefSeq, Sep 2017]

**Accessions** — [HGNC:920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:920) · Entrez [10317](https://www.ncbi.nlm.nih.gov/gene/10317) · UniProt [Q9Y2C3](https://www.uniprot.org/uniprotkb/Q9Y2C3) · Ensembl [ENSG00000183778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183778)

## Data

Gene col 11454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11454); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11454]; `tensor/DDL_lfc|DDL_z.npy` [11454]; `embed/gene_vectors.npy` [11454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11454 or target_col == 11454). Every well: [[B3GALT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
