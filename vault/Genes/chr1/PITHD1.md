---
symbol: "PITHD1"
type: "gene"
col: 652
ensembl_id: "ENSG00000057757"
name: "PITH domain containing 1"
location: "1p36.11"
module: 49
arm: "+"
pooled_cpm: 26.63
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PITHD1

*PITH domain containing 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.23× (z +26.0, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0714×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0946×); [[Naproxen (drug)]] 0.05 µM in 1 line (AN3 CA 0.0853×).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIKE1]] (+0.57, fdr 1e-05), [[RHBDD2]] (+0.53, fdr 1e-05), [[POLR2C]] (+0.51, fdr 3e-05); moves opposite to [[ERBIN]] (-0.47, fdr 7e-05), [[AGT]] (-0.45, fdr 1e-04), [[CHN1]] (-0.41, fdr 4e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MEX3A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.23×** | +26.0 | 0e+00 | 47/47 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.23×** | +18.4 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.89×** | +16.6 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.78×** | +16.0 | 0e+00 | 43/47 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.74×** | +15.8 | 0e+00 | 46/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +13.9 | 4e-42 | 46/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.22×** | +12.5 | 9e-34 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +12.4 | 2e-33 | 41/45 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +11.9 | 4e-31 | 43/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.02×** | +11.0 | 1e-26 | 43/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +10.7 | 8e-25 | 43/48 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.96×** | +10.5 | 4e-24 | 41/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +10.2 | 6e-23 | 39/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +9.9 | 2e-21 | 41/48 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.79×** | +8.8 | 5e-17 | 37/46 (LoVo, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +8.7 | 1e-16 | 40/48 (HepG2/C3A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.4 | 2e-06 | 26/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +4.1 | 1e-03 | 21/48 (LOX-IMVI, C32, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.002 | 21/47 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.002 | 16/46 (hTERT-HPNE, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.005 | 14/48 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.006 | 11/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 652.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0714×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0946×); [[Naproxen (drug)]] 0.05 µM in 1 line (AN3 CA 0.0853×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 0.811× | -3.3 | 0.55 | 17/48 (A549, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.4 | 14 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +16.5) | — |
| [[SW480 (line)]] | alt | 30.3 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +17.3) | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +17.0) | — |
| [[PANC-1 (line)]] | alt | 28.5 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.4) | — |
| [[RKO (line)]] | wt | 30.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +14.9) | — |
| [[LoVo (line)]] | wt | 26.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +18.1) | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 31.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 47.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.68× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 24.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +19.2) | — |
| [[HT-29 (line)]] | alt | 33.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +15.9) | — |
| [[J82 (line)]] | alt | 41.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.5) | — |
| [[KATO III (line)]] | alt | 23.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +14.6) | [[Ixazomib (drug)]] 5 µM 0.0517× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 26.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +17.1) | — |
| [[CFPAC-1 (line)]] | alt | 33.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 29.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.44× (z +8.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.7) | — |
| [[A-427 (line)]] | wt | 25.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0714× (z -11.2) |
| [[C32 (line)]] | wt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 32.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 24.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 37.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.8) | — |
| [[A-172 (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[A498 (line)]] | wt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.4) | — |
| [[A549 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 46.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.95× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0946× (z -10.8) |
| [[SW 900 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +13.6) | — |
| [[SW48 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIKE1]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[RHBDD2]] | +0.53 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[POLR2C]] | +0.51 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[DNAJB2]] | +0.49 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[NQO2]] | +0.45 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[HGS]] | +0.45 | +0.44 / +0.21 | both halves | 7e-04 |  |
| [[NAGK]] | +0.45 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[RETSAT]] | +0.45 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[RPS6KB2]] | +0.44 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[KLHL21]] | +0.44 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[TMEM167B]] | +0.44 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[PIGH]] | +0.44 | +0.26 / +0.55 | both halves | 4e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERBIN]] | -0.47 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[AGT]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[CHN1]] | -0.41 | -0.28 / -0.26 | both halves | 4e-04 |  |
| [[TBC1D5]] | -0.41 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[PVT1]] | -0.41 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[MEX3A]] | -0.41 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[SUPT16H]] | -0.40 | -0.27 / -0.29 | both halves | 3e-04 |  |
| [[SINHCAF]] | -0.40 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[SNRPE]] | -0.40 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[FOXP1]] | -0.40 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[BDNF]] | -0.39 | -0.33 / -0.25 | both halves | 4e-04 |  |
| [[LINC02832]] | -0.39 | -0.26 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEX3A]] | B | MEX3A activity raises PITHD1's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without MEX3A | 0.042 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.293). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.0, -51.4); signed map (-9.5, 20.0). **Vector** length 50.0, 9.39% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +12.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +16.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +9.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | -0.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -2.5 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | +11.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | PITH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:23,778,418-23,788,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT014, TXNL1CL; previously C1orf128 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZP4](https://www.uniprot.org/uniprotkb/Q9GZP4) (PITH domain-containing protein 1):

> Promotes megakaryocyte differentiation by up-regulating RUNX1 expression. Regulates RUNX1 expression by activating the proximal promoter of the RUNX1 gene and by enhancing the translation activity of an internal ribosome entry site (IRES) element in the RUNX1 gene.

**Summary**, from NCBI Gene [57095](https://www.ncbi.nlm.nih.gov/gene/57095):

> Involved in positive regulation of DNA-templated transcription and positive regulation of megakaryocyte differentiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25022) · Entrez [57095](https://www.ncbi.nlm.nih.gov/gene/57095) · UniProt [Q9GZP4](https://www.uniprot.org/uniprotkb/Q9GZP4) · Ensembl [ENSG00000057757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057757)

## Data

Gene col 652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 652); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 652]; `tensor/DDL_lfc|DDL_z.npy` [652]; `embed/gene_vectors.npy` [652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 652 or target_col == 652). Every well: [[PITHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
