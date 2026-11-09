---
symbol: "ADAMTS9"
type: "gene"
col: 8743
ensembl_id: "ENSG00000163638"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 9"
location: "3p14.1"
module: 98
arm: "+"
pooled_cpm: 31.89
n_lines_expressing: 32
n_dd_up: 25
n_dd_down: 37
n_dd_up_clean: 24
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# ADAMTS9

*ADAM metallopeptidase with thrombospondin type 1 motif 9* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 1.94× (z +9.6, q 4e-19, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.285× (z -18.2, q 0e+00, down in 29 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST3B1]] (+0.74, fdr 7e-06), [[ITGA10]] (+0.67, fdr 7e-06), [[B3GNT5]] (+0.67, fdr 7e-06); moves opposite to [[SIRLNT]] (-0.54, fdr 2e-05), [[PKD1L1-AS1]] (-0.49, fdr 4e-05), [[CAT]] (-0.46, fdr 4e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HSD11B1]] → it (grade B ⚠); 10 go from it, the strongest it → [[LRIG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.94×** | +9.6 | 4e-19 | 20/29 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.93×** | +9.5 | 6e-19 | 19/29 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.90×** | +9.3 | 2e-18 | 18/29 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.7 | 6e-16 | 19/29 (HOP62, J82, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.80×** | +8.5 | 2e-15 | 19/29 (HOP62, J82, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.80×** | +8.5 | 2e-15 | 20/29 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.78×** | +8.4 | 4e-15 | 19/29 (HOP62, J82, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.73×** | +8.0 | 1e-13 | 22/29 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.81×** | +7.9 | 1e-13 | 17/29 (HOP62, J82, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.69×** | +7.6 | 1e-12 | 19/29 (HOP62, J82, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.69×** | +7.6 | 1e-12 | 19/29 (HOP62, J82, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.71×** | +7.5 | 3e-12 | 14/29 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.59×** | +6.7 | 1e-09 | 19/29 (HOP62, J82, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.58×** | +6.6 | 1e-09 | 19/30 (HOP62, J82, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.56×** | +6.5 | 4e-09 | 16/29 (HOP62, J82, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.285×** | -18.2 | 0e+00 | 29/30 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.303×** | -17.3 | 0e+00 | 28/29 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.434×** | -12.1 | 2e-31 | 22/29 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.592×** | -7.6 | 4e-12 | 24/30 (SNU-423, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -7.1 | 1e-10 | 13/30 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -6.5 | 1e-08 | 17/29 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.4 | 2e-08 | 20/28 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.637×** | -6.3 | 2e-08 | 20/29 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -6.2 | 4e-08 | 20/29 (LOX-IMVI, SHP-77, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.706×** | -6.1 | 5e-08 | 15/30 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.697×** | -5.9 | 2e-07 | 16/30 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.685×** | -5.5 | 2e-06 | 15/29 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.769×** | -5.4 | 3e-06 | 15/30 (C32, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.681×** | -5.2 | 1e-05 | 15/24 (SK-MEL-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.702×** | -4.9 | 3e-05 | 14/22 (HEC-1-A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.755×** | -4.8 | 5e-05 | 14/30 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.770×** | -4.5 | 2e-04 | 18/30 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.735×** | -4.5 | 3e-04 | 13/29 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.723×** | -4.3 | 4e-04 | 12/29 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.817×** | -4.1 | 0.001 | 11/30 (C32, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.3 | 20 (1 ⚠) | 0 | [[Budesonide (drug)]] 0.5 µM 20.0× (z +16.5) | — |
| [[J82 (line)]] | alt | 15.0 | 17 | 0 | [[Triamcinolone (drug)]] 5 µM 5.52× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 27.5 | 8 | 5 (3 ⚠) | [[Budesonide (drug)]] 5 µM 5.54× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.127× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.161× (z -10.7) |
| [[C32 (line)]] | wt | 89.1 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0723× (z -21.7) |
| [[SK-MEL-2 (line)]] | alt | 54.9 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0897× (z -16.2) |
| [[SNU-423 (line)]] | alt | 81.9 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Budesonide (drug)]] 5 µM 4.05× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 233 | 2 (1 ⚠) | 5 (1 ⚠) | [[Peretinoin (drug)]] 5 µM 3.89× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.0452× (z -21.2) |
| [[A-172 (line)]] | wt | 9.82 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.94× (z +9.5) | [[Hydroxyurea (drug)]] 0.05 µM 0.0872× (z -9.8) |
| [[A549 (line)]] | wt | 112 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0769× (z -15.5) |
| [[CHP-212 (line)]] | wt | 193 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0837× (z -10.4) |
| [[SW480 (line)]] | alt | 13.9 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.136× (z -13.6) |
| [[A498 (line)]] | wt | 43.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +19.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 97.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -15.5) |
| [[COLO 205 (line)]] | alt | 68.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0794× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0921× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.306× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.7) |
| [[H4 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0765× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 55.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -8.8) |
| [[RKO (line)]] | wt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0807× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.163× (z -8.5) |
| [[A-427 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST3B1]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ITGA10]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[B3GNT5]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | pathway: O-linked glycosylation |
| [[DNER]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[STXBP5-AS1]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SLC26A2]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[FOXC2]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[FKBP5]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TLR2]] | +0.59 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MOSMO]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PTX3]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[PKD1L1-AS1]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CAT]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ULK1]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[EML1]] | -0.44 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B1]] | B | HSD11B1 activity raises ADAMTS9's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without HSD11B1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[LRIG1]] | B | LRIG1 activity raises ADAMTS9's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 3.52× lower at baseline in the lines without LRIG1 | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises ADAMTS9's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[ANGPTL4]] | B | ANGPTL4 activity lowers ADAMTS9's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 1.32× higher at baseline in the lines without ANGPTL4 | 0.074 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[ABL1]] | B | ABL1 activity raises ADAMTS9's level | compounds that target ABL1: 4 of 6 lower it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRIG1]] | B | ADAMTS9 activity raises LRIG1's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.39× lower at baseline in the lines without ADAMTS9 | 0.021 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[ZC3H12C]] | B | ADAMTS9 activity raises ZC3H12C's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without ADAMTS9 | 0.027 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[ELOVL6]] | B | ADAMTS9 activity raises ELOVL6's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without ADAMTS9 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[HIPK2]] | B | ADAMTS9 activity raises HIPK2's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without ADAMTS9 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[MYO1B]] | B | ADAMTS9 activity raises MYO1B's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.01× lower at baseline in the lines without ADAMTS9 | 0.034 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[MYO1B]] | B | ADAMTS9 activity strengthens MYO1B's drug response | lines that do not express ADAMTS9 (14) vs lines expressing it (28) | the lines without ADAMTS9 respond 0.47× as strongly (z diff +2.60); strongest at Dinaciclib 0.5 µM: 1.10x vs 0.62x (z diff +5.5) | 0.046 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2; target measured in part of the lines; artifact flags |
| [[IL4R]] | B | ADAMTS9 activity strengthens IL4R's drug response | lines that do not express ADAMTS9 (18) vs lines expressing it (27) | the lines without ADAMTS9 respond 0.75× as strongly (z diff +1.26); strongest at Dinaciclib 0.5 µM: 0.44x vs 0.28x (z diff +2.3) | 0.052 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2; target measured in part of the lines; artifact flags |
| [[HS3ST3B1]] | B | ADAMTS9 activity raises HS3ST3B1's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.96× lower at baseline in the lines without ADAMTS9 | 0.056 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[SLC7A2]] | B | ADAMTS9 activity raises SLC7A2's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without ADAMTS9 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[HSD11B1]] | B | ADAMTS9 activity raises HSD11B1's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without ADAMTS9 | 0.074 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 15.1); signed map (17.3, 32.9). **Vector** length 119, 31.5% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +8.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.6 | +9.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.5 | +9.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.4 | +8.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.2 | +6.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -7.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:64,515,654-64,688,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1312 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 8 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2N4](https://www.uniprot.org/uniprotkb/Q9P2N4) (A disintegrin and metalloproteinase with thrombospondin motifs 9):

> Cleaves the large aggregating proteoglycans, aggrecan (at the '1838-Glu-|-Ala-1839' site) and versican (at the '1428-Glu-|-Ala-1429' site). In addition, catalyzes the shedding of the endopeptidase MMP14 (at the '314-Tyr-|-Gly-315' site), releasing the catalytic domain from the cell surface thereby preventing the downstream pro-MMP2 activation. Is involved in extracellular matrix proteolysis and in ciliary vesicle growth during ciliogenesis in metalloendopeptidase activity dependent manner. Has …

**Summary**, from NCBI Gene [56999](https://www.ncbi.nlm.nih.gov/gene/56999):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. Members of the ADAMTS family have been implicated in the cleavage of …

**Accessions** — [HGNC:13202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13202) · Entrez [56999](https://www.ncbi.nlm.nih.gov/gene/56999) · UniProt [Q9P2N4](https://www.uniprot.org/uniprotkb/Q9P2N4) · Ensembl [ENSG00000163638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163638)

## Data

Gene col 8743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8743); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8743]; `tensor/DDL_lfc|DDL_z.npy` [8743]; `embed/gene_vectors.npy` [8743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8743 or target_col == 8743). Every well: [[ADAMTS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
