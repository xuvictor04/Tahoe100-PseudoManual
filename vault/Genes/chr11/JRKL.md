---
symbol: "JRKL"
type: "gene"
col: 11395
ensembl_id: "ENSG00000183340"
name: "JRK like"
location: "11q21"
module: 16
arm: "+"
pooled_cpm: 15.24
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# JRKL

*JRK like* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +20.4, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.300× (z -17.8, q 0e+00, down in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.304× (z -17.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXSM]] (+0.64, fdr 1e-05), [[WASL-DT]] (+0.53, fdr 5e-05), [[MOCS3]] (+0.52, fdr 1e-04); moves opposite to [[DNA2]] (-0.43, fdr 7e-05), [[GUSBP11]] (-0.43, fdr 3e-04), [[CTDSPL]] (-0.41, fdr 1e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PGAP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +20.4 | 0e+00 | 41/46 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +8.3 | 4e-14 | 34/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.65×** | +7.5 | 2e-11 | 31/48 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +7.0 | 3e-10 | 30/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +6.7 | 2e-09 | 28/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.5 | 6e-09 | 29/48 (A-172, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.0 | 1e-07 | 26/48 (HOP62, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.9 | 7e-05 | 19/45 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 3e-04 | 15/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 20/47 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 21/47 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.007 | 16/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.007 | 4/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.007 | 14/46 (KATO III, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.013 | 14/47 (NCI-H1792, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.300×** | -17.8 | 0e+00 | 41/46 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.304×** | -17.6 | 0e+00 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.526×** | -13.4 | 7e-39 | 39/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.417×** | -12.9 | 4e-36 | 39/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.458×** | -11.5 | 1e-28 | 42/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -7.4 | 1e-11 | 31/48 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -6.4 | 1e-08 | 23/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -6.1 | 6e-08 | 25/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.651×** | -6.1 | 8e-08 | 26/47 (COLO 205, PANC-1, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.740×** | -4.4 | 5e-04 | 20/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -3.8 | 0.006 | 19/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.633×** | -3.5 | 0.020 | 10/36 (KATO III, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.853× | -3.3 | 0.043 | 4/48 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.085 | 4/48 (SW 1088, LS 180, …) | rises with dose | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -14.1) |
| [[PANC-1 (line)]] | alt | 18.2 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.2) |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.8) |
| [[KATO III (line)]] | alt | 44.1 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.257× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.5) |
| [[LoVo (line)]] | wt | 13.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -13.8) |
| [[A-427 (line)]] | wt | 11.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -9.6) |
| [[HOP62 (line)]] | alt | 12.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.0675× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -10.5) |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -11.7) |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -11.3) |
| [[SW480 (line)]] | alt | 18.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -11.2) |
| [[C32 (line)]] | wt | 5.88 | 0 | 2 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0657× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 12.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -11.7) |
| [[RKO (line)]] | wt | 9.37 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.8) | [[Pimozide (drug)]] 0.5 µM 0.112× (z -9.8) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.1) |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0881× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.3) |
| [[SW 900 (line)]] | alt | 15.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 26.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.146× (z -14.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +13.1) | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -10.1) |
| [[HS-578T (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.1) | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 7.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0263× (z -20.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXSM]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[WASL-DT]] | +0.53 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[MOCS3]] | +0.52 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[RRAGA]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FANCF]] | +0.51 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[C6orf120]] | +0.50 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[ZEB1-AS1]] | +0.50 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[TMEM186]] | +0.50 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[GTF2E1]] | +0.50 | +0.57 / +0.32 | both halves | 1e-04 |  |
| [[METTL13]] | +0.49 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ZNF526]] | +0.49 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[TIMM8B]] | +0.48 | +0.57 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNA2]] | -0.43 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[GUSBP11]] | -0.43 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[CTDSPL]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[POLE2]] | -0.41 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[MAN2B1]] | -0.40 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[LRCH4]] | -0.40 | -0.22 / -0.30 | both halves | 6e-04 |  |
| [[DUS1L]] | -0.39 | -0.26 / -0.28 | both halves | 4e-04 |  |
| [[STAG3L5P-1]] | -0.39 | -0.38 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity raises JRKL's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without PGAP4 | 0.084 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.211). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.7, 15.6); signed map (-2.8, -29.1). **Vector** length 71.1, 13.4% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +20.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -13.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -17.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -17.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -11.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -12.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | JRK like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:96,389,989-96,507,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HHMJG |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

UniProt [Q9Y4A0](https://www.uniprot.org/uniprotkb/Q9Y4A0) carries no function annotation.

**Summary**, from NCBI Gene [8690](https://www.ncbi.nlm.nih.gov/gene/8690):

> The function of this gene has not yet been defined, however, the encoded protein shares similarity with the human (41% identical) and mouse (34% identical) jerky gene products. This protein may act as a nuclear regulatory protein. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:6200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6200) · Entrez [8690](https://www.ncbi.nlm.nih.gov/gene/8690) · UniProt [Q9Y4A0](https://www.uniprot.org/uniprotkb/Q9Y4A0) · Ensembl [ENSG00000183340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183340)

## Data

Gene col 11395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11395); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11395]; `tensor/DDL_lfc|DDL_z.npy` [11395]; `embed/gene_vectors.npy` [11395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11395 or target_col == 11395). Every well: [[JRKL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JRKL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
