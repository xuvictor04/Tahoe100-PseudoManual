---
symbol: "HPS3"
type: "gene"
col: 8773
ensembl_id: "ENSG00000163755"
name: "HPS3 biogenesis of lysosomal organelles complex 2 subunit 1"
location: "3q24"
module: 124
arm: "-"
pooled_cpm: 71.34
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 36
n_dd_up_clean: 6
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# HPS3

*HPS3 biogenesis of lysosomal organelles complex 2 subunit 1* — 3q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +5.0, q 4e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.415× (z -20.3, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PJA2]] (+0.63, fdr 3e-05), [[RAB3A]] (+0.59, fdr 2e-04), [[TRAM2]] (+0.57, fdr 4e-05); moves opposite to [[POU6F1]] (-0.63, fdr 8e-05), [[GABPB1]] (-0.57, fdr 2e-04), [[PCBD2]] (-0.56, fdr 3e-05).
> It sits in the **-** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NAV2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.0 | 4e-04 | 25/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.016 | 22/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.016 | 24/47 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.035 | 20/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.043 | 22/48 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.23×** | +3.4 | 0.060 | 19/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.080 | 19/48 (KATO III, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.415×** | -20.3 | 0e+00 | 42/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.550×** | -13.8 | 6e-41 | 37/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.442×** | -13.3 | 2e-38 | 42/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -13.0 | 3e-36 | 42/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.457×** | -12.8 | 2e-35 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -10.5 | 1e-23 | 38/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -9.3 | 1e-18 | 34/47 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.543×** | -9.2 | 2e-18 | 34/43 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.599×** | -8.4 | 4e-15 | 38/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -8.3 | 6e-15 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.612×** | -7.5 | 2e-12 | 36/48 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -7.4 | 8e-12 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.632×** | -7.2 | 3e-11 | 32/47 (COLO 205, HS-578T, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -7.2 | 3e-11 | 31/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.660×** | -6.8 | 5e-10 | 30/49 (Panc 03.27, A549, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -5.8 | 2e-07 | 31/49 (MIA PaCa-2, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -5.3 | 3e-06 | 27/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -5.2 | 6e-06 | 21/49 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.4 | 3e-04 | 24/48 (HS-578T, SNU-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.704×** | -4.1 | 1e-03 | 25/49 (SK-MEL-2, A498, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 90.9 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -22.0) |
| [[SW 900 (line)]] | alt | 156 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -17.9) |
| [[HS-578T (line)]] | alt | 113 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -25.3) |
| [[NCI-H23 (line)]] | alt | 62.2 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 48.1 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -16.2) |
| [[A-172 (line)]] | wt | 98.4 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -14.7) |
| [[COLO 205 (line)]] | alt | 68.9 | 0 | 6 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -13.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.6) |
| [[J82 (line)]] | alt | 184 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -18.6) |
| [[NCI-H1792 (line)]] | alt | 66.7 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 159 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -18.3) |
| [[SNU-423 (line)]] | alt | 105 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -16.4) |
| [[Hs 766T (line)]] | wt | 81.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -18.5) |
| [[SW480 (line)]] | alt | 51.0 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -16.1) |
| [[A498 (line)]] | wt | 154 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -17.4) |
| [[A549 (line)]] | wt | 73.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 47.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 57.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -13.1) |
| [[HT-29 (line)]] | alt | 55.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.316× (z -10.6) |
| [[RKO (line)]] | wt | 42.2 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -14.9) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 67.7 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.6) |
| [[A-427 (line)]] | wt | 50.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.372× (z -9.3) |
| [[HOP62 (line)]] | alt | 62.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 77.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.5) |
| [[SHP-77 (line)]] | alt | 94.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.8) |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.1) |
| [[BT-474 (line)]] | alt | 33.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -9.2) |
| [[C32 (line)]] | wt | 41.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.7) |
| [[H4 (line)]] | wt | 49.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -14.3) |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -10.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0908× (z -8.5) |
| [[SW1417 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -10.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PJA2]] | +0.63 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[RAB3A]] | +0.59 | +0.46 / +0.31 | both halves | 2e-04 |  |
| [[TRAM2]] | +0.57 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[MIDEAS]] | +0.56 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[GDE1]] | +0.56 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[HLTF]] | +0.56 | +0.37 / +0.38 | both halves | 9e-05 | ⚠ same locus (43.1 kb: neighbours can correlate without regulation) |
| [[PIP4P2]] | +0.56 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[DEPP1]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[ALDOA]] | +0.55 | +0.43 / +0.37 | both halves | 9e-05 |  |
| [[DNAAF3]] | +0.55 | +0.44 / +0.21 | both halves | 7e-04 |  |
| [[ZNF184]] | +0.54 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[PCTP]] | +0.54 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[RYBP]] | +0.53 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU6F1]] | -0.63 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[GABPB1]] | -0.57 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[PCBD2]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PBLD]] | -0.56 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[ATXN7L3-AS1]] | -0.54 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[BICRAL]] | -0.53 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[AP4S1]] | -0.53 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[ITPA]] | -0.53 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[EPM2A]] | -0.53 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[PPP3CB-AS1]] | -0.53 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[NINJ2]] | -0.52 | -0.52 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[SLC20A2]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PCBP1-AS1]] | -0.51 | -0.38 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV2]] | B | NAV2 activity raises HPS3's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without NAV2 | 0.011 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[LINC01322]] | B | LINC01322 activity weakens HPS3's drug response | lines that do not express LINC01322 (35) vs lines expressing it (13) | the lines without LINC01322 respond 1.36× as strongly (z diff -1.73); strongest at Topotecan (hydrochloride) 5 µM: 0.49x vs 0.71x (z diff -2.6) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, TM4SF4, TIMD4; target measured in part of the lines; artifact flags |
| [[DEPP1]] | B | DEPP1 activity raises HPS3's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without DEPP1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HPS3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers HPS3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PIP4P2]] | C | PIP4P2 activity strengthens HPS3's drug response | lines that do not express PIP4P2 (4) vs lines expressing it (44) | the lines without PIP4P2 respond 0.58× as strongly (z diff +2.46); strongest at Idarubicin (hydrochloride) 5 µM: 0.82x vs 0.43x (z diff +5.1) | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **-** arm (projection on the module's main direction -0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.8, 10.6); signed map (-29.7, 23.9). **Vector** length 95.7, 27.7% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.0 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -20.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.0 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | HPS3 biogenesis of lysosomal organelles complex 2 subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q24 — chr3:149,129,638-149,173,732 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUTAL, BLOC2S1 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969F9](https://www.uniprot.org/uniprotkb/Q969F9) (BLOC-2 complex member HPS3):

> Involved in early stages of melanosome biogenesis and maturation.

**Summary**, from NCBI Gene [84343](https://www.ncbi.nlm.nih.gov/gene/84343):

> This gene encodes a protein containing a potential clathrin-binding motif, consensus dileucine signals, and tyrosine-based sorting signals for targeting to vesicles of lysosomal lineage. The encoded protein may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 3. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:15597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15597) · Entrez [84343](https://www.ncbi.nlm.nih.gov/gene/84343) · UniProt [Q969F9](https://www.uniprot.org/uniprotkb/Q969F9) · Ensembl [ENSG00000163755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163755)

## Data

Gene col 8773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8773); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8773]; `tensor/DDL_lfc|DDL_z.npy` [8773]; `embed/gene_vectors.npy` [8773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8773 or target_col == 8773). Every well: [[HPS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
