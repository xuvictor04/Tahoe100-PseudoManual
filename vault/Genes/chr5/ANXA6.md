---
symbol: "ANXA6"
type: "gene"
col: 12327
ensembl_id: "ENSG00000197043"
name: "annexin A6"
location: "5q33.1"
module: 132
arm: "+"
pooled_cpm: 34.64
n_lines_expressing: 42
n_dd_up: 16
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# ANXA6

*annexin A6* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.28× (z +15.0, q 0e+00, up in 21 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.37× (z +8.3, q 1e-14, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.306× (z -31.6, q 0e+00, down in 38 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG3]] (+0.72, fdr 7e-06), [[PAPSS1]] (+0.70, fdr 1e-05), [[USP35]] (+0.67, fdr 1e-05); moves opposite to [[GTF2IRD2B]] (-0.67, fdr 1e-05), [[EP300]] (-0.65, fdr 2e-05), [[TOPORS]] (-0.63, fdr 1e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[FHL1]] → it (grade B ⚠); 5 go from it, the strongest it → [[KIF3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12327.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +15.0 | 0e+00 | 21/27 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +14.3 | 4e-44 | 29/35 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +9.7 | 9e-20 | 19/29 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +8.3 | 1e-14 | 24/40 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +6.9 | 5e-10 | 21/40 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +6.8 | 1e-09 | 19/40 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.6 | 4e-09 | 21/40 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 22/40 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 15/40 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 5e-04 | 17/40 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 10/40 (PANC-1, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +4.2 | 0.001 | 12/40 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 13/40 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.025 | 7/40 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.044 | 7/39 (SW1417, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.056 | 7/40 (Panc 03.27, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12327.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.306×** | -31.6 | 0e+00 | 38/40 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.372×** | -18.7 | 0e+00 | 37/40 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.457×** | -14.8 | 0e+00 | 35/40 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -13.4 | 9e-39 | 30/40 (SNU-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.612×** | -13.1 | 3e-37 | 30/39 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.541×** | -11.2 | 5e-27 | 35/40 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -10.6 | 2e-24 | 33/40 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -9.9 | 3e-21 | 32/40 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.634×** | -8.6 | 5e-16 | 27/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -7.0 | 1e-10 | 21/40 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.4 | 6e-09 | 22/40 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.737×** | -5.8 | 4e-07 | 19/39 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -5.2 | 1e-05 | 18/40 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -4.8 | 7e-05 | 20/37 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.777×** | -4.8 | 7e-05 | 16/39 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -4.5 | 2e-04 | 18/40 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.809×** | -4.0 | 0.002 | 13/40 (LOX-IMVI, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12327. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 85.7 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -30.0) |
| [[SW480 (line)]] | alt | 29.1 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 74.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -25.2) |
| [[H4 (line)]] | wt | 43.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.8) |
| [[HS-578T (line)]] | alt | 100 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.7) |
| [[PANC-1 (line)]] | alt | 17.1 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.63× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.1) |
| [[SNU-1 (line)]] | wt | 58.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.3) |
| [[SW1417 (line)]] | alt | 69.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -18.2) |
| [[A-172 (line)]] | wt | 144 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 87.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0787× (z -20.2) |
| [[NCI-H2030 (line)]] | alt | 31.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 24.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -16.4) |
| [[A498 (line)]] | wt | 95.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -19.3) |
| [[J82 (line)]] | alt | 54.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -19.4) |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.8) |
| [[LoVo (line)]] | wt | 8.73 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.18× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.8) |
| [[RKO (line)]] | wt | 33.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -16.1) |
| [[SNU-423 (line)]] | alt | 27.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.0) |
| [[SW 1088 (line)]] | alt | 130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.7) |
| [[SW 1271 (line)]] | alt | 77.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.6) |
| [[A-427 (line)]] | wt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -10.6) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.7) |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0769× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.8) |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.9) |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0826× (z -9.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 10.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.6) |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12327), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | +0.72 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.70 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[USP35]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[COL18A1]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[MPP1]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[STARD3NL]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[MBOAT2]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CS]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[WASF3]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[APMAP]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[JAM3]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.61 | +0.65 / +0.40 | both halves | 5e-05 | pathway: Muscle contraction |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | -0.67 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[EP300]] | -0.65 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TOPORS]] | -0.63 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.63 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[CREBBP]] | -0.63 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[UNK]] | -0.61 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[PDCD7]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[DNAI4]] | -0.60 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.59 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[INO80D]] | -0.59 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[RBBP6]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LINC01004]] | -0.58 | -0.62 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHL1]] | B | FHL1 activity raises ANXA6's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without FHL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[COL6A2]] | B | COL6A2 activity raises ANXA6's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without COL6A2 | 0.020 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[MYO5A]] | B | MYO5A activity raises ANXA6's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 4.01× lower at baseline in the lines without MYO5A | 0.040 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[COL5A1]] | B | COL5A1 activity raises ANXA6's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.84× lower at baseline in the lines without COL5A1 | 0.050 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[VASH1]] | B | VASH1 activity raises ANXA6's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without VASH1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[KIF3C]] | B | KIF3C activity raises ANXA6's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 3.60× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[SPEG]] | B | SPEG activity raises ANXA6's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without SPEG | 0.065 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1 |
| [[LOXL1]] | B | LOXL1 activity raises ANXA6's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without LOXL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[TOP2A]] | B | TOP2A activity raises ANXA6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SCARA3]] | B | SCARA3 activity raises ANXA6's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without SCARA3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[DKK3]] | B | DKK3 activity raises ANXA6's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without DKK3 | 0.080 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[HLTF]] | B | HLTF activity raises ANXA6's level | lines that do not express HLTF (8) vs lines expressing it (42) | 3.38× lower at baseline in the lines without HLTF | 0.082 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF3C]] | B | ANXA6 activity raises KIF3C's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.35× lower at baseline in the lines without ANXA6 | 0.006 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[CRTAP]] | B | ANXA6 activity raises CRTAP's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without ANXA6 | 0.009 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[BLMH]] | B | ANXA6 activity raises BLMH's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.37× lower at baseline in the lines without ANXA6 | 0.057 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[OPA1]] | B | ANXA6 activity raises OPA1's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 1.20× lower at baseline in the lines without ANXA6 | 0.059 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[NXPE3]] | B | ANXA6 activity raises NXPE3's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.17× lower at baseline in the lines without ANXA6 | 0.060 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.9, -6.5); signed map (-35.5, -13.4). **Vector** length 114, 29.4% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +14.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -18.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -31.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.9 | -10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -13.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | annexin A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,100,706-151,157,815 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX6 |
| Gene groups (HGNC) | Annexins |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P08133](https://www.uniprot.org/uniprotkb/P08133) (Annexin A6):

> May associate with CD21. May regulate the release of Ca(2+) from intracellular stores.

**Summary**, from NCBI Gene [309](https://www.ncbi.nlm.nih.gov/gene/309):

> Annexin VI belongs to a family of calcium-dependent membrane and phospholipid binding proteins. Several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. The annexin VI gene is approximately 60 kbp long and contains 26 exons. It encodes a protein of about 68 kDa that consists of eight 68-amino acid repeats separated by linking sequences of variable lengths. It is highly similar to human annexins I and II sequences, each of …

**Accessions** — [HGNC:544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:544) · Entrez [309](https://www.ncbi.nlm.nih.gov/gene/309) · UniProt [P08133](https://www.uniprot.org/uniprotkb/P08133) · Ensembl [ENSG00000197043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197043)

## Data

Gene col 12327: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12327); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12327, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12327]; `tensor/DDL_lfc|DDL_z.npy` [12327]; `embed/gene_vectors.npy` [12327]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12327 or target_col == 12327). Every well: [[ANXA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
