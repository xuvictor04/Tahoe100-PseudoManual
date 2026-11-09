---
symbol: "SRPX"
type: "gene"
col: 2194
ensembl_id: "ENSG00000101955"
name: "sushi repeat containing protein X-linked"
location: "Xp11.4"
module: 104
arm: "+"
pooled_cpm: 18.92
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 18
direction_downstream: 36
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# SRPX

*sushi repeat containing protein X-linked* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.92× (z +16.0, q 0e+00, up in 11 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +11.0, q 1e-25, up in 14 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -28.0, q 0e+00, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAAM2]] (+0.68, fdr 1e-05), [[FN1]] (+0.66, fdr 7e-06), [[RNF175]] (+0.61, fdr 2e-05); moves opposite to [[C12orf50]] (-0.54, fdr 1e-05), [[SLAMF7]] (-0.54, fdr 1e-05), [[ANKRD30B]] (-0.53, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 36 go from it, the strongest it → [[ITGA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +16.0 | 0e+00 | 11/14 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +12.9 | 2e-35 | 15/20 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +11.0 | 1e-25 | 14/26 (A549, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +7.0 | 4e-10 | 7/24 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 1e-06 | 12/25 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.43×** | +5.5 | 3e-06 | 13/25 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.41×** | +5.3 | 9e-06 | 11/25 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 1e-04 | 7/15 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.36×** | +4.7 | 1e-04 | 11/25 (NCI-H1792, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 8e-04 | 11/25 (NCI-H1792, Hs 766T, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.33×** | +4.2 | 0.002 | 8/25 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.002 | 1/23 (NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 8/26 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.008 | 8/26 (NCI-H1792, Hs 766T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.3 | 0.035 | 4/14 (A549, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.039 | 10/25 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.048 | 9/24 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.056 | 16/26 (NCI-H1792, Hs 766T, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -28.0 | 0e+00 | 24/26 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.344×** | -16.4 | 0e+00 | 23/25 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.338×** | -16.2 | 0e+00 | 25/26 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.482×** | -11.3 | 1e-27 | 22/26 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.550×** | -9.3 | 2e-18 | 18/26 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -8.6 | 7e-16 | 13/25 (BT-474, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -6.0 | 2e-07 | 18/26 (SNU-423, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.684×** | -5.9 | 3e-07 | 16/26 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.692×** | -5.7 | 7e-07 | 11/24 (NCI-H23, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.779×** | -5.5 | 2e-06 | 16/26 (A-172, RPMI-7951, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.734×** | -4.8 | 8e-05 | 15/26 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -4.5 | 3e-04 | 11/25 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 4e-04 | 15/25 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.754×** | -4.4 | 5e-04 | 16/26 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.757×** | -4.3 | 6e-04 | 11/23 (RKO, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.763×** | -4.2 | 1e-03 | 19/26 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 172 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -50.9) |
| [[NCI-H460 (line)]] | wt | 62.4 | 8 (1 ⚠) | 8 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.25× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.0638× (z -37.3) |
| [[A-172 (line)]] | wt | 65.0 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -36.5) |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -33.6) |
| [[NCI-H1792 (line)]] | alt | 56.3 | 5 | 2 | [[Clobetasol propionate (drug)]] 0.5 µM 3.29× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -32.7) |
| [[H4 (line)]] | wt | 54.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0206× (z -24.8) |
| [[SNU-423 (line)]] | alt | 46.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.1) |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -26.1) |
| [[A498 (line)]] | wt | 14.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.3) |
| [[HCT15 (line)]] | alt | 6.33 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -10.6) |
| [[Hs 766T (line)]] | wt | 7.19 | 1 | 1 | [[Triamcinolone (drug)]] 5 µM 5.71× (z +9.7) | [[Pyridoxine (drug)]] 0.5 µM 0.112× (z -8.5) |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -12.0) |
| [[J82 (line)]] | alt | 10.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -14.5) |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -12.4) |
| [[BT-474 (line)]] | alt | 5.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -9.1) |
| [[HOP62 (line)]] | alt | 6.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -18.8) |
| [[RKO (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0912× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -10.3) |
| [[A-427 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAAM2]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[FN1]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[RNF175]] | +0.61 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[AEBP1]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ITGA8]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[FAH]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TRAM2]] | +0.57 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SDC2]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[RNF144A]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[COPS8]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf50]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SLAMF7]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ANKRD30B]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PCED1B]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[C15orf48]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PATJ]] | -0.50 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[AMIGO2]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BMP2]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MBP]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LINC00472]] | -0.48 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[LINC02154]] | -0.48 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[CREB1]] | -0.47 | -0.50 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 6, C 12. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises SRPX's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[PATJ]] | B | PATJ activity lowers SRPX's level | lines that do not express PATJ (9) vs lines expressing it (41) | 6.08× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[SIRPA]] | B | SIRPA activity raises SRPX's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 3.73× lower at baseline in the lines without SIRPA | 0.064 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[LOXL3]] | B | LOXL3 activity raises SRPX's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without LOXL3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[TDRD9]] | B | TDRD9 activity raises SRPX's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 3.61× lower at baseline in the lines without TDRD9 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[LINC00472]] | B | LINC00472 activity raises SRPX's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 2.84× lower at baseline in the lines without LINC00472 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT |
| [[AEBP1]] | C | AEBP1 activity raises SRPX's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 5.66× lower at baseline in the lines without AEBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LINC02154]] | C | LINC02154 activity raises SRPX's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 4.38× lower at baseline in the lines without LINC02154 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises SRPX's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.46× lower at baseline in the lines without PDGFRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises SRPX's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 7.42× lower at baseline in the lines without ITGA4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises SRPX's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.22× lower at baseline in the lines without WNT5A | 0.013 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[FN1]] | C | FN1 activity raises SRPX's level | lines that do not express FN1 (29) vs lines expressing it (21) | 5.29× lower at baseline in the lines without FN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 27, C 9. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA5]] | B | SRPX activity raises ITGA5's level | lines that do not express SRPX (22) vs lines expressing it (28) | 3.38× lower at baseline in the lines without SRPX | 0.013 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[SFXN3]] | B | SRPX activity raises SFXN3's level | lines that do not express SRPX (22) vs lines expressing it (28) | 1.97× lower at baseline in the lines without SRPX | 0.013 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[P3H3]] | B | SRPX activity raises P3H3's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without SRPX | 0.013 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | B | SRPX activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[LAMB1]] | B | SRPX activity raises LAMB1's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.61× lower at baseline in the lines without SRPX | 0.023 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[CERCAM]] | B | SRPX activity raises CERCAM's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.73× lower at baseline in the lines without SRPX | 0.032 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | SRPX activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.20× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[TRAM2]] | B | SRPX activity raises TRAM2's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without SRPX | 0.039 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[C12orf50]] | B | SRPX activity raises C12orf50's level | lines that do not express SRPX (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without SRPX | 0.044 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[TRAF1]] | B | SRPX activity raises TRAF1's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.40× lower at baseline in the lines without SRPX | 0.053 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[PATJ]] | B | SRPX activity lowers PATJ's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.84× higher at baseline in the lines without SRPX | 0.054 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | SRPX activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 0.85× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.7, 24.0); signed map (25.1, 39.6). **Vector** length 78.9, 20.1% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.8 | +5.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.7 | +5.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.3 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -16.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -28.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | sushi repeat containing protein X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:38,149,336-38,220,924 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ETX1, SRPX1 |
| Gene groups (HGNC) | Sushi domain containing |
| Hallmark sets | APICAL_SURFACE, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [P78539](https://www.uniprot.org/uniprotkb/P78539) (Sushi repeat-containing protein SRPX):

> May be involved in phagocytosis during disk shedding, cell adhesion to cells other than the pigment epithelium or signal transduction.

**Summary**, from NCBI Gene [8406](https://www.ncbi.nlm.nih.gov/gene/8406):

> Predicted to be an extracellular matrix structural constituent. Predicted to be involved in phagolysosome assembly. Predicted to act upstream of or within several processes, including negative regulation of cell proliferation involved in contact inhibition; positive regulation of extrinsic apoptotic signaling pathway in absence of ligand; and response to endoplasmic reticulum stress. Located in extracellular matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11309) · Entrez [8406](https://www.ncbi.nlm.nih.gov/gene/8406) · UniProt [P78539](https://www.uniprot.org/uniprotkb/P78539) · Ensembl [ENSG00000101955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101955)

## Data

Gene col 2194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2194); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2194]; `tensor/DDL_lfc|DDL_z.npy` [2194]; `embed/gene_vectors.npy` [2194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2194 or target_col == 2194). Every well: [[SRPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
