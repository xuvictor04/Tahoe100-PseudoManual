---
symbol: "ACAD9"
type: "gene"
col: 10845
ensembl_id: "ENSG00000177646"
name: "acyl-CoA dehydrogenase family member 9"
location: "3q21.3"
module: 83
arm: "+"
pooled_cpm: 47.63
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# ACAD9

*acyl-CoA dehydrogenase family member 9* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +18.4, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.661× (z -8.0, q 5e-13, down in 35 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.769× (z -7.2, q 9e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGG]] (+0.73, fdr 2e-05), [[RECQL5]] (+0.73, fdr 7e-06), [[HCG18]] (+0.71, fdr 1e-05); moves opposite to [[USP2]] (-0.67, fdr 1e-05), [[FAM102B]] (-0.65, fdr 2e-05), [[CAT]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +18.4 | 0e+00 | 44/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.0 | 6e-10 | 32/48 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.4 | 1e-05 | 23/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.3 | 2e-05 | 22/48 (C32, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +4.8 | 2e-04 | 25/48 (J82, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.32×** | +4.7 | 2e-04 | 26/47 (RKO, AsPC-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.4 | 0.062 | 5/48 (CFPAC-1, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.071 | 12/48 (SK-MEL-2, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.16 | 12/48 (A-172, CHP-212, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -8.0 | 5e-13 | 35/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -7.4 | 4e-11 | 35/47 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -7.2 | 9e-11 | 33/48 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.698×** | -6.2 | 7e-08 | 30/48 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.727×** | -6.2 | 7e-08 | 29/48 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -4.6 | 3e-04 | 26/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -4.0 | 0.006 | 19/48 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.867× | -3.9 | 0.006 | 14/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.834× | -3.5 | 0.026 | 19/48 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.838× | -3.4 | 0.035 | 12/48 (LoVo, A-172, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.846× | -3.3 | 0.058 | 21/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.856× | -3.0 | 0.11 | 18/48 (A-427, A-172, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.857× | -3.0 | 0.11 | 14/48 (A498, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 59.0 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.440× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[KATO III (line)]] | alt | 84.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.267× (z -14.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +15.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -9.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 71.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 28.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A-427 (line)]] | wt | 75.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[C32 (line)]] | wt | 25.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.128× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 41.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.352× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 2 | — | [[Hesperidin (drug)]] 5 µM 0.168× (z -9.0) |
| [[Hs 766T (line)]] | wt | 32.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[J82 (line)]] | alt | 56.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -14.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 61.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 1271 (line)]] | alt | 54.1 | 0 | 2 | — | [[Darolutamide (drug)]] 0.5 µM 0.0497× (z -11.0) |
| [[SW48 (line)]] | wt | 46.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.4) | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.196× (z -9.8) |
| [[SW480 (line)]] | alt | 52.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.621× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 67.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 51.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.260× (z -10.1) ⚠ toxic |
| [[H4 (line)]] | wt | 75.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0449× (z -20.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 73.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +15.9) | — |
| [[HS-578T (line)]] | alt | 47.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 48.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +14.5) | — |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 35.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +19.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 62.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.1) | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.366× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGG]] | +0.73 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[RECQL5]] | +0.73 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[HCG18]] | +0.71 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.69 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TRNT1]] | +0.68 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[ZNF26]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MAEA]] | +0.67 | +0.58 / +0.52 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[LENG8-AS1]] | +0.67 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ALG8]] | +0.66 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[DUS2]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 | same gene group |
| [[TRIM39]] | +0.66 | +0.46 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | -0.67 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.65 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[CAT]] | -0.62 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CYRIA]] | -0.62 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[KRAS]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[HMGN3]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SERAC1]] | -0.60 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ALAD]] | -0.60 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CDC14B]] | -0.60 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | -0.59 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[LIFR]] | -0.59 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TMOD2]] | -0.59 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ACAD9's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LGR4]] | B | LGR4 activity lowers ACAD9's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.16× higher at baseline in the lines without LGR4 | 0.077 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers ACAD9's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-6.3, 18.6); signed map (7.8, 0.6). **Vector** length 99.8, 24.0% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +18.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.0 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.0 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.5 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.9 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,879,596-128,924,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPD002, MGC14452 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Mitochondrial complex I assembly complex; Flavoproteins |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H845](https://www.uniprot.org/uniprotkb/Q9H845) (Complex I assembly factor ACAD9, mitochondrial):

> Together with NDUFAF1 and ECSIT, forms part of the mitochondrial complex I (MCIA),which is required for the biogenesis of respiratory Complex I (CI) and is therefore crucial for the activation of the oxidative phosphorylation system. ECSIT binding triggers a large conformational change, switching ACAD9 from a fatty acid oxidation (FAO) enzyme to a CI assembly factor. The function in CI assembly is independent of the fatty acid oxidation (FAO) activity of the protein. As FAO enzyme, it catalyzes …

**Summary**, from NCBI Gene [28976](https://www.ncbi.nlm.nih.gov/gene/28976):

> This gene encodes a member of the acyl-CoA dehydrogenase family. Members of this family of proteins localize to the mitochondria and catalyze the rate-limiting step in the beta-oxidation of fatty acyl-CoA. The encoded protein is specifically active toward palmitoyl-CoA and long-chain unsaturated substrates. Mutations in this gene cause acyl-CoA dehydrogenase family member type 9 deficiency. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:21497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21497) · Entrez [28976](https://www.ncbi.nlm.nih.gov/gene/28976) · UniProt [Q9H845](https://www.uniprot.org/uniprotkb/Q9H845) · Ensembl [ENSG00000177646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177646)

## Data

Gene col 10845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10845); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10845]; `tensor/DDL_lfc|DDL_z.npy` [10845]; `embed/gene_vectors.npy` [10845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10845 or target_col == 10845). Every well: [[ACAD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
