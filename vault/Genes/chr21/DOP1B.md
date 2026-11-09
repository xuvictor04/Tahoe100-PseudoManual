---
symbol: "DOP1B"
type: "gene"
col: 6606
ensembl_id: "ENSG00000142197"
name: "DOP1 leucine zipper like protein B"
location: "21q22.12"
module: 2
arm: "+"
pooled_cpm: 43.37
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DOP1B

*DOP1 leucine zipper like protein B* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.95× (z +27.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.344× (z -12.3, q 7e-32, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKZ]] (+0.62, fdr 1e-05), [[PACS2]] (+0.61, fdr 3e-05), [[PIP4K2A]] (+0.60, fdr 2e-05); moves opposite to [[RAE1]] (-0.57, fdr 4e-05), [[ZNF304]] (-0.56, fdr 4e-05), [[PNISR-AS1]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +27.4 | 0e+00 | 47/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +25.8 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +22.8 | 0e+00 | 46/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +9.8 | 2e-20 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +8.0 | 2e-13 | 28/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +7.8 | 8e-13 | 23/49 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +7.6 | 3e-12 | 27/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +7.5 | 4e-12 | 30/49 (SW480, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +7.2 | 3e-11 | 28/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +7.1 | 6e-11 | 30/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +7.1 | 6e-11 | 24/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.9 | 2e-10 | 27/48 (C32, SW480, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +6.7 | 1e-09 | 26/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +6.4 | 8e-09 | 18/48 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +6.2 | 2e-08 | 22/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +5.7 | 4e-07 | 21/47 (SW480, LS 180, …) | two highest doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.60×** | +5.4 | 2e-06 | 19/48 (SW480, A-172, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -12.3 | 7e-32 | 41/49 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.761×** | -9.8 | 3e-20 | 31/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -9.7 | 5e-20 | 30/48 (RKO, SNU-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -8.6 | 2e-15 | 28/48 (LOX-IMVI, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.805×** | -5.2 | 2e-05 | 17/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.815×** | -5.0 | 6e-05 | 21/48 (A-172, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.828×** | -4.8 | 1e-04 | 18/45 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **0.680×** | -4.4 | 6e-04 | 14/46 (SW48, HCT15, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -4.3 | 0.001 | 4/49 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.849× | -3.9 | 0.007 | 14/47 (Panc 03.27, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.860× | -3.8 | 0.007 | 16/47 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.870× | -3.5 | 0.020 | 16/47 (HS-578T, Panc 03.27, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.5 | 0.023 | 14/48 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.864× | -3.4 | 0.023 | 16/46 (NCI-H1573, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.869× | -3.4 | 0.023 | 14/49 (Panc 03.27, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.045 | 14/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Econazole (drug)]] 5 µM |  | 0.889× | -3.0 | 0.083 | 12/48 (NCI-H1573, A498, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.891× | -2.9 | 0.097 | 9/48 (SW48, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 42.9 | 7 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.05× (z +19.7) | [[TAK-901 (drug)]] 5 µM 0.221× (z -9.6) |
| [[A-172 (line)]] | wt | 67.4 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.90× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.462× (z -11.7) |
| [[PANC-1 (line)]] | alt | 37.0 | 3 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 45.6 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +11.0) | [[TAK-901 (drug)]] 5 µM 0.104× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 91.2 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.5) | [[Selinexor (drug)]] 5 µM 0.461× (z -13.3) |
| [[SW1417 (line)]] | alt | 86.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 48.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.482× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 41.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.69× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 55.4 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 26.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.31× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 25.9 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.317× (z -11.1) |
| [[LoVo (line)]] | wt | 44.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 54.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 42.4 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.87× (z +11.6) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.316× (z -9.9) |
| [[SHP-77 (line)]] | alt | 47.8 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.54× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.75× (z +9.0) | — |
| [[A498 (line)]] | wt | 27.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 24.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.09× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 51.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.97× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[HS-578T (line)]] | alt | 48.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 42.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.4) | [[Lonafarnib (drug)]] 5 µM 0.129× (z -9.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.42× (z +10.4) | — |
| [[KATO III (line)]] | alt | 15.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.54× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 51.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.10× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 29.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.3) | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.305× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.297× (z -9.9) |
| [[SNU-423 (line)]] | alt | 38.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.75× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 29.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.16× (z +9.0) | — |
| [[A549 (line)]] | wt | 28.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 37.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.59× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 23.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +10.7) | — |
| [[SW48 (line)]] | wt | 85.7 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.310× (z -9.3) |
| [[AN3 CA (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 65.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 39.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +8.5) | — |
| [[H4 (line)]] | wt | 17.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.18× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.229× (z -10.0) |
| [[BT-474 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKZ]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PACS2]] | +0.61 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[PIP4K2A]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[EPS15]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CBL]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[LIMK1]] | +0.59 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SPIRE1]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CORO7]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PLCG2]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[STX2]] | +0.58 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[RALGPS1]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[INPP4A]] | +0.58 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAE1]] | -0.57 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ZNF304]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PNISR-AS1]] | -0.55 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[RBM7]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[YTHDF3]] | -0.53 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[KLHL3]] | -0.53 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[RPRD1B]] | -0.53 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TNS2]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[JPH2]] | -0.53 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[SMG8]] | -0.52 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[HMG20A]] | -0.50 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[PRR3]] | -0.50 | -0.32 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (1.4, 2.7); signed map (-44.1, -7.5). **Vector** length 118, 32.2% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.2 | +22.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +27.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +25.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.9 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.8 | +7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.7 | +6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +8.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.2 | +6.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.9 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.9 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -9.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -2.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | DOP1 leucine zipper like protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:36,156,782-36,294,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0933; previously C21orf5, DOPEY2 |
| Gene groups (HGNC) | DOP1 leucine zipper like protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3R5](https://www.uniprot.org/uniprotkb/Q9Y3R5) (Protein DOP1B):

> May play a role in regulating membrane trafficking of cargo proteins. Together with ATP9A and MON2, regulates SNX3 retromer-mediated endosomal sorting of WLS away from lysosomal degradation.

**Summary**, from NCBI Gene [9980](https://www.ncbi.nlm.nih.gov/gene/9980):

> Involved in cognition and embryonic pattern specification. Located in early endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1291) · Entrez [9980](https://www.ncbi.nlm.nih.gov/gene/9980) · UniProt [Q9Y3R5](https://www.uniprot.org/uniprotkb/Q9Y3R5) · Ensembl [ENSG00000142197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142197)

## Data

Gene col 6606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6606); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6606]; `tensor/DDL_lfc|DDL_z.npy` [6606]; `embed/gene_vectors.npy` [6606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6606 or target_col == 6606). Every well: [[DOP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
