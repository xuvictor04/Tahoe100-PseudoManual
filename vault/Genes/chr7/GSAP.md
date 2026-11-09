---
symbol: "GSAP"
type: "gene"
col: 11775
ensembl_id: "ENSG00000186088"
name: "gamma-secretase activating protein"
location: "7q11.23"
module: 5
arm: "+"
pooled_cpm: 42.87
n_lines_expressing: 44
n_dd_up: 2
n_dd_down: 40
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GSAP

*gamma-secretase activating protein* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.27× (z +3.6, q 0.094, up in 16 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.196× (z -24.0, q 0e+00, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENOX2]] (+0.51, fdr 1e-04), [[ZC3H12C]] (+0.51, fdr 5e-04), [[SPOPL-DT]] (+0.50, fdr 9e-05); moves opposite to [[PTOV1]] (-0.51, fdr 1e-04), [[MEF2D]] (-0.50, fdr 8e-05), [[PLOD1]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TRABD2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.094 | 16/42 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Finasteride (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.094 | 13/42 (NCI-H460, A498, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.5 | 0.094 | 13/42 (SW 900, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.25× | +3.3 | 0.14 | 15/42 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.196×** | -24.0 | 0e+00 | 41/42 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.200×** | -23.7 | 0e+00 | 41/42 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.323×** | -23.5 | 0e+00 | 38/42 (NCI-H1573, A549, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.237×** | -21.1 | 0e+00 | 41/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.355×** | -15.2 | 0e+00 | 39/42 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.413×** | -13.0 | 1e-36 | 36/41 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -11.9 | 1e-30 | 34/42 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.451×** | -11.7 | 1e-29 | 35/42 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -11.1 | 5e-27 | 33/42 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.471×** | -11.1 | 1e-26 | 32/42 (SNU-423, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.480×** | -10.4 | 2e-23 | 34/42 (MIA PaCa-2, NCI-H1573, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.276×** | -9.9 | 2e-21 | 34/43 (Panc 03.27, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.524×** | -9.5 | 1e-19 | 34/42 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.511×** | -9.5 | 1e-19 | 32/39 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.537×** | -9.1 | 3e-18 | 31/42 (SNU-423, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.526×** | -8.4 | 1e-15 | 30/42 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -8.4 | 2e-15 | 27/41 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.568×** | -8.3 | 4e-15 | 33/42 (KATO III, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -7.6 | 9e-13 | 24/42 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -7.5 | 2e-12 | 29/40 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 93.8 | 0 | 22 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -22.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0671× (z -21.0) |
| [[LoVo (line)]] | wt | 61.7 | 0 | 15 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -24.9) |
| [[SK-MEL-2 (line)]] | alt | 72.2 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.127× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -31.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0807× (z -20.8) |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -21.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.134× (z -20.6) |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 0 | 12 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0169× (z -26.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0952× (z -15.9) |
| [[SW480 (line)]] | alt | 54.7 | 0 | 12 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0988× (z -21.5) |
| [[A549 (line)]] | wt | 56.8 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -25.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0853× (z -17.5) |
| [[KATO III (line)]] | alt | 101 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0871× (z -24.4) |
| [[NCI-H1792 (line)]] | alt | 110 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -20.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0730× (z -19.7) |
| [[SW48 (line)]] | wt | 80.8 | 0 | 11 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.114× (z -13.2) |
| [[SNU-423 (line)]] | alt | 46.7 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -16.6) |
| [[RKO (line)]] | wt | 34.7 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -24.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.130× (z -14.7) |
| [[A498 (line)]] | wt | 81.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -15.5) |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0450× (z -24.4) |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -13.1) |
| [[A-172 (line)]] | wt | 29.1 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.137× (z -13.0) |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -12.0) |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -12.1) |
| [[COLO 205 (line)]] | alt | 37.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -9.9) |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -11.7) |
| [[J82 (line)]] | alt | 19.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.250× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.109× (z -15.1) |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.200× (z -13.6) |
| [[A-427 (line)]] | wt | 24.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 41.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.171× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 51.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -12.3) |
| [[SW 900 (line)]] | alt | 25.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.233× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 26.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.279× (z -9.5) |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -10.0) |
| [[HOP62 (line)]] | alt | 23.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | +0.51 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[ZC3H12C]] | +0.51 | +0.24 / +0.48 | both halves | 5e-04 |  |
| [[SPOPL-DT]] | +0.50 | +0.37 / +0.42 | both halves | 9e-05 |  |
| [[TRABD2B]] | +0.49 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[LINC01829]] | +0.49 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[SERPINB8]] | +0.49 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[GPATCH4]] | +0.48 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[LINC02320]] | +0.47 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[LACC1]] | +0.46 | +0.21 / +0.40 | both halves | 7e-04 |  |
| [[SERPINB2]] | +0.45 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[TFAM]] | +0.45 | +0.31 / +0.31 | both halves | 2e-04 |  |
| [[PYCR2]] | +0.45 | +0.25 / +0.31 | both halves | 4e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTOV1]] | -0.51 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[MEF2D]] | -0.50 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[PLOD1]] | -0.49 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[ARHGAP35]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[GAPDH]] | -0.48 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[KANTR]] | -0.48 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[HCFC1R1]] | -0.48 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PKD1]] | -0.46 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[GPI]] | -0.45 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[GNAI2]] | -0.45 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[HDGFL2]] | -0.45 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[TBC1D17]] | -0.45 | -0.33 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2B]] | B | TRABD2B activity raises GSAP's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without TRABD2B | 0.010 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[LINC02320]] | B | LINC02320 activity raises GSAP's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.01× lower at baseline in the lines without LINC02320 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[RPH3AL]] | B | RPH3AL activity raises GSAP's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without RPH3AL | 0.064 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[MYD88]] | B | MYD88 activity raises GSAP's level | lines that do not express MYD88 (5) vs lines expressing it (45) | 2.68× lower at baseline in the lines without MYD88 | 0.091 | ⚠ within organs, on part of the lines; also absent: PRRG1, KIFC3, HMGA1P4 |
| [[TARID]] | B | TARID activity raises GSAP's level | lines that do not express TARID (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TARID | 0.095 | ⚠ within organs, on part of the lines; also absent: STEAP4, ANXA10, HLA-DRB1 |
| [[PHF11]] | C | PHF11 activity raises GSAP's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 3.69× lower at baseline in the lines without PHF11 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.355). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (8.4, -7.4); signed map (15.5, 22.4). **Vector** length 80.7, 21.5% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | -8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.7 | +0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -21.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -11.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.2 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.1 | -3.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -9.1 |

## What is on record

|  |  |
|---|---|
| Name | gamma-secretase activating protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:77,310,751-77,416,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC54103; previously PION |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D1B5](https://www.uniprot.org/uniprotkb/A4D1B5) (Gamma-secretase-activating protein):

> Regulator of gamma-secretase activity, which specifically activates the production of amyloid-beta protein (amyloid-beta protein 40 and amyloid-beta protein 42), without affecting the cleavage of other gamma-secretase targets such has Notch. The gamma-secretase complex is an endoprotease complex that catalyzes the intramembrane cleavage of integral membrane proteins such as Notch receptors and APP (amyloid-beta precursor protein). Specifically promotes the gamma-cleavage of APP CTF-alpha (also …

**Summary**, from NCBI Gene [54103](https://www.ncbi.nlm.nih.gov/gene/54103):

> Accumulation of neurotoxic amyloid-beta is a major hallmark of Alzheimer disease (AD; MIM 104300). Formation of amyloid-beta is catalyzed by gamma-secretase (see PSEN1; MIM 104311), a protease with numerous substrates. PION, or GSAP, selectively increases amyloid-beta production through a mechanism involving its interaction with both gamma-secretase and its substrate, the amyloid-beta precursor protein (APP; MIM 104760) C-terminal fragment (APP-CTF) (He et al., 2010 [PubMed 20811458]).[supplied …

**Accessions** — [HGNC:28042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28042) · Entrez [54103](https://www.ncbi.nlm.nih.gov/gene/54103) · UniProt [A4D1B5](https://www.uniprot.org/uniprotkb/A4D1B5) · Ensembl [ENSG00000186088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186088)

## Data

Gene col 11775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11775); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11775]; `tensor/DDL_lfc|DDL_z.npy` [11775]; `embed/gene_vectors.npy` [11775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11775 or target_col == 11775). Every well: [[GSAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
