---
symbol: "DENND11"
type: "gene"
col: 15021
ensembl_id: "ENSG00000257093"
name: "DENN domain containing 11"
location: "7q34"
module: 176
arm: "+"
pooled_cpm: 40.15
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 36
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# DENND11

*DENN domain containing 11* — 7q34

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.263× (z -41.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC43A1]] (+0.54, fdr 1e-05), [[CIBAR1]] (+0.52, fdr 4e-05), [[EPHX4]] (+0.50, fdr 3e-05); moves opposite to [[SAP30BP]] (-0.50, fdr 4e-05), [[SNAI2]] (-0.48, fdr 3e-05), [[OSMR]] (-0.47, fdr 4e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ENPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 1.15× | +4.3 | 0.010 | 17/48 (Hs 766T, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.16× | +3.3 | 0.28 | 11/48 (H4, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.28 | 10/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.28 | 9/48 (KATO III, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.263×** | -41.4 | 0e+00 | 46/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -22.6 | 0e+00 | 42/48 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.388×** | -20.8 | 0e+00 | 40/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.392×** | -20.5 | 0e+00 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -16.7 | 0e+00 | 39/48 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.551×** | -13.1 | 3e-37 | 36/48 (LoVo, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.614×** | -10.7 | 8e-25 | 30/47 (SW480, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -10.2 | 1e-22 | 40/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.629×** | -10.2 | 2e-22 | 37/48 (SW 900, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -9.1 | 5e-18 | 35/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -8.8 | 5e-17 | 29/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -8.7 | 1e-16 | 31/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.672×** | -8.7 | 1e-16 | 32/48 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -8.7 | 2e-16 | 33/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -8.1 | 3e-14 | 35/47 (RKO, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -7.8 | 3e-13 | 28/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.638×** | -5.2 | 6e-06 | 21/47 (SK-MEL-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.646×** | -5.0 | 1e-05 | 22/47 (SNU-423, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -4.8 | 4e-05 | 24/48 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.772×** | -4.1 | 9e-04 | 15/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 70.1 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -38.2) |
| [[SW480 (line)]] | alt | 55.7 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -23.5) |
| [[HEC-1-A (line)]] | alt | 53.0 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -25.2) |
| [[HT-29 (line)]] | alt | 94.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.2) |
| [[A498 (line)]] | wt | 86.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -27.5) |
| [[RKO (line)]] | wt | 69.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -30.1) |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -11.4) |
| [[SW 900 (line)]] | alt | 72.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -26.0) |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 23.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -17.8) |
| [[COLO 205 (line)]] | alt | 67.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -17.5) |
| [[HOP62 (line)]] | alt | 31.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.8) |
| [[KATO III (line)]] | alt | 46.3 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -15.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.5) |
| [[LS 180 (line)]] | wt | 43.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 49.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -18.6) |
| [[SW1417 (line)]] | alt | 64.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -20.4) |
| [[BT-474 (line)]] | alt | 55.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.7) |
| [[HCT15 (line)]] | alt | 56.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 31.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -22.7) |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.0) |
| [[A549 (line)]] | wt | 28.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.9) |
| [[AN3 CA (line)]] | alt | 65.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.3) |
| [[C-33 A (line)]] | alt | 57.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -25.2) |
| [[HS-578T (line)]] | alt | 25.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -14.7) |
| [[J82 (line)]] | alt | 27.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -24.0) |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -15.7) |
| [[SW48 (line)]] | wt | 55.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -20.0) |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.8) |
| [[C32 (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.5) |
| [[H4 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0851× (z -19.4) |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.7) |
| [[SW 1271 (line)]] | alt | 52.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.0) |
| [[A-172 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC43A1]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CIBAR1]] | +0.52 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[EPHX4]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SLC25A27]] | +0.48 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[CNOT6L]] | +0.48 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[TUB]] | +0.47 | +0.40 / +0.46 | both halves | 4e-05 |  |
| [[RAVER2]] | +0.47 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[LRP5]] | +0.47 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[KLHL23]] | +0.46 | +0.26 / +0.44 | both halves | 4e-04 |  |
| [[TTPA]] | +0.46 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[DLX6-AS1]] | +0.46 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[HOXB6]] | +0.46 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30BP]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[SNAI2]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[OSMR]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ADPRHL1]] | -0.47 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[EHD2]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[AKAP12]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[C11orf91]] | -0.44 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[RHCG]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[CSNK1A1]] | -0.44 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[LINC00702]] | -0.43 | -0.57 / -0.29 | both halves | 3e-04 |  |
| [[S100A10]] | -0.43 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CAPNS1]] | -0.43 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises DENND11's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without ENPP4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[TOP2A]] | B | TOP2A activity raises DENND11's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.2, 41.5); signed map (12.1, -2.7). **Vector** length 78.0, 17.7% of its response variance represented; |z| ≥ 3 in 1,354 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +5.2 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.5 | +1.9 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -22.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -16.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,656,728-141,702,166 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LCHN; previously KIAA1147 |
| Gene groups (HGNC) | DENN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D1U4](https://www.uniprot.org/uniprotkb/A4D1U4) (DENN domain-containing protein 11):

> Probable guanine nucleotide exchange factor (GEF). May promote the exchange of GDP to GTP, converting inactive GDP-bound small GTPases into their active GTP-bound form (Probable). May play a role in neuritogenesis, as well as in neuronal recovery and/or restructuring in the hippocampus following transient cerebral ischemia (By similarity).

**Summary**, from NCBI Gene [57189](https://www.ncbi.nlm.nih.gov/gene/57189):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29472) · Entrez [57189](https://www.ncbi.nlm.nih.gov/gene/57189) · UniProt [A4D1U4](https://www.uniprot.org/uniprotkb/A4D1U4) · Ensembl [ENSG00000257093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257093)

## Data

Gene col 15021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15021); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15021]; `tensor/DDL_lfc|DDL_z.npy` [15021]; `embed/gene_vectors.npy` [15021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15021 or target_col == 15021). Every well: [[DENND11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
