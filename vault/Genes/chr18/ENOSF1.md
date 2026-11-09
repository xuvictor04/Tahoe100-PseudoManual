---
symbol: "ENOSF1"
type: "gene"
col: 5285
ensembl_id: "ENSG00000132199"
name: "enolase superfamily member 1"
location: "18p11.32"
module: 124
arm: "+"
pooled_cpm: 86.97
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# ENOSF1

*enolase superfamily member 1* — 18p11.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 2.72×, SK-MEL-2 2.09×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.10×; ⚠ cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.431× (z -13.1, q 1e-36, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF337-AS1]] (+0.64, fdr 4e-05), [[ANKRD18A]] (+0.64, fdr 1e-04), [[GABPB1-AS1]] (+0.62, fdr 5e-05); moves opposite to [[TWF2]] (-0.65, fdr 1e-04), [[ATOSB]] (-0.64, fdr 4e-05), [[CARD19]] (-0.63, fdr 8e-05).
> It sits in the **+** arm of [[Module 124]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5285.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 2.72×, SK-MEL-2 2.09×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 2.10×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.27× | +3.6 | 0.21 | 23/47 (NCI-H23, A-172, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.53 | 15/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5285.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -13.1 | 1e-36 | 45/48 (NCI-H1792, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.470×** | -11.8 | 1e-29 | 42/48 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.489×** | -11.2 | 1e-26 | 45/48 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -9.6 | 1e-19 | 38/48 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -9.6 | 1e-19 | 38/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -7.9 | 3e-13 | 41/48 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -7.7 | 1e-12 | 35/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.600×** | -7.7 | 1e-12 | 35/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -7.7 | 1e-12 | 42/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -7.3 | 2e-11 | 34/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.632×** | -7.2 | 4e-11 | 36/47 (SW480, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -6.3 | 1e-08 | 39/49 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.689×** | -5.8 | 3e-07 | 35/48 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.775×** | -5.6 | 9e-07 | 24/48 (A549, NCI-H1573, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.687×** | -5.5 | 1e-06 | 32/48 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -5.1 | 1e-05 | 31/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.769×** | -3.9 | 0.002 | 25/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.636×** | -3.7 | 0.005 | 26/49 (NCI-H1792, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.796×** | -3.5 | 0.009 | 23/48 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.861× | -3.3 | 0.022 | 17/49 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 196 | 0 | 15 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.195× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 230 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.234× (z -15.0) |
| [[SW480 (line)]] | alt | 76.4 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -14.0) |
| [[PANC-1 (line)]] | alt | 107 | 0 | 8 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -15.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 90.7 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.361× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -14.1) |
| [[SNU-423 (line)]] | alt | 98.4 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -10.7) |
| [[LoVo (line)]] | wt | 76.4 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.349× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.392× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 144 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.444× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 181 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -15.1) |
| [[J82 (line)]] | alt | 128 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.187× (z -18.8) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.397× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.304× (z -11.1) |
| [[RKO (line)]] | wt | 112 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -12.8) |
| [[HCT15 (line)]] | alt | 117 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -10.8) |
| [[A-427 (line)]] | wt | 89.2 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.448× (z -9.0) |
| [[COLO 205 (line)]] | alt | 109 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.197× (z -14.7) |
| [[H4 (line)]] | wt | 48.0 | 0 | 3 (3 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0562× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 97.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.376× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.415× (z -9.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.214× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 87.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.400× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 42.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 41.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.310× (z -9.5) |
| [[HOP62 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.312× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[RPMI-7951 (line)]] | alt | 79.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.275× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Lonafarnib (drug)]] 5 µM 0.132× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.320× (z -8.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -11.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C-33 A (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.269× (z -10.0) ⚠ toxic |
| [[C32 (line)]] | wt | 62.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.218× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -12.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 62.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.414× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -8.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW 1271 (line)]] | alt | 102 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0960× (z -9.9) |
| [[SW48 (line)]] | wt | 72.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.258× (z -8.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF337-AS1]] | +0.64 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD18A]] | +0.64 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | +0.62 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[SNX5]] | +0.61 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[GCFC2]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[CASD1]] | +0.59 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[QTRT1]] | +0.58 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[SPTY2D1OS]] | +0.56 | +0.51 / +0.21 | both halves | 7e-04 |  |
| [[NFYC]] | +0.56 | +0.59 / +0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[VPS35L]] | +0.56 | +0.52 / +0.27 | both halves | 3e-04 |  |
| [[WARS2-AS1]] | +0.56 | +0.56 / +0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[SLC16A9]] | +0.55 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[ZNF124]] | +0.55 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[DUS3L]] | +0.54 | +0.30 / +0.40 | both halves | 2e-04 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWF2]] | -0.65 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[ATOSB]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[CARD19]] | -0.63 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[SPSB3]] | -0.61 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[USP35]] | -0.61 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[ZNRD2]] | -0.61 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[PCMT1]] | -0.60 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[MACO1]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[OSTF1]] | -0.60 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[TMEM184B]] | -0.59 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.58 | -0.56 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[AGPAT2]] | -0.58 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SIPA1]] | -0.58 | -0.50 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (5.5, 3.6); signed map (21.8, -32.6). **Vector** length 87.8, 25.6% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.0 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.5 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.1 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | -0.3 |
|  | [[Afatinib (drug)]] 5 µM |  | +2.0 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.2 | -7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -11.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -11.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | enolase superfamily member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:670,318-712,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSRTSBETA, rTS, TYMSAS, FUCD |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5Y1](https://www.uniprot.org/uniprotkb/Q7L5Y1) (Mitochondrial enolase superfamily member 1):

> Plays a role in the catabolism of L-fucose, a sugar that is part of the carbohydrates that are attached to cellular glycoproteins. Catalyzes the dehydration of L-fuconate to 2-keto-3-deoxy-L-fuconate by the abstraction of the 2-proton to generate an enediolate intermediate that is stabilized by the magnesium ion.

**Summary**, from NCBI Gene [55556](https://www.ncbi.nlm.nih.gov/gene/55556):

> This gene can encode a mitochondrial enzyme that is thought to convert L-fuconate to 2-keto-3-deoxy-L-fuconate. This locus was originally identified as the source of antisense RNAs of the adjacent thymidylate synthase gene. Splice variants at this locus may contain an alternate 3' exon that is complementary to the 3'UTR and terminal intron of the thymidylate synthase (TS) RNA and may downregulate TS expression. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:30365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30365) · Entrez [55556](https://www.ncbi.nlm.nih.gov/gene/55556) · UniProt [Q7L5Y1](https://www.uniprot.org/uniprotkb/Q7L5Y1) · Ensembl [ENSG00000132199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132199)

## Data

Gene col 5285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5285); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5285]; `tensor/DDL_lfc|DDL_z.npy` [5285]; `embed/gene_vectors.npy` [5285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5285 or target_col == 5285). Every well: [[ENOSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENOSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
