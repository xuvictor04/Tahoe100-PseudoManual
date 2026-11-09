---
symbol: "CACNB3"
type: "gene"
col: 9482
ensembl_id: "ENSG00000167535"
name: "calcium voltage-gated channel auxiliary subunit beta 3"
location: "12q13.12"
module: 2
arm: "+"
pooled_cpm: 9.25
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CACNB3

*calcium voltage-gated channel auxiliary subunit beta 3* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +8.1, q 3e-13, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -17.7, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLGL1]] (+0.65, fdr 1e-05), [[PCGF2]] (+0.62, fdr 1e-05), [[TESK1]] (+0.59, fdr 1e-05); moves opposite to [[CRADD]] (-0.57, fdr 3e-05), [[CAAP1]] (-0.55, fdr 1e-05), [[JPX]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.1 | 3e-13 | 23/45 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.1 | 3e-07 | 19/32 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.7 | 2e-06 | 23/44 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.5 | 5e-06 | 17/42 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 0.001 | 6/18 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.002 | 13/48 (A549, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.029 | 12/43 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.3 | 0.059 | 12/38 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.078 | 7/44 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | 1.58× | +3.1 | 0.10 | 5/38 (LoVo, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.10 | 12/43 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.13 | 5/47 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.381×** | -17.7 | 0e+00 | 38/44 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.287×** | -16.1 | 0e+00 | 36/44 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.331×** | -14.3 | 4e-44 | 42/47 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -13.8 | 3e-41 | 40/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -11.7 | 8e-30 | 34/42 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.437×** | -10.7 | 9e-25 | 36/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -8.3 | 1e-14 | 31/46 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -7.0 | 2e-10 | 28/47 (LOX-IMVI, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.586×** | -6.9 | 3e-10 | 31/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.605×** | -6.5 | 4e-09 | 25/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.607×** | -6.4 | 6e-09 | 25/46 (SK-MEL-2, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.632×** | -5.9 | 1e-07 | 25/47 (NCI-H460, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.435×** | -5.6 | 8e-07 | 22/43 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.663×** | -5.3 | 4e-06 | 20/47 (HS-578T, HEC-1-A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -4.9 | 3e-05 | 21/47 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -4.2 | 8e-04 | 14/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.722×** | -4.0 | 0.002 | 16/44 (H4, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -16.9) |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0836× (z -11.3) |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0820× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 5.42 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0324× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0797× (z -22.5) |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0447× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -11.1) |
| [[A549 (line)]] | wt | 9.37 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.6) |
| [[HOP62 (line)]] | alt | 7.26 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.9) |
| [[HS-578T (line)]] | alt | 9.81 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -10.5) |
| [[LS 180 (line)]] | wt | 6.81 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0292× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 8.74 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0700× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 5.64 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 6.72 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -12.2) |
| [[PANC-1 (line)]] | alt | 6.94 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.1) |
| [[RKO (line)]] | wt | 9.30 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -9.2) |
| [[SW480 (line)]] | alt | 10.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.193× (z -10.7) |
| [[A-427 (line)]] | wt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -9.0) |
| [[A498 (line)]] | wt | 8.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -13.8) |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0970× (z -10.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 5.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0449× (z -11.3) |
| [[COLO 205 (line)]] | alt | 8.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0982× (z -9.0) |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0763× (z -8.7) |
| [[Hs 766T (line)]] | wt | 5.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0507× (z -11.8) |
| [[J82 (line)]] | alt | 8.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -12.6) |
| [[KATO III (line)]] | alt | 10.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0767× (z -12.8) |
| [[LoVo (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 9.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.97 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0807× (z -10.6) |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLGL1]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PCGF2]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TESK1]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GPR161]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CDS2]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[GIT1]] | +0.55 | +0.58 / +0.60 | both halves | 8e-06 | pathway: Neuronal System |
| [[NOL4L]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CDIPT]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[UBTD1]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[KIAA1191]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TMEM8B]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[KIFC2]] | +0.53 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRADD]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CAAP1]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[JPX]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PIGL]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TAS2R14]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PRH1]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[RGS5]] | -0.45 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[OPA3]] | -0.45 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[THOC2]] | -0.44 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[NCOA5]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ELP4]] | -0.44 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[INTS7]] | -0.44 | -0.31 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises CACNB3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.31× lower at baseline in the lines without MSI1 | 0.083 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[MID2]] | B | MID2 activity raises CACNB3's level | lines that do not express MID2 (17) vs lines expressing it (33) | 1.23× lower at baseline in the lines without MID2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF711, FRMPD3, RPS6KA6 |
| [[TP53I13]] | C | TP53I13 activity lowers CACNB3's level | lines that do not express TP53I13 (4) vs lines expressing it (46) | 1.40× higher at baseline in the lines without TP53I13 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC25A37; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.2, -20.2); signed map (-49.1, -11.3). **Vector** length 60.3, 9.53% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +5.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -17.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -10.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -13.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -14.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit beta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:48,813,794-48,828,941 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CACNLB3 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; Calcium voltage-gated channel auxiliary beta subunits; SH3 domain containing |
| Reactome | 13 pathways, smallest: Presynaptic depolarization and calcium channel opening; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; Adrenaline,noradrenaline inhibits insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P54284](https://www.uniprot.org/uniprotkb/P54284) (Voltage-dependent L-type calcium channel subunit beta-3):

> Regulatory subunit of the voltage-gated calcium channel that gives rise to L-type calcium currents. Increases CACNA1B peak calcium current and shifts the voltage dependencies of channel activation and inactivation (By similarity). Increases CACNA1C peak calcium current and shifts the voltage dependencies of channel activation and inactivation (By similarity).

**Summary**, from NCBI Gene [784](https://www.ncbi.nlm.nih.gov/gene/784):

> This gene encodes a regulatory beta subunit of the voltage-dependent calcium channel. Beta subunits are composed of five domains, which contribute to the regulation of surface expression and gating of calcium channels and may also play a role in the regulation of transcription factors and calcium transport. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:1403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1403) · Entrez [784](https://www.ncbi.nlm.nih.gov/gene/784) · UniProt [P54284](https://www.uniprot.org/uniprotkb/P54284) · Ensembl [ENSG00000167535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167535)

## Data

Gene col 9482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9482); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9482]; `tensor/DDL_lfc|DDL_z.npy` [9482]; `embed/gene_vectors.npy` [9482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9482 or target_col == 9482). Every well: [[CACNB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
