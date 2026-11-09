---
symbol: "UFL1-AS1"
type: "gene"
col: 13923
ensembl_id: "ENSG00000233797"
name: "UFL1 antisense RNA 1"
location: "6q16.1"
module: 10
arm: "+"
pooled_cpm: 14.78
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# UFL1-AS1

*UFL1 antisense RNA 1* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +11.2, q 4e-26, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.301× (z -10.9, q 2e-25, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BDNF-AS]] (+0.82, fdr 1e-05), [[RFX3-DT]] (+0.81, fdr 1e-05), [[OXA1L-DT]] (+0.79, fdr 7e-06); moves opposite to [[SH3PXD2B]] (-0.70, fdr 2e-04), [[MAST3]] (-0.69, fdr 4e-04), [[PBX4]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +11.2 | 4e-26 | 36/46 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.5 | 1e-05 | 26/44 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +4.9 | 2e-04 | 28/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.66×** | +4.6 | 5e-04 | 25/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +4.5 | 8e-04 | 26/46 (SW480, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.003 | 24/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.004 | 18/46 (NCI-H2347, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.43×** | +4.0 | 0.004 | 19/47 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.011 | 17/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.013 | 16/46 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.015 | 17/47 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.016 | 16/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.063 | 17/46 (HT-29, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.092 | 15/46 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.301×** | -10.9 | 2e-25 | 38/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.302×** | -10.9 | 2e-25 | 41/46 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.371×** | -9.1 | 2e-17 | 37/45 (COLO 205, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.435×** | -7.6 | 5e-12 | 33/46 (C-33 A, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.476×** | -6.8 | 1e-09 | 32/46 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.477×** | -6.8 | 1e-09 | 29/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.493×** | -6.1 | 9e-08 | 29/46 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.517×** | -5.8 | 5e-07 | 26/44 (LS 180, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.319×** | -5.3 | 8e-06 | 27/43 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.564×** | -5.2 | 9e-06 | 27/46 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.341×** | -5.0 | 3e-05 | 29/46 (LS 180, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.618×** | -4.4 | 5e-04 | 25/46 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.735×** | -4.0 | 0.003 | 20/47 (SHP-77, SW480, …) | all doses, flat |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.669×** | -3.7 | 0.010 | 17/46 (SK-MEL-2, Hs 766T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.663×** | -3.6 | 0.011 | 18/45 (LS 180, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -3.6 | 0.011 | 20/47 (CHP-212, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.466×** | -3.5 | 0.014 | 18/46 (SNU-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.616×** | -3.2 | 0.048 | 9/47 (LoVo, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.712×** | -3.0 | 0.077 | 10/47 (MIA PaCa-2, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.2 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.192× (z -10.8) |
| [[LoVo (line)]] | wt | 28.4 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.0969× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.217× (z -9.8) |
| [[LS 180 (line)]] | wt | 63.5 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0901× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0635× (z -8.9) |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0547× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0916× (z -9.3) |
| [[COLO 205 (line)]] | alt | 29.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0494× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 32.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.171× (z -10.2) |
| [[A-172 (line)]] | wt | 4.18 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.3) | — |
| [[A-427 (line)]] | wt | 24.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 41.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.152× (z -8.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 23.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0450× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 6.90 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0781× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 7.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +10.9) | — |
| [[A498 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDNF-AS]] | +0.82 | +0.84 / +0.54 | both halves | 1e-05 | same gene group |
| [[RFX3-DT]] | +0.81 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.79 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.79 | +0.83 / +0.67 | both halves | 7e-06 |  |
| [[PRANCR]] | +0.79 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.78 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[AK9]] | +0.78 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[MGAM]] | +0.78 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[MAD2L1-DT]] | +0.77 | +0.77 / +0.45 | both halves | 3e-05 |  |
| [[LEKR1]] | +0.77 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.77 | +0.76 / +0.44 | both halves | 3e-05 | same gene group |
| [[IQCH-AS1]] | +0.76 | +0.80 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.70 | -0.71 / -0.31 | both halves | 2e-04 |  |
| [[MAST3]] | -0.69 | -0.61 / -0.24 | both halves | 4e-04 |  |
| [[PBX4]] | -0.68 | -0.61 / -0.32 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.65 | -0.65 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity raises UFL1-AS1's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.74× lower at baseline in the lines without APPAT | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises UFL1-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without FSIP2-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers UFL1-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[LINC02940]] | B | LINC02940 activity raises UFL1-AS1's level | lines that do not express LINC02940 (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without LINC02940 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC02641; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers UFL1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.9, 16.3); signed map (27.9, -10.2). **Vector** length 83.8, 19.9% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.3 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | UFL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q16.1 — chr6:96,199,840-96,521,728 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41007) · Entrez [100861530](https://www.ncbi.nlm.nih.gov/gene/100861530) · Ensembl [ENSG00000233797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233797)

## Data

Gene col 13923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13923); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13923]; `tensor/DDL_lfc|DDL_z.npy` [13923]; `embed/gene_vectors.npy` [13923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13923 or target_col == 13923). Every well: [[UFL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UFL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
