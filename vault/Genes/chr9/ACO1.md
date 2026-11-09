---
symbol: "ACO1"
type: "gene"
col: 4371
ensembl_id: "ENSG00000122729"
name: "aconitase 1"
location: "9p21.1"
module: 45
arm: "+"
pooled_cpm: 58.18
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ACO1

*aconitase 1* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.56× (z +24.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.662× (z -10.6, q 2e-23, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A23]] (+0.64, fdr 2e-05), [[TWSG1]] (+0.59, fdr 1e-05), [[HMGN3]] (+0.59, fdr 1e-05); moves opposite to [[EIF5]] (-0.54, fdr 4e-05), [[ZNF689]] (-0.54, fdr 6e-05), [[ZNF562]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDON]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +24.0 | 0e+00 | 46/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +20.3 | 0e+00 | 46/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +20.3 | 0e+00 | 45/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +13.2 | 1e-37 | 38/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +12.1 | 9e-32 | 38/48 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +9.5 | 2e-19 | 29/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +9.0 | 2e-17 | 32/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +8.0 | 1e-13 | 34/48 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +7.1 | 7e-11 | 24/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.8 | 6e-10 | 27/47 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.30×** | +6.6 | 2e-09 | 22/47 (NCI-H2347, KATO III, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.5 | 3e-09 | 19/35 (HS-578T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.4 | 8e-09 | 20/47 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.9 | 1e-07 | 20/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.4 | 3e-06 | 20/47 (AsPC-1, HS-578T, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +4.7 | 7e-05 | 19/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | 1.12× | +3.9 | 0.002 | 6/48 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.013 | 6/47 (KATO III, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.3 | 0.019 | 3/47 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.662×** | -10.6 | 2e-23 | 36/47 (SNU-423, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -5.0 | 2e-04 | 18/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -4.5 | 0.001 | 0/48 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.841× | -4.5 | 0.001 | 12/47 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.839× | -4.2 | 0.003 | 18/46 (LOX-IMVI, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.9 | 0.010 | 14/47 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.864× | -3.8 | 0.014 | 15/46 (HT-29, A498, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.025 | 10/46 (C32, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.025 | 14/47 (NCI-H2030, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.877× | -3.4 | 0.039 | 6/47 (H4, NCI-H661, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.878× | -3.4 | 0.040 | 6/48 (NCI-H2122, SW1417, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.876× | -3.3 | 0.047 | 15/46 (HT-29, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.882× | -3.2 | 0.050 | 10/46 (SW 900, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.053 | 7/47 (A-172, LoVo, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.917× | -3.2 | 0.053 | 7/47 (J82, Panc 03.27, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.884× | -3.2 | 0.053 | 5/47 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.887× | -3.1 | 0.062 | 9/46 (LoVo, Hs 766T, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.891× | -3.0 | 0.090 | 8/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.892× | -2.9 | 0.093 | 6/47 (AsPC-1, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 60.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.12× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 40.9 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 44.3 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +17.5) | — |
| [[SW480 (line)]] | alt | 43.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 71.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 43.7 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.407× (z -9.4) |
| [[LS 180 (line)]] | wt | 46.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 45.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 61.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.09× (z +11.0) | — |
| [[KATO III (line)]] | alt | 47.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +11.7) | — |
| [[LoVo (line)]] | wt | 36.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 45.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.28× (z +16.0) | — |
| [[RKO (line)]] | wt | 71.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 74.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.90× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.11× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.369× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 86.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0897× (z -16.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 60.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 54.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.295× (z -12.5) |
| [[COLO 205 (line)]] | alt | 30.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -8.9) ⚠ cell-cycle shift, explains ~87% of this change |
| [[J82 (line)]] | alt | 90.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 77.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0809× (z -9.2) |
| [[SW 900 (line)]] | alt | 66.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.365× (z -8.9) |
| [[SW48 (line)]] | wt | 46.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.224× (z -8.9) |
| [[A-172 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A23]] | +0.64 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[TWSG1]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CTSH]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 | pathway: Metabolism of vitamins and cofactors |
| [[CAT]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 | STRING 416 |
| [[ATP5F1C]] | +0.57 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[TMEM38B]] | +0.57 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[ALAD]] | +0.56 | +0.40 / +0.48 | both halves | 5e-05 | pathway: Iron uptake and transport; STRING 711 |
| [[HSDL2]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[GUSB]] | +0.56 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[TMEM219]] | +0.56 | +0.53 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5]] | -0.54 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNF689]] | -0.54 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ZNF562]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[C10orf88]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[DNTTIP2]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[PLAC8L1]] | -0.52 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MSH4]] | -0.52 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[FAM32A]] | -0.52 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[CHTF8]] | -0.52 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[MMADHC-DT]] | -0.51 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[CLCF1]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PBDC1]] | -0.51 | -0.38 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDON]] | C | CDON activity lowers ACO1's level | lines that do not express CDON (3) vs lines expressing it (47) | 1.60× higher at baseline in the lines without CDON | 0.078 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.8, -9.8); signed map (-27.8, -7.3). **Vector** length 98.8, 24.2% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.9 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.4 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +20.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +20.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.2 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -7.4 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | aconitase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:32,384,603-32,454,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IRP1, IREBP; previously IREB1 |
| Gene groups (HGNC) | Aconitases |
| Reactome | 4 pathways, smallest: Metabolism of cofactors; Iron uptake and transport; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P21399](https://www.uniprot.org/uniprotkb/P21399) (Cytoplasmic aconitate hydratase):

> Bifunctional iron sensor that switches between 2 activities depending on iron availability. Iron deprivation, promotes its mRNA binding activity through which it regulates the expression of genes involved in iron uptake, sequestration and utilization. Binds to iron-responsive elements (IRES) in the untranslated region of target mRNAs preventing for instance the translation of ferritin and aminolevulinic acid synthase and stabilizing the transferrin receptor mRNA.; Conversely, when cellular iron …

**Summary**, from NCBI Gene [48](https://www.ncbi.nlm.nih.gov/gene/48):

> The protein encoded by this gene is a bifunctional, cytosolic protein that functions as an essential enzyme in the TCA cycle and interacts with mRNA to control the levels of iron inside cells. When cellular iron levels are high, this protein binds to a 4Fe-4S cluster and functions as an aconitase. Aconitases are iron-sulfur proteins that function to catalyze the conversion of citrate to isocitrate. When cellular iron levels are low, the protein binds to iron-responsive elements (IREs), which …

**Accessions** — [HGNC:117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:117) · Entrez [48](https://www.ncbi.nlm.nih.gov/gene/48) · UniProt [P21399](https://www.uniprot.org/uniprotkb/P21399) · Ensembl [ENSG00000122729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122729)

## Data

Gene col 4371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4371); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4371]; `tensor/DDL_lfc|DDL_z.npy` [4371]; `embed/gene_vectors.npy` [4371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4371 or target_col == 4371). Every well: [[ACO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
