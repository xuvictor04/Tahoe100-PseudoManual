---
symbol: "TBC1D1"
type: "gene"
col: 807
ensembl_id: "ENSG00000065882"
name: "TBC1 domain family member 1"
location: "4p14"
module: 6
arm: "+"
pooled_cpm: 51.34
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TBC1D1

*TBC1 domain family member 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.56× (z +11.8, q 3e-29, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.493× (z -18.6, q 0e+00, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.605× (z -9.4, q 2e-18, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX7]] (+0.61, fdr 1e-05), [[ABCC4]] (+0.60, fdr 1e-05), [[MAN2A1]] (+0.60, fdr 1e-05); moves opposite to [[CWC25]] (-0.54, fdr 1e-05), [[CLBA1]] (-0.53, fdr 2e-05), [[YJU2B]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CD24]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +11.8 | 3e-29 | 40/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +10.0 | 3e-21 | 36/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.4 | 3e-08 | 25/47 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.8 | 7e-07 | 24/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.6 | 5e-04 | 16/39 (CFPAC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +4.5 | 7e-04 | 18/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.57×** | +4.4 | 1e-03 | 17/48 (LoVo, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.001 | 20/48 (LoVo, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 21/47 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.003 | 21/48 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.004 | 18/48 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.6 | 0.014 | 17/48 (LoVo, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.014 | 17/48 (LoVo, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.018 | 20/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.019 | 20/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.024 | 17/47 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.031 | 17/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.062 | 15/47 (HS-578T, SW 900, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.493×** | -18.6 | 0e+00 | 43/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -9.4 | 2e-18 | 36/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -8.4 | 6e-15 | 37/49 (RKO, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.629×** | -8.3 | 1e-14 | 33/48 (AN3 CA, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -7.0 | 2e-10 | 33/47 (SW48, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.567×** | -5.5 | 3e-06 | 28/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -5.0 | 5e-05 | 22/48 (LoVo, C-33 A, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.700×** | -4.8 | 1e-04 | 28/47 (SW 1271, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.776×** | -4.7 | 1e-04 | 21/48 (A498, KATO III, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.844× | -4.5 | 5e-04 | 19/48 (CHP-212, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.031 | 16/47 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.831×** | -3.3 | 0.053 | 16/48 (Panc 03.27, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.839× | -3.1 | 0.072 | 12/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.848× | -3.1 | 0.081 | 17/48 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.081 | 11/48 (LOX-IMVI, LS 180, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 89.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -15.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.242× (z -9.6) |
| [[LoVo (line)]] | wt | 108 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -19.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -11.0) |
| [[RKO (line)]] | wt | 131 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -13.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 66.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -21.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -12.8) |
| [[A498 (line)]] | wt | 74.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -15.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 50.8 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.20× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -14.4) |
| [[PANC-1 (line)]] | alt | 25.4 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.93× (z +9.8) | — |
| [[SW48 (line)]] | wt | 70.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0477× (z -10.8) |
| [[SW480 (line)]] | alt | 39.2 | 2 | 1 | [[Tucidinostat (drug)]] 0.5 µM 2.17× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.472× (z -8.5) |
| [[AN3 CA (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0468× (z -19.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 89.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 31.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[J82 (line)]] | alt | 57.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 32.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 24.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 62.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.0835× (z -9.0) |
| [[A-172 (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 88.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -13.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 46.2 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 2.72× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX7]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ABCC4]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MAN2A1]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SYTL4]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PRSS12]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CARMIL1]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[LYPD6]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GOLM1]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[FARP1]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[TMEM109]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ARHGEF26]] | +0.55 | +0.69 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC25]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CLBA1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[YJU2B]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.52 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[LRRC27]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[OSCP1]] | -0.50 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[NR1H3]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DNTTIP1]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CDKL3]] | -0.49 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[KLC4]] | -0.49 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[TERF2IP]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[KIAA0319L]] | -0.48 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD24]] | B | CD24 activity lowers TBC1D1's level | lines that do not express CD24 (24) vs lines expressing it (26) | 1.30× higher at baseline in the lines without CD24 | 0.056 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TBC1D1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EMB]] | B | EMB activity lowers TBC1D1's level | lines that do not express EMB (21) vs lines expressing it (29) | 1.17× higher at baseline in the lines without EMB | 0.061 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, SUSD5, PKIA |
| [[MECOM]] | B | MECOM activity raises TBC1D1's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.25× lower at baseline in the lines without MECOM | 0.070 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.4, 37.0); signed map (-2.3, 16.1). **Vector** length 120, 34.1% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.4 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.3 | -18.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -8.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.7 | -1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:37,891,084-38,139,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TBC, TBC1, KIAA1108 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 3 pathways, smallest: Translocation of SLC2A4 (GLUT4) to the plasma membrane; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TI0](https://www.uniprot.org/uniprotkb/Q86TI0) (TBC1 domain family member 1):

> May act as a GTPase-activating protein for Rab family protein(s). May play a role in the cell cycle and differentiation of various tissues. Involved in the trafficking and translocation of GLUT4-containing vesicles and insulin-stimulated glucose uptake into cells (By similarity).

**Summary**, from NCBI Gene [23216](https://www.ncbi.nlm.nih.gov/gene/23216):

> TBC1D1 is the founding member of a family of proteins sharing a 180- to 200-amino acid TBC domain presumed to have a role in regulating cell growth and differentiation. These proteins share significant homology with TRE2 (USP6; MIM 604334), yeast Bub2, and CDC16 (MIM 603461) (White et al., 2000 [PubMed 10965142]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:11578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11578) · Entrez [23216](https://www.ncbi.nlm.nih.gov/gene/23216) · UniProt [Q86TI0](https://www.uniprot.org/uniprotkb/Q86TI0) · Ensembl [ENSG00000065882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065882)

## Data

Gene col 807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 807); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 807]; `tensor/DDL_lfc|DDL_z.npy` [807]; `embed/gene_vectors.npy` [807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 807 or target_col == 807). Every well: [[TBC1D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
