---
symbol: "ZDHHC2"
type: "gene"
col: 2428
ensembl_id: "ENSG00000104219"
name: "zDHHC palmitoyltransferase 2"
location: "8p22"
module: 132
arm: "+"
pooled_cpm: 36.42
n_lines_expressing: 40
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# ZDHHC2

*zDHHC palmitoyltransferase 2* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.42× (z +8.1, q 3e-13, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.605× (z -11.5, q 6e-28, down in 25 of 38 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.677× (z -9.0, q 9e-17, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMOD2]] (+0.62, fdr 7e-06), [[SVIP]] (+0.60, fdr 1e-05), [[MTURN]] (+0.57, fdr 1e-05); moves opposite to [[NUP214]] (-0.56, fdr 3e-05), [[TM9SF4]] (-0.52, fdr 3e-05), [[SUPT6H]] (-0.50, fdr 3e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C12orf75]] → it (grade B ⚠); 3 go from it, the strongest it → [[KLHL5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +8.1 | 3e-13 | 24/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +7.5 | 1e-11 | 21/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.6 | 6e-09 | 17/32 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.0 | 7e-05 | 15/35 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +4.7 | 3e-04 | 13/38 (SHP-77, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 0.002 | 10/37 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +4.3 | 0.002 | 10/38 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.009 | 12/37 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.013 | 13/38 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.023 | 4/38 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.039 | 13/37 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.3 | 0.040 | 1/38 (CFPAC-1) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.051 | 4/38 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.053 | 6/37 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.061 | 8/37 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.062 | 5/37 (SW480, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.062 | 9/38 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.071 | 6/38 (A549, Panc 03.27, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.071 | 6/38 (C-33 A, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.100 | 3/36 (CFPAC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.605×** | -11.5 | 6e-28 | 25/38 (A549, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -9.0 | 9e-17 | 25/37 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.700×** | -8.2 | 6e-14 | 24/38 (A-427, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.781×** | -8.0 | 1e-13 | 22/38 (SW 900, AsPC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.727×** | -7.3 | 3e-11 | 21/38 (SW48, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -6.8 | 1e-09 | 20/37 (SW480, HCT15, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -6.7 | 1e-09 | 20/38 (CHP-212, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.603×** | -6.1 | 9e-08 | 19/33 (SW48, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.766×** | -5.9 | 3e-07 | 18/37 (SK-MEL-2, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.782×** | -5.7 | 9e-07 | 20/38 (A-427, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.791×** | -5.4 | 4e-06 | 17/38 (SW48, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **0.797×** | -5.0 | 2e-05 | 17/36 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.804×** | -5.0 | 2e-05 | 13/38 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.9 | 3e-05 | 1/38 (SHP-77) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.681×** | -4.6 | 2e-04 | 16/38 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.794×** | -3.8 | 0.005 | 8/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.796×** | -3.7 | 0.006 | 8/38 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.018 | 9/38 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.756×** | -3.3 | 0.022 | 9/37 (SW480, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.041 | 6/36 (SW 900, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.774×** | -3.1 | 0.048 | 8/37 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.910× | -3.1 | 0.048 | 7/38 (Hs 766T, A-172, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.048 | 6/37 (HCT15, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.830×** | -3.1 | 0.048 | 10/38 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 197 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -20.3) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -11.7) |
| [[A549 (line)]] | wt | 64.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -13.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[Panc 03.27 (line)]] | alt | 59.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 42.3 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.344× (z -12.4) |
| [[A-172 (line)]] | wt | 91.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -15.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.0 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AsPC-1 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -13.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 26.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.02× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 39.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.136× (z -8.9) |
| [[HOP62 (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.05× (z +8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 62.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.492× (z -9.4) ⚠ cell-cycle shift, explains ~56% of this change |
| [[RKO (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW 900 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -15.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 63.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A498 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.90 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD2]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SVIP]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MTURN]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CDH2]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SNX30]] | +0.53 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MCUR1]] ⚠ | +0.53 | +0.46 / +0.51 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLAIN1]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D9]] | +0.52 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[MGAT4A]] | +0.51 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Late SARS-CoV-2 Infection Events |
| [[RALGPS2]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HABP4]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[AKT3]] | +0.51 | +0.51 / +0.46 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[CCDC50]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP214]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[TM9SF4]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SUPT6H]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NAT10]] | -0.50 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[RECQL5]] | -0.50 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SAP30BP]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ACOX3]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[FAM120B]] | -0.49 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[PDCD6]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[RPAP1]] | -0.48 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[USP8]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SLC30A6]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf75]] | B | C12orf75 activity raises ZDHHC2's level | lines that do not express C12orf75 (5) vs lines expressing it (45) | 4.73× lower at baseline in the lines without C12orf75 | 0.060 | ⚠ within organs, on part of the lines; also absent: FKBP7, VAT1, KCNC4 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL5]] | B | ZDHHC2 activity raises KLHL5's level | lines that do not express ZDHHC2 (10) vs lines expressing it (40) | 3.76× lower at baseline in the lines without ZDHHC2 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000289145, TGFB1, PGM5P2 |
| [[TMOD2]] | B | ZDHHC2 activity raises TMOD2's level | lines that do not express ZDHHC2 (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without ZDHHC2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000289145, TGFB1, PGM5P2 |
| [[BEND7]] | B | ZDHHC2 activity raises BEND7's level | lines that do not express ZDHHC2 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without ZDHHC2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ENSG00000289145, TGFB1, PGM5P2 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.283). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.6, -50.3); signed map (46.3, 1.8). **Vector** length 92.4, 21.7% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,156,482-17,224,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF372, DHHC2 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 7 pathways, smallest: Surfactant metabolism; Maturation of spike protein_9694548; Translation of Structural Proteins_9694635 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIJ5](https://www.uniprot.org/uniprotkb/Q9UIJ5) (Palmitoyltransferase ZDHHC2):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates and is involved in a variety of cellular processes. Has no stringent fatty acid selectivity and in addition to palmitate can also transfer onto target proteins myristate from tetradecanoyl-CoA and stearate from octadecanoyl-CoA (By similarity). In the nervous system, plays a role in long term synaptic potentiation by palmitoylating AKAP5 through which it regulates protein trafficking from the dendritic …

**Summary**, from NCBI Gene [51201](https://www.ncbi.nlm.nih.gov/gene/51201):

> Enables protein homodimerization activity and protein-cysteine S-palmitoyltransferase activity. Involved in several processes, including peptidyl-L-cysteine S-palmitoylation; protein localization to membrane raft; and synapse assembly. Located in Golgi apparatus; endoplasmic reticulum membrane; and plasma membrane. Is active in postsynaptic recycling endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18469) · Entrez [51201](https://www.ncbi.nlm.nih.gov/gene/51201) · UniProt [Q9UIJ5](https://www.uniprot.org/uniprotkb/Q9UIJ5) · Ensembl [ENSG00000104219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104219)

## Data

Gene col 2428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2428); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2428]; `tensor/DDL_lfc|DDL_z.npy` [2428]; `embed/gene_vectors.npy` [2428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2428 or target_col == 2428). Every well: [[ZDHHC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
