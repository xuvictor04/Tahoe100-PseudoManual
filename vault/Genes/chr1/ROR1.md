---
symbol: "ROR1"
type: "gene"
col: 11685
ensembl_id: "ENSG00000185483"
name: "ROR family WNT receptor 1"
location: "1p31.3"
module: 174
arm: "+"
pooled_cpm: 72.38
n_lines_expressing: 36
n_dd_up: 14
n_dd_down: 29
n_dd_up_clean: 8
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# ROR1

*ROR family WNT receptor 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 2.13× (z +10.9, q 7e-25, up in 23 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.713× (z -6.9, q 3e-09, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHOD3]] (+0.54, fdr 3e-05), [[NRG2]] (+0.52, fdr 2e-05), [[PRAG1]] (+0.51, fdr 2e-05); moves opposite to [[C11orf52]] (-0.44, fdr 1e-04), [[PRMT2]] (-0.44, fdr 1e-04), [[HOMEZ]] (-0.43, fdr 5e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TBC1D8]] → it (grade B ⚠); 8 go from it, the strongest it → [[FAM3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **2.13×** | +10.9 | 7e-25 | 23/34 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +9.3 | 3e-18 | 18/34 (LoVo, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +9.0 | 3e-17 | 16/34 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +6.2 | 7e-08 | 21/34 (A498, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.51×** | +5.9 | 3e-07 | 17/34 (HOP62, J82, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +5.9 | 3e-07 | 19/34 (HOP62, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.47×** | +5.6 | 2e-06 | 17/34 (HOP62, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +5.5 | 3e-06 | 16/34 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.46×** | +5.2 | 1e-05 | 16/33 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 2e-05 | 16/34 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 7e-05 | 15/34 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 18/34 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.29×** | +3.7 | 0.010 | 11/34 (HOP62, J82, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.069 | 14/34 (NCI-H2347, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.713×** | -6.9 | 3e-09 | 24/34 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -6.7 | 8e-09 | 23/32 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.682×** | -6.4 | 4e-08 | 19/34 (HEC-1-A, SW 900, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -6.0 | 3e-07 | 19/34 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.666×** | -5.8 | 6e-07 | 22/33 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.698×** | -5.6 | 2e-06 | 20/34 (HEC-1-A, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.680×** | -5.6 | 2e-06 | 23/34 (Panc 03.27, SW 900, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.696×** | -5.5 | 3e-06 | 21/34 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.699×** | -5.2 | 2e-05 | 18/33 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.712×** | -4.7 | 1e-04 | 19/33 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.625×** | -4.7 | 1e-04 | 21/33 (HT-29, RPMI-7951, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -4.3 | 8e-04 | 18/32 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -4.2 | 0.001 | 16/34 (RPMI-7951, SW48, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.006 | 15/35 (HEC-1-A, SW 900, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -3.7 | 0.008 | 16/34 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.747×** | -3.7 | 0.008 | 15/33 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.780×** | -3.6 | 0.011 | 12/34 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.756×** | -3.5 | 0.012 | 19/34 (C32, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.027 | 15/33 (HEC-1-A, CHP-212, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 87.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.461× (z -8.9) |
| [[PANC-1 (line)]] | alt | 224 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -17.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 18.7 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 4.81× (z +10.3) | — |
| [[KATO III (line)]] | alt | 135 | 0 | 4 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.374× (z -9.3) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 30.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +25.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.72× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 68.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.76× (z +15.2) ⚠ cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.224× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 174 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 41.3 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 3.36× (z +9.4) | — |
| [[C32 (line)]] | wt | 87.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.228× (z -9.5) |
| [[H4 (line)]] | wt | 18.9 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +11.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 42.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +17.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 63.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 49.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.293× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -9.9) ⚠ cell-cycle shift, explains ~88% of this change |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -10.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 37.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.77 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.00 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHOD3]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[NRG2]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 | same gene group |
| [[PRAG1]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 | same gene group |
| [[SLC20A1]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[MAP3K5]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PSD3]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TBC1D4]] | +0.49 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[RGS17]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[F2R]] | +0.49 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[ETV4]] | +0.48 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[ITGA3]] | +0.48 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[SHB]] | +0.47 | +0.40 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf52]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PRMT2]] | -0.44 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[HOMEZ]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PCGF3]] | -0.42 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[OTUD7B]] | -0.41 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[TRADD]] | -0.40 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[DCP1A]] | -0.39 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[ZNF506]] | -0.39 | -0.34 / -0.32 | both halves | 1e-04 |  |
| [[TEKTIP1]] | -0.38 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[DUSP16]] | -0.37 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[RPAP3-DT]] | -0.37 | -0.32 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | TBC1D8 activity raises ROR1's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.78× lower at baseline in the lines without TBC1D8 | 0.019 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[FHOD3]] | B | FHOD3 activity raises ROR1's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 2.42× lower at baseline in the lines without FHOD3 | 0.067 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM3C]] | B | ROR1 activity raises FAM3C's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.94× lower at baseline in the lines without ROR1 | 0.010 | ⚠ within organs, on part of the lines |
| [[ENDOD1]] | B | ROR1 activity raises ENDOD1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without ROR1 | 0.022 | ⚠ within organs, on part of the lines |
| [[SSH1]] | B | ROR1 activity raises SSH1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without ROR1 | 0.026 | ⚠ within organs, on part of the lines |
| [[HPCAL1]] | B | ROR1 activity raises HPCAL1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without ROR1 | 0.031 | ⚠ within organs, on part of the lines |
| [[GNA12]] | B | ROR1 activity raises GNA12's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.41× lower at baseline in the lines without ROR1 | 0.040 | ⚠ within organs, on part of the lines |
| [[ENDOD1]] | B | ROR1 activity strengthens ENDOD1's drug response | lines that do not express ROR1 (12) vs lines expressing it (34) | the lines without ROR1 respond 0.76× as strongly (z diff +0.86); strongest at Homoharringtonine 0.5 µM: 0.93x vs 0.44x (z diff +4.4) | 0.069 | ⚠ within organs, on part of the lines; target measured in part of the lines; both ways; artifact flags |
| [[ETV1]] | B | ROR1 activity raises ETV1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without ROR1 | 0.081 | ⚠ within organs, on part of the lines |
| [[TRIB2]] | B | ROR1 activity raises TRIB2's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without ROR1 | 0.082 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.8, 4.2); signed map (8.3, 50.2). **Vector** length 97.6, 23.8% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +10.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +9.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -6.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | ROR family WNT receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:63,774,017-64,181,498 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NTRKR1 |
| Gene groups (HGNC) | I-set domain containing; Pseudokinases; Kringle domain containing; ROR family WNT receptors |
| Reactome | 4 pathways, smallest: WNT5A-dependent internalization of FZD2, FZD5 and ROR2; PCP/CE pathway; Beta-catenin independent WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01973](https://www.uniprot.org/uniprotkb/Q01973) (Inactive tyrosine-protein kinase transmembrane receptor ROR1):

> Has very low kinase activity in vitro and is unlikely to function as a tyrosine kinase in vivo. Receptor for ligand WNT5A which activates downstream NFkB signaling pathway and may result in the inhibition of WNT3A-mediated signaling. In the inner ear, crucial for spiral ganglion neurons to innervate auditory hair cells. Via IGFBP5 ligand, forms a complex with ERBB2 to enhance CREB oncogenic signaling.

**Summary**, from NCBI Gene [4919](https://www.ncbi.nlm.nih.gov/gene/4919):

> This gene encodes a receptor tyrosine kinase-like orphan receptor that modulates neurite growth in the central nervous system. The encoded protein is a glycosylated type I membrane protein that belongs to the ROR subfamily of cell surface receptors. It is a pseudokinase that lacks catalytic activity and may interact with the non-canonical Wnt signalling pathway. This gene is highly expressed during early embryonic development but expressed at very low levels in adult tissues. Increased …

**Accessions** — [HGNC:10256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10256) · Entrez [4919](https://www.ncbi.nlm.nih.gov/gene/4919) · UniProt [Q01973](https://www.uniprot.org/uniprotkb/Q01973) · Ensembl [ENSG00000185483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185483)

## Data

Gene col 11685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11685); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11685]; `tensor/DDL_lfc|DDL_z.npy` [11685]; `embed/gene_vectors.npy` [11685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11685 or target_col == 11685). Every well: [[ROR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
