---
symbol: "FBRS"
type: "gene"
col: 8019
ensembl_id: "ENSG00000156860"
name: "fibrosin"
location: "16p11.2"
module: 173
arm: "+"
pooled_cpm: 39.65
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# FBRS

*fibrosin* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +15.2, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.558× (z -9.4, q 2e-18, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGL2]] (+0.72, fdr 7e-06), [[ATXN1L]] (+0.71, fdr 1e-05), [[MEPCE]] (+0.70, fdr 9e-06); moves opposite to [[GGCT]] (-0.62, fdr 4e-05), [[WASF3]] (-0.61, fdr 6e-05), [[LYPLA1]] (-0.58, fdr 4e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HSD17B14]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +15.2 | 0e+00 | 40/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +12.4 | 1e-32 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +11.0 | 5e-26 | 37/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +8.2 | 4e-14 | 38/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.1 | 8e-14 | 39/48 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +7.7 | 1e-12 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +6.8 | 6e-10 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.9 | 2e-07 | 29/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +5.3 | 9e-06 | 29/49 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.8 | 7e-05 | 27/48 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.023 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.5 | 0.023 | 0/49 | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.073 | 14/48 (SW48, A549, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.21×** | +3.1 | 0.087 | 19/47 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.558×** | -9.4 | 2e-18 | 41/48 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -8.5 | 5e-15 | 39/48 (NCI-H661, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -8.3 | 3e-14 | 36/48 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.621×** | -7.7 | 2e-12 | 41/48 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.702×** | -7.7 | 2e-12 | 42/48 (BT-474, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.687×** | -6.1 | 1e-07 | 34/48 (LOX-IMVI, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.731×** | -4.9 | 8e-05 | 22/39 (SHP-77, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.562×** | -4.9 | 8e-05 | 30/48 (AsPC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.740×** | -4.8 | 8e-05 | 28/46 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Allantoin (drug)]] 5 µM |  | **0.796×** | -4.5 | 3e-04 | 26/48 (LOX-IMVI, SW480, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.756×** | -4.5 | 3e-04 | 27/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.757×** | -4.3 | 7e-04 | 24/47 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.772×** | -4.2 | 0.001 | 22/47 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.789×** | -3.6 | 0.014 | 20/42 (NCI-H23, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.808×** | -3.5 | 0.020 | 14/48 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.803×** | -3.4 | 0.026 | 15/48 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.046 | 9/48 (RKO, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +15.7) | — |
| [[NCI-H460 (line)]] | wt | 28.8 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +13.2) | — |
| [[A498 (line)]] | wt | 70.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 83.4 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -10.0) |
| [[A549 (line)]] | wt | 35.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[AsPC-1 (line)]] | alt | 48.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 28.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 39.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.4) | [[Lonafarnib (drug)]] 5 µM 0.115× (z -10.5) ⚠ toxic |
| [[LS 180 (line)]] | wt | 34.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 50.7 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.93× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~77% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.89× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0449× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 47.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.2) | [[Pimitespib (drug)]] 5 µM 0.0801× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 52.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 32.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HCT15 (line)]] | alt | 55.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HepG2_C3A (line)]] | wt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.9) | — |
| [[J82 (line)]] | alt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.2) | — |
| [[LoVo (line)]] | wt | 30.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 44.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +10.2) | — |
| [[SW48 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 31.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +10.1) | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGL2]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ATXN1L]] | +0.71 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[MEPCE]] | +0.70 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[AKT1S1]] | +0.70 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[SCAF1]] | +0.69 | +0.60 / +0.62 | both halves | 7e-06 | STRING 409 |
| [[CACTIN]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DMWD]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[EP300]] | +0.68 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[KDM6B]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MED12]] | +0.67 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SIX5]] | +0.67 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ZNF687]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGCT]] | -0.62 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[WASF3]] | -0.61 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[LYPLA1]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PACC1]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[FXN]] | -0.57 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[METAP1]] | -0.56 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[TMEM241]] | -0.56 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[NHP2]] | -0.55 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[FAR1]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD17B14]] | C | HSD17B14 activity raises FBRS's level | lines that do not express HSD17B14 (3) vs lines expressing it (47) | 1.31× lower at baseline in the lines without HSD17B14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BFSP1, DNAJB5, MYADM; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.0, -22.1); signed map (16.3, -21.2). **Vector** length 96.1, 24.0% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +15.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.7 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +11.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | -0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +0.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | -0.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | fibrosin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,658,431-30,670,810 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBS, FLJ11618; previously FBS1 |
| Matched by | ensembl_id |

UniProt [Q9HAH7](https://www.uniprot.org/uniprotkb/Q9HAH7) carries no function annotation.

**Summary**, from NCBI Gene [64319](https://www.ncbi.nlm.nih.gov/gene/64319):

> Fibrosin is a lymphokine secreted by activated lymphocytes that induces fibroblast proliferation (Prakash and Robbins, 1998 [PubMed 9809749]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20442) · Entrez [64319](https://www.ncbi.nlm.nih.gov/gene/64319) · UniProt [Q9HAH7](https://www.uniprot.org/uniprotkb/Q9HAH7) · Ensembl [ENSG00000156860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156860)

## Data

Gene col 8019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8019); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8019]; `tensor/DDL_lfc|DDL_z.npy` [8019]; `embed/gene_vectors.npy` [8019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8019 or target_col == 8019). Every well: [[FBRS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBRS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
