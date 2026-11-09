---
symbol: "MANCR"
type: "gene"
col: 13789
ensembl_id: "ENSG00000231298"
name: "mitotically associated long non coding RNA"
location: "10p15.1"
module: 13
arm: "+"
pooled_cpm: 51.53
n_lines_expressing: 30
n_dd_up: 9
n_dd_down: 59
n_dd_up_clean: 6
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 36
direction_downstream: 34
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MANCR

*mitotically associated long non coding RNA* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.76× (z +6.2, q 3e-07, up in 13 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.37× (z +4.9, q 2e-04, up in 17 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 59 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.184× (z -18.4, q 0e+00, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM19]] (+0.72, fdr 7e-06), [[DCBLD2]] (+0.66, fdr 7e-06), [[TRBC2]] (+0.66, fdr 1e-05); moves opposite to [[ACSL1]] (-0.58, fdr 1e-05), [[FLVCR2]] (-0.55, fdr 2e-05), [[MT1M]] (-0.53, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[CARD11]] → it (grade B ⚠); 34 go from it, the strongest it → [[TGFA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.2 | 3e-07 | 13/28 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.2 | 4e-05 | 10/25 (MIA PaCa-2, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.2 | 5e-05 | 7/22 (RPMI-7951, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.9 | 2e-04 | 17/28 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.004 | 13/28 (HepG2/C3A, SHP-77, …) | all doses, flat | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.011 | 12/28 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.019 | 8/28 (HOP62, LS 180, …) | all doses, flat | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.056 | 5/26 (AsPC-1, A498, …) | all doses, flat | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.063 | 14/28 (A498, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 59 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13789.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.184×** | -18.4 | 0e+00 | 28/28 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.201×** | -17.5 | 0e+00 | 27/28 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.246×** | -15.3 | 0e+00 | 28/28 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.518×** | -10.1 | 8e-22 | 24/28 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.414×** | -9.2 | 4e-18 | 26/27 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.449×** | -8.7 | 3e-16 | 28/28 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.435×** | -8.7 | 3e-16 | 24/27 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.474×** | -8.1 | 4e-14 | 21/28 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.503×** | -7.0 | 2e-10 | 24/29 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -6.7 | 1e-09 | 21/28 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.543×** | -6.6 | 2e-09 | 23/29 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.620×** | -6.5 | 5e-09 | 21/28 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.562×** | -6.2 | 2e-08 | 22/28 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.567×** | -6.1 | 3e-08 | 20/27 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.551×** | -6.1 | 3e-08 | 22/28 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.576×** | -6.0 | 8e-08 | 17/28 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.552×** | -6.0 | 9e-08 | 20/28 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 530 | 0 | 40 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0241× (z -35.0) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.00927× (z -31.1) |
| [[A-172 (line)]] | wt | 226 | 0 | 32 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0393× (z -25.2) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.0257× (z -20.1) |
| [[SW480 (line)]] | alt | 175 | 0 | 22 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0162× (z -29.5) |
| [[HepG2_C3A (line)]] | wt | 74.0 | 0 | 10 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0223× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 62.3 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0778× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 43.6 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0485× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 36.5 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0436× (z -15.8) |
| [[SNU-423 (line)]] | alt | 96.4 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0328× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -11.4) |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0867× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 49.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0748× (z -12.1) |
| [[COLO 205 (line)]] | alt | 58.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0418× (z -14.9) |
| [[SW 900 (line)]] | alt | 61.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.2) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 0.0828× (z -11.5) |
| [[LoVo (line)]] | wt | 16.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0990× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 45.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -11.3) |
| [[H4 (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0618× (z -14.6) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.0771× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0640× (z -13.4) |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -11.2) |
| [[KATO III (line)]] | alt | 15.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -8.9) |
| [[A-427 (line)]] | wt | 6.76 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM19]] | +0.72 | +0.76 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[DCBLD2]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TRBC2]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[LINC02813]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CNIH3]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC00973]] | +0.64 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[EVA1A-AS]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[CSMD2]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ANGPTL2]] | +0.62 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[PTHLH]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[MIR4280HG]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.62 | +0.57 / +0.66 | both halves | 9e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[FLVCR2]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[MT1M]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TSC22D3]] | -0.53 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[NNMT]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 17, C 19. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | CARD11 activity raises MANCR's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without CARD11 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[CFAP20DC]] | B | CFAP20DC activity raises MANCR's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without CFAP20DC | 0.032 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |
| [[WFDC10B]] | B | WFDC10B activity raises MANCR's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 3.02× lower at baseline in the lines without WFDC10B | 0.032 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[EDNRA]] | B | EDNRA activity raises MANCR's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without EDNRA | 0.032 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[IGFBP3]] | B | IGFBP3 activity raises MANCR's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without IGFBP3 | 0.038 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[SHC4]] | B | SHC4 activity raises MANCR's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.31× lower at baseline in the lines without SHC4 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent |
| [[LINC02813]] | B | LINC02813 activity raises MANCR's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.28× lower at baseline in the lines without LINC02813 | 0.049 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[IL11]] | B | IL11 activity raises MANCR's level | lines that do not express IL11 (27) vs lines expressing it (23) | 2.53× lower at baseline in the lines without IL11 | 0.054 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[LINC01705]] | B | LINC01705 activity raises MANCR's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.97× lower at baseline in the lines without LINC01705 | 0.064 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[CSMD2]] | B | CSMD2 activity raises MANCR's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.67× lower at baseline in the lines without CSMD2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[APCDD1L]] | B | APCDD1L activity raises MANCR's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without APCDD1L | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[GLYATL2]] | B | GLYATL2 activity raises MANCR's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without GLYATL2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476 |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 18, C 16. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFA]] | B | MANCR activity raises TGFA's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without MANCR | 0.022 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[STK10]] | B | MANCR activity raises STK10's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without MANCR | 0.028 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[ANTXR2]] | B | MANCR activity raises ANTXR2's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without MANCR | 0.028 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[SHC3]] | B | MANCR activity raises SHC3's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.54× lower at baseline in the lines without MANCR | 0.029 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[BACH1]] | B | MANCR activity raises BACH1's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.73× lower at baseline in the lines without MANCR | 0.039 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[LINC01705]] | B | MANCR activity raises LINC01705's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.47× lower at baseline in the lines without MANCR | 0.049 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[EPHB6]] | B | MANCR activity raises EPHB6's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without MANCR | 0.051 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[PRDM8]] | B | MANCR activity raises PRDM8's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without MANCR | 0.052 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[TGFA]] | B | MANCR activity strengthens TGFA's drug response | lines that do not express MANCR (9) vs lines expressing it (23) | the lines without MANCR respond 0.55× as strongly (z diff +2.63); strongest at Idarubicin (hydrochloride) 5 µM: 0.94x vs 0.49x (z diff +5.2) | 0.057 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; target measured in part of the lines; artifact flags |
| [[E2F7]] | B | MANCR activity weakens E2F7's drug response | lines that do not express MANCR (19) vs lines expressing it (24) | the lines without MANCR respond 1.24× as strongly (z diff -1.03); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.95x vs 1.11x (z diff -3.4) | 0.058 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2; target measured in part of the lines; both ways; artifact flags |
| [[RP2]] | B | MANCR activity raises RP2's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MANCR | 0.060 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[CFAP20DC]] | B | MANCR activity raises CFAP20DC's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without MANCR | 0.061 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 9.1); signed map (11.9, 51.2). **Vector** length 128, 40.8% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +6.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +0.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.1 | -7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.5 | -6.5 |
|  | [[Binimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | -4.9 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -8.7 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | -4.8 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | mitotically associated long non coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p15.1 — chr10:4,581,295-4,678,216 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CR749391; previously LINC00704 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44678) · Entrez [100216001](https://www.ncbi.nlm.nih.gov/gene/100216001) · Ensembl [ENSG00000231298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231298)

## Data

Gene col 13789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13789); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13789]; `tensor/DDL_lfc|DDL_z.npy` [13789]; `embed/gene_vectors.npy` [13789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13789 or target_col == 13789). Every well: [[MANCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
