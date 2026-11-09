---
symbol: "RBM23"
type: "gene"
col: 1966
ensembl_id: "ENSG00000100461"
name: "RNA binding motif protein 23"
location: "14q11.2"
module: 51
arm: "+"
pooled_cpm: 34.74
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# RBM23

*RNA binding motif protein 23* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +24.2, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.396× (z -18.8, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YJU2]] (+0.80, fdr 7e-06), [[ZNF764]] (+0.79, fdr 7e-06), [[FIZ1]] (+0.78, fdr 7e-06); moves opposite to [[METAP1]] (-0.79, fdr 7e-06), [[STRN]] (-0.71, fdr 3e-05), [[PIGF]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GUCY1B2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +24.2 | 0e+00 | 43/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +10.4 | 6e-23 | 40/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.3 | 3e-18 | 29/45 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +9.2 | 4e-18 | 34/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.6 | 3e-06 | 23/47 (HOP62, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +5.5 | 4e-06 | 23/47 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.003 | 16/46 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +4.1 | 0.003 | 12/47 (LoVo, Panc 03.27, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +4.0 | 0.003 | 19/46 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.006 | 16/46 (NCI-H23, LoVo, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.093 | 11/46 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.096 | 15/46 (HEC-1-A, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1966.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.396×** | -18.8 | 0e+00 | 44/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.425×** | -17.4 | 0e+00 | 44/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.459×** | -15.8 | 0e+00 | 44/47 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.539×** | -12.5 | 6e-34 | 43/47 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.582×** | -11.0 | 6e-26 | 38/46 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -8.2 | 3e-14 | 33/46 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -7.8 | 4e-13 | 30/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -7.2 | 4e-11 | 31/47 (A498, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.737×** | -6.0 | 2e-07 | 30/47 (SW48, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.582×** | -5.7 | 5e-07 | 27/47 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.754×** | -5.7 | 5e-07 | 24/47 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -5.6 | 1e-06 | 23/47 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.754×** | -5.5 | 2e-06 | 24/46 (AsPC-1, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.770×** | -5.3 | 5e-06 | 20/47 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.797×** | -4.4 | 4e-04 | 18/46 (SW 900, COLO 205, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.807×** | -4.3 | 5e-04 | 20/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -4.3 | 5e-04 | 20/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.822×** | -4.0 | 0.002 | 17/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.003 | 16/46 (H4, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.900× | -3.0 | 0.061 | 8/47 (AN3 CA, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.0 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.396× (z -10.1) |
| [[LoVo (line)]] | wt | 42.4 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.383× (z -10.7) |
| [[SW480 (line)]] | alt | 42.1 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.348× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 55.5 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.288× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 48.5 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -16.0) |
| [[PANC-1 (line)]] | alt | 27.5 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.378× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.388× (z -10.4) |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 52.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -10.6) |
| [[A498 (line)]] | wt | 26.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.262× (z -12.4) |
| [[COLO 205 (line)]] | alt | 51.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.235× (z -12.2) |
| [[HOP62 (line)]] | alt | 34.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.362× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 35.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 44.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.330× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 44.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.326× (z -8.8) |
| [[SNU-423 (line)]] | alt | 31.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.298× (z -10.0) |
| [[KATO III (line)]] | alt | 47.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.427× (z -9.6) |
| [[RKO (line)]] | wt | 30.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.228× (z -10.7) |
| [[A-172 (line)]] | wt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +13.3) | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -9.4) |
| [[BT-474 (line)]] | alt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.6) | — |
| [[C32 (line)]] | wt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 40.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.9) | — |
| [[H4 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HCT15 (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.6) | — |
| [[J82 (line)]] | alt | 30.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.344× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 27.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.2) | — |
| [[SW48 (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YJU2]] | +0.80 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.79 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.78 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[COQ7]] | +0.77 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TRMO]] | +0.75 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[LARP7]] | +0.75 | +0.79 / +0.65 | both halves | 7e-06 | same gene group |
| [[NAIF1]] | +0.75 | +0.80 / +0.50 | both halves | 1e-05 |  |
| [[EPC2]] | +0.74 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.73 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[USP16]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[HELQ]] | +0.72 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.79 | -0.80 / -0.63 | both halves | 7e-06 |  |
| [[STRN]] | -0.71 | -0.74 / -0.44 | both halves | 3e-05 |  |
| [[PIGF]] | -0.70 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.69 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[LPCAT4]] | -0.69 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[PALS2]] | -0.67 | -0.75 / -0.54 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.66 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[EPS15]] | -0.65 | -0.72 / -0.43 | both halves | 3e-05 |  |
| [[FAR1]] | -0.65 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.64 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.64 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[MPZL1]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GUCY1B2]] | B | GUCY1B2 activity raises RBM23's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without GUCY1B2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.5, 10.4); signed map (12.0, -28.9). **Vector** length 122, 33.4% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +15.0 | +24.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.4 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.7 | +9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.3 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +5.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.0 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.3 | -18.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.8 | -12.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -15.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -4.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,893,204-22,919,182 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10482, CAPERbeta; previously RNPC4 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U06](https://www.uniprot.org/uniprotkb/Q86U06) (Probable RNA-binding protein 23):

> RNA-binding protein that acts both as a transcription coactivator and pre-mRNA splicing factor. Regulates steroid hormone receptor-mediated transcription, independently of the pre-mRNA splicing factor activity.

**Summary**, from NCBI Gene [55147](https://www.ncbi.nlm.nih.gov/gene/55147):

> This gene encodes a member of the U2AF-like family of RNA binding proteins. This protein interacts with some steroid nuclear receptors, localizes to the promoter of a steroid- responsive gene, and increases transcription of steroid-responsive transcriptional reporters in a hormone-dependent manner. It is also implicated in the steroid receptor-dependent regulation of alternative splicing. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:20155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20155) · Entrez [55147](https://www.ncbi.nlm.nih.gov/gene/55147) · UniProt [Q86U06](https://www.uniprot.org/uniprotkb/Q86U06) · Ensembl [ENSG00000100461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100461)

## Data

Gene col 1966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1966); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1966]; `tensor/DDL_lfc|DDL_z.npy` [1966]; `embed/gene_vectors.npy` [1966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1966 or target_col == 1966). Every well: [[RBM23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
