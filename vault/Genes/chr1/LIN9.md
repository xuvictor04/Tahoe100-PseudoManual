---
symbol: "LIN9"
type: "gene"
col: 11460
ensembl_id: "ENSG00000183814"
name: "lin-9 DREAM MuvB core complex component"
location: "1q42.12"
module: 71
arm: "+"
pooled_cpm: 34.7
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# LIN9

*lin-9 DREAM MuvB core complex component* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.44× (z +7.4, q 1e-10, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.43× (z +7.1, q 2e-10, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.592× (z -10.5, q 5e-23, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCM]] (+0.80, fdr 7e-06), [[OIP5]] (+0.79, fdr 7e-06), [[MTBP]] (+0.77, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DSCC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +7.4 | 1e-10 | 29/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.44×** | +7.3 | 1e-10 | 28/47 (LS 180, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.1 | 2e-10 | 28/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +6.3 | 5e-08 | 27/48 (NCI-H23, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.33×** | +5.7 | 1e-06 | 21/47 (PANC-1, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.5 | 4e-06 | 23/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.4 | 8e-04 | 21/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.003 | 18/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 10/48 (Panc 03.27, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.018 | 16/47 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.020 | 10/47 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.12× | +3.3 | 0.042 | 7/48 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.052 | 12/48 (AsPC-1, CHP-212, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +3.1 | 0.072 | 13/47 (SW480, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.17× | +3.1 | 0.072 | 7/48 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -10.5 | 5e-23 | 38/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.617×** | -9.6 | 1e-19 | 35/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -9.6 | 2e-19 | 31/46 (HEC-1-A, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -9.3 | 2e-18 | 37/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -8.6 | 6e-16 | 27/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -8.4 | 5e-15 | 29/41 (C-33 A, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -7.1 | 8e-11 | 24/38 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.701×** | -7.1 | 8e-11 | 28/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -6.6 | 3e-09 | 26/48 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.744×** | -5.9 | 2e-07 | 24/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.825×** | -5.4 | 3e-06 | 27/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.773×** | -5.2 | 1e-05 | 23/48 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.8 | 6e-05 | 0/48 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.804×** | -4.4 | 5e-04 | 17/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.827×** | -3.8 | 0.006 | 13/48 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.879× | -3.7 | 0.008 | 14/48 (CFPAC-1, CHP-212, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.846× | -3.3 | 0.025 | 14/47 (HOP62, A-172, …) | two highest doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.057 | 8/47 (RKO, A-427, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.859× | -3.0 | 0.061 | 7/48 (A-172, HOP62, …) | rises with dose |  |
| [[Futibatinib (drug)]] 5 µM |  | **0.757×** | -2.9 | 0.086 | 10/44 (COLO 205, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.5) |
| [[SW480 (line)]] | alt | 48.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.422× (z -11.1) |
| [[A498 (line)]] | wt | 38.0 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.426× (z -12.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.435× (z -12.4) |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.306× (z -9.7) |
| [[A-427 (line)]] | wt | 43.1 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.259× (z -17.7) |
| [[AN3 CA (line)]] | alt | 65.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 54.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0746× (z -21.9) |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -14.2) |
| [[HOP62 (line)]] | alt | 32.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.334× (z -8.9) |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -19.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 28.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.180× (z -9.0) ⚠ toxic |
| [[RKO (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.231× (z -8.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SK-MEL-2 (line)]] | alt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.6) |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.213× (z -11.0) |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0406× (z -9.2) |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCM]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[OIP5]] | +0.79 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[MTBP]] | +0.77 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[LRR1]] | +0.75 | +0.63 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RFWD3]] | +0.75 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[SASS6]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[NUP107]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SLF1]] | +0.73 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[PLK4]] | +0.72 | +0.72 / +0.74 | both halves | 7e-06 | pathway: G2/M Transition; STRING 536 |
| [[RBL1]] | +0.72 | +0.80 / +0.79 | both halves | 7e-06 | pathway: G0 and Early G1; STRING 931 |
| [[CDCA5]] | +0.71 | +0.70 / +0.74 | both halves | 7e-06 | pathway: S Phase |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCC1]] | C | DSCC1 activity raises LIN9's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises LIN9's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without ZNF367 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises LIN9's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without NDC80 | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PKN3]] | C | PKN3 activity raises LIN9's level | lines that do not express PKN3 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without PKN3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NUDT7, ITPKA, DNM1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.6, -49.3); signed map (-41.5, -42.6). **Vector** length 121, 32.5% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.51 to 4); *IP6 and IP7 transport between cytosol and nucleus* (reactome, mean cos +0.51 to 4); *IPs transport between nucleus and cytosol* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.9 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.6 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -3.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | lin-9 DREAM MuvB core complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:226,231,149-226,309,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TGS |
| Gene groups (HGNC) | MuvB complex subunits |
| Reactome | 14 pathways, smallest: Polo-like kinase mediated events; Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1; Transcription of E2F targets under negative control by DREAM complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TKA1](https://www.uniprot.org/uniprotkb/Q5TKA1) (Protein lin-9 homolog):

> Acts as a tumor suppressor. Inhibits DNA synthesis. Its ability to inhibit oncogenic transformation is mediated through its association with RB1. Plays a role in the expression of genes required for the G1/S transition.

**Summary**, from NCBI Gene [286826](https://www.ncbi.nlm.nih.gov/gene/286826):

> This gene encodes a tumor suppressor protein that inhibits DNA synthesis and oncogenic transformation through association with the retinoblastoma 1 protein. The encoded protein also interacts with a complex of other cell cycle regulators to repress cell cycle-dependent gene expression in non-dividing cells. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:30830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30830) · Entrez [286826](https://www.ncbi.nlm.nih.gov/gene/286826) · UniProt [Q5TKA1](https://www.uniprot.org/uniprotkb/Q5TKA1) · Ensembl [ENSG00000183814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183814)

## Data

Gene col 11460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11460); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11460]; `tensor/DDL_lfc|DDL_z.npy` [11460]; `embed/gene_vectors.npy` [11460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11460 or target_col == 11460). Every well: [[LIN9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
