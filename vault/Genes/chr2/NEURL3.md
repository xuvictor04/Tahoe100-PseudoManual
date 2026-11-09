---
symbol: "NEURL3"
type: "gene"
col: 8636
ensembl_id: "ENSG00000163121"
name: "neuralized E3 ubiquitin protein ligase 3"
location: "2q11.2"
module: 14
arm: "+"
pooled_cpm: 5.11
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 21
direction_downstream: 34
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NEURL3

*neuralized E3 ubiquitin protein ligase 3* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 14.3× (z +20.7, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.447× (z -4.4, q 0.004, down in 18 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NINJ1]] (+0.79, fdr 7e-06), [[RASGRP1]] (+0.74, fdr 7e-06), [[LTB]] (+0.71, fdr 7e-06); moves opposite to [[NUP155]] (-0.57, fdr 1e-05), [[ZNF731P]] (-0.57, fdr 1e-05), [[NCBP1]] (-0.56, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[MAF]] → it (grade B ⚠); 34 go from it, the strongest it → [[NUP155]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **14.3×** | +20.7 | 0e+00 | 29/29 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **14.3×** | +14.6 | 0e+00 | 28/28 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **8.16×** | +11.1 | 2e-26 | 30/31 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.67×** | +8.5 | 3e-15 | 29/32 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +8.4 | 5e-15 | 22/30 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **3.37×** | +6.7 | 2e-09 | 28/31 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +6.4 | 1e-08 | 22/35 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.77×** | +5.6 | 1e-06 | 21/34 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +5.5 | 3e-06 | 16/24 (NCI-H1573, SNU-423, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 19/33 (A549, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.14×** | +4.2 | 0.001 | 18/30 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[venetoclax (drug)]] 5 µM |  | **3.50×** | +3.6 | 0.014 | 7/21 (HEC-1-A, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.017 | 14/32 (MIA PaCa-2, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.447×** | -4.4 | 0.004 | 18/32 (A498, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.452×** | -4.3 | 0.004 | 19/32 (Hs 766T, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.468×** | -4.2 | 0.006 | 17/34 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.497×** | -3.8 | 0.017 | 16/32 (A498, AsPC-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.501×** | -3.8 | 0.017 | 18/34 (A549, A498, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.515×** | -3.6 | 0.024 | 14/31 (SW 900, A498, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **0.517×** | -3.6 | 0.024 | 13/35 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.525×** | -3.5 | 0.030 | 15/35 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.540×** | -3.4 | 0.047 | 10/33 (A498, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.549×** | -3.3 | 0.056 | 18/30 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.551×** | -3.3 | 0.056 | 14/33 (COLO 205, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0584× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[CFPAC-1 (line)]] | alt | 21.8 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0349× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[HEC-1-A (line)]] | alt | 10.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +14.2) | — |
| [[A498 (line)]] | wt | 13.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 20.9× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[J82 (line)]] | alt | 4.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.0× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 26.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[NCI-H2347 (line)]] | alt | 5.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 1.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 1.49 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 36.9× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +13.6) | — |
| [[A549 (line)]] | wt | 7.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 72.3× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 7.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 1.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.8× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 6.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 4.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.0× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 2.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 2.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 6.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 3.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +9.7) | — |
| [[SW480 (line)]] | alt | 1.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +9.3) | — |
| [[A-427 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.867 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NINJ1]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[RASGRP1]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[LTB]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[STAP2]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[IL32]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[SLC41A2]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PIK3IP1]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[TNFRSF9]] | +0.68 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[CCL5]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[LACTB]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[SLC2A6]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.56 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[ATP2A2]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ATP1A1]] | -0.55 | -0.63 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAF]] | B | MAF activity raises NEURL3's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.12× lower at baseline in the lines without MAF | 0.002 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[GBP5]] | B | GBP5 activity raises NEURL3's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.07× lower at baseline in the lines without GBP5 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[GBP2]] | B | GBP2 activity raises NEURL3's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CD5L]] | B | CD5L activity raises NEURL3's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.91× lower at baseline in the lines without CD5L | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[STK32A]] | B | STK32A activity raises NEURL3's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without STK32A | 0.013 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[IL15]] | B | IL15 activity raises NEURL3's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without IL15 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ADAM7-AS1]] | B | ADAM7-AS1 activity raises NEURL3's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without ADAM7-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[TNFAIP6]] | B | TNFAIP6 activity raises NEURL3's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without TNFAIP6 | 0.038 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[LINC02384]] | B | LINC02384 activity weakens NEURL3's drug response | lines that do not express LINC02384 (19) vs lines expressing it (16) | the lines without LINC02384 respond 1.47× as strongly (z diff -1.19); strongest at Harringtonine 5 µM: 9.67x vs 6.01x (z diff -2.2) | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IL15RA]] | B | IL15RA activity raises NEURL3's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without IL15RA | 0.044 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[RRAD]] | B | RRAD activity raises NEURL3's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without RRAD | 0.048 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[DUSP10]] | B | DUSP10 activity raises NEURL3's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without DUSP10 | 0.062 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 30, C 4. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP155]] | B | NEURL3 activity lowers NUP155's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.51× higher at baseline in the lines without NEURL3 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[KIAA1217]] | B | NEURL3 activity raises KIAA1217's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without NEURL3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[TNIP1]] | B | NEURL3 activity raises TNIP1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without NEURL3 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[IL15]] | B | NEURL3 activity raises IL15's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 3.12× lower at baseline in the lines without NEURL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[RAB9A]] | B | NEURL3 activity raises RAB9A's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without NEURL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[NR1D1]] | B | NEURL3 activity raises NR1D1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without NEURL3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[TBC1D8]] | B | NEURL3 activity raises TBC1D8's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without NEURL3 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[CCL5]] | B | NEURL3 activity raises CCL5's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 4.04× lower at baseline in the lines without NEURL3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[MAF]] | B | NEURL3 activity raises MAF's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 3.44× lower at baseline in the lines without NEURL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[GBP4]] | B | NEURL3 activity raises GBP4's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 3.33× lower at baseline in the lines without NEURL3 | 0.017 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[TNFRSF1B]] | B | NEURL3 activity raises TNFRSF1B's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without NEURL3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[RAB24]] | B | NEURL3 activity raises RAB24's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without NEURL3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 2.2); signed map (42.7, 10.5). **Vector** length 99.1, 30.2% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNFR2 non-canonical NF-kB pathway* (reactome, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +20.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +1.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | neuralized E3 ubiquitin protein ligase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,497,646-96,508,109 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Lincr, LOC93082, RNF132 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EH8](https://www.uniprot.org/uniprotkb/Q96EH8) (E3 ubiquitin-protein ligase NEURL3):

> E3 ubiquitin-protein ligase that plays a role in various biological processes such as lung development or innate immunity. Seems to utilize UBE2E1. Promotes innate antiviral response by catalyzing 'Lys-63'-linked ubiquitination of IRF7. Also inhibits hepatitis C virus assembly by directly binding to viral E1 envelope glycoprotein to disrupt its interaction with E2. Plays an essential role in TLR4-mediated activation of MAPK pathways by promoting 'Lys-48'-linked polyubiquitination of the …

**Summary**, from NCBI Gene [93082](https://www.ncbi.nlm.nih.gov/gene/93082):

> Enables ubiquitin protein ligase activity. Involved in positive regulation of proteasomal protein catabolic process. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25162) · Entrez [93082](https://www.ncbi.nlm.nih.gov/gene/93082) · UniProt [Q96EH8](https://www.uniprot.org/uniprotkb/Q96EH8) · Ensembl [ENSG00000163121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163121)

## Data

Gene col 8636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8636); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8636]; `tensor/DDL_lfc|DDL_z.npy` [8636]; `embed/gene_vectors.npy` [8636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8636 or target_col == 8636). Every well: [[NEURL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEURL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
