---
symbol: "LINC02210-CRHR1"
type: "gene"
col: 15421
ensembl_id: "ENSG00000263715"
name: "LINC02210-CRHR1 readthrough"
location: "17q21.31"
module: 179
arm: "+"
pooled_cpm: 31.15
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# LINC02210-CRHR1

*LINC02210-CRHR1 readthrough* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +8.3, q 7e-14, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -16.5, q 0e+00, down in 34 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.533× (z -12.6, q 4e-34, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATG9B]] (+0.64, fdr 7e-06), [[HLA-F-AS1]] (+0.63, fdr 1e-05), [[MICE]] (+0.60, fdr 1e-05); moves opposite to [[ZNF644]] (-0.52, fdr 1e-05), [[TIGD2]] (-0.52, fdr 1e-05), [[MYCBP2]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATG9B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.3 | 7e-14 | 24/47 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.9 | 1e-06 | 15/47 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 9e-06 | 22/46 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.003 | 11/47 (J82, BT-474, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.23×** | +4.1 | 0.005 | 16/46 (LS 180, HOP62, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.25× | +3.3 | 0.11 | 6/46 (LoVo, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.11 | 14/45 (CFPAC-1, AN3 CA, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.16× | +3.0 | 0.17 | 10/46 (SNU-423, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.559×** | -16.5 | 0e+00 | 34/46 (CFPAC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -12.6 | 4e-34 | 30/46 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -12.4 | 4e-33 | 32/47 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -8.7 | 4e-16 | 27/46 (CHP-212, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -7.9 | 3e-13 | 27/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.718×** | -6.4 | 2e-08 | 27/46 (J82, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.748×** | -5.8 | 5e-07 | 21/46 (SW480, PANC-1, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.774×** | -5.1 | 2e-05 | 22/46 (SNU-1, NCI-H460, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.778×** | -5.0 | 3e-05 | 21/47 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.783×** | -4.9 | 5e-05 | 23/42 (HCT15, NCI-H1573, …) | all doses, flat | composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | 0.835× | -3.6 | 0.016 | 13/46 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.831×** | -3.6 | 0.017 | 16/36 (NCI-H1573, CFPAC-1, …) | all doses, flat | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.840× | -3.5 | 0.021 | 11/47 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.886× | -3.4 | 0.025 | 6/48 (CFPAC-1, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.833×** | -3.4 | 0.027 | 19/38 (CFPAC-1, HOP62, …) | all doses, flat | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.029 | 9/45 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.048 | 5/47 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.057 | 6/46 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.057 | 11/46 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.755×** | -2.9 | 0.083 | 5/46 (HCT15, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -29.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 55.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -20.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -16.1) |
| [[HOP62 (line)]] | alt | 47.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 126 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -25.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.148× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 60.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.464× (z -9.4) |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 42.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -11.0) |
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.358× (z -9.5) |
| [[SHP-77 (line)]] | alt | 72.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +26.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SW480 (line)]] | alt | 39.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.368× (z -10.5) |
| [[A-427 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -8.9) |
| [[COLO 205 (line)]] | alt | 53.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.221× (z -9.0) |
| [[LoVo (line)]] | wt | 26.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 10.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.04× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -10.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.326× (z -8.6) |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 26.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -9.0) |
| [[C32 (line)]] | wt | 11.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0845× (z -10.4) |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0776× (z -10.6) ⚠ toxic |
| [[H4 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0742× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[KATO III (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +16.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0945× (z -13.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW48 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG9B]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HLA-F-AS1]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[MICE]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[C12orf73]] | +0.56 | +0.29 / +0.61 | both halves | 2e-04 |  |
| [[F11R]] | +0.55 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CDC26]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CERK]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[GNRH1]] | +0.53 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SLC2A1-DT]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DDN-AS1]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TBC1D22A-DT]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[L3MBTL1]] | +0.52 | +0.38 / +0.56 | both halves | 7e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MYCBP2]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[PARVA]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ARHGAP24]] | -0.49 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DNAH5]] | -0.48 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[KRT7]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[XRN2]] | -0.48 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[TNS3]] | -0.47 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[FNDC3A]] | -0.46 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[SNAI2]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CUX1]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATG9B]] | B | ATG9B activity raises LINC02210-CRHR1's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without ATG9B | 0.061 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[MIR4458HG]] | B | MIR4458HG activity raises LINC02210-CRHR1's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without MIR4458HG | 0.098 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (8.0, -22.5); signed map (-26.2, 26.5). **Vector** length 94.7, 20.6% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.6 | -12.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -16.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -12.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | LINC02210-CRHR1 readthrough |
| Locus type | readthrough (other) |
| Location | 17q21.31 — chr17:45,620,344-45,835,826 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [104909134](https://www.ncbi.nlm.nih.gov/gene/104909134):

> This locus represents naturally occurring readthrough transcription between neighboring genes CRHR1-IT1, CRHR1 intronic transcript 1 (Gene ID: 147081) and CRHR1, corticotropin releasing hormone receptor 1 (Gene ID: 1394) on chromosome 17. The readthrough transcript encodes a protein that shares sequence identity with the product of the CRHR1 gene. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:51483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51483) · Entrez [104909134](https://www.ncbi.nlm.nih.gov/gene/104909134) · Ensembl [ENSG00000263715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263715)

## Data

Gene col 15421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15421); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15421]; `tensor/DDL_lfc|DDL_z.npy` [15421]; `embed/gene_vectors.npy` [15421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15421 or target_col == 15421). Every well: [[LINC02210-CRHR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LINC02210-CRHR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
