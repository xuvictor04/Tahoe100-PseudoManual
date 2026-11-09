---
symbol: "POTEF"
type: "gene"
col: 12247
ensembl_id: "ENSG00000196604"
name: "POTE ankyrin domain family member F"
location: "2q21.1"
module: 17
arm: "+"
pooled_cpm: 12.54
n_lines_expressing: 21
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# POTEF

*POTE ankyrin domain family member F* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.16× (z +20.0, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.765× (z -4.6, q 0.002, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POTEE]] (+0.73, fdr 7e-06), [[FAR2P1]] (+0.68, fdr 1e-05, ⚠ same locus), [[THOC1]] (+0.58, fdr 4e-05), [[DHRS2]] (+0.57, fdr 2e-05); moves opposite to [[TMEM11-DT]] (-0.52, fdr 2e-04), [[FBXW11]] (-0.48, fdr 7e-05), [[METTL4]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[POTEE]] → it (grade C ⚠); 9 go from it, the strongest it → [[ZNF30]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +20.0 | 0e+00 | 16/19 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.48×** | +15.4 | 0e+00 | 19/19 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.44×** | +15.2 | 0e+00 | 19/19 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +11.1 | 2e-26 | 17/19 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +9.7 | 5e-20 | 16/19 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +8.5 | 1e-15 | 15/19 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.1 | 9e-08 | 15/19 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.7 | 1e-06 | 1/18 (SW48) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.6 | 1e-06 | 12/19 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +5.3 | 6e-06 | 9/19 (NCI-H1573, C-33 A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.2 | 9e-06 | 5/19 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.9 | 5e-05 | 6/19 (HepG2/C3A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 1e-04 | 9/19 (C-33 A, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 7e-04 | 0/19 | two highest doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +4.3 | 7e-04 | 11/19 (HepG2/C3A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +3.7 | 0.007 | 12/19 (NCI-H1573, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.009 | 0/19 | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.765×** | -4.6 | 0.002 | 15/19 (HS-578T, H4, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.704×** | -4.0 | 0.019 | 0/19 | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.741×** | -3.7 | 0.044 | 6/19 (SNU-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM |  | 0.832× | -3.2 | 0.20 | 7/19 (HS-578T, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 140 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.0746× (z -18.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.0 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.83× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.358× (z -9.0) |
| [[LS 180 (line)]] | wt | 20.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +15.3) | — |
| [[SNU-1 (line)]] | wt | 66.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -13.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 77.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.146× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 70.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 52.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 8.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +9.7) | — |
| [[SW480 (line)]] | alt | 4.52 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.47× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -13.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +10.9) | — |
| [[A-172 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POTEE]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[FAR2P1]] | +0.68 | +0.53 / +0.76 | both halves | 1e-05 | ⚠ same locus (33.0 kb, same strand: neighbours can correlate without regulation) |
| [[THOC1]] | +0.58 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[DHRS2]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[IFTAP]] | +0.55 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[LINC01518]] | +0.55 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[HOOK1]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ANKRD24]] | +0.55 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[STRA6LP]] | +0.54 | +0.41 / +0.37 | both halves | 7e-05 |  |
| [[CCDC113]] | +0.52 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[ROGDI]] | +0.52 | +0.43 / +0.29 | both halves | 2e-04 |  |
| [[MLST8]] | +0.52 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[RNF214]] | +0.52 | +0.32 / +0.50 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.52 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[FBXW11]] | -0.48 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[METTL4]] | -0.47 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[PRDM10]] | -0.47 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[PRDX1]] | -0.47 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[MCM9]] | -0.47 | -0.52 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[EXOSC3]] | -0.46 | -0.35 / -0.24 | both halves | 5e-04 |  |
| [[TXN]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SAP30L-AS1]] | -0.46 | -0.24 / -0.35 | both halves | 4e-04 |  |
| [[SNTB2]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[MICB]] | -0.45 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[SFXN5]] | -0.44 | -0.28 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POTEE]] | C | POTEE activity raises POTEF's level | lines that do not express POTEE (29) vs lines expressing it (21) | 10.32× lower at baseline in the lines without POTEE | 9e-06 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises POTEF's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 4.30× lower at baseline in the lines without CCDC144NL-AS1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[PHF2P2]] | C | PHF2P2 activity raises POTEF's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.39× lower at baseline in the lines without PHF2P2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[AACSP1]] | C | AACSP1 activity raises POTEF's level | lines that do not express AACSP1 (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without AACSP1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00408, ENSG00000277757, NAA11; co-absent with the target |
| [[LINC02327]] | C | LINC02327 activity raises POTEF's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 2.18× lower at baseline in the lines without LINC02327 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF30]] | B | POTEF activity raises ZNF30's level | lines that do not express POTEF (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without POTEF | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[BSN]] | B | POTEF activity raises BSN's level | lines that do not express POTEF (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without POTEF | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[DHRS2]] | B | [[FAR2P1]], POTEF activity raises DHRS2's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 2.84× lower at baseline in the lines without FAR2P1, POTEF | 0.018 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[MLST8]] | B | [[FAR2P1]], POTEF activity raises MLST8's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 1.19× lower at baseline in the lines without FAR2P1, POTEF | 0.037 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[CEP63]] | B | [[FAR2P1]], POTEF activity raises CEP63's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 1.21× lower at baseline in the lines without FAR2P1, POTEF | 0.062 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[AMOT]] | B | POTEF activity raises AMOT's level | lines that do not express POTEF (29) vs lines expressing it (21) | 1.60× lower at baseline in the lines without POTEF | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[POTEE]] | C | [[FAR2P1]], POTEF activity raises POTEE's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 3.25× lower at baseline in the lines without FAR2P1, POTEF | 0.001 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target; co-absent genes |
| [[CCDC144NL-AS1]] | C | POTEF activity raises CCDC144NL-AS1's level | lines that do not express POTEF (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without POTEF | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[NFASC]] | C | POTEF activity raises NFASC's level | lines that do not express POTEF (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without POTEF | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.0, 27.7); signed map (0.1, -7.1). **Vector** length 48.4, 11.6% of its response variance represented; |z| ≥ 3 in 469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +15.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +5.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | POTE ankyrin domain family member F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,073,535-130,129,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POTEACTIN, POTE2alpha; previously A26C1B |
| Gene groups (HGNC) | POTE ankyrin domain containing |
| Matched by | ensembl_id |

UniProt [A5A3E0](https://www.uniprot.org/uniprotkb/A5A3E0) carries no function annotation.

**Summary**, from NCBI Gene [728378](https://www.ncbi.nlm.nih.gov/gene/728378):

> Predicted to enable protein kinase binding activity. Predicted to be a structural constituent of postsynaptic actin cytoskeleton. Predicted to be involved in axonogenesis and cell motility. Located in blood microparticle; extracellular exosome; and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33905) · Entrez [728378](https://www.ncbi.nlm.nih.gov/gene/728378) · UniProt [A5A3E0](https://www.uniprot.org/uniprotkb/A5A3E0) · Ensembl [ENSG00000196604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196604)

## Data

Gene col 12247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12247); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12247]; `tensor/DDL_lfc|DDL_z.npy` [12247]; `embed/gene_vectors.npy` [12247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12247 or target_col == 12247). Every well: [[POTEF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POTEF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
