---
symbol: "ATXN2L"
type: "gene"
col: 9658
ensembl_id: "ENSG00000168488"
name: "ataxin 2 like"
location: "16p11.2"
module: 126
arm: "+"
pooled_cpm: 115.2
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# ATXN2L

*ataxin 2 like* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.82× (z +8.8, q 7e-16, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.76× (z +8.4, q 2e-14, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.594× (z -7.8, q 4e-12, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATN1]] (+0.67, fdr 1e-05), [[UBQLN4]] (+0.61, fdr 3e-05), [[MTA2]] (+0.59, fdr 3e-05); moves opposite to [[SEC61G]] (-0.51, fdr 2e-04), [[MYO1E]] (-0.50, fdr 3e-04), [[IMP3]] (-0.50, fdr 2e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +8.8 | 7e-16 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +8.4 | 2e-14 | 45/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.68×** | +7.6 | 4e-12 | 42/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +7.5 | 1e-11 | 34/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +7.1 | 2e-10 | 45/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +6.9 | 4e-10 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.4 | 1e-08 | 41/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +6.2 | 4e-08 | 46/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 4e-07 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +5.4 | 3e-06 | 36/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.001 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.028 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.035 | 24/48 (A498, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.18× | +3.3 | 0.035 | 22/48 (SW480, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.594×** | -7.8 | 4e-12 | 45/48 (AsPC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.669×** | -6.0 | 5e-07 | 43/48 (AsPC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -5.3 | 3e-05 | 40/48 (AsPC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -4.8 | 2e-04 | 26/48 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -4.8 | 2e-04 | 37/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.825×** | -3.9 | 0.008 | 19/49 (SNU-1, NCI-H23, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -3.9 | 0.008 | 28/47 (AN3 CA, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.779×** | -3.8 | 0.012 | 30/49 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.11 | 21/48 (LOX-IMVI, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 104 | 9 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.28× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 4.48× (z +18.0) | — |
| [[PANC-1 (line)]] | alt | 140 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.6) | — |
| [[SW480 (line)]] | alt | 115 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.25× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 198 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -12.5) |
| [[HOP62 (line)]] | alt | 73.2 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.50× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 90.3 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.54× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.9) | — |
| [[LoVo (line)]] | wt | 79.1 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.10× (z +12.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 103 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.85× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 128 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.89× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.498× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 105 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -9.5) |
| [[SNU-1 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -8.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A-427 (line)]] | wt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.1) | — |
| [[A498 (line)]] | wt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.5) | — |
| [[A549 (line)]] | wt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 70.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.37× (z +12.4) ⚠ toxic | — |
| [[HEC-1-A (line)]] | alt | 94.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 103 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.7) |
| [[SNU-423 (line)]] | alt | 97.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 94.0 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0863× (z -9.1) |
| [[SW 900 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.91× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 142 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 133 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATN1]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.61 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[MTA2]] | +0.59 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SLC4A2]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[TMEM268]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ATP13A1]] | +0.58 | +0.37 / +0.61 | both halves | 9e-05 |  |
| [[SGPL1]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GAA]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[STRN4]] | +0.56 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[U2AF2]] | +0.56 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[CNOT1]] | +0.55 | +0.52 / +0.59 | both halves | 1e-05 | STRING 474 |
| [[MBD6]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61G]] | -0.51 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MYO1E]] | -0.50 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[IMP3]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[POMP]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[SF3B6]] | -0.49 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[METTL23]] | -0.49 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[MRPL51]] ⚠ | -0.49 | -0.28 / -0.54 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | -0.48 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | -0.47 | -0.36 / -0.50 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GCC2]] | -0.47 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | -0.46 | -0.30 / -0.52 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PLIN3]] | -0.46 | -0.18 / -0.50 | ⚠ not reproduced | 0.001 |  |
| [[ACTR6]] | -0.46 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CTR9]] | -0.46 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SPCS1]] | -0.46 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[FAM32A]] | -0.46 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ATXN2L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ATXN2L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, -24.1); signed map (-12.7, -35.5). **Vector** length 96.6, 30.3% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.0 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.5 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,822,999-28,837,237 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A2lp, A2D |
| Gene groups (HGNC) | Ataxin 2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWM7](https://www.uniprot.org/uniprotkb/Q8WWM7) (Ataxin-2-like protein):

> Involved in the regulation of stress granule and P-body formation.

**Summary**, from NCBI Gene [11273](https://www.ncbi.nlm.nih.gov/gene/11273):

> This gene encodes an ataxin type 2 related protein of unknown function. This protein is a member of the spinocerebellar ataxia (SCAs) family, which is associated with a complex group of neurodegenerative disorders. Several alternatively spliced transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:31326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31326) · Entrez [11273](https://www.ncbi.nlm.nih.gov/gene/11273) · UniProt [Q8WWM7](https://www.uniprot.org/uniprotkb/Q8WWM7) · Ensembl [ENSG00000168488](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168488)

## Data

Gene col 9658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9658); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9658]; `tensor/DDL_lfc|DDL_z.npy` [9658]; `embed/gene_vectors.npy` [9658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9658 or target_col == 9658). Every well: [[ATXN2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
