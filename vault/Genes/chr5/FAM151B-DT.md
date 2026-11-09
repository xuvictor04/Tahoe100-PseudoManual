---
symbol: "FAM151B-DT"
type: "gene"
col: 14584
ensembl_id: "ENSG00000249042"
name: "FAM151B divergent transcript"
location: "5q14.1"
module: 21
arm: "+"
pooled_cpm: 20.4
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# FAM151B-DT

*FAM151B divergent transcript* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.01× (z +11.2, q 2e-26, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.32× (z +4.5, q 9e-04, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.640× (z -7.1, q 7e-10, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLJ40194]] (+0.65, fdr 1e-05), [[PNISR]] (+0.63, fdr 8e-06), [[SLC3A1]] (+0.62, fdr 7e-06); moves opposite to [[ELOVL1]] (-0.56, fdr 3e-05), [[CPTP]] (-0.54, fdr 3e-05), [[ASAP1]] (-0.54, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLRK1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +11.2 | 2e-26 | 34/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +10.0 | 3e-21 | 28/33 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.9 | 2e-04 | 16/36 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +4.5 | 9e-04 | 17/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.5 | 9e-04 | 17/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.4 | 0.001 | 18/43 (A-172, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.005 | 16/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.008 | 19/47 (A498, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.010 | 15/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.011 | 16/48 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.7 | 0.011 | 15/48 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.013 | 16/48 (NCI-H1573, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.016 | 15/47 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.040 | 15/47 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.043 | 8/48 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.044 | 14/48 (NCI-H1573, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.053 | 10/48 (NCI-H1573, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.057 | 9/46 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -7.1 | 7e-10 | 29/48 (SNU-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -5.7 | 3e-06 | 28/48 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.706×** | -5.5 | 6e-06 | 23/48 (COLO 205, HT-29, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -5.5 | 6e-06 | 25/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -5.2 | 3e-05 | 24/47 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -5.1 | 3e-05 | 25/46 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.727×** | -5.1 | 3e-05 | 23/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -4.9 | 6e-05 | 22/48 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.806×** | -4.8 | 9e-05 | 24/47 (COLO 205, HS-578T, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -4.8 | 1e-04 | 18/48 (SW48, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.741×** | -4.8 | 1e-04 | 20/48 (COLO 205, KATO III, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.7 | 1e-04 | 5/48 (C-33 A, RPMI-7951, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.756×** | -4.4 | 4e-04 | 20/47 (LS 180, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.758×** | -4.4 | 5e-04 | 14/48 (HT-29, COLO 205, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.784×** | -3.9 | 0.004 | 16/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.007 | 18/48 (NCI-H1573, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.797×** | -3.5 | 0.018 | 12/48 (NCI-H23, NCI-H1573, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.796×** | -3.4 | 0.021 | 9/48 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.037 | 18/48 (SW 1271, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.075 | 11/47 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.828×** | -2.9 | 0.093 | 12/47 (COLO 205, BT-474, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 66.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -8.8) |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -8.6) |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.174× (z -9.8) |
| [[A549 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.238× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0738× (z -8.6) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLJ40194]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PNISR]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[SLC3A1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ACSM3]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[EOGT-DT]] | +0.60 | +0.52 / +0.60 | both halves | 1e-05 | same gene group |
| [[TSPOAP1-AS1]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[FMC1]] | +0.59 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[DLEU7]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[FAM217A]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZRANB2-AS1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NCK1-DT]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 | same gene group |
| [[BORCS7]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL1]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[CPTP]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ASAP1]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PLXNA1]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[UBL4A]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[EIPR1]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.52 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[ZBED4]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DUSP7]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ICE1]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[PWP2]] | -0.51 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[MICAL2]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRK1-AS1]] | B | KLRK1-AS1 activity raises FAM151B-DT's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without KLRK1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers FAM151B-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[C11orf52]] | B | C11orf52 activity raises FAM151B-DT's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.33× lower at baseline in the lines without C11orf52 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[TPM2]] | B | TPM2 activity raises FAM151B-DT's level | lines that do not express TPM2 (12) vs lines expressing it (38) | 1.15× lower at baseline in the lines without TPM2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GAB3, CYBRD1, CACNG6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, 28.7); signed map (35.9, 2.8). **Vector** length 82.4, 16.5% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.6 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.5 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.5 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -4.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | FAM151B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.1 — chr5:80,411,231-80,488,095 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SLC7A11AR |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55578) · Entrez [121232370](https://www.ncbi.nlm.nih.gov/gene/121232370) · Ensembl [ENSG00000249042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249042)

## Data

Gene col 14584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14584); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14584]; `tensor/DDL_lfc|DDL_z.npy` [14584]; `embed/gene_vectors.npy` [14584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14584 or target_col == 14584). Every well: [[FAM151B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM151B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
