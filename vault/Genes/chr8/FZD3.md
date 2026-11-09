---
symbol: "FZD3"
type: "gene"
col: 2434
ensembl_id: "ENSG00000104290"
name: "frizzled class receptor 3"
location: "8p21.1"
module: 186
arm: "+"
pooled_cpm: 21.18
n_lines_expressing: 41
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# FZD3

*frizzled class receptor 3* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +7.8, q 3e-12, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.424× (z -26.2, q 0e+00, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VGLL4]] (+0.60, fdr 1e-05), [[TLCD4]] (+0.57, fdr 1e-05), [[BIVM]] (+0.55, fdr 3e-05); moves opposite to [[MIR4435-2HG]] (-0.52, fdr 4e-05), [[SETX]] (-0.52, fdr 2e-05), [[SLC35C2]] (-0.51, fdr 3e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[TMED8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.8 | 3e-12 | 21/38 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 6e-10 | 18/37 (NCI-H2347, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.5 | 2e-08 | 20/37 (H4, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +6.2 | 7e-08 | 18/39 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.2 | 7e-08 | 13/28 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +6.1 | 7e-08 | 17/38 (LoVo, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.7 | 8e-07 | 17/39 (HEC-1-A, NCI-H2347, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +5.5 | 3e-06 | 16/38 (NCI-H23, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.4 | 7e-04 | 13/37 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.15× | +4.3 | 1e-03 | 7/39 (NCI-H460, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.005 | 11/39 (RPMI-7951, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 9/39 (KATO III, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.006 | 5/39 (LoVo, SW480, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.8 | 0.006 | 14/38 (LS 180, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.006 | 5/39 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.017 | 6/39 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Vandetanib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.023 | 4/38 (NCI-H1573, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.424×** | -26.2 | 0e+00 | 32/38 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -15.1 | 0e+00 | 32/37 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.506×** | -14.2 | 2e-43 | 28/39 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.517×** | -13.7 | 1e-40 | 26/37 (NCI-H23, HCT15, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -13.5 | 1e-39 | 33/39 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -13.1 | 3e-37 | 25/37 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -13.0 | 2e-36 | 28/37 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -11.6 | 2e-29 | 30/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.375×** | -11.1 | 8e-27 | 29/36 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -9.8 | 4e-21 | 30/37 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.684×** | -8.2 | 1e-14 | 27/38 (AN3 CA, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -7.2 | 2e-11 | 21/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -7.2 | 4e-11 | 19/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.732×** | -6.4 | 8e-09 | 20/38 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.747×** | -6.3 | 1e-08 | 19/37 (NCI-H23, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.762×** | -5.9 | 2e-07 | 19/38 (LS 180, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clotrimazole (drug)]] 5 µM |  | 0.869× | -4.3 | 5e-04 | 10/39 (SW480, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.5 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0676× (z -38.1) |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 26.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.8) |
| [[SNU-1 (line)]] | wt | 40.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -11.1) |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -11.0) |
| [[A-172 (line)]] | wt | 19.0 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.8) |
| [[H4 (line)]] | wt | 29.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.8) |
| [[LoVo (line)]] | wt | 44.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -13.4) |
| [[A549 (line)]] | wt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -9.5) |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0846× (z -10.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.100× (z -9.3) |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.0) |
| [[HCT15 (line)]] | alt | 43.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -11.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.9) |
| [[HOP62 (line)]] | alt | 12.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.8) |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -23.2) |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -17.0) |
| [[SW480 (line)]] | alt | 32.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.433× (z -9.4) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -17.5) |
| [[C32 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.1) |
| [[RKO (line)]] | wt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -16.7) |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.368× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.3) |
| [[A498 (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VGLL4]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TLCD4]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[BIVM]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SNX27]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[BMPR1A]] | +0.55 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[SMAD5]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[DDHD2]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TMEM64]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[CIAO2A]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[SLC25A30]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PDK1]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CHPT1]] | +0.52 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4435-2HG]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[SETX]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SLC35C2]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[CHMP1A]] | -0.49 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ANAPC1P4]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF674]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[ZNF274]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ENDOV]] | -0.47 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[PSORS1C1]] | -0.46 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[KATNIP]] | -0.46 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TUT7]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PMEPA1]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMED8]] | B | FZD3 activity raises TMED8's level | lines that do not express FZD3 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without FZD3 | 0.060 | ⚠ within organs, on part of the lines; also absent: FBXO16, SLC16A10, LINC02456; maybe low, not absent; its own permutation p |
| [[FAM234B]] | B | FZD3 activity raises FAM234B's level | lines that do not express FZD3 (9) vs lines expressing it (41) | 2.01× lower at baseline in the lines without FZD3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FBXO16, SLC16A10, LINC02456; maybe low, not absent; its own permutation p |
| [[GCDH]] | B | FZD3 activity raises GCDH's level | lines that do not express FZD3 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without FZD3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FBXO16, SLC16A10, LINC02456; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, -3.0); signed map (-20.8, -27.3). **Vector** length 74.1, 14.3% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +6.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -26.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -11.1 |

## What is on record

|  |  |
|---|---|
| Name | frizzled class receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:28,494,205-28,574,267 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Fz-3 |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled |
| Reactome | 8 pathways, smallest: Class B/2 (Secretin family receptors); Ca2+ pathway; Asymmetric localization of PCP proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPG1](https://www.uniprot.org/uniprotkb/Q9NPG1) (Frizzled-3):

> Receptor for Wnt proteins. Most of frizzled receptors are coupled to the beta-catenin canonical signaling pathway, which leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin and activation of Wnt target genes. A second signaling pathway involving PKC and calcium fluxes has been seen for some family members, but it is not yet clear if it represents a distinct pathway or if it can be integrated in the canonical pathway, as PKC seems to …

**Summary**, from NCBI Gene [7976](https://www.ncbi.nlm.nih.gov/gene/7976):

> This gene is a member of the frizzled gene family. Members of this family encode seven-transmembrane domain proteins that are receptors for the wingless type MMTV integration site family of signaling proteins. Most frizzled receptors are coupled to the beta-catenin canonical signaling pathway. The function of this protein is unknown, although it may play a role in mammalian hair follicle development. Alternative splicing results in multiple transcript variants. This gene is a susceptibility …

**Accessions** — [HGNC:4041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4041) · Entrez [7976](https://www.ncbi.nlm.nih.gov/gene/7976) · UniProt [Q9NPG1](https://www.uniprot.org/uniprotkb/Q9NPG1) · Ensembl [ENSG00000104290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104290)

## Data

Gene col 2434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2434); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2434]; `tensor/DDL_lfc|DDL_z.npy` [2434]; `embed/gene_vectors.npy` [2434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2434 or target_col == 2434). Every well: [[FZD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
