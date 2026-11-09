---
symbol: "SLC16A7"
type: "gene"
col: 4006
ensembl_id: "ENSG00000118596"
name: "solute carrier family 16 member 7"
location: "12q14.1"
module: 167
arm: "+"
pooled_cpm: 20.61
n_lines_expressing: 27
n_dd_up: 43
n_dd_down: 24
n_dd_up_clean: 40
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# SLC16A7

*solute carrier family 16 member 7* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.20× (z +10.1, q 2e-21, up in 10 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.83× (z +8.1, q 7e-14, up in 15 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.539× (z -8.3, q 5e-14, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALT1]] (+0.65, fdr 7e-06), [[SLC39A8]] (+0.65, fdr 1e-05), [[DPYD]] (+0.63, fdr 1e-05); moves opposite to [[TMEM158]] (-0.51, fdr 1e-04), [[HBEGF]] (-0.51, fdr 2e-05), [[MYH16]] (-0.47, fdr 3e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RHOBTB3]] → it (grade B ⚠); 3 go from it, the strongest it → [[BCL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +10.1 | 2e-21 | 10/16 (H4, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +9.9 | 1e-20 | 8/18 (NCI-H2030, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +9.5 | 3e-19 | 6/17 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.83×** | +8.1 | 7e-14 | 15/24 (CFPAC-1, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +7.6 | 3e-12 | 12/25 (NCI-H2347, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +5.9 | 3e-07 | 12/24 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.54×** | +5.7 | 9e-07 | 17/25 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +5.6 | 2e-06 | 17/24 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +5.4 | 5e-06 | 14/25 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.45×** | +5.0 | 3e-05 | 12/24 (CFPAC-1, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 6e-05 | 15/25 (NCI-H460, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +4.8 | 7e-05 | 15/25 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 7e-05 | 16/24 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 7e-05 | 13/24 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 1e-04 | 10/24 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.27×** | +4.5 | 2e-04 | 11/25 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 4e-04 | 12/24 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 7e-04 | 12/24 (CFPAC-1, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4006.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.539×** | -8.3 | 5e-14 | 19/24 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.699×** | -6.8 | 3e-09 | 17/24 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -6.6 | 7e-09 | 13/24 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.610×** | -6.4 | 2e-08 | 15/24 (NCI-H460, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -5.7 | 2e-06 | 16/24 (J82, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -5.3 | 1e-05 | 15/24 (HT-29, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.693×** | -4.9 | 6e-05 | 18/24 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.696×** | -4.9 | 7e-05 | 11/24 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.698×** | -4.6 | 3e-04 | 17/25 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.714×** | -4.5 | 3e-04 | 10/24 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -4.3 | 1e-03 | 12/22 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.729×** | -4.3 | 1e-03 | 13/24 (CFPAC-1, SW 900, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.737×** | -4.1 | 0.002 | 15/24 (SNU-423, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.740×** | -4.1 | 0.002 | 14/23 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.809×** | -4.1 | 0.002 | 12/25 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.012 | 10/25 (CFPAC-1, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.016 | 11/25 (SW 900, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.017 | 7/25 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.787×** | -3.1 | 0.043 | 5/25 (A498, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.0 | 3 | 4 (3 ⚠) | [[Binimetinib (drug)]] 5 µM 3.00× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.329× (z -8.8) |
| [[A498 (line)]] | wt | 81.4 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.347× (z -9.6) |
| [[SHP-77 (line)]] | alt | 91.8 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -14.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HT-29 (line)]] | alt | 34.7 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.192× (z -10.6) |
| [[J82 (line)]] | alt | 74.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.356× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 64.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -9.6) ⚠ cell-cycle shift, explains ~22% of this change |
| [[RPMI-7951 (line)]] | alt | 44.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SNU-423 (line)]] | alt | 29.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.186× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 7.13 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.102× (z -8.6) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT1]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SLC39A8]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[DPYD]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[CP]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[IRAK3]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[STOM]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[BICC1]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 | **novel candidate** |
| [[NNMT]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FGA]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CD38]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[HOPX]] | +0.55 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[DCN]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | -0.51 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[HBEGF]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MYH16]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PRDM8]] | -0.47 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[PLAUR]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[TCP10L]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CSF2]] | -0.46 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[PLEKHG5]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[C11orf68]] | -0.43 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[EHD1]] | -0.42 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SLC7A11-AS1]] | -0.42 | -0.47 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOBTB3]] | B | RHOBTB3 activity raises SLC16A7's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 3.53× lower at baseline in the lines without RHOBTB3 | 0.052 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises SLC16A7's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PRDM8]] | B | PRDM8 activity raises SLC16A7's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.85× lower at baseline in the lines without PRDM8 | 0.078 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[PLEKHG5]] | B | PLEKHG5 activity lowers SLC16A7's level | lines that do not express PLEKHG5 (5) vs lines expressing it (45) | 2.58× higher at baseline in the lines without PLEKHG5 | 0.099 | ⚠ within organs, on part of the lines; also absent: TNFRSF25, SLC22A20P, ENSG00000287264; maybe low, not absent |
| [[NNMT]] | C | NNMT activity raises SLC16A7's level | lines that do not express NNMT (24) vs lines expressing it (26) | 3.63× lower at baseline in the lines without NNMT | 0.020 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[PDGFRL]] | C | PDGFRL activity raises SLC16A7's level | lines that do not express PDGFRL (16) vs lines expressing it (34) | 3.41× lower at baseline in the lines without PDGFRL | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC16A7, ITPR1, TOX2; co-absent with the target |
| [[MAP2]] | C | MAP2 activity raises SLC16A7's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 3.80× lower at baseline in the lines without MAP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent; co-absent with the target |
| [[CSF2]] | C | CSF2 activity raises SLC16A7's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 3.86× lower at baseline in the lines without CSF2 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2; co-absent with the target |
| [[CFH]] | C | CFH activity raises SLC16A7's level | lines that do not express CFH (28) vs lines expressing it (22) | 3.15× lower at baseline in the lines without CFH | 0.072 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises SLC16A7's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without BICC1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL6]] | B | SLC16A7 activity raises BCL6's level | lines that do not express SLC16A7 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without SLC16A7 | 0.069 | ⚠ within organs, on part of the lines; also absent: NDNF, EDIL3-DT, ZNF229 |
| [[CFH]] | C | SLC16A7 activity raises CFH's level | lines that do not express SLC16A7 (23) vs lines expressing it (27) | 3.41× lower at baseline in the lines without SLC16A7 | 0.034 | ⚠ within organs, on part of the lines; also absent: NDNF, EDIL3-DT, ZNF229; co-absent with the target |
| [[NNMT]] | C | SLC16A7 activity raises NNMT's level | lines that do not express SLC16A7 (23) vs lines expressing it (27) | 4.00× lower at baseline in the lines without SLC16A7 | 0.073 | ⚠ within organs, on part of the lines; also absent: NDNF, EDIL3-DT, ZNF229; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.1, 19.2); signed map (49.9, 26.2). **Vector** length 89.7, 27.2% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +8.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +5.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 16 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:59,596,029-59,789,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCT2 |
| Gene groups (HGNC) | Solute carrier family 16 |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Proton-coupled monocarboxylate transport; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O60669](https://www.uniprot.org/uniprotkb/O60669) (Monocarboxylate transporter 2):

> Proton-coupled monocarboxylate symporter. Catalyzes the rapid transport across the plasma membrane of monocarboxylates such as L-lactate, pyruvate and ketone bodies, acetoacetate, beta-hydroxybutyrate and acetate. Dimerization is functionally required and both subunits work cooperatively in transporting substrate.

**Summary**, from NCBI Gene [9194](https://www.ncbi.nlm.nih.gov/gene/9194):

> This gene is a member of the monocarboxylate transporter family. Members in this family transport metabolites, such as lactate, pyruvate, and ketone bodies. The protein encoded by this gene catalyzes the proton-linked transport of monocarboxylates and has the highest affinity for pyruvate. This protein has been reported to be more highly expressed in prostate and colorectal cancer specimens when compared to control specimens. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:10928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10928) · Entrez [9194](https://www.ncbi.nlm.nih.gov/gene/9194) · UniProt [O60669](https://www.uniprot.org/uniprotkb/O60669) · Ensembl [ENSG00000118596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118596)

## Data

Gene col 4006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4006); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4006]; `tensor/DDL_lfc|DDL_z.npy` [4006]; `embed/gene_vectors.npy` [4006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4006 or target_col == 4006). Every well: [[SLC16A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC16A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
