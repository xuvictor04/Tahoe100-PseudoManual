---
symbol: "GP6-AS1"
type: "gene"
col: 15537
ensembl_id: "ENSG00000267265"
name: "GP6 antisense RNA 1"
location: "19q13.42"
module: 212
arm: "+"
pooled_cpm: 91.96
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 32
n_dd_up_clean: 11
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# GP6-AS1

*GP6 antisense RNA 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.28× (z +10.3, q 6e-22, up in 31 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.298× (z -14.4, q 4e-44, down in 29 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.559× (z -7.2, q 1e-10, down in 24 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAI3]] (+0.74, fdr 8e-06), [[ATG101]] (+0.73, fdr 7e-06), [[SEC22B]] (+0.70, fdr 7e-06); moves opposite to [[RNF146]] (-0.68, fdr 1e-05), [[ZMYND11]] (-0.63, fdr 1e-05), [[HNRNPH3]] (-0.62, fdr 1e-05).
> It is in [[Module 212]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[SYCE1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +10.3 | 6e-22 | 31/35 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +9.3 | 3e-18 | 30/35 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +8.7 | 6e-16 | 27/35 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.6 | 7e-09 | 22/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.3 | 1e-05 | 21/35 (SNU-1, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +4.9 | 7e-05 | 24/36 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 7e-05 | 25/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +3.6 | 0.019 | 16/35 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.022 | 19/35 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +3.5 | 0.023 | 13/35 (HEC-1-A, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.026 | 18/35 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.64×** | +3.2 | 0.058 | 16/35 (SNU-1, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +3.1 | 0.089 | 15/35 (A-172, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.298×** | -14.4 | 4e-44 | 29/32 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.340×** | -13.3 | 4e-38 | 28/35 (hTERT-HPNE, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -7.2 | 1e-10 | 24/35 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.542×** | -7.0 | 4e-10 | 28/33 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.557×** | -6.9 | 4e-10 | 25/35 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -6.9 | 6e-10 | 27/36 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -6.5 | 8e-09 | 23/35 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.607×** | -6.2 | 5e-08 | 30/35 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -6.1 | 5e-08 | 27/35 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.605×** | -6.0 | 1e-07 | 26/35 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.619×** | -5.9 | 2e-07 | 24/36 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -5.6 | 1e-06 | 22/34 (NCI-H1792, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.616×** | -5.5 | 1e-06 | 24/35 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.654×** | -5.0 | 2e-05 | 27/34 (NCI-H1573, SHP-77, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.656×** | -5.0 | 2e-05 | 23/35 (NCI-H1792, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.768×** | -4.4 | 3e-04 | 23/35 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.746×** | -4.2 | 7e-04 | 22/35 (NCI-H1573, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.709×** | -4.2 | 7e-04 | 19/34 (A549, NCI-H1573, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -4.2 | 7e-04 | 22/37 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 139 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.73× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -10.5) |
| [[A498 (line)]] | wt | 197 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0907× (z -18.3) |
| [[C-33 A (line)]] | alt | 152 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -14.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 65.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 82.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 222 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.166× (z -12.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.216× (z -10.6) |
| [[SNU-1 (line)]] | wt | 216 | 2 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.55× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 151 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -8.5) |
| [[H4 (line)]] | wt | 792 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.254× (z -8.9) |
| [[HS-578T (line)]] | alt | 27.4 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.81× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -9.1) |
| [[J82 (line)]] | alt | 72.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.253× (z -9.7) |
| [[KATO III (line)]] | alt | 227 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0943× (z -17.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 25.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.39× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -18.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0686× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 214 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 235 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -15.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0443× (z -21.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 71.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.280× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 22.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 304 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI3]] | +0.74 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[ATG101]] | +0.73 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ARF4]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.69 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[INTS4]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ATAT1]] | +0.67 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[TMEM41B]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SDF2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.66 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[HM13]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ZNF841]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | -0.68 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.63 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPH3]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[USP24]] | -0.62 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[IQCH-AS1]] | -0.61 | -0.61 / -0.34 | both halves | 1e-04 | same gene group |
| [[JADE2]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[USP13]] | -0.60 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[DCUN1D1]] | -0.59 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[DNAI4]] | -0.59 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[ARID1B]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[HDGF]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GALNT7-DT]] | -0.58 | -0.59 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GP6-AS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCE1L]] | B | GP6-AS1 activity raises SYCE1L's level | lines that do not express GP6-AS1 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without GP6-AS1 | 0.080 | ⚠ within organs, on part of the lines |
| [[NME7]] | B | GP6-AS1 activity raises NME7's level | lines that do not express GP6-AS1 (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without GP6-AS1 | 0.092 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.6, -25.3); signed map (-43.4, 9.5). **Vector** length 128, 41.0% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.8 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.4 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -6.0 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.2 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.8 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | GP6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.42 — chr19:55,006,193-55,048,086 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55305) · Entrez [107985325](https://www.ncbi.nlm.nih.gov/gene/107985325) · Ensembl [ENSG00000267265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267265)

## Data

Gene col 15537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15537); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15537]; `tensor/DDL_lfc|DDL_z.npy` [15537]; `embed/gene_vectors.npy` [15537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15537 or target_col == 15537). Every well: [[GP6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GP6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
