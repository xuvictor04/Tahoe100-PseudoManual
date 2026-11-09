---
symbol: "GSTA4"
type: "gene"
col: 10021
ensembl_id: "ENSG00000170899"
name: "glutathione S-transferase alpha 4"
location: "6p12.2"
module: 45
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 23
n_dd_up_clean: 24
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# GSTA4

*glutathione S-transferase alpha 4* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.29× (z +9.9, q 2e-20, up in 5 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +8.0, q 2e-13, up in 21 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.358× (z -12.8, q 1e-34, down in 36 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO7]] (+0.63, fdr 3e-05), [[PLA2G12A]] (+0.63, fdr 7e-06), [[RAD23B]] (+0.63, fdr 6e-05); moves opposite to [[C3orf62]] (-0.58, fdr 7e-05), [[WNK4]] (-0.57, fdr 2e-05), [[CHADL]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Glycyrrhizic acid (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10021.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +9.9 | 2e-20 | 5/8 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.72×** | +9.6 | 4e-19 | 23/41 (A-427, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +8.0 | 2e-13 | 21/41 (NCI-H2347, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +7.5 | 8e-12 | 12/26 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.8 | 9e-10 | 14/25 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +6.4 | 2e-08 | 19/40 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +6.0 | 2e-07 | 19/40 (HOP62, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.3 | 7e-06 | 11/42 (J82, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.3 | 8e-06 | 5/13 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 1e-04 | 8/42 (LS 180, SW 900, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 2e-04 | 9/42 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 9/42 (HOP62, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.43×** | +4.4 | 4e-04 | 4/42 (PANC-1, A-172, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 5e-04 | 8/40 (SK-MEL-2, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +4.3 | 8e-04 | 7/41 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 9/41 (C32, HT-29, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 9/42 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 3/41 (BT-474, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.002 | 11/41 (LS 180, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 11/42 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.358×** | -12.8 | 1e-34 | 36/42 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.510×** | -11.9 | 5e-30 | 28/37 (HT-29, NCI-H2030, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.396×** | -11.2 | 6e-27 | 25/41 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.404×** | -11.0 | 6e-26 | 30/41 (COLO 205, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -10.4 | 4e-23 | 25/37 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -8.6 | 1e-15 | 22/35 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.498×** | -8.3 | 6e-15 | 21/39 (A-427, COLO 205, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.636×** | -5.6 | 1e-06 | 13/40 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.679×** | -4.7 | 2e-04 | 14/41 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.479×** | -4.6 | 2e-04 | 12/37 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -4.5 | 3e-04 | 14/41 (LS 180, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.693×** | -4.4 | 4e-04 | 10/42 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -4.0 | 0.002 | 13/41 (HS-578T, HOP62, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.734×** | -3.9 | 0.004 | 10/42 (H4, NCI-H23, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.725×** | -3.9 | 0.004 | 9/41 (SW1417, hTERT-HPNE, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.006 | 15/38 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.756×** | -3.3 | 0.026 | 3/42 (NCI-H460, SW480, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **0.759×** | -3.3 | 0.028 | 5/42 (A498, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.756×** | -3.3 | 0.028 | 10/40 (SW480, HepG2/C3A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.035 | 6/42 (A498, C32, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.765×** | -3.1 | 0.042 | 4/42 (HS-578T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.26 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.175× (z -9.3) |
| [[A-427 (line)]] | wt | 8.12 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0884× (z -11.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 3.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0523× (z -9.4) |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0506× (z -8.9) |
| [[HT-29 (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 3.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -8.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 9.70 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.177× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 3.63 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 7.47 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 6.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -8.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | +0.63 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[PLA2G12A]] | +0.63 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.63 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[BCL9]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SCPEP1]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TMEM9]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PECR]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[GSTM4]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 | same gene group; pathway: Biological oxidations; STRING 858 |
| [[ATP6V1A]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf62]] | -0.58 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[WNK4]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CHADL]] | -0.57 | -0.53 / -0.43 | both halves | 4e-05 |  |
| [[NEK10]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC11]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TLNRD1]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[KDSR]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[BLZF2P]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[AGO2]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[KCNJ14]] | -0.51 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PPIEL-1]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[CRK]] | -0.51 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity lowers GSTA4's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 2.68× higher at baseline in the lines without C11orf91 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity lowers GSTA4's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.95× higher at baseline in the lines without C21orf91-OT1 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[NEK10]] | B | NEK10 activity raises GSTA4's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without NEK10 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[JAKMIP2]] | B | JAKMIP2 activity raises GSTA4's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without JAKMIP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises GSTA4's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.38× lower at baseline in the lines without SLC5A4-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | B | GSTA4 activity lowers the cells' numbers under Glycyrrhizic acid 0.5 µM (makes them more sensitive) | lines that do not express GSTA4 (5) vs lines expressing it (43) | the lines without GSTA4: 1.22× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PHGDH, P3H3; maybe low, not absent |
| [[TRIT1]] | B | GSTA4 activity raises TRIT1's level | lines that do not express GSTA4 (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without GSTA4 | 0.092 | ⚠ within organs, on part of the lines; also absent: PHGDH, P3H3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.6, -8.1); signed map (-30.9, -16.0). **Vector** length 51.1, 6.96% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.1 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.6 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase alpha 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.2 — chr6:52,977,948-52,995,304 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Reactome | 3 pathways, smallest: Glutathione conjugation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [O15217](https://www.uniprot.org/uniprotkb/O15217) (Glutathione S-transferase A4):

> Glutathione S-transferase involved in the metabolism of electrophilic exogenous and endogenous compounds by glutathione conjugation. Catalyzes the nucleophilic attack of the sulfur atom of glutathione on the electrophilic groups of a wide range of substrates. Has high catalytic efficiency with toxic lipid peroxidation products such as 4-hydroxynonenal (4-HNE) and other long-chain 4-hydroxyalkenals, playing a major role in the protection from oxidative stress. Is involved in the regulation of …

**Summary**, from NCBI Gene [2941](https://www.ncbi.nlm.nih.gov/gene/2941):

> Cytosolic and membrane-bound forms of glutathione S-transferase are encoded by two distinct supergene families. These enzymes are involved in cellular defense against toxic, carcinogenic, and pharmacologically active electrophilic compounds. At present, eight distinct classes of the soluble cytoplasmic mammalian glutathione S-transferases have been identified: alpha, kappa, mu, omega, pi, sigma, theta and zeta. This gene encodes a glutathione S-tranferase belonging to the alpha class. The alpha …

**Accessions** — [HGNC:4629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4629) · Entrez [2941](https://www.ncbi.nlm.nih.gov/gene/2941) · UniProt [O15217](https://www.uniprot.org/uniprotkb/O15217) · Ensembl [ENSG00000170899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170899)

## Data

Gene col 10021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10021); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10021]; `tensor/DDL_lfc|DDL_z.npy` [10021]; `embed/gene_vectors.npy` [10021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10021 or target_col == 10021). Every well: [[GSTA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
