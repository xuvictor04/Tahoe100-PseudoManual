---
symbol: "RPGRIP1L"
type: "gene"
col: 2372
ensembl_id: "ENSG00000103494"
name: "RPGRIP1 like"
location: "16q12.2"
module: 49
arm: "+"
pooled_cpm: 24.51
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# RPGRIP1L

*RPGRIP1 like* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.86× (z +11.3, q 6e-27, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.344× (z -19.4, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POT1]] (+0.66, fdr 1e-05), [[SCFD2]] (+0.63, fdr 7e-06), [[FAM98A]] (+0.62, fdr 2e-05); moves opposite to [[FOXC1]] (-0.56, fdr 4e-05), [[GCNT4]] (-0.53, fdr 1e-04), [[SLC49A4]] (-0.52, fdr 4e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MSX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +11.3 | 6e-27 | 33/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +9.6 | 3e-19 | 16/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +9.1 | 2e-17 | 33/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +8.5 | 4e-15 | 31/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.6 | 3e-06 | 20/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.9 | 9e-05 | 19/46 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.9 | 9e-05 | 21/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 12/47 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.013 | 13/47 (A549, NCI-H1573, …) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.019 | 10/47 (A498, KATO III, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.019 | 10/47 (NCI-H2030, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.344×** | -19.4 | 0e+00 | 45/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.527×** | -16.4 | 0e+00 | 32/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -16.3 | 0e+00 | 41/46 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.447×** | -14.6 | 0e+00 | 41/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -13.1 | 5e-37 | 34/47 (A498, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -12.0 | 4e-31 | 34/47 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -8.1 | 5e-14 | 27/46 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -7.3 | 3e-11 | 29/46 (SNU-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -6.4 | 8e-09 | 25/47 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -6.1 | 4e-08 | 25/47 (KATO III, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -6.1 | 4e-08 | 24/47 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.714×** | -6.1 | 4e-08 | 22/46 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -5.9 | 1e-07 | 22/43 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.736×** | -5.4 | 4e-06 | 21/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -4.7 | 1e-04 | 20/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.786×** | -4.4 | 5e-04 | 14/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -3.6 | 0.009 | 15/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.015 | 17/47 (SW48, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 45.2 | 0 | 11 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -20.3) |
| [[H4 (line)]] | wt | 46.1 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 7 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -13.1) |
| [[A498 (line)]] | wt | 66.9 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -19.1) |
| [[SW480 (line)]] | alt | 22.8 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.235× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 5 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.202× (z -9.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.5) |
| [[J82 (line)]] | alt | 30.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.6) |
| [[PANC-1 (line)]] | alt | 27.7 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -10.9) |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.7) |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -16.6) |
| [[KATO III (line)]] | alt | 23.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.196× (z -11.2) |
| [[LoVo (line)]] | wt | 14.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.189× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.0) |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.1) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0859× (z -8.6) |
| [[BT-474 (line)]] | alt | 6.27 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0745× (z -9.4) |
| [[C-33 A (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.106× (z -8.9) |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -10.4) |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.6) |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -9.7) |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.274× (z -8.7) |
| [[SW 1088 (line)]] | alt | 66.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0498× (z -9.6) |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -8.5) |
| [[SW48 (line)]] | wt | 21.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0916× (z -10.6) |
| [[A-427 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POT1]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SCFD2]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FAM98A]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ELP1]] | +0.59 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[WDR36]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[IFT122]] | +0.57 | +0.45 / +0.47 | both halves | 3e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 505 |
| [[TOMM70]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ERI3]] | +0.56 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[NUP214]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ALDH18A1]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[TRAP1]] | +0.55 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[DLAT]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXC1]] | -0.56 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[GCNT4]] | -0.53 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[SLC49A4]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MED13]] | -0.52 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[RNF103]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[EIF3J-DT]] | -0.51 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[MSX1]] | -0.51 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[LINC01762]] | -0.50 | -0.39 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[C1orf54]] | -0.50 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[ATXN7L3-AS1]] | -0.50 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[PLSCR2]] | -0.50 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[LRRC8C-DT]] | -0.50 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[TMEM47]] | -0.49 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX1]] | B | MSX1 activity raises RPGRIP1L's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 2.18× lower at baseline in the lines without MSX1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[THRB]] | B | THRB activity lowers RPGRIP1L's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.48× higher at baseline in the lines without THRB | 0.060 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[HDAC6]] | B | HDAC6 activity lowers RPGRIP1L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HLTF]] | B | HLTF activity raises RPGRIP1L's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without HLTF | 0.090 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[TBC1D32]] | C | TBC1D32 activity raises RPGRIP1L's level | lines that do not express TBC1D32 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without TBC1D32 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ACOT12, ENSG00000271590, ENSG00000288545 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.409). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.3, -32.1); signed map (-15.2, -58.7). **Vector** length 94.1, 22.7% of its response variance represented; |z| ≥ 3 in 1,190 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +8.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.1 | +3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.5 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -3.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.4 | -0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -13.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RPGRIP1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:53,598,153-53,703,938 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1005, CORS3, JBTS7, MKS5, NPHP8, FTM, PPP1R134 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; C2 domain containing; MKS complex; NPHP complex |
| Reactome | 6 pathways, smallest: Hedgehog 'off' state; Anchoring of the basal body to the plasma membrane; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CZ1](https://www.uniprot.org/uniprotkb/Q68CZ1) (Protein fantom):

> Negatively regulates signaling through the G protein-coupled thromboxane A2 receptor (TBXA2R). May be involved in mechanisms like programmed cell death, craniofacial development, patterning of the limbs, and formation of the left-right axis (By similarity). Involved in the organization of apical junctions; the function is proposed to implicate a NPHP1-4-8 module. Does not seem to be strictly required for ciliogenesis. Involved in establishment of planar cell polarity such as in cochlear sensory …

**Summary**, from NCBI Gene [23322](https://www.ncbi.nlm.nih.gov/gene/23322):

> The protein encoded by this gene can localize to the basal body-centrosome complex or to primary cilia and centrosomes in ciliated cells. The encoded protein has been found to interact with nephrocystin-4. Defects in this gene are a cause of Joubert syndrome type 7 (JBTS7) and Meckel syndrome type 5 (MKS5). [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:29168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29168) · Entrez [23322](https://www.ncbi.nlm.nih.gov/gene/23322) · UniProt [Q68CZ1](https://www.uniprot.org/uniprotkb/Q68CZ1) · Ensembl [ENSG00000103494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103494)

## Data

Gene col 2372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2372); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2372]; `tensor/DDL_lfc|DDL_z.npy` [2372]; `embed/gene_vectors.npy` [2372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2372 or target_col == 2372). Every well: [[RPGRIP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPGRIP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
