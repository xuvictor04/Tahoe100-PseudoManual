---
symbol: "SORT1"
type: "gene"
col: 5526
ensembl_id: "ENSG00000134243"
name: "sortilin 1"
location: "1p13.3"
module: 106
arm: "+"
pooled_cpm: 34.59
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 11
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SORT1

*sortilin 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.45× (z +22.4, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.696× (z -6.5, q 4e-08, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM245]] (+0.68, fdr 1e-05), [[CPD]] (+0.64, fdr 7e-06), [[SLC44A1]] (+0.63, fdr 1e-05); moves opposite to [[GPATCH2L]] (-0.60, fdr 1e-05), [[ZNF341-AS1]] (-0.59, fdr 3e-05), [[ZNF432]] (-0.58, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 11 go from it, the strongest it → [[PRKACA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.45×** | +22.4 | 0e+00 | 41/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.00×** | +19.9 | 0e+00 | 41/41 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.95×** | +19.5 | 0e+00 | 40/41 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +12.9 | 4e-36 | 39/41 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +10.6 | 3e-24 | 35/41 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.00×** | +10.4 | 3e-23 | 36/42 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.8 | 7e-10 | 23/40 (C-33 A, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +6.1 | 6e-08 | 21/41 (HEC-1-A, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.40×** | +6.1 | 6e-08 | 17/35 (SNU-423, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.7 | 7e-07 | 21/42 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **1.71×** | +5.1 | 2e-05 | 18/39 (KATO III, SW 900, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.2 | 0.001 | 17/41 (SW480, KATO III, …) | rises with dose | composition shift |
| [[Budesonide (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 16/41 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 13/41 (LoVo, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.005 | 13/42 (C32, LoVo, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.006 | 8/40 (SNU-423, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.025 | 9/42 (C32, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.026 | 16/41 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.696×** | -6.5 | 4e-08 | 24/40 (COLO 205, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.726×** | -5.4 | 2e-05 | 20/41 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -5.3 | 2e-05 | 22/41 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -4.8 | 2e-04 | 20/41 (SK-MEL-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.769×** | -4.7 | 3e-04 | 19/41 (SW480, HT-29, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -4.7 | 3e-04 | 17/41 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.4 | 8e-04 | 20/41 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.841× | -4.4 | 8e-04 | 20/42 (A-427, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.636×** | -4.3 | 0.001 | 19/35 (SW48, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.787×** | -4.0 | 0.004 | 15/41 (A-427, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.816×** | -3.7 | 0.013 | 15/41 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.819×** | -3.6 | 0.017 | 13/41 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.876× | -3.3 | 0.036 | 4/41 (J82, BT-474, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.836× | -3.2 | 0.054 | 12/42 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.843× | -3.1 | 0.076 | 5/41 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 0.844× | -3.0 | 0.076 | 7/41 (RPMI-7951, SHP-77, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.726×** | -3.0 | 0.076 | 6/41 (NCI-H1792, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.888× | -3.0 | 0.076 | 2/42 (KATO III, RPMI-7951) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 14.5 | 16 (1 ⚠) | 1 | [[Budesonide (drug)]] 5 µM 17.4× (z +11.9) | [[Temsirolimus (drug)]] 0.5 µM 0.114× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 18.7 | 16 (1 ⚠) | 0 | [[Dexamethasone (drug)]] 0.5 µM 8.40× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 43.1 | 16 | 0 | [[Budesonide (drug)]] 5 µM 5.86× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 9.26 | 15 | 0 | [[Budesonide (drug)]] 5 µM 12.1× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 35.7 | 7 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +11.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -10.1) |
| [[SNU-423 (line)]] | alt | 41.2 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +10.8) | — |
| [[A-172 (line)]] | wt | 33.4 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.30× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.271× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.316× (z -9.1) |
| [[J82 (line)]] | alt | 39.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 11.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.55× (z +17.0) | — |
| [[SW480 (line)]] | alt | 49.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.94× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.27× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +12.8) | — |
| [[LoVo (line)]] | wt | 36.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 59.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.72× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 58.8 | 2 | 1 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.53× (z +9.6) | [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 57.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.82× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -9.7) |
| [[RKO (line)]] | wt | 37.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 31.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.157× (z -23.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[C-33 A (line)]] | alt | 38.0 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.70× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 26.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.37× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 149 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.97× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -12.4) |
| [[Hs 766T (line)]] | wt | 87.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 66.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -9.2) |
| [[KATO III (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +8.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 72.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.85 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM245]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CPD]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 | pathway: Golgi Associated Vesicle Biogenesis; STRING 675 |
| [[SLC44A1]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[AGFG2]] | +0.61 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SNX30]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[THRA]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[MGAT4A]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[APMAP]] | +0.57 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ABCD3]] | +0.57 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[TBC1D2B]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | -0.59 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZNF432]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZNF621]] | -0.58 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[MRPL45P2]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[EIF5]] | -0.56 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.56 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[LUCAT1]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[GSK3B-DT]] | -0.56 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[SPHK1]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[NOXRED1]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[HSCB]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKACA]] | B | SORT1 activity raises PRKACA's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without SORT1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[NMNAT1]] | B | SORT1 activity raises NMNAT1's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without SORT1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[EMP2]] | B | SORT1 activity raises EMP2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.90× lower at baseline in the lines without SORT1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[AGFG2]] | B | SORT1 activity raises AGFG2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without SORT1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[PAPSS1]] | B | SORT1 activity raises PAPSS1's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without SORT1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[ATP6V0E2]] | B | SORT1 activity raises ATP6V0E2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without SORT1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[DHCR24]] | B | SORT1 activity raises DHCR24's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without SORT1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[GUSB]] | B | SORT1 activity raises GUSB's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without SORT1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[KANK2]] | B | SORT1 activity raises KANK2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without SORT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[ZNF621]] | B | SORT1 activity raises ZNF621's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without SORT1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[HLTF]] | B | SORT1 activity lowers HLTF's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.02× higher at baseline in the lines without SORT1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, 5.7); signed map (-4.1, 19.6). **Vector** length 115, 30.4% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +6.0 | +12.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.7 | +10.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +10.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +19.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sortilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,309,568-109,397,918 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Gp95, NT3 |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99523](https://www.uniprot.org/uniprotkb/Q99523) (Sortilin):

> Functions as a sorting receptor in the Golgi compartment and as a clearance receptor on the cell surface. Required for protein transport from the Golgi apparatus to the lysosomes by a pathway that is independent of the mannose-6-phosphate receptor (M6PR). Lysosomal proteins bind specifically to the receptor in the Golgi apparatus and the resulting receptor-ligand complex is transported to an acidic prelysosomal compartment where the low pH mediates the dissociation of the complex. The receptor …

**Summary**, from NCBI Gene [6272](https://www.ncbi.nlm.nih.gov/gene/6272):

> This gene encodes a member of the VPS10-related sortilin family of proteins. The encoded preproprotein is proteolytically processed by furin to generate the mature receptor. This receptor plays a role in the trafficking of different proteins to either the cell surface, or subcellular compartments such as lysosomes and endosomes. Expression levels of this gene may influence the risk of myocardial infarction in human patients. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:11186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11186) · Entrez [6272](https://www.ncbi.nlm.nih.gov/gene/6272) · UniProt [Q99523](https://www.uniprot.org/uniprotkb/Q99523) · Ensembl [ENSG00000134243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134243)

## Data

Gene col 5526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5526); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5526]; `tensor/DDL_lfc|DDL_z.npy` [5526]; `embed/gene_vectors.npy` [5526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5526 or target_col == 5526). Every well: [[SORT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
