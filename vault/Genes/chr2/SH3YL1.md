---
symbol: "SH3YL1"
type: "gene"
col: 426
ensembl_id: "ENSG00000035115"
name: "SH3 and SYLF domain containing 1"
location: "2p25.3"
module: 63
arm: "+"
pooled_cpm: 48.71
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 36
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SH3YL1

*SH3 and SYLF domain containing 1* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.28× (z +4.5, q 0.004, up in 17 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 1.49× (z +3.9, q 0.026, up in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.48×, LS 180 2.19×, AsPC-1 2.57×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 1.99×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.271× (z -34.6, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSL24D1]] (+0.57, fdr 1e-05), [[EIF4B]] (+0.51, fdr 4e-05), [[SRP72]] (+0.51, fdr 3e-04); moves opposite to [[BCAR1]] (-0.53, fdr 5e-05), [[ZNF101]] (-0.46, fdr 8e-05), [[IL27RA]] (-0.44, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GJB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 426.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.48×, LS 180 2.19×, AsPC-1 2.57×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 1.99×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.5 | 0.004 | 17/34 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.026 | 13/47 (NCI-H1573, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.20×** | +3.5 | 0.095 | 17/45 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.20× | +3.2 | 0.15 | 10/46 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.15 | 9/47 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.19 | 9/46 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.19 | 14/46 (LOX-IMVI, RPMI-7951, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.19 | 3/46 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.271×** | -34.6 | 0e+00 | 44/45 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.337×** | -20.4 | 0e+00 | 43/45 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.365×** | -18.9 | 0e+00 | 46/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.367×** | -18.8 | 0e+00 | 40/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.355×** | -18.6 | 0e+00 | 42/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.415×** | -16.5 | 0e+00 | 44/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -15.4 | 0e+00 | 41/47 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.466×** | -14.3 | 2e-44 | 41/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.493×** | -13.2 | 3e-38 | 41/46 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.521×** | -12.2 | 2e-32 | 37/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.580×** | -10.2 | 1e-22 | 39/46 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.612×** | -9.2 | 2e-18 | 34/46 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -8.8 | 4e-17 | 36/46 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.630×** | -8.6 | 2e-16 | 35/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -8.1 | 2e-14 | 37/47 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -6.4 | 5e-09 | 30/45 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -6.2 | 2e-08 | 28/46 (H4, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -5.1 | 9e-06 | 27/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.831×** | -4.9 | 3e-05 | 22/46 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.770×** | -4.5 | 1e-04 | 27/46 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.9 | 0.002 | 19/46 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.1 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -24.1) |
| [[PANC-1 (line)]] | alt | 73.0 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -34.7) |
| [[KATO III (line)]] | alt | 148 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0592× (z -20.2) |
| [[LoVo (line)]] | wt | 56.1 | 1 (1 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 46.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.9) |
| [[LS 180 (line)]] | wt | 112 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -18.9) |
| [[SW1417 (line)]] | alt | 78.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -23.8) |
| [[COLO 205 (line)]] | alt | 126 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 74.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -20.2) |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -18.9) |
| [[RKO (line)]] | wt | 36.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -23.2) |
| [[H4 (line)]] | wt | 28.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 87.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -26.4) |
| [[SW 900 (line)]] | alt | 39.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -19.1) |
| [[SW480 (line)]] | alt | 25.3 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.2) |
| [[A-172 (line)]] | wt | 46.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.6) |
| [[A549 (line)]] | wt | 26.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -22.2) |
| [[AsPC-1 (line)]] | alt | 79.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -16.8) |
| [[BT-474 (line)]] | alt | 79.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -23.5) |
| [[CFPAC-1 (line)]] | alt | 54.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -24.3) |
| [[HT-29 (line)]] | alt | 93.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -20.4) |
| [[HCT15 (line)]] | alt | 100 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -14.5) |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.3) |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.2) |
| [[J82 (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 39.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.277× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -17.3) |
| [[SNU-1 (line)]] | wt | 48.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -11.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -19.0) |
| [[SW48 (line)]] | wt | 77.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.2) |
| [[A-427 (line)]] | wt | 30.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.136× (z -8.5) |
| [[A498 (line)]] | wt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -18.6) |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.9) |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~66% of this change |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSL24D1]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[EIF4B]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SRP72]] | +0.51 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[COPB2-DT]] | +0.49 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[MORF4L1]] | +0.48 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[RPS9]] | +0.48 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[RPL14]] | +0.48 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[NPM1]] | +0.47 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[EPRS1]] | +0.47 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[FAM172A]] | +0.46 | +0.40 / +0.43 | both halves | 4e-05 |  |
| [[PYCR1]] | +0.46 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[HSPA9]] | +0.46 | +0.34 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAR1]] | -0.53 | -0.40 / -0.48 | both halves | 5e-05 | same gene group |
| [[ZNF101]] | -0.46 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[IL27RA]] | -0.44 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[ENDOG]] | -0.44 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[TUBA4A]] | -0.43 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[HDAC7]] | -0.43 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[IRF2BPL]] | -0.43 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[GASAL1]] | -0.43 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[GJB2]] | -0.42 | -0.21 / -0.48 | both halves | 7e-04 |  |
| [[ST3GAL2]] | -0.42 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[LINC01145-1]] | -0.42 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[ZNF827]] | -0.42 | -0.35 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJB2]] | B | GJB2 activity raises SH3YL1's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without GJB2 | 0.030 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[TUBA4A]] | B | TUBA4A activity raises SH3YL1's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without TUBA4A | 0.033 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SH3YL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.346). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.6, -25.1); signed map (-23.8, -33.4). **Vector** length 61.6, 13.2% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | +2.1 | -5.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -6.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -15.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -2.8 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.7 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and SYLF domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:217,730-266,398 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ray, DKFZP586F1318 |
| Gene groups (HGNC) | SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q96HL8](https://www.uniprot.org/uniprotkb/Q96HL8) carries no function annotation.

**Summary**, from NCBI Gene [26751](https://www.ncbi.nlm.nih.gov/gene/26751):

> Enables phosphatase binding activity and phosphatidylinositol binding activity. Predicted to be involved in regulation of ruffle assembly. Predicted to act upstream of or within phosphatidylinositol biosynthetic process. Located in ruffle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29546) · Entrez [26751](https://www.ncbi.nlm.nih.gov/gene/26751) · UniProt [Q96HL8](https://www.uniprot.org/uniprotkb/Q96HL8) · Ensembl [ENSG00000035115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035115)

## Data

Gene col 426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 426); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 426]; `tensor/DDL_lfc|DDL_z.npy` [426]; `embed/gene_vectors.npy` [426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 426 or target_col == 426). Every well: [[SH3YL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3YL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
