---
symbol: "FAM78B"
type: "gene"
col: 12057
ensembl_id: "ENSG00000188859"
name: "family with sequence similarity 78 member B"
location: "1q24.1"
module: 132
arm: "+"
pooled_cpm: 14.71
n_lines_expressing: 35
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 33
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# FAM78B

*family with sequence similarity 78 member B* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.98× (z +11.5, q 5e-28, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.376× (z -16.4, q 0e+00, down in 29 of 32 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.438× (z -9.8, q 2e-20, down in 22 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARNL3]] (+0.56, fdr 3e-05), [[MCF2L2]] (+0.54, fdr 3e-05), [[GNAZ]] (+0.53, fdr 4e-05); moves opposite to [[C5orf34]] (-0.46, fdr 1e-04), [[NUDT16-DT]] (-0.46, fdr 2e-04), [[PRRG2]] (-0.45, fdr 2e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 33 go from it, the strongest it → [[ABCA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.98×** | +11.5 | 5e-28 | 23/32 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +5.9 | 1e-06 | 14/32 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 9e-06 | 16/31 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +4.6 | 5e-04 | 13/32 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +4.6 | 5e-04 | 10/32 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.10 | 9/31 (A-427, KATO III, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | 1.67× | +3.2 | 0.10 | 7/32 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clotrimazole (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.10 | 4/31 (A-427, NCI-H1792, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.31× | +3.0 | 0.16 | 10/31 (A498, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12057.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.376×** | -16.4 | 0e+00 | 29/32 (SK-MEL-2, LOX-IMVI, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.363×** | -12.0 | 8e-31 | 24/32 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.438×** | -9.8 | 2e-20 | 22/32 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.438×** | -9.8 | 2e-20 | 28/31 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -8.9 | 4e-17 | 22/31 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.453×** | -8.8 | 1e-16 | 22/32 (LOX-IMVI, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.509×** | -8.0 | 9e-14 | 22/31 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -7.2 | 4e-11 | 22/31 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.580×** | -6.5 | 7e-09 | 22/32 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -6.2 | 3e-08 | 20/31 (A-427, SNU-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.522×** | -6.0 | 1e-07 | 19/32 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -5.9 | 2e-07 | 22/31 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.590×** | -5.9 | 2e-07 | 18/28 (A-427, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.611×** | -5.8 | 2e-07 | 18/31 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -5.6 | 9e-07 | 19/31 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -4.6 | 1e-04 | 20/31 (SW48, A-427, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.608×** | -3.1 | 0.053 | 12/31 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.760×** | -3.1 | 0.053 | 14/31 (C32, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -3.0 | 0.057 | 0/32 | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.831×** | -2.9 | 0.077 | 6/33 (A498, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 56.1 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0698× (z -28.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0724× (z -29.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0600× (z -22.0) |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -15.7) |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 10 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0664× (z -13.4) |
| [[A-427 (line)]] | wt | 66.6 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0988× (z -20.3) |
| [[C32 (line)]] | wt | 90.3 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0980× (z -16.2) |
| [[LoVo (line)]] | wt | 14.6 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -11.2) |
| [[SW48 (line)]] | wt | 38.1 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0597× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.125× (z -10.1) |
| [[PANC-1 (line)]] | alt | 7.97 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -15.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HS-578T (line)]] | alt | 7.24 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0518× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 8.42 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0757× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 6.28 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.29× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0579× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 26.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.44× (z +10.2) ⚠ unreliable plate only | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0994× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -11.3) |
| [[RKO (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 4.54 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.92× (z +9.6) | — |
| [[A549 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARNL3]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MCF2L2]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[GNAZ]] | +0.53 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[GNAO1]] | +0.53 | +0.53 / +0.40 | both halves | 5e-05 | same gene group |
| [[RASGEF1C]] | +0.52 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[EMSLR]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[BRSK2]] | +0.50 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[OTUD7A]] | +0.50 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[TMOD2]] | +0.49 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[STOX2]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[MICAL3]] | +0.49 | +0.45 / +0.41 | both halves | 4e-05 | same gene group |
| [[CGREF1]] | +0.49 | +0.42 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf34]] | -0.46 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[NUDT16-DT]] | -0.46 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[PRRG2]] | -0.45 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[TCEANC2]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 | same gene group |
| [[DNASE1]] | -0.43 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ACOX1]] | -0.43 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[GLE1]] | -0.43 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[ZNF490]] | -0.43 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[METTL21EP-1]] | -0.42 | -0.42 / -0.26 | both halves | 4e-04 |  |
| [[NDUFS1]] | -0.42 | -0.38 / -0.32 | both halves | 1e-04 |  |
| [[LSM8]] | -0.42 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[IKZF4]] | -0.41 | -0.36 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises FAM78B's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 3.52× lower at baseline in the lines without GNAZ | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises FAM78B's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 3.24× lower at baseline in the lines without ANK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[CNTNAP3B]] | B | CNTNAP3B activity raises FAM78B's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without CNTNAP3B | 0.018 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LDLRAD3]] | B | LDLRAD3 activity raises FAM78B's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 3.13× lower at baseline in the lines without LDLRAD3 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BRSK2]] | B | BRSK2 activity raises FAM78B's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without BRSK2 | 0.043 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises FAM78B's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without MCOLN2 | 0.088 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 33, C 0. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | FAM78B activity raises ABCA3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without FAM78B | 0.005 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[GARNL3]] | B | FAM78B activity raises GARNL3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.03× lower at baseline in the lines without FAM78B | 0.008 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[POLR1B]] | B | FAM78B activity raises POLR1B's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without FAM78B | 0.012 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[LDLRAD3]] | B | FAM78B activity raises LDLRAD3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.10× lower at baseline in the lines without FAM78B | 0.012 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[NARS2]] | B | FAM78B activity raises NARS2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without FAM78B | 0.018 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[XPO6]] | B | FAM78B activity raises XPO6's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without FAM78B | 0.019 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[CNTNAP3B]] | B | FAM78B activity raises CNTNAP3B's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.55× lower at baseline in the lines without FAM78B | 0.019 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[RBFA]] | B | FAM78B activity raises RBFA's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.62× lower at baseline in the lines without FAM78B | 0.021 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[CMSS1]] | B | FAM78B activity raises CMSS1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.57× lower at baseline in the lines without FAM78B | 0.022 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[FXN]] | B | FAM78B activity raises FXN's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without FAM78B | 0.023 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[ATP6V1E2]] | B | FAM78B activity raises ATP6V1E2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without FAM78B | 0.024 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[FMNL2]] | B | FAM78B activity raises FMNL2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without FAM78B | 0.025 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.4, 41.0); signed map (26.9, 30.0). **Vector** length 71.8, 16.3% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +11.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | -0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.3 | -9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | -16.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 78 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:166,057,426-166,167,001 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q5VT40](https://www.uniprot.org/uniprotkb/Q5VT40) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13495) · Entrez [149297](https://www.ncbi.nlm.nih.gov/gene/149297) · UniProt [Q5VT40](https://www.uniprot.org/uniprotkb/Q5VT40) · Ensembl [ENSG00000188859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188859)

## Data

Gene col 12057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12057); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12057]; `tensor/DDL_lfc|DDL_z.npy` [12057]; `embed/gene_vectors.npy` [12057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12057 or target_col == 12057). Every well: [[FAM78B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM78B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
