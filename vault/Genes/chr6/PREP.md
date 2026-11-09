---
symbol: "PREP"
type: "gene"
col: 1423
ensembl_id: "ENSG00000085377"
name: "prolyl endopeptidase"
location: "6q21"
module: 134
arm: "+"
pooled_cpm: 94.19
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# PREP

*prolyl endopeptidase* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.19× (z +11.2, q 4e-26, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.457× (z -20.5, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.606× (z -13.6, q 9e-40, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAN]] (+0.54, fdr 3e-05), [[GRPEL1]] (+0.52, fdr 2e-05), [[SLC16A1]] (+0.52, fdr 2e-05); moves opposite to [[P2RX4]] (-0.54, fdr 1e-05), [[STX4]] (-0.54, fdr 5e-05), [[CLCN7]] (-0.52, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.19×** | +11.2 | 4e-26 | 34/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +10.1 | 3e-21 | 34/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +5.7 | 3e-06 | 22/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +5.5 | 5e-06 | 20/46 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.031 | 17/47 (HOP62, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.14× | +3.5 | 0.050 | 16/47 (SW48, H4, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.13× | +3.3 | 0.070 | 7/47 (HEC-1-A, SNU-423, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +3.3 | 0.073 | 9/47 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.12× | +3.1 | 0.12 | 2/48 (NCI-H460, HS-578T) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -20.5 | 0e+00 | 39/44 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.500×** | -18.9 | 0e+00 | 39/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.606×** | -13.6 | 9e-40 | 36/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -11.4 | 4e-28 | 34/46 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -11.1 | 2e-26 | 29/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.631×** | -10.5 | 6e-24 | 32/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -10.2 | 2e-22 | 28/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.677×** | -10.2 | 2e-22 | 29/47 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -10.1 | 4e-22 | 32/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.706×** | -8.8 | 1e-16 | 25/45 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.756×** | -7.6 | 2e-12 | 30/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.764×** | -7.3 | 1e-11 | 28/47 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -6.5 | 4e-09 | 21/47 (HT-29, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.823×** | -5.1 | 2e-05 | 20/46 (SW 1271, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -5.0 | 2e-05 | 22/47 (SW 1271, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.813×** | -4.7 | 9e-05 | 22/47 (LoVo, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.824×** | -4.4 | 3e-04 | 19/47 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.868× | -3.8 | 0.003 | 14/47 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.884× | -3.3 | 0.021 | 15/47 (KATO III, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 223 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -20.4) |
| [[KATO III (line)]] | alt | 275 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -20.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.184× (z -20.0) |
| [[HOP62 (line)]] | alt | 87.1 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 160 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 76.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.563× (z -11.1) |
| [[J82 (line)]] | alt | 73.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.6) |
| [[LS 180 (line)]] | wt | 261 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.212× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 85.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.588× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 91.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.508× (z -13.0) |
| [[PANC-1 (line)]] | alt | 101 | 1 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.79× (z +12.7) | [[Harringtonine (drug)]] 5 µM 0.467× (z -13.3) |
| [[A-172 (line)]] | wt | 51.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -22.3) |
| [[C-33 A (line)]] | alt | 159 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.358× (z -10.9) |
| [[C32 (line)]] | wt | 171 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.266× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 137 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -19.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 188 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 89.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 122 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.441× (z -9.3) |
| [[SNU-423 (line)]] | alt | 87.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.6) |
| [[SW480 (line)]] | alt | 75.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.462× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 83.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.363× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 49.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 91.1 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 4.40× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.452× (z -9.2) |
| [[SW 1088 (line)]] | alt | 74.2 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 0.5 µM 0.0724× (z -9.0) |
| [[SW 1271 (line)]] | alt | 79.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0463× (z -13.1) |
| [[SW1417 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 82.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -9.7) |
| [[A-427 (line)]] | wt | 68.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -15.2) |
| [[H4 (line)]] | wt | 43.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.291× (z -8.8) |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 84.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0530× (z -14.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 92.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -15.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAN]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[GRPEL1]] | +0.52 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[SLC16A1]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CDK8]] | +0.52 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SRSF7]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[SERGEF]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CHSY1]] | +0.50 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[OLA1]] | +0.49 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[AMD1]] | +0.49 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[MTERF3]] | +0.49 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[WDR43]] | +0.48 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[MACIR]] | +0.48 | +0.45 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RX4]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[STX4]] | -0.54 | -0.40 / -0.59 | both halves | 5e-05 | pathway: HALLMARK_COMPLEMENT |
| [[CLCN7]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[NECAP2]] | -0.52 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TSC1]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GRIPAP1]] | -0.48 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ZNF630]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MOSPD2]] | -0.46 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RRAGC-DT]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SMARCA1]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[FNIP1]] | -0.46 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[C11orf54]] | -0.46 | -0.36 / -0.40 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.5, -21.3); signed map (-45.3, 26.0). **Vector** length 116, 31.6% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +11.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +3.4 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +5.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +3.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.5 | -4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -20.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.9 | -7.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.2 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | prolyl endopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:105,273,218-105,454,062 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [P48147](https://www.uniprot.org/uniprotkb/P48147) (Prolyl endopeptidase):

> Cleaves peptide bonds on the C-terminal side of prolyl residues within peptides that are up to approximately 30 amino acids long.

**Summary**, from NCBI Gene [5550](https://www.ncbi.nlm.nih.gov/gene/5550):

> The protein encoded by this gene is a cytosolic prolyl endopeptidase that cleaves peptide bonds on the C-terminal side of prolyl residues within peptides that are up to approximately 30 amino acids long. Prolyl endopeptidases have been reported to be involved in the maturation and degradation of peptide hormones and neuropeptides. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9358) · Entrez [5550](https://www.ncbi.nlm.nih.gov/gene/5550) · UniProt [P48147](https://www.uniprot.org/uniprotkb/P48147) · Ensembl [ENSG00000085377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085377)

## Data

Gene col 1423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1423); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1423]; `tensor/DDL_lfc|DDL_z.npy` [1423]; `embed/gene_vectors.npy` [1423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1423 or target_col == 1423). Every well: [[PREP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PREP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
