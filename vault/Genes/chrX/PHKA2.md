---
symbol: "PHKA2"
type: "gene"
col: 499
ensembl_id: "ENSG00000044446"
name: "phosphorylase kinase regulatory subunit alpha 2"
location: "Xp22.13"
module: 68
arm: "-"
pooled_cpm: 43.2
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# PHKA2

*phosphorylase kinase regulatory subunit alpha 2* — Xp22.13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.465× (z -28.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHQ1]] (+0.69, fdr 7e-06), [[TAF5L]] (+0.68, fdr 1e-05), [[SLC27A1]] (+0.68, fdr 2e-04); moves opposite to [[ARRDC3-AS1]] (-0.71, fdr 5e-05), [[APLF]] (-0.69, fdr 1e-05), [[TSGA10]] (-0.68, fdr 6e-05).
> It sits in the **-** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.029 | 11/48 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.8 | 0.048 | 7/48 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.14 | 10/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 1.25× | +3.1 | 0.29 | 9/46 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -28.2 | 0e+00 | 45/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.420×** | -21.3 | 0e+00 | 40/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.457×** | -20.4 | 0e+00 | 45/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -15.5 | 0e+00 | 36/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -15.3 | 0e+00 | 41/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.568×** | -14.7 | 0e+00 | 37/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -13.6 | 2e-40 | 33/48 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.615×** | -12.6 | 9e-35 | 31/48 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.621×** | -12.4 | 2e-33 | 30/46 (COLO 205, C-33 A, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -10.8 | 2e-25 | 37/48 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -10.7 | 3e-25 | 35/47 (AN3 CA, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.683×** | -9.9 | 2e-21 | 34/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -9.8 | 4e-21 | 34/48 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -9.3 | 5e-19 | 27/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -9.3 | 8e-19 | 31/46 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -7.1 | 4e-11 | 24/48 (COLO 205, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.637×** | -6.1 | 2e-08 | 24/49 (Hs 766T, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.813×** | -5.4 | 2e-06 | 18/48 (C32, SNU-423, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -5.4 | 2e-06 | 23/48 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -5.4 | 2e-06 | 19/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 82.2 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -18.1) |
| [[SW480 (line)]] | alt | 83.6 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -13.9) |
| [[A-172 (line)]] | wt | 41.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.1) |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.6) |
| [[Hs 766T (line)]] | wt | 52.0 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 74.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -18.8) |
| [[HOP62 (line)]] | alt | 35.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.8) |
| [[KATO III (line)]] | alt | 68.7 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -10.8) |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.415× (z -11.0) |
| [[A498 (line)]] | wt | 34.4 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.324× (z -11.5) |
| [[SW 900 (line)]] | alt | 40.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.0) |
| [[A549 (line)]] | wt | 52.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 97.3 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -17.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.6) |
| [[J82 (line)]] | alt | 36.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.5) |
| [[LoVo (line)]] | wt | 24.6 | 0 | 4 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.363× (z -10.6) |
| [[SW1417 (line)]] | alt | 60.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -12.9) |
| [[A-427 (line)]] | wt | 55.6 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.6) |
| [[BT-474 (line)]] | alt | 46.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.0) |
| [[H4 (line)]] | wt | 55.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.8) |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 39.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 47.0 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.8) |
| [[SW48 (line)]] | wt | 41.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.8) |
| [[HCT15 (line)]] | alt | 53.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -11.5) |
| [[RKO (line)]] | wt | 38.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -12.5) |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -10.3) ⚠ toxic |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0692× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.384× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 36.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.2) |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*27 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHQ1]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.68 | +0.68 / +0.31 | both halves | 2e-04 |  |
| [[L2HGDH]] | +0.67 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[IQCB1]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.64 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[ELP1]] | +0.64 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[CEP131]] | +0.64 | +0.59 / +0.27 | both halves | 3e-04 |  |
| [[BRAT1]] | +0.63 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[INPP5B]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.63 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[LRRC42]] | +0.62 | +0.63 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*73 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRDC3-AS1]] | -0.71 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[APLF]] | -0.69 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[TSGA10]] | -0.68 | -0.68 / -0.38 | both halves | 6e-05 |  |
| [[MMADHC-DT]] | -0.68 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[PATL2]] | -0.67 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | -0.67 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[RIPK2-DT]] | -0.67 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[WAC-AS1]] | -0.67 | -0.66 / -0.34 | both halves | 1e-04 |  |
| [[LINC01762]] | -0.66 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[TMEM202-AS1]] | -0.66 | -0.64 / -0.29 | both halves | 3e-04 |  |
| [[MAD2L1-DT]] | -0.65 | -0.67 / -0.26 | both halves | 4e-04 |  |
| [[SLFN5]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PHKA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **-** arm (projection on the module's main direction -0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (6.5, 12.0); signed map (-39.9, -12.1). **Vector** length 82.1, 18.2% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.2 |
|  | [[NG25 (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -20.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -14.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylase kinase regulatory subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.13 — chrX:18,892,298-18,984,114 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PHK, PYK |
| Gene groups (HGNC) | Phosphorylase kinase subunits |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P46019](https://www.uniprot.org/uniprotkb/P46019) (Phosphorylase b kinase regulatory subunit alpha, liver isoform):

> Phosphorylase b kinase catalyzes the phosphorylation of serine in certain substrates, including troponin I. The alpha chain may bind calmodulin.

**Summary**, from NCBI Gene [5256](https://www.ncbi.nlm.nih.gov/gene/5256):

> Phosphorylase kinase is a polymer of 16 subunits, four each of alpha, beta, gamma and delta. The alpha subunit includes the skeletal muscle and hepatic isoforms, and the hepatic isoform is encoded by this gene. The beta subunit is the same in both the muscle and hepatic isoforms, and encoded by one gene. The gamma subunit also includes the skeletal muscle and hepatic isoforms, which are encoded by two different genes. The delta subunit is a calmodulin and can be encoded by three different …

**Accessions** — [HGNC:8926](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8926) · Entrez [5256](https://www.ncbi.nlm.nih.gov/gene/5256) · UniProt [P46019](https://www.uniprot.org/uniprotkb/P46019) · Ensembl [ENSG00000044446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000044446)

## Data

Gene col 499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 499); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 499]; `tensor/DDL_lfc|DDL_z.npy` [499]; `embed/gene_vectors.npy` [499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 499 or target_col == 499). Every well: [[PHKA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHKA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
