---
symbol: "SPAG4"
type: "gene"
col: 700
ensembl_id: "ENSG00000061656"
name: "sperm associated antigen 4"
location: "20q11.22"
module: 103
arm: "+"
pooled_cpm: 8.81
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# SPAG4

*sperm associated antigen 4* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.84× (z +13.9, q 5e-41, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.283× (z -16.7, q 0e+00, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD27-AS1]] (+0.62, fdr 2e-04), [[OGFOD2]] (+0.61, fdr 1e-05), [[TMEM134]] (+0.59, fdr 6e-05); moves opposite to [[CPT1A]] (-0.57, fdr 4e-05), [[DNAH14]] (-0.57, fdr 1e-05), [[COA7]] (-0.56, fdr 2e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[KBTBD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +13.9 | 5e-41 | 36/37 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +8.5 | 4e-15 | 26/35 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +7.2 | 2e-10 | 25/35 (Hs 766T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.003 | 18/41 (NCI-H2030, A498, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.84×** | +3.9 | 0.012 | 13/36 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.081 | 5/37 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.081 | 8/39 (CFPAC-1, C32, …) | top dose only | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.097 | 10/38 (J82, HOP62, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.61× | +3.0 | 0.15 | 8/37 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.283×** | -16.7 | 0e+00 | 35/38 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.229×** | -13.8 | 4e-41 | 33/37 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.288×** | -11.7 | 3e-29 | 34/40 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.299×** | -10.9 | 2e-25 | 38/40 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -9.7 | 3e-20 | 28/37 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.362×** | -9.5 | 1e-19 | 31/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.364×** | -9.5 | 2e-19 | 35/41 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.392×** | -8.8 | 1e-16 | 31/40 (NCI-H1792, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.404×** | -8.5 | 1e-15 | 31/40 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.479×** | -6.9 | 3e-10 | 23/40 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.518×** | -6.2 | 4e-08 | 24/39 (RPMI-7951, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.507×** | -6.1 | 4e-08 | 23/34 (NCI-H1792, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -5.8 | 3e-07 | 23/40 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -5.8 | 3e-07 | 22/41 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -4.9 | 4e-05 | 21/37 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.600×** | -4.8 | 6e-05 | 19/41 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.606×** | -4.7 | 9e-05 | 19/38 (HOP62, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 34.4 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0628× (z -16.5) |
| [[HOP62 (line)]] | alt | 17.8 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -15.3) |
| [[PANC-1 (line)]] | alt | 12.1 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.2) | [[Digitoxin (drug)]] 0.5 µM 0.159× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0271× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 19.3 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.6) |
| [[Hs 766T (line)]] | wt | 16.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.0) |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.0) |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -9.9) |
| [[HS-578T (line)]] | alt | 8.60 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0495× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0507× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 8.77 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +10.5) | [[Harringtonine (drug)]] 5 µM 0.0628× (z -12.7) |
| [[SW480 (line)]] | alt | 5.12 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -10.0) |
| [[A549 (line)]] | wt | 5.85 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -15.8) |
| [[COLO 205 (line)]] | alt | 7.27 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0370× (z -10.5) |
| [[KATO III (line)]] | alt | 6.27 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0934× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 8.88 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +11.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 8.56 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 3.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0385× (z -9.5) |
| [[J82 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 5.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 8.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.1) |
| [[A-172 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.992 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD27-AS1]] | +0.62 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[OGFOD2]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TMEM134]] | +0.59 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[WDR20]] | +0.59 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[POLR2A]] | +0.59 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[RECQL5]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[GTF2B]] | +0.57 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[DNAJC4]] | +0.57 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[SUOX]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[NIM1K]] | +0.56 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[INTS6L]] | +0.56 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[IKZF4]] | +0.56 | +0.37 / +0.57 | both halves | 8e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1A]] | -0.57 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DNAH14]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[COA7]] | -0.56 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[ZC3H14]] | -0.56 | -0.40 / -0.65 | both halves | 4e-05 |  |
| [[EFR3A]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.54 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[MATR3-1]] | -0.54 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[RBFA]] | -0.54 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[AGPS]] | -0.53 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[CIAO1]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MAP9]] | -0.53 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[MCUR1]] ⚠ | -0.52 | -0.33 / -0.56 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[FKTN]] | -0.52 | -0.29 / -0.57 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPAG4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KBTBD4]] | B | SPAG4 activity raises KBTBD4's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without SPAG4 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |
| [[NARF]] | B | SPAG4 activity raises NARF's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without SPAG4 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |
| [[DNAJC4]] | B | SPAG4 activity raises DNAJC4's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without SPAG4 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |
| [[GUCD1]] | B | SPAG4 activity raises GUCD1's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without SPAG4 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |
| [[RBFA]] | B | SPAG4 activity lowers RBFA's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without SPAG4 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.5, -14.7); signed map (2.4, 12.9). **Vector** length 82.4, 17.7% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +13.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.1 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -10.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,615,829-35,621,094 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUN4, CT127 |
| Gene groups (HGNC) | SUN family |
| Hallmark sets | GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPE6](https://www.uniprot.org/uniprotkb/Q9NPE6) (Sperm-associated antigen 4 protein):

> Involved in spermatogenesis. Required for sperm head formation but not required to establish and maintain general polarity of the sperm head. Required for anchoring and organization of the manchette. Required for targeting of SUN3 and probably SYNE1 through a probable SUN1:SYNE3 LINC complex to the nuclear envelope and involved in accurate posterior sperm head localization of the complex. May anchor SUN3 the nuclear envelope. Involved in maintenance of the nuclear envelope integrity. May assist …

**Summary**, from NCBI Gene [6676](https://www.ncbi.nlm.nih.gov/gene/6676):

> The mammalian sperm flagellum contains two cytoskeletal structures associated with the axoneme: the outer dense fibers surrounding the axoneme in the midpiece and principal piece and the fibrous sheath surrounding the outer dense fibers in the principal piece of the tail. Defects in these structures are associated with abnormal tail morphology, reduced sperm motility, and infertility. In the rat, the protein encoded by this gene associates with an outer dense fiber protein via a leucine zipper …

**Accessions** — [HGNC:11214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11214) · Entrez [6676](https://www.ncbi.nlm.nih.gov/gene/6676) · UniProt [Q9NPE6](https://www.uniprot.org/uniprotkb/Q9NPE6) · Ensembl [ENSG00000061656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061656)

## Data

Gene col 700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 700); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 700]; `tensor/DDL_lfc|DDL_z.npy` [700]; `embed/gene_vectors.npy` [700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 700 or target_col == 700). Every well: [[SPAG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
