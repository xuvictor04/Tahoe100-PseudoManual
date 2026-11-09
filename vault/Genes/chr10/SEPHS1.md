---
symbol: "SEPHS1"
type: "gene"
col: 1460
ensembl_id: "ENSG00000086475"
name: "selenophosphate synthetase 1"
location: "10p13"
module: 29
arm: "+"
pooled_cpm: 18.17
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SEPHS1

*selenophosphate synthetase 1* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +22.3, q 0e+00, up in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.40× (z +10.3, q 7e-23, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.601× (z -15.8, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.73, fdr 7e-06), [[RNASEH2B]] (+0.66, fdr 1e-05), [[ABCB10]] (+0.65, fdr 7e-06); moves opposite to [[ZKSCAN1]] (-0.60, fdr 7e-06), [[MTHFR]] (-0.60, fdr 2e-05), [[POLD4]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KCTD15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +22.3 | 0e+00 | 36/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +18.2 | 0e+00 | 24/30 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +10.8 | 8e-25 | 23/38 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +10.3 | 7e-23 | 27/48 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.9 | 4e-13 | 24/47 (NCI-H1792, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +7.8 | 4e-13 | 24/42 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +7.8 | 5e-13 | 28/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.8 | 5e-07 | 17/41 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 2e-06 | 18/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.29×** | +5.5 | 2e-06 | 16/48 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +5.5 | 2e-06 | 16/47 (A-427, LoVo, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 10/44 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 6/47 (KATO III, AsPC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.23×** | +4.3 | 6e-04 | 16/45 (A549, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.002 | 8/46 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 4/43 (NCI-H2030, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 7/44 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.20× | +3.8 | 0.004 | 12/47 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.005 | 3/46 (Hs 766T, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.005 | 11/47 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.5 | 0.010 | 7/47 (LS 180, NCI-H460, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.052 | 5/45 (MIA PaCa-2, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.601×** | -15.8 | 0e+00 | 36/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -13.2 | 3e-37 | 34/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.572×** | -12.3 | 3e-32 | 35/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.657×** | -9.2 | 4e-18 | 28/47 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -8.1 | 8e-14 | 25/47 (MIA PaCa-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -6.4 | 2e-08 | 23/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.766×** | -5.9 | 4e-07 | 21/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.763×** | -5.7 | 8e-07 | 19/47 (NCI-H1573, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -5.2 | 1e-05 | 19/47 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.793×** | -5.1 | 2e-05 | 13/47 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.003 | 3/48 (HCT15, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.792×** | -3.7 | 0.012 | 5/48 (H4, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.846× | -3.5 | 0.023 | 8/48 (SHP-77, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.035 | 11/46 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.749×** | -3.3 | 0.037 | 9/48 (C-33 A, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.859× | -3.1 | 0.070 | 10/44 (RKO, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +11.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 33.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -17.9) |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -9.7) |
| [[HOP62 (line)]] | alt | 14.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.4) |
| [[J82 (line)]] | alt | 31.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -14.3) |
| [[A-427 (line)]] | wt | 37.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -9.2) |
| [[A498 (line)]] | wt | 15.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.0) |
| [[H4 (line)]] | wt | 12.7 | 0 | 2 (1 ⚠) | — | [[Vilanterol (drug)]] 0.5 µM 0.0851× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.15× (z +10.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 15.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.4) |
| [[LoVo (line)]] | wt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.8) |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -8.8) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.73 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[RNASEH2B]] | +0.66 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PTGFRN]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RAB11FIP2]] | +0.65 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NAE1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PDCL3]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CIPC]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TOR3A]] | +0.61 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[NNT]] | +0.61 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[CMTM4]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN1]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[MTHFR]] | -0.60 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[POLD4]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NBEAL1]] | -0.56 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[MIDN]] | -0.56 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[INAFM1]] | -0.56 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[H3-3B]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[RIOK3]] | -0.55 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[IER5]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[TUT7]] | -0.54 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[CLIP2]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[BTG1]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD15]] | B | KCTD15 activity raises SEPHS1's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without KCTD15 | 0.008 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[ADCY3]] | B | ADCY3 activity raises SEPHS1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.25× lower at baseline in the lines without ADCY3 | 0.082 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.4, -27.7); signed map (-13.3, -41.5). **Vector** length 88.2, 17.9% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +10.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +18.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +22.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -15.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | selenophosphate synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,317,428-13,348,298 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPS, SPS1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P49903](https://www.uniprot.org/uniprotkb/P49903) (Zincore component SEPHS1):

> Core component of the zincore complex, a heterotetramer that acts as a molecular 'grip' to stabilize transcription factors at DNA-binding sites across the genome, thereby controlling gene expression. The zincore complex binds specifically to zinc finger transcription factors, such as ZFP91, ZNF652, ZNF526 and PRDM15, and stabilizes them onto their cognate DNA motif. Within the complex, SEPHS1, recognizes and binds the backbone of zinc fingers of transcription factors in a sequence-independent …

**Summary**, from NCBI Gene [22929](https://www.ncbi.nlm.nih.gov/gene/22929):

> This gene encodes an enzyme that synthesizes selenophosphate from selenide and ATP. Selenophosphate is the selenium donor used to synthesize selenocysteine, which is co-translationally incorporated into selenoproteins at in-frame UGA codons. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:19685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19685) · Entrez [22929](https://www.ncbi.nlm.nih.gov/gene/22929) · UniProt [P49903](https://www.uniprot.org/uniprotkb/P49903) · Ensembl [ENSG00000086475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086475)

## Data

Gene col 1460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1460); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1460]; `tensor/DDL_lfc|DDL_z.npy` [1460]; `embed/gene_vectors.npy` [1460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1460 or target_col == 1460). Every well: [[SEPHS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPHS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
