---
symbol: "NAA16"
type: "gene"
col: 10292
ensembl_id: "ENSG00000172766"
name: "N-alpha-acetyltransferase 16, NatA auxiliary subunit"
location: "13q14.11"
module: 146
arm: "+"
pooled_cpm: 49.87
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# NAA16

*N-alpha-acetyltransferase 16, NatA auxiliary subunit* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.31× (z +12.9, q 2e-35, up in 42 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +12.6, q 5e-34, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.632× (z -6.8, q 5e-09, down in 26 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.769× (z -4.1, q 0.007, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDS5B]] (+0.68, fdr 7e-06), [[HSF2]] (+0.68, fdr 7e-06), [[BLMH]] (+0.65, fdr 7e-06); moves opposite to [[ATP6V1D]] (-0.61, fdr 1e-05), [[NOP14-AS1]] (-0.52, fdr 1e-05), [[BLZF1]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NABP1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[EGR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.9 | 2e-35 | 42/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +12.6 | 5e-34 | 40/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +11.9 | 2e-30 | 43/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.16×** | +11.9 | 3e-30 | 44/47 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +11.0 | 5e-26 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +10.0 | 2e-21 | 43/48 (LS 180, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +9.5 | 1e-19 | 41/48 (CFPAC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +9.3 | 1e-18 | 41/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +9.2 | 2e-18 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.2 | 2e-18 | 40/48 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.8 | 1e-16 | 35/48 (RKO, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.89×** | +8.6 | 6e-16 | 35/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +7.5 | 2e-12 | 37/49 (SW480, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +7.4 | 6e-12 | 36/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.86×** | +6.9 | 3e-10 | 38/49 (RKO, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +5.5 | 2e-06 | 32/48 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 1e-04 | 25/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -6.8 | 5e-09 | 26/41 (AN3 CA, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.769×** | -4.1 | 0.007 | 24/48 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.770×** | -4.1 | 0.007 | 17/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.770×** | -4.1 | 0.007 | 27/48 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.045 | 16/49 (NCI-H661, AsPC-1, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **0.799×** | -3.5 | 0.045 | 13/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.807×** | -3.3 | 0.068 | 21/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.809×** | -3.3 | 0.068 | 19/47 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.812×** | -3.2 | 0.074 | 15/49 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.870× | -3.1 | 0.11 | 9/48 (NCI-H661, HOP62, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.821× | -3.1 | 0.11 | 11/48 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.824× | -3.0 | 0.12 | 17/49 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | 0.691× | -3.0 | 0.12 | 15/46 (AsPC-1, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.5 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +16.2) | — |
| [[LS 180 (line)]] | wt | 43.3 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +12.2) | — |
| [[LoVo (line)]] | wt | 36.2 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.60× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 41.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.18× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +10.9) | — |
| [[A498 (line)]] | wt | 46.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.78× (z +10.7) | — |
| [[KATO III (line)]] | alt | 57.6 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.19× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 37.3 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.15× (z +10.3) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.68× (z +9.2) | — |
| [[RKO (line)]] | wt | 70.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.1) | — |
| [[A-172 (line)]] | wt | 28.5 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.34× (z +9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[A-427 (line)]] | wt | 47.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 38.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 120 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 56.9 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 11.0× (z +14.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 2 (2 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0829× (z -10.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 30.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.49× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 39.2 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.97× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 342 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 55.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 35.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.12× (z +10.6) ⚠ toxic | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0708× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 24.7 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.56× (z +8.7) | — |
| [[H4 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.24× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 52.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 49.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.04× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.56× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 82.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.321× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5B]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 | same gene group |
| [[HSF2]] | +0.68 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[BLMH]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 | same gene group |
| [[PCGF6]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.60 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.59 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CIBAR1]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[REPS1]] | +0.57 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FBXO9]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[OSBPL1A]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[BLZF1]] | -0.50 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.49 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[NABP1]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[C6orf62]] | -0.47 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[LINC00910]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[KCTD5]] | -0.46 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SLC9A1]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[UBAP2]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[EGR1]] | -0.46 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[SAP30BP]] | -0.46 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NABP1]] | C | NABP1 activity lowers NAA16's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 2.14× higher at baseline in the lines without NABP1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGR1]] | C | NAA16's natural level strengthens EGR1's drug response | NAA16's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.01; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.2, -8.6); signed map (-29.4, -16.8). **Vector** length 80.2, 22.0% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +0.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | +11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.5 | +2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | +9.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 16, NatA auxiliary subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,311,267-41,377,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22054, MGC40612, PRO2435; previously NARG1L |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; Tetratricopeptide repeat domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6N069](https://www.uniprot.org/uniprotkb/Q6N069) (N-alpha-acetyltransferase 16, NatA auxiliary subunit):

> Auxillary subunit of the N-terminal acetyltransferase A (NatA) complex which displays alpha (N-terminal) acetyltransferase activity.

**Summary**, from NCBI Gene [79612](https://www.ncbi.nlm.nih.gov/gene/79612):

> Enables ribosome binding activity. Involved in protein maturation. Located in cytosol. Part of NatA complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26164) · Entrez [79612](https://www.ncbi.nlm.nih.gov/gene/79612) · UniProt [Q6N069](https://www.uniprot.org/uniprotkb/Q6N069) · Ensembl [ENSG00000172766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172766)

## Data

Gene col 10292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10292); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10292]; `tensor/DDL_lfc|DDL_z.npy` [10292]; `embed/gene_vectors.npy` [10292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10292 or target_col == 10292). Every well: [[NAA16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
