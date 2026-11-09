---
symbol: "MPP2"
type: "gene"
col: 3005
ensembl_id: "ENSG00000108852"
name: "MAGUK p55 scaffold protein 2"
location: "17q21.31"
module: 154
arm: "+"
pooled_cpm: 7.85
n_lines_expressing: 43
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 12
direction_downstream: 21
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# MPP2

*MAGUK p55 scaffold protein 2* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.32× (z +11.0, q 2e-25, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.473× (z -13.9, q 3e-41, down in 25 of 35 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTNA]] (+0.66, fdr 1e-05), [[SNTA1]] (+0.65, fdr 4e-05), [[ATG16L2]] (+0.62, fdr 3e-05); moves opposite to [[IQCH-AS1]] (-0.61, fdr 6e-05), [[LIX1-AS1]] (-0.58, fdr 7e-05), [[GNG12-AS1]] (-0.56, fdr 5e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 21 go from it, the strongest it → [[HACE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +11.0 | 2e-25 | 24/40 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +9.5 | 4e-19 | 24/40 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +7.4 | 2e-11 | 19/39 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +5.8 | 1e-06 | 14/38 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.008 | 10/37 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.032 | 11/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.067 | 6/34 (SHP-77, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | 1.29× | +3.2 | 0.11 | 1/37 (PANC-1) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.11 | 4/37 (NCI-H661, RPMI-7951, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.13 | 1/41 (MIA PaCa-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.473×** | -13.9 | 3e-41 | 25/35 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.429×** | -11.1 | 3e-26 | 23/33 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -9.1 | 2e-17 | 26/40 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.9 | 4e-13 | 25/35 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.682×** | -7.1 | 1e-10 | 17/41 (J82, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -7.1 | 2e-10 | 15/38 (NCI-H23, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -6.9 | 6e-10 | 19/39 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.593×** | -6.6 | 3e-09 | 18/38 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -6.1 | 9e-08 | 18/36 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -5.9 | 2e-07 | 16/35 (RPMI-7951, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.652×** | -5.6 | 1e-06 | 14/37 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -5.3 | 4e-06 | 16/33 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.667×** | -5.3 | 5e-06 | 14/36 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -4.9 | 3e-05 | 21/35 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -4.8 | 6e-05 | 11/20 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.700×** | -4.7 | 1e-04 | 15/39 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.746×** | -3.8 | 0.004 | 13/40 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Megestrol (drug)]] 0.5 µM |  | **0.756×** | -3.7 | 0.007 | 11/37 (CHP-212, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 46.9 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0403× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.3) |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 9 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0641× (z -13.5) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0897× (z -11.8) |
| [[J82 (line)]] | alt | 18.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 8.28 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0938× (z -13.3) |
| [[A-172 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A-427 (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 7.28 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0586× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 5.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 3.38 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0514× (z -10.5) |
| [[PANC-1 (line)]] | alt | 2.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.8) |
| [[RKO (line)]] | wt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 6.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0756× (z -9.1) |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -9.2) |
| [[SW480 (line)]] | alt | 6.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.6) |
| [[A498 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNA]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.65 | +0.66 / +0.42 | both halves | 4e-05 | same gene group |
| [[ATG16L2]] | +0.62 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PPP2R5B]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TMEM145]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.60 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[ZNRF1]] | +0.59 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[RASSF2]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.58 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[RGS9]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CDON]] | +0.57 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[UBA6]] | +0.57 | +0.62 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCH-AS1]] | -0.61 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[LIX1-AS1]] | -0.58 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[GNG12-AS1]] | -0.56 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[GABPB1-AS1]] | -0.55 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[CCDC90B-AS1]] | -0.55 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[WARS2-AS1]] | -0.55 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[LINC00571]] | -0.55 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[RFX3-DT]] | -0.55 | -0.51 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[HNF4G]] | -0.55 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[EPM2A]] | -0.54 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[PCAT1]] | -0.54 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[HCG17]] | -0.54 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[DPH5-DT]] | -0.53 | -0.53 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MPP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM145]] | B | TMEM145 activity raises MPP2's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without TMEM145 | 0.028 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[TTLL7]] | B | TTLL7 activity raises MPP2's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without TTLL7 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MPP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MPP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SNTA1]] | B | SNTA1 activity raises MPP2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without SNTA1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[SARDH]] | B | SARDH activity raises MPP2's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without SARDH | 0.090 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[ASRGL1]] | B | ASRGL1 activity lowers MPP2's level | lines that do not express ASRGL1 (7) vs lines expressing it (43) | 1.36× higher at baseline in the lines without ASRGL1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, LINC02026, MYO15B; maybe low, not absent |
| [[NRN1]] | B | NRN1 activity raises MPP2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without NRN1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[FAM229B]] | C | FAM229B activity raises MPP2's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 4.01× lower at baseline in the lines without FAM229B | 0.040 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT; co-absent with the target |
| [[SMARCD3]] | C | SMARCD3 activity raises MPP2's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[WDR54]] | C | WDR54 activity raises MPP2's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without WDR54 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | B | MPP2 activity raises HACE1's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.29× lower at baseline in the lines without MPP2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[SMARCD3]] | B | MPP2 activity raises SMARCD3's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.47× lower at baseline in the lines without MPP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[FAM234B]] | B | MPP2 activity raises FAM234B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without MPP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[WDR54]] | B | MPP2 activity raises WDR54's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.05× lower at baseline in the lines without MPP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[ZNF8-DT]] | B | MPP2 activity raises ZNF8-DT's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without MPP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[IQCH-AS1]] | B | MPP2 activity strengthens IQCH-AS1's drug response | lines that do not express MPP2 (7) vs lines expressing it (41) | the lines without MPP2 respond 0.76× as strongly (z diff +0.71); strongest at Homoharringtonine 5 µM: 0.95x vs 2.31x (z diff +5.5) | 0.020 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT; target measured in part of the lines; both ways; artifact flags |
| [[MAD2L2]] | B | MPP2 activity raises MAD2L2's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without MPP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[TTLL7]] | B | MPP2 activity raises TTLL7's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.84× lower at baseline in the lines without MPP2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[PCAT1]] | B | MPP2 activity lowers PCAT1's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.36× higher at baseline in the lines without MPP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[CHD1L]] | B | MPP2 activity raises CHD1L's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.22× lower at baseline in the lines without MPP2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[SH3PXD2B]] | B | MPP2 activity raises SH3PXD2B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.74× lower at baseline in the lines without MPP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[DNMT3B]] | B | MPP2 activity raises DNMT3B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.20× lower at baseline in the lines without MPP2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.4, -3.1); signed map (-6.5, 47.9). **Vector** length 76.3, 14.3% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +11.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.0 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -13.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.1 | -5.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -4.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MAGUK p55 scaffold protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,875,357-43,909,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761D0712; previously DLG2 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14168](https://www.uniprot.org/uniprotkb/Q14168) (MAGUK p55 subfamily member 2):

> Postsynaptic MAGUK scaffold protein that links CADM1 cell adhesion molecules to core components of the postsynaptic density (By similarity). In CA1 pyramidal neurons, required for synaptic KCNN2-containing channel function and long-term potentiation expression (By similarity). Seems to negatively regulate SRC function in epithelial cells.

**Summary**, from NCBI Gene [4355](https://www.ncbi.nlm.nih.gov/gene/4355):

> Palmitoylated membrane protein 2 is a member of a family of membrane-associated proteins termed MAGUKs (membrane-associated guanylate kinase homologs). MAGUKs interact with the cytoskeleton and regulate cell proliferation, signaling pathways, and intracellular junctions. Palmitoylated membrane protein 2 contains a conserved sequence, called the SH3 (src homology 3) motif, found in several other proteins that associate with the cytoskeleton and are suspected to play important roles in signal …

**Accessions** — [HGNC:7220](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7220) · Entrez [4355](https://www.ncbi.nlm.nih.gov/gene/4355) · UniProt [Q14168](https://www.uniprot.org/uniprotkb/Q14168) · Ensembl [ENSG00000108852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108852)

## Data

Gene col 3005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3005); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3005]; `tensor/DDL_lfc|DDL_z.npy` [3005]; `embed/gene_vectors.npy` [3005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3005 or target_col == 3005). Every well: [[MPP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
