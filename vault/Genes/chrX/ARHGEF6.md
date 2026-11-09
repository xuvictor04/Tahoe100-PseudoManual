---
symbol: "ARHGEF6"
type: "gene"
col: 4996
ensembl_id: "ENSG00000129675"
name: "Rac/Cdc42 guanine nucleotide exchange factor 6"
location: "Xq26.3"
module: 13
arm: "+"
pooled_cpm: 7.51
n_lines_expressing: 30
n_dd_up: 28
n_dd_down: 22
n_dd_up_clean: 21
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 41
direction_downstream: 43
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ARHGEF6

*Rac/Cdc42 guanine nucleotide exchange factor 6* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +19.7, q 0e+00, up in 12 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.502× (z -9.0, q 1e-16, down in 19 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFRB]] (+0.71, fdr 7e-06), [[FBN1]] (+0.68, fdr 7e-06), [[PTGFR]] (+0.67, fdr 9e-06); moves opposite to [[PTX3]] (-0.50, fdr 5e-05), [[RAPGEF5]] (-0.48, fdr 8e-05), [[IKBKB]] (-0.47, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[GXYLT2]] → it (grade B ⚠); 43 go from it, the strongest it → [[GXYLT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +19.7 | 0e+00 | 12/22 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +16.1 | 0e+00 | 3/12 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +12.5 | 2e-33 | 4/16 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +9.5 | 4e-19 | 5/20 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.4 | 2e-11 | 7/23 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.0 | 3e-10 | 4/23 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.72×** | +6.8 | 9e-10 | 14/25 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.8 | 9e-10 | 5/26 (Hs 766T, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.5 | 6e-09 | 3/13 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.1 | 5e-08 | 4/24 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.3 | 5e-06 | 3/23 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +5.3 | 5e-06 | 9/27 (NCI-H1792, A498, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-05 | 16/25 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 4e-05 | 8/26 (NCI-H460, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 4e-05 | 10/25 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 3e-04 | 8/25 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 2/27 (NCI-H2030, LOX-IMVI) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.002 | 10/26 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.002 | 7/27 (NCI-H460, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.502×** | -9.0 | 1e-16 | 19/25 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -8.7 | 8e-16 | 17/24 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.527×** | -8.4 | 1e-14 | 15/24 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.530×** | -8.0 | 2e-13 | 18/24 (NCI-H460, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.577×** | -7.2 | 7e-11 | 17/26 (SNU-423, hTERT-HPNE, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.635×** | -5.7 | 1e-06 | 12/25 (SNU-423, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -5.2 | 2e-05 | 12/21 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.680×** | -5.0 | 3e-05 | 9/25 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.778×** | -4.6 | 2e-04 | 16/25 (PANC-1, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.704×** | -4.6 | 3e-04 | 8/23 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.708×** | -4.5 | 3e-04 | 11/25 (HS-578T, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.726×** | -4.2 | 0.001 | 18/28 (SNU-423, HOP62, …) | all doses, flat | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.732×** | -4.1 | 0.002 | 12/25 (H4, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.747×** | -3.8 | 0.006 | 12/27 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.018 | 12/25 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.023 | 13/22 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.023 | 3/25 (SNU-1, HOP62, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.023 | 6/26 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.780×** | -3.2 | 0.036 | 4/25 (HOP62, H4, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.801×** | -2.9 | 0.098 | 8/25 (H4, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.0 | 1 | 10 (4 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.95× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.0633× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.132× (z -13.1) |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.4) |
| [[A498 (line)]] | wt | 40.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -11.3) |
| [[H4 (line)]] | wt | 19.8 | 0 | 5 (3 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0386× (z -12.4) |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -9.2) |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.219× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.8) |
| [[A-172 (line)]] | wt | 7.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.7) |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM 0.0733× (z -8.6) |
| [[J82 (line)]] | alt | 4.82 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0734× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0507× (z -14.0) |
| [[SW 900 (line)]] | alt | 9.72 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0825× (z -9.9) |
| [[A-427 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.939 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFRB]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FBN1]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[PTGFR]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[COL5A1]] | +0.62 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[B3GNT9]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SIRLNT]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[KCNE4]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[MXRA5]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[NID2]] | +0.59 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[SLC14A2]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MSC-AS1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTX3]] | -0.50 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[RAPGEF5]] | -0.48 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[IKBKB]] | -0.47 | -0.40 / -0.52 | both halves | 5e-05 | pathway: Death Receptor Signaling |
| [[BCL2L1]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CSF3]] | -0.46 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[MCTP1]] | -0.46 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[SRGN]] | -0.45 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[MT2A]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PKP2]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ANK3]] | -0.44 | -0.46 / -0.38 | both halves | 7e-05 | pathway: Cell junction organization; STRING 490 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 12, C 29. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | GXYLT2 activity raises ARHGEF6's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.70× lower at baseline in the lines without GXYLT2 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[CA12]] | B | CA12 activity raises ARHGEF6's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without CA12 | 0.024 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[PAPPA2]] | B | PAPPA2 activity raises ARHGEF6's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without PAPPA2 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[HHIPL2]] | B | HHIPL2 activity raises ARHGEF6's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without HHIPL2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ARHGEF6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NID2]] | B | NID2 activity raises ARHGEF6's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without NID2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[PKP2]] | B | PKP2 activity lowers ARHGEF6's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.70× higher at baseline in the lines without PKP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[TDO2]] | B | TDO2 activity raises ARHGEF6's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without TDO2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1 |
| [[EDIL3]] | B | EDIL3 activity raises ARHGEF6's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without EDIL3 | 0.080 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[CPQ]] | B | CPQ activity raises ARHGEF6's level | lines that do not express CPQ (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without CPQ | 0.081 | ⚠ within organs, on part of the lines; also absent: NETO2, LINC01725, KMO; maybe low, not absent |
| [[TGFBI]] | B | TGFBI activity raises ARHGEF6's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without TGFBI | 0.095 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[P2RX7]] | B | P2RX7 activity raises ARHGEF6's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.40× lower at baseline in the lines without P2RX7 | 0.099 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 24, C 19. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | ARHGEF6 activity raises GXYLT2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.19× lower at baseline in the lines without ARHGEF6 | 0.013 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[B3GNT9]] | B | ARHGEF6 activity raises B3GNT9's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without ARHGEF6 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[CPQ]] | B | ARHGEF6 activity raises CPQ's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.61× lower at baseline in the lines without ARHGEF6 | 0.018 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[RAPGEF5]] | B | ARHGEF6 activity lowers RAPGEF5's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.99× higher at baseline in the lines without ARHGEF6 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[LINC01119]] | B | ARHGEF6 activity raises LINC01119's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 1.98× lower at baseline in the lines without ARHGEF6 | 0.024 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[CERCAM]] | B | ARHGEF6 activity raises CERCAM's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without ARHGEF6 | 0.038 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | ARHGEF6 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.86× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | ARHGEF6 activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.84× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| cells under [[Fumaric acid (drug)]] 5 µM | B | ARHGEF6 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.84× the cells of the other lines | 0.064 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[DZIP1L]] | B | ARHGEF6 activity raises DZIP1L's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without ARHGEF6 | 0.067 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | B | ARHGEF6 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.87× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[PCDHGA2]] | B | ARHGEF6 activity raises PCDHGA2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without ARHGEF6 | 0.073 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.6, 20.6); signed map (27.0, 44.7). **Vector** length 77.3, 20.6% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +19.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +4.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -8.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.0 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.9 | -7.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | Rac/Cdc42 guanine nucleotide exchange factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:136,665,547-136,780,932 (-) |
| Ensembl biotype | protein_coding |
| Also known as | alphaPIX, Cool-2, KIAA0006, alpha-PIX, Cool2, αPix; previously MRX46 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH3 domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 19 pathways, smallest: Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; G beta:gamma signalling through CDC42; Cell-extracellular matrix interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15052](https://www.uniprot.org/uniprotkb/Q15052) (Rho guanine nucleotide exchange factor 6):

> Acts as a RAC1 guanine nucleotide exchange factor (GEF).

**Summary**, from NCBI Gene [9459](https://www.ncbi.nlm.nih.gov/gene/9459):

> Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein belongs to a family of cytoplasmic proteins that activate the Ras-like family of Rho proteins by exchanging bound GDP for GTP. It may form a complex with G proteins and stimulate Rho-dependent signals. This protein is activated by PI3-kinase. Mutations in this gene can cause X-chromosomal non-specific cognitive …

**Accessions** — [HGNC:685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:685) · Entrez [9459](https://www.ncbi.nlm.nih.gov/gene/9459) · UniProt [Q15052](https://www.uniprot.org/uniprotkb/Q15052) · Ensembl [ENSG00000129675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129675)

## Data

Gene col 4996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4996); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4996]; `tensor/DDL_lfc|DDL_z.npy` [4996]; `embed/gene_vectors.npy` [4996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4996 or target_col == 4996). Every well: [[ARHGEF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
