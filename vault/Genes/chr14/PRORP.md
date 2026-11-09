---
symbol: "PRORP"
type: "gene"
col: 2037
ensembl_id: "ENSG00000100890"
name: "protein only RNase P catalytic subunit"
location: "14q13.2"
module: 1
arm: "+"
pooled_cpm: 51.48
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PRORP

*protein only RNase P catalytic subunit* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +14.5, q 8e-45, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.747× (z -7.1, q 6e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFG1L]] (+0.71, fdr 7e-06), [[MCPH1]] (+0.69, fdr 1e-05), [[UTP20]] (+0.69, fdr 7e-06); moves opposite to [[PPP1R2]] (-0.64, fdr 2e-05), [[CDON]] (-0.62, fdr 1e-05), [[ARRB2]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +14.5 | 8e-45 | 39/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.7 | 4e-12 | 29/48 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.6 | 5e-12 | 28/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +6.4 | 3e-08 | 33/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.29×** | +6.1 | 1e-07 | 31/48 (A-427, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.9 | 3e-07 | 28/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.6 | 4e-04 | 24/48 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 8e-04 | 24/47 (NCI-H2347, A549, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 1e-03 | 23/47 (A549, C32, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 25/48 (HT-29, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.006 | 21/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +3.7 | 0.009 | 18/47 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.23×** | +3.5 | 0.022 | 15/48 (A-427, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.040 | 16/48 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.068 | 15/46 (SW480, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.069 | 17/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -7.1 | 6e-10 | 34/48 (SW480, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.687×** | -6.5 | 3e-08 | 35/46 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.720×** | -5.7 | 3e-06 | 31/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.750×** | -5.0 | 1e-04 | 23/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.626×** | -4.2 | 0.003 | 29/48 (RKO, SHP-77, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.011 | 20/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -3.8 | 0.014 | 22/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.803×** | -3.7 | 0.018 | 25/47 (SHP-77, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.825×** | -3.3 | 0.053 | 21/47 (SW480, SW48, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.880× | -3.1 | 0.097 | 13/48 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.841× | -3.0 | 0.14 | 20/48 (Panc 03.27, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 64.2 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.61× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -12.6) |
| [[LoVo (line)]] | wt | 72.8 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +20.3) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 59.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~99% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.452× (z -8.5) |
| [[RKO (line)]] | wt | 57.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 62.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 54.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 45.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -10.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 23.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.6) | [[Docetaxel (drug)]] 0.05 µM 0.161× (z -12.5) ⚠ transcription drop |
| [[NCI-H1573 (line)]] | alt | 62.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 80.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[A498 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.0) | — |
| [[J82 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.0) | — |
| [[KATO III (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[MIA PaCa-2 (line)]] | alt | 62.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 72.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 58.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.502× (z -8.5) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -21.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.7) | — |
| [[SW 1271 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0876× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.212× (z -12.3) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 65.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFG1L]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MCPH1]] | +0.69 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[UTP20]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 | pathway: rRNA processing |
| [[TASOR]] | +0.69 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[E2F3]] | +0.67 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.67 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.67 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[DHX37]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 | pathway: rRNA processing |
| [[MRPS7]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SNAPC5]] | +0.65 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[FEM1A]] | +0.65 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[CDK12]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R2]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[CDON]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ARRB2]] | -0.62 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[RIMS3]] | -0.62 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[GPR160]] | -0.62 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PJA2]] | -0.62 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[KDM3A]] | -0.61 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[RNF114]] | -0.61 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TSPAN33]] | -0.60 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[STRN]] | -0.60 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[CAT]] | -0.60 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.60 | -0.63 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PRORP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PRORP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.7, 5.6); signed map (17.3, -27.0). **Vector** length 122, 33.5% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +14.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.8 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.2 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.5 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.0 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | protein only RNase P catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:35,121,846-35,277,622 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPP3; previously KIAA0391 |
| Gene groups (HGNC) | Mitochondrial RNase P complex; Pentatricopeptide repeat containing |
| Reactome | 6 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing in the mitochondrion; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [O15091](https://www.uniprot.org/uniprotkb/O15091) (Mitochondrial ribonuclease P catalytic subunit):

> Catalytic ribonuclease component of mitochondrial ribonuclease P, a complex composed of TRMT10C/MRPP1, HSD17B10/MRPP2 and PRORP/MRPP3, which cleaves tRNA molecules in their 5'-ends. The presence of TRMT10C/MRPP1, HSD17B10/MRPP2 is required to catalyze tRNA molecules in their 5'-ends.

**Summary**, from NCBI Gene [9692](https://www.ncbi.nlm.nih.gov/gene/9692):

> Enables ribonuclease P activity. Involved in mitochondrial tRNA 5'-end processing. Located in mitochondrion. Part of mitochondrial ribonuclease P complex. Is active in mitochondrial matrix. Implicated in combined oxidative phosphorylation deficiency 54. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19958) · Entrez [9692](https://www.ncbi.nlm.nih.gov/gene/9692) · UniProt [O15091](https://www.uniprot.org/uniprotkb/O15091) · Ensembl [ENSG00000100890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100890)

## Data

Gene col 2037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2037); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2037]; `tensor/DDL_lfc|DDL_z.npy` [2037]; `embed/gene_vectors.npy` [2037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2037 or target_col == 2037). Every well: [[PRORP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRORP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
