---
symbol: "GOLGA1"
type: "gene"
col: 5942
ensembl_id: "ENSG00000136935"
name: "golgin A1"
location: "9q33.3"
module: 28
arm: "+"
pooled_cpm: 56.51
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# GOLGA1

*golgin A1* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.23× (z +4.9, q 5e-04, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.397× (z -21.9, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.453× (z -18.8, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1A]] (+0.70, fdr 7e-06), [[SAFB2]] (+0.65, fdr 1e-05), [[SEC23B]] (+0.65, fdr 1e-05); moves opposite to [[LPCAT4]] (-0.58, fdr 1e-05), [[SESTD1]] (-0.57, fdr 4e-05), [[LMTK2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.9 | 5e-04 | 23/48 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.12× | +3.7 | 0.068 | 7/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.11 | 9/47 (SW480, LS 180, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.38 | 12/48 (A-172, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -21.9 | 0e+00 | 46/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.453×** | -18.8 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.453×** | -18.8 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.523×** | -15.4 | 0e+00 | 45/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.491×** | -13.9 | 1e-41 | 42/47 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -13.6 | 4e-40 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.386×** | -11.8 | 3e-30 | 39/48 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.431×** | -10.4 | 1e-23 | 38/49 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.644×** | -10.4 | 1e-23 | 37/48 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -10.0 | 1e-21 | 40/48 (J82, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.673×** | -9.4 | 3e-19 | 34/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.694×** | -8.6 | 3e-16 | 33/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -8.3 | 6e-15 | 39/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -8.1 | 3e-14 | 29/47 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -6.9 | 2e-10 | 30/48 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.853× | -5.3 | 3e-06 | 17/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.843× | -4.0 | 0.001 | 18/48 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.900× | -3.5 | 0.009 | 10/49 (SNU-1, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.863× | -3.5 | 0.010 | 16/47 (NCI-H460, SK-MEL-2, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.901× | -3.5 | 0.010 | 15/48 (Hs 766T, J82, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.872× | -3.2 | 0.024 | 14/48 (MIA PaCa-2, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 85.2 | 0 | 11 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.299× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 62.9 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.294× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 86.4 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.282× (z -11.7) |
| [[SNU-423 (line)]] | alt | 73.8 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -13.2) |
| [[PANC-1 (line)]] | alt | 53.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -18.4) |
| [[SW480 (line)]] | alt | 55.2 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.253× (z -18.0) |
| [[HS-578T (line)]] | alt | 51.7 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -13.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.296× (z -10.6) |
| [[HOP62 (line)]] | alt | 42.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.379× (z -9.8) |
| [[KATO III (line)]] | alt | 72.5 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -29.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -11.5) |
| [[LS 180 (line)]] | wt | 41.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 66.1 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -13.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.114× (z -10.7) |
| [[BT-474 (line)]] | alt | 55.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.274× (z -11.3) |
| [[COLO 205 (line)]] | alt | 75.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -10.9) |
| [[H4 (line)]] | wt | 55.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -10.9) |
| [[Hs 766T (line)]] | wt | 79.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.453× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 48.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 92.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -12.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 64.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0997× (z -9.3) |
| [[HCT15 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 47.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.408× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.257× (z -9.2) |
| [[RKO (line)]] | wt | 76.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -11.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.198× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 64.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.269× (z -9.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -8.9) |
| [[A-172 (line)]] | wt | 88.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.486× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A498 (line)]] | wt | 49.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.373× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 61.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.233× (z -9.6) |
| [[LoVo (line)]] | wt | 56.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -10.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -13.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -9.8) |
| [[SW 1271 (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0697× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 28.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.324× (z -8.5) |
| [[SW1417 (line)]] | alt | 42.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.395× (z -8.9) |
| [[SW48 (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -9.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1A]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SAFB2]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SEC23B]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PAN2]] | +0.64 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[LYSMD3]] | +0.63 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[UFL1]] | +0.62 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[ZNF397]] | +0.62 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[POLI]] | +0.62 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[XRRA1]] | +0.62 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[DDX50]] | +0.62 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 | same gene group; pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 644 |
| [[ZC3H6]] | +0.62 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT4]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SESTD1]] | -0.57 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[LMTK2]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CMTM8]] | -0.56 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[SRPK2]] | -0.56 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[CDYL]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[XPR1]] | -0.55 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[HACD3]] | -0.54 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[UBE2G1]] | -0.54 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[ZNF277]] | -0.54 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[CYRIB]] | -0.53 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[PLXND1]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.4, 17.3); signed map (8.6, -16.3). **Vector** length 94.1, 25.4% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.7 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | -0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +0.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -13.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -21.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -11.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -10.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | golgin A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,878,275-124,948,492 (-) |
| Ensembl biotype | protein_coding |
| Also known as | golgin-97, MGC33154 |
| Gene groups (HGNC) | Golgins |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92805](https://www.uniprot.org/uniprotkb/Q92805) (Golgin subfamily A member 1):

> Involved in vesicular trafficking at the Golgi apparatus level. Involved in endosome-to-Golgi trafficking. Mechanistically, captures transport vesicles arriving from endosomes via the protein TBC1D23. Recognized vesicles are then tethered to the trans-Golgi before subsequent SNARE engagement and vesicle fusion. Selectively regulates E-cadherin transport from the trans-Golgi network in tubulovesicular carriers.; (Microbial infection) Plays an important role in poxvirus morphogenesis. …

**Summary**, from NCBI Gene [2800](https://www.ncbi.nlm.nih.gov/gene/2800):

> The Golgi apparatus, which participates in glycosylation and transport of proteins and lipids in the secretory pathway, consists of a series of stacked cisternae (flattened membrane sacs). Interactions between the Golgi and microtubules are thought to be important for the reorganization of the Golgi after it fragments during mitosis. This gene encodes one of the golgins, a family of proteins localized to the Golgi. This encoded protein is associated with Sjogren's syndrome. [provided by RefSeq, …

**Accessions** — [HGNC:4424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4424) · Entrez [2800](https://www.ncbi.nlm.nih.gov/gene/2800) · UniProt [Q92805](https://www.uniprot.org/uniprotkb/Q92805) · Ensembl [ENSG00000136935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136935)

## Data

Gene col 5942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5942); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5942]; `tensor/DDL_lfc|DDL_z.npy` [5942]; `embed/gene_vectors.npy` [5942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5942 or target_col == 5942). Every well: [[GOLGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
