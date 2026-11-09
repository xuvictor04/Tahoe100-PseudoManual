---
symbol: "KHNYN"
type: "gene"
col: 1963
ensembl_id: "ENSG00000100441"
name: "KH and NYN domain containing"
location: "14q12"
module: 7
arm: "+"
pooled_cpm: 33.83
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# KHNYN

*KH and NYN domain containing* — 14q12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (18 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.433× (z -10.8, q 2e-24, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.597× (z -6.7, q 2e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM83G]] (+0.70, fdr 7e-06), [[MEPCE]] (+0.70, fdr 7e-06), [[ZNF687]] (+0.67, fdr 7e-06); moves opposite to [[HMGN3]] (-0.58, fdr 1e-05), [[PEBP1]] (-0.57, fdr 3e-05), [[ASAH1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | 1.32× | +3.6 | 0.14 | 21/47 (KATO III, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.5 | 0.14 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.44 | 16/48 (A549, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.433×** | -10.8 | 2e-24 | 43/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.437×** | -10.7 | 3e-24 | 45/48 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.440×** | -10.6 | 6e-24 | 44/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.510×** | -8.7 | 4e-16 | 38/47 (COLO 205, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.508×** | -8.4 | 8e-15 | 33/46 (NCI-H460, HCT15, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.585×** | -6.9 | 5e-10 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -6.7 | 2e-09 | 36/48 (H4, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.541×** | -6.6 | 4e-09 | 23/34 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.544×** | -6.5 | 5e-09 | 36/46 (SK-MEL-2, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.639×** | -5.8 | 4e-07 | 35/47 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.660×** | -5.4 | 4e-06 | 26/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -5.4 | 4e-06 | 33/47 (CHP-212, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -5.2 | 7e-06 | 31/49 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -5.2 | 8e-06 | 27/48 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.688×** | -4.8 | 5e-05 | 30/48 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.548×** | -4.1 | 0.002 | 26/47 (NCI-H460, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.554×** | -4.0 | 0.002 | 26/46 (Panc 03.27, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.555×** | -4.0 | 0.002 | 27/48 (RPMI-7951, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.756×** | -3.4 | 0.017 | 17/48 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.615×** | -3.3 | 0.024 | 17/47 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.619×** | -3.2 | 0.026 | 21/46 (SW48, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.852× | -2.9 | 0.068 | 14/48 (RKO, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.730×** | -2.9 | 0.068 | 11/48 (NCI-H23, HS-578T, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.659×** | -2.8 | 0.087 | 15/47 (SHP-77, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 38.8 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -11.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 35.9 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.200× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 43.9 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.219× (z -12.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 36.6 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.288× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 52.8 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 55.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[HEC-1-A (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 35.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0768× (z -9.0) |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LOX-IMVI (line)]] | wt | 35.8 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.265× (z -9.3) |
| [[LS 180 (line)]] | wt | 52.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW48 (line)]] | wt | 29.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.115× (z -11.0) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM83G]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[MEPCE]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ZNF687]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SERPINB8]] | +0.65 | +0.65 / +0.57 | both halves | 8e-06 |  |
| [[ZNF646]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SCAF1]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[KDM6B]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[NOP14-AS1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CSRNP2]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CACTIN]] | +0.60 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TLNRD1]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FBRS]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | -0.58 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[PEBP1]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ASAH1]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[RHOT1]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PPP1R12B]] | -0.54 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SNX4]] | -0.54 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[SKP2]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TTLL5]] | -0.53 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[TYW1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ARL6IP5]] | -0.53 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[NDUFB6]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity raises KHNYN's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without LACC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.3, 5.7); signed map (10.8, -17.3). **Vector** length 92.6, 23.6% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.9 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | -0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -10.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | KH and NYN domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,429,286-24,441,843 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0323 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [O15037](https://www.uniprot.org/uniprotkb/O15037) carries no function annotation.

**Summary**, from NCBI Gene [23351](https://www.ncbi.nlm.nih.gov/gene/23351):

> The protein encoded by this gene contains a ribonuclease NYN domain and belongs to the N4BP1 family. The protein is a cofactor for the zinc finger antiviral protein (ZAP protein) which targets viral RNA for degradation and restricts SARS-CoV-2 infection. [provided by RefSeq, Sep 2021]

**Accessions** — [HGNC:20166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20166) · Entrez [23351](https://www.ncbi.nlm.nih.gov/gene/23351) · UniProt [O15037](https://www.uniprot.org/uniprotkb/O15037) · Ensembl [ENSG00000100441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100441)

## Data

Gene col 1963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1963); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1963]; `tensor/DDL_lfc|DDL_z.npy` [1963]; `embed/gene_vectors.npy` [1963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1963 or target_col == 1963). Every well: [[KHNYN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHNYN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
