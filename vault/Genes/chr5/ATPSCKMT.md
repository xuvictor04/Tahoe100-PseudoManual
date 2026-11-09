---
symbol: "ATPSCKMT"
type: "gene"
col: 7457
ensembl_id: "ENSG00000150756"
name: "ATP synthase c subunit lysine N-methyltransferase"
location: "5p15.2"
module: 60
arm: "+"
pooled_cpm: 11.86
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# ATPSCKMT

*ATP synthase c subunit lysine N-methyltransferase* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.85× (z +14.8, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.275× (z -14.2, q 8e-43, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT5]] (+0.68, fdr 7e-06, ⚠ same locus), [[CCT3]] (+0.64, fdr 7e-06), [[CCT4]] (+0.63, fdr 7e-06), [[RBM12B]] (+0.62, fdr 1e-05); moves opposite to [[CDKN2D]] (-0.60, fdr 4e-05), [[WIPF2]] (-0.55, fdr 1e-05), [[SIRT2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.85×** | +14.8 | 0e+00 | 47/47 (HT-29, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.8 | 2e-06 | 26/45 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.6 | 8e-04 | 20/48 (A498, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.48×** | +4.1 | 0.005 | 17/45 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.98×** | +3.9 | 0.008 | 14/46 (BT-474, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.008 | 19/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.009 | 15/47 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.023 | 13/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.3 | 0.067 | 6/19 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.091 | 10/47 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.091 | 6/47 (SNU-423, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.41×** | +3.1 | 0.091 | 12/47 (HT-29, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brimonidine (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.091 | 3/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.091 | 7/48 (NCI-H2030, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.275×** | -14.2 | 8e-43 | 43/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.447×** | -12.5 | 2e-33 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.338×** | -11.9 | 3e-30 | 36/46 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.377×** | -10.7 | 1e-24 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.436×** | -9.1 | 9e-18 | 36/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.591×** | -5.8 | 8e-07 | 21/46 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -5.4 | 5e-06 | 24/40 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.601×** | -5.4 | 5e-06 | 26/46 (A-427, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -5.2 | 1e-05 | 23/43 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -5.2 | 1e-05 | 21/48 (SW1417, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.660×** | -4.5 | 3e-04 | 18/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.4 | 0.030 | 9/48 (SHP-77, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.706×** | -3.2 | 0.071 | 14/46 (A-427, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.709×** | -3.1 | 0.077 | 8/47 (CFPAC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0505× (z -21.2) |
| [[A-427 (line)]] | wt | 32.2 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0301× (z -23.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.217× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 14.4 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.75× (z +8.5) | [[Digitoxin (drug)]] 0.5 µM 0.157× (z -10.1) |
| [[SW480 (line)]] | alt | 22.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -15.1) |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0381× (z -14.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -8.9) |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0990× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -12.1) |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 8.42 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.53× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HT-29 (line)]] | alt | 14.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.48× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.0317× (z -19.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 7.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0843× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -9.7) |
| [[LoVo (line)]] | wt | 7.79 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 7.31 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0497× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0850× (z -8.8) |
| [[A498 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A549 (line)]] | wt | 7.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0592× (z -12.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0539× (z -13.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 9.82 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.43× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 9.28 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0851× (z -8.6) |
| [[KATO III (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -11.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 7.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0782× (z -9.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 1 | — | [[Pasireotide (acetate) (drug)]] 0.5 µM 0.0617× (z -9.5) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | +0.68 | +0.68 / +0.58 | both halves | 7e-06 | STRING 699; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CCT3]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCT4]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RBM12B]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CCT6A]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[HSPD1]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[AHSA1]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[L3HYPDH]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CHORDC1]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[PTGES3]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[PSMB7]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[HSP90AA2P]] | +0.59 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[PSMD14]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.60 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[WIPF2]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[DOP1A]] | -0.53 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[TXNIP]] | -0.53 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[DCXR]] | -0.52 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[GPX4]] | -0.52 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[GGNBP2]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[MED19]] | -0.52 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PHPT1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[NBPF19]] | -0.52 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SHOC2]] | -0.51 | -0.56 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.7, -12.3); signed map (-26.2, -30.0). **Vector** length 72.5, 13.8% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of tubulin folding intermediates by CCT/TriC* (reactome, mean cos +0.51 to 5); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.51 to 5); *Folding of actin by CCT/TriC* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +14.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.7 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.6 | -12.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.3 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +1.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase c subunit lysine N-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,225,507-10,249,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JS-2; previously FAM173B |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4H8](https://www.uniprot.org/uniprotkb/Q6P4H8) (ATP synthase subunit C lysine N-methyltransferase):

> Mitochondrial protein-lysine N-methyltransferase that trimethylates ATP synthase subunit C, ATP5MC1 and ATP5MC2. Trimethylation is required for proper incorporation of the C subunit into the ATP synthase complex and mitochondrial respiration. Promotes chronic pain. Involved in persistent inflammatory and neuropathic pain: methyltransferase activity in the mitochondria of sensory neurons promotes chronic pain via a pathway that depends on the production of reactive oxygen species (ROS) and on …

**Summary**, from NCBI Gene [134145](https://www.ncbi.nlm.nih.gov/gene/134145):

> Enables protein-lysine N-methyltransferase activity. Involved in several processes, including peptidyl-lysine trimethylation; positive regulation of proton-transporting ATP synthase activity, rotational mechanism; and positive regulation of sensory perception of pain. Located in mitochondrial crista. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27029) · Entrez [134145](https://www.ncbi.nlm.nih.gov/gene/134145) · UniProt [Q6P4H8](https://www.uniprot.org/uniprotkb/Q6P4H8) · Ensembl [ENSG00000150756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150756)

## Data

Gene col 7457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7457); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7457]; `tensor/DDL_lfc|DDL_z.npy` [7457]; `embed/gene_vectors.npy` [7457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7457 or target_col == 7457). Every well: [[ATPSCKMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATPSCKMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
