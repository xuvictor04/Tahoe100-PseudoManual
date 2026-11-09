---
symbol: "IL6R"
type: "gene"
col: 8372
ensembl_id: "ENSG00000160712"
name: "interleukin 6 receptor"
location: "1q21.3"
module: 113
arm: "+"
pooled_cpm: 33.98
n_lines_expressing: 46
n_dd_up: 32
n_dd_down: 9
n_dd_up_clean: 28
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# IL6R

*interleukin 6 receptor* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.65× (z +11.9, q 1e-29, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.469× (z -9.3, q 1e-17, down in 32 of 44 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.481× (z -8.9, q 1e-16, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALOXE3]] (+0.60, fdr 1e-05), [[ADPRHL1]] (+0.59, fdr 1e-05), [[KLF6]] (+0.56, fdr 1e-05); moves opposite to [[AGO1]] (-0.48, fdr 6e-05), [[USP6NL]] (-0.48, fdr 3e-05), [[CYB5B]] (-0.46, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CRYM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.65×** | +11.9 | 1e-29 | 35/42 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +11.4 | 8e-28 | 38/44 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +11.1 | 3e-26 | 37/42 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +10.0 | 2e-21 | 26/42 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.27×** | +10.0 | 2e-21 | 37/44 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +9.4 | 3e-19 | 26/44 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.52×** | +7.2 | 6e-11 | 29/45 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +7.0 | 2e-10 | 34/44 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +6.8 | 7e-10 | 27/43 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.7 | 8e-07 | 27/43 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.62×** | +5.7 | 8e-07 | 25/43 (HT-29, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +5.6 | 8e-07 | 22/44 (HT-29, KATO III, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.60×** | +5.5 | 2e-06 | 25/43 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +5.1 | 1e-05 | 23/44 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +4.8 | 5e-05 | 23/44 (RKO, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 6e-05 | 25/44 (J82, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.06×** | +4.6 | 1e-04 | 25/43 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.469×** | -9.3 | 1e-17 | 32/44 (A-172, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.481×** | -8.9 | 1e-16 | 33/44 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.545×** | -7.4 | 2e-11 | 30/44 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.685×** | -6.6 | 7e-09 | 28/44 (SNU-423, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.647×** | -5.1 | 3e-05 | 20/32 (A549, SK-MEL-2, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.735×** | -3.6 | 0.026 | 18/42 (A-427, NCI-H1792, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.737×** | -3.5 | 0.039 | 16/44 (J82, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.746×** | -3.3 | 0.058 | 13/44 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.769×** | -3.2 | 0.081 | 15/43 (RKO, A549, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.834× | -3.2 | 0.091 | 15/44 (SW 900, Hs 766T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -3.1 | 0.10 | 2/45 (MIA PaCa-2, AsPC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 31.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 26.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 38.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.7× (z +17.8) | — |
| [[A-172 (line)]] | wt | 40.4 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0977× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.118× (z -12.3) |
| [[COLO 205 (line)]] | alt | 39.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.78× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 68.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.8) | — |
| [[KATO III (line)]] | alt | 22.3 | 5 | 0 | [[Auranofin (drug)]] 5 µM 5.84× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 68.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.288× (z -9.6) |
| [[BT-474 (line)]] | alt | 30.9 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 6.48× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 41.8 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.58× (z +12.9) | — |
| [[RKO (line)]] | wt | 45.1 | 1 | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.55× (z +8.9) | [[Selinexor (drug)]] 5 µM 0.293× (z -11.7) |
| [[HOP62 (line)]] | alt | 24.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.80× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 53.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.2) | [[Selinexor (drug)]] 5 µM 0.227× (z -12.6) |
| [[A498 (line)]] | wt | 27.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.51× (z +10.8) | — |
| [[C32 (line)]] | wt | 70.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 36.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +14.4) | — |
| [[LoVo (line)]] | wt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +18.1) | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 12.2× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +10.6) | — |
| [[SW480 (line)]] | alt | 25.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.73× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.59× (z +9.1) | — |
| [[A549 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.318× (z -8.6) |
| [[J82 (line)]] | alt | 40.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.348× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 39.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.467× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.35× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 88.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.441× (z -8.7) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOXE3]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[KLF6]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CEBPB]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 | pathway: Transcriptional regulation of granulopoiesis |
| [[GADD45A]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[FSTL3]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[ABHD5]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[HACD1]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[RHOD]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[CRYM]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[TMBIM1]] | +0.49 | +0.39 / +0.44 | both halves | 6e-05 |  |
| [[PLAGL1]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO1]] | -0.48 | -0.47 / -0.39 | both halves | 6e-05 | pathway: Adherens junctions interactions |
| [[USP6NL]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CYB5B]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[CNPY3]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ECT2]] | -0.44 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SKP2]] | -0.44 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[MZT1]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SNRNP200]] | -0.43 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[FOXK1]] | -0.43 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ATP5F1B]] | -0.42 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[MBOAT1]] | -0.42 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[GVQW3]] | -0.42 | -0.28 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYM]] | B | CRYM activity raises IL6R's level | lines that do not express CRYM (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without CRYM | 0.018 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[LINC02057]] | B | LINC02057 activity raises IL6R's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without LINC02057 | 0.091 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.427). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.9, 13.2); signed map (14.7, 26.9). **Vector** length 126, 37.8% of its response variance represented; |z| ≥ 3 in 1,580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +4.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.5 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.1 | +3.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.6 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.4 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -1.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 6 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,405,193-154,469,450 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD126, IL-6R, IL-1Ra, IL6RA, gp80 |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; Interleukin receptors |
| Reactome | 19 pathways, smallest: MAPK1 (ERK2) activation; MAPK3 (ERK1) activation; Interleukin-6 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P08887](https://www.uniprot.org/uniprotkb/P08887) (Interleukin-6 receptor subunit alpha):

> Part of the receptor for interleukin 6. Binds to IL6 with low affinity, but does not transduce a signal. Signal activation necessitate an association with IL6ST. Activation leads to the regulation of the immune response, acute-phase reactions and hematopoiesis. The interaction with membrane-bound IL6R and IL6ST stimulates 'classic signaling', the restricted expression of the IL6R limits classic IL6 signaling to only a few tissues such as the liver and some cells of the immune system. Whereas …

**Summary**, from NCBI Gene [3570](https://www.ncbi.nlm.nih.gov/gene/3570):

> This gene encodes a subunit of the interleukin 6 (IL6) receptor complex. Interleukin 6 is a potent pleiotropic cytokine that regulates cell growth and differentiation and plays an important role in the immune response. The IL6 receptor is a protein complex consisting of this protein and interleukin 6 signal transducer (IL6ST/GP130/IL6-beta), a receptor subunit also shared by many other cytokines. Dysregulated production of IL6 and this receptor are implicated in the pathogenesis of many …

**Accessions** — [HGNC:6019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6019) · Entrez [3570](https://www.ncbi.nlm.nih.gov/gene/3570) · UniProt [P08887](https://www.uniprot.org/uniprotkb/P08887) · Ensembl [ENSG00000160712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160712)

## Data

Gene col 8372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8372); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8372]; `tensor/DDL_lfc|DDL_z.npy` [8372]; `embed/gene_vectors.npy` [8372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8372 or target_col == 8372). Every well: [[IL6R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL6R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
