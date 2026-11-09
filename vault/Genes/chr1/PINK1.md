---
symbol: "PINK1"
type: "gene"
col: 8196
ensembl_id: "ENSG00000158828"
name: "PTEN induced kinase 1"
location: "1p36.12"
module: 145
arm: "+"
pooled_cpm: 16.16
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 19
n_dd_up_clean: 23
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# PINK1

*PTEN induced kinase 1* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.66× (z +7.2, q 2e-10, up in 20 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +5.5, q 5e-06, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.319× (z -16.3, q 0e+00, down in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.557× (z -11.8, q 2e-29, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ULK1]] (+0.72, fdr 1e-05), [[TMEM50A]] (+0.71, fdr 7e-06), [[SAP30L]] (+0.63, fdr 1e-05); moves opposite to [[SF3B3]] (-0.59, fdr 1e-05), [[C19orf48]] (-0.56, fdr 1e-05), [[PFAS]] (-0.55, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.2 | 2e-10 | 20/36 (NCI-H2347, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.6 | 8e-09 | 20/29 (NCI-H2347, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.5 | 5e-06 | 24/46 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.8 | 2e-04 | 15/42 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +4.8 | 2e-04 | 22/48 (LS 180, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +4.6 | 4e-04 | 20/45 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 4e-04 | 18/47 (A-427, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 17/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 16/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.003 | 15/45 (A-427, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.004 | 18/46 (HS-578T, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.004 | 13/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.004 | 17/45 (CFPAC-1, KATO III, …) | two highest doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.006 | 12/46 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.008 | 18/47 (MIA PaCa-2, A-172, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.008 | 15/48 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.014 | 15/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.021 | 5/42 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.319×** | -16.3 | 0e+00 | 45/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -11.8 | 2e-29 | 30/45 (A-427, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.293×** | -7.5 | 2e-11 | 33/45 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.352×** | -6.3 | 3e-08 | 28/44 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.376×** | -5.9 | 3e-07 | 32/45 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.656×** | -5.8 | 8e-07 | 22/47 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -5.6 | 1e-06 | 26/47 (HS-578T, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.403×** | -5.5 | 2e-06 | 26/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -5.4 | 3e-06 | 28/43 (HS-578T, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.429×** | -5.1 | 2e-05 | 23/42 (A498, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.705×** | -5.0 | 4e-05 | 20/47 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.695×** | -4.9 | 5e-05 | 23/47 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -4.9 | 5e-05 | 22/45 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.699×** | -4.8 | 6e-05 | 18/48 (LoVo, SNU-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -4.6 | 1e-04 | 8/48 (HOP62, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.509×** | -4.4 | 4e-04 | 13/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.779×** | -3.3 | 0.025 | 6/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.5 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -12.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 9.42 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.5) |
| [[A-427 (line)]] | wt | 34.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -20.2) |
| [[J82 (line)]] | alt | 27.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -9.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0750× (z -15.3) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.197× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.127× (z -13.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -11.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.3) |
| [[A498 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -9.2) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 9.23 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0993× (z -9.1) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.2) |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -11.1) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.0) |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.3) |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK1]] | +0.72 | +0.56 / +0.78 | both halves | 1e-05 | pathway: Autophagy; STRING 573 |
| [[TMEM50A]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SAP30L]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[HEBP2]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[RB1CC1]] | +0.63 | +0.50 / +0.67 | both halves | 1e-05 | pathway: Autophagy; STRING 719 |
| [[MXD4]] | +0.62 | +0.46 / +0.68 | both halves | 2e-05 | same gene group |
| [[CASTOR2]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[FBXL20]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[DUSP18]] | +0.60 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[GABARAPL2]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Autophagy; STRING 708 |
| [[MACO1]] | +0.59 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[BSDC1]] | +0.58 | +0.43 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[C19orf48]] | -0.56 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PFAS]] | -0.55 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TCERG1]] | -0.55 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[MAK16]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NOL11]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[SMARCAD1]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[UTP20]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SNX5]] | -0.53 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[DCPS]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[NOC3L]] | -0.53 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[NAA15]] | -0.52 | -0.38 / -0.58 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.4, -43.4); signed map (-17.3, 14.1). **Vector** length 94.3, 22.2% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +3.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.5 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +4.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -16.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.8 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | PTEN induced kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,633,458-20,651,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BRPK; previously PARK6 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; PTEN induced kinase 1 family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 7 pathways, smallest: FOXO-mediated transcription of cell death genes; PINK1-PRKN Mediated Mitophagy; Mitophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXM7](https://www.uniprot.org/uniprotkb/Q9BXM7) (Serine/threonine-protein kinase PINK1, mitochondrial):

> Serine/threonine-protein kinase which acts as a sensor of mitochondrial damage and protects against mitochondrial dysfunction during cellular stress. It phosphorylates mitochondrial proteins to coordinate mitochondrial quality control mechanisms that remove and replace dysfunctional mitochondrial components. In healthy mitochondria, PINK1 is translocated across the mitochondrial outer membrane (MOM) via the translocase of the outer membrane (TOM) complex, and inserted into the mitochondrial …

**Summary**, from NCBI Gene [65018](https://www.ncbi.nlm.nih.gov/gene/65018):

> This gene encodes a serine/threonine protein kinase that localizes to mitochondria. It is thought to protect cells from stress-induced mitochondrial dysfunction. Mutations in this gene cause one form of autosomal recessive early-onset Parkinson disease. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14581) · Entrez [65018](https://www.ncbi.nlm.nih.gov/gene/65018) · UniProt [Q9BXM7](https://www.uniprot.org/uniprotkb/Q9BXM7) · Ensembl [ENSG00000158828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158828)

## Data

Gene col 8196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8196); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8196]; `tensor/DDL_lfc|DDL_z.npy` [8196]; `embed/gene_vectors.npy` [8196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8196 or target_col == 8196). Every well: [[PINK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PINK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
