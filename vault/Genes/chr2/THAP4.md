---
symbol: "THAP4"
type: "gene"
col: 10771
ensembl_id: "ENSG00000176946"
name: "THAP domain containing 4"
location: "2q37.3"
module: 5
arm: "+"
pooled_cpm: 24.55
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# THAP4

*THAP domain containing 4* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.57× (z +9.5, q 1e-18, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -18.1, q 0e+00, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF142]] (+0.66, fdr 1e-05), [[CAPN15]] (+0.64, fdr 1e-05), [[SENP3]] (+0.63, fdr 1e-05); moves opposite to [[LIMA1]] (-0.61, fdr 1e-05), [[HMSD]] (-0.56, fdr 3e-04), [[HYCC1]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NEDD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +9.5 | 1e-18 | 28/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.9 | 1e-06 | 26/48 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.6 | 3e-06 | 25/48 (AsPC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.4 | 7e-06 | 23/47 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.0 | 7e-05 | 21/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.8 | 2e-04 | 15/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.22×** | +4.2 | 0.002 | 12/47 (HT-29, A-172, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.005 | 6/48 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +3.9 | 0.007 | 12/48 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.015 | 19/46 (LoVo, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.029 | 15/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.062 | 15/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.062 | 15/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -18.1 | 0e+00 | 32/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -9.3 | 3e-18 | 35/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -8.8 | 2e-16 | 30/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.684×** | -8.1 | 1e-13 | 29/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.708×** | -7.1 | 2e-10 | 27/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.720×** | -6.5 | 1e-08 | 22/41 (A-172, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.750×** | -6.1 | 8e-08 | 23/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.764×** | -5.7 | 7e-07 | 25/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.784×** | -5.2 | 1e-05 | 23/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.804×** | -4.7 | 2e-04 | 18/48 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.893× | -3.4 | 0.034 | 13/48 (SNU-1, NCI-H1792, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.803×** | -3.3 | 0.042 | 8/47 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.863× | -3.1 | 0.067 | 13/48 (HCT15, NCI-H2347, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.901× | -3.1 | 0.067 | 9/48 (J82, SW 1271, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 23.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +22.4) | — |
| [[AsPC-1 (line)]] | alt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +17.1) | — |
| [[BT-474 (line)]] | alt | 21.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.45× (z +11.2) | [[Simotinib (drug)]] 5 µM 0.160× (z -10.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 29.0 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.25× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -20.0) |
| [[A-172 (line)]] | wt | 27.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -22.2) |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -12.6) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.438× (z -9.4) |
| [[A-427 (line)]] | wt | 37.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -11.9) |
| [[A498 (line)]] | wt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.0) |
| [[A549 (line)]] | wt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -8.6) |
| [[COLO 205 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +14.6) | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -10.4) |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[J82 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.2) |
| [[LoVo (line)]] | wt | 26.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[RKO (line)]] | wt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.1000× (z -14.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW1417 (line)]] | alt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF142]] | +0.66 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CAPN15]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SENP3]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[HSF1]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RPUSD4]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ZNF749]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[TRMT1]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[KMT2D]] | +0.62 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[TLCD3A]] | +0.61 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[MACROD1]] | +0.60 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ADCY3]] | +0.60 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[CUL4A]] | +0.60 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMA1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[HMSD]] | -0.56 | -0.28 / -0.67 | both halves | 3e-04 |  |
| [[HYCC1]] | -0.55 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[CCDC148]] | -0.55 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CD83]] | -0.53 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[NFKBIZ]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[PTGER4]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[MAK]] | -0.51 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TMEM14C]] | -0.51 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[PICALM]] | -0.51 | -0.18 / -0.46 | ⚠ not reproduced | 9e-04 |  |
| [[LMNA]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[NEDD9]] | -0.50 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[SAV1]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEDD9]] | B | NEDD9 activity lowers THAP4's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.30× higher at baseline in the lines without NEDD9 | 0.065 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[KCTD15]] | B | KCTD15 activity raises THAP4's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without KCTD15 | 0.089 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises THAP4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises THAP4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.0, -31.1); signed map (-0.7, -52.6). **Vector** length 80.5, 14.4% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -18.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,584,405-241,637,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-36, Nb(III) |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WY91](https://www.uniprot.org/uniprotkb/Q8WY91) (Peroxynitrite isomerase THAP4):

> Heme-binding protein able to scavenge peroxynitrite and to protect free L-tyrosine against peroxynitrite-mediated nitration, by acting as a peroxynitrite isomerase that converts peroxynitrite to nitrate. Therefore, this protein likely plays a role in peroxynitrite sensing and in the detoxification of reactive nitrogen and oxygen species (RNS and ROS, respectively). Is able to bind nitric oxide (NO) in vitro, but may act as a sensor of peroxynitrite levels in vivo, possibly modulating the …

**Summary**, from NCBI Gene [51078](https://www.ncbi.nlm.nih.gov/gene/51078):

> Enables several functions, including heme binding activity; nitric oxide binding activity; and peroxynitrite isomerase activity. Involved in nitrate metabolic process and tyrosine metabolic process. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23187) · Entrez [51078](https://www.ncbi.nlm.nih.gov/gene/51078) · UniProt [Q8WY91](https://www.uniprot.org/uniprotkb/Q8WY91) · Ensembl [ENSG00000176946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176946)

## Data

Gene col 10771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10771); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10771]; `tensor/DDL_lfc|DDL_z.npy` [10771]; `embed/gene_vectors.npy` [10771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10771 or target_col == 10771). Every well: [[THAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
