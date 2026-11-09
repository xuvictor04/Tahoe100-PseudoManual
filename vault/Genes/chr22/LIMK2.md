---
symbol: "LIMK2"
type: "gene"
col: 11297
ensembl_id: "ENSG00000182541"
name: "LIM domain kinase 2"
location: "22q12.2"
module: 19
arm: "+"
pooled_cpm: 35.85
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LIMK2

*LIM domain kinase 2* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +25.5, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.524× (z -15.3, q 0e+00, down in 31 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.213×, A498 0.290×, Hs 766T 0.236×, A-427 0.239×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.0539×, SNU-423 0.210×, A498 0.302×, J82 0.307×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.251×, NCI-H460 0.247×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.199×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.178×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H460 0.485×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAX7]] (+0.41, fdr 8e-05), [[EBLN2]] (+0.41, fdr 1e-04), [[CAVIN2-AS1]] (+0.40, fdr 1e-04); moves opposite to [[ASPH]] (-0.44, fdr 5e-05), [[MTFR1]] (-0.41, fdr 1e-04), [[HDLBP]] (-0.37, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLA2G2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +25.5 | 0e+00 | 39/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +10.6 | 9e-24 | 35/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +10.4 | 5e-23 | 32/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +9.9 | 4e-21 | 35/48 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.6 | 3e-12 | 26/47 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +7.0 | 3e-10 | 22/48 (C32, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +6.9 | 4e-10 | 21/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +5.3 | 9e-06 | 21/46 (A498, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +5.2 | 1e-05 | 18/47 (C32, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +5.1 | 2e-05 | 20/48 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.15× | +4.8 | 9e-05 | 18/47 (C32, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.23×** | +4.7 | 1e-04 | 15/44 (SW480, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +4.3 | 9e-04 | 12/49 (HEC-1-A, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +4.1 | 0.002 | 19/47 (LoVo, A549, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.1 | 0.002 | 1/49 (NCI-H1792) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.002 | 14/48 (A498, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.9 | 0.003 | 8/48 (LoVo, Hs 766T, …) | all doses, flat |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.13× | +3.8 | 0.004 | 5/48 (SW480, C32, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.004 | 10/47 (LoVo, Hs 766T, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.011 | 15/47 (LoVo, Hs 766T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.014 | 8/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11297.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.213×, A498 0.290×, Hs 766T 0.236×, A-427 0.239×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LS 180 0.0539×, SNU-423 0.210×, A498 0.302×, J82 0.307×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.251×, NCI-H460 0.247×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.199×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.178×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (NCI-H460 0.485×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.524×** | -15.3 | 0e+00 | 31/43 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -10.9 | 2e-25 | 23/35 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.638×** | -9.9 | 1e-20 | 25/39 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.862× | -3.6 | 0.051 | 11/48 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.5 | 0.051 | 18/48 (Hs 766T, SW1417, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.770×** | -3.3 | 0.095 | 13/46 (J82, A549, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.873× | -3.2 | 0.095 | 10/48 (NCI-H1792, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.485× (z -8.8) |
| [[HS-578T (line)]] | alt | 31.8 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +15.7) | [[Lonafarnib (drug)]] 5 µM 0.122× (z -9.2) ⚠ toxic |
| [[A498 (line)]] | wt | 40.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.4) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -12.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 31.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 29.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 32.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -16.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +20.8) | — |
| [[SNU-423 (line)]] | alt | 31.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 32.5 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 24.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.44× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.5) | — |
| [[A-172 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 44.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.75× (z +10.2) | — |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.178× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -11.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 94.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0539× (z -24.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX7]] | +0.41 | +0.38 / +0.37 | both halves | 8e-05 |  |
| [[EBLN2]] | +0.41 | +0.37 / +0.34 | both halves | 1e-04 |  |
| [[CAVIN2-AS1]] | +0.40 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[IKBKE]] | +0.40 | +0.53 / +0.29 | both halves | 2e-04 |  |
| [[ZNF670]] | +0.40 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[MTF2]] | +0.39 | +0.20 / +0.46 | both halves | 7e-04 |  |
| [[TYK2]] | +0.39 | +0.45 / +0.31 | both halves | 2e-04 |  |
| [[SLC15A5]] | +0.39 | +0.35 / +0.33 | both halves | 1e-04 |  |
| [[NLGN4Y]] | +0.38 | +0.47 / +0.24 | both halves | 5e-04 |  |
| [[STAP2]] | +0.38 | +0.48 / +0.28 | both halves | 3e-04 |  |
| [[BIK]] | +0.38 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[IL4I1]] | +0.38 | +0.47 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPH]] | -0.44 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[MTFR1]] | -0.41 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[HDLBP]] | -0.37 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[BPNT2]] | -0.36 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[MAP1B]] | -0.36 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[ABCB8]] | -0.36 | -0.36 / -0.26 | both halves | 4e-04 |  |
| [[STYX]] | -0.36 | -0.11 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[CLTC]] | -0.36 | -0.44 / -0.31 | both halves | 2e-04 | pathway: EPH-Ephrin signaling |
| [[GOLGA3]] | -0.35 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[HAPSTR1]] | -0.35 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PITRM1]] | -0.35 | -0.24 / -0.34 | both halves | 5e-04 |  |
| [[CLNS1A]] | -0.35 | -0.28 / -0.31 | both halves | 3e-04 |  |
| [[TXNDC5]] | -0.35 | -0.39 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2G2A]] | B | PLA2G2A activity raises LIMK2's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 1.71× lower at baseline in the lines without PLA2G2A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1 |
| [[BIK]] | B | BIK activity strengthens LIMK2's drug response | lines that do not express BIK (15) vs lines expressing it (33) | the lines without BIK respond 0.96× as strongly (z diff +0.08); strongest at Belinostat 5 µM: 1.29x vs 1.69x (z diff +2.0) | 0.072 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.260). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.1, 55.6); signed map (45.0, 3.7). **Vector** length 83.8, 16.6% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +25.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +7.0 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.1 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.5 | -15.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,212,239-31,280,080 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing; LIMK/TESK kinase family |
| Reactome | 11 pathways, smallest: RHO GTPases Activate ROCKs; Sema4D induced cell migration and growth-cone collapse; Sema4D in semaphorin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P53671](https://www.uniprot.org/uniprotkb/P53671) (LIM domain kinase 2):

> Serine/threonine-protein kinase that plays an essential role in the regulation of actin filament dynamics. Acts downstream of several Rho family GTPase signal transduction pathways. Involved in astral microtubule organization and mitotic spindle orientation during early stages of mitosis by mediating phosphorylation of TPPP. Displays serine/threonine-specific phosphorylation of myelin basic protein and histone (MBP) in vitro. Suppresses ciliogenesis via multiple pathways; phosphorylation of …

**Summary**, from NCBI Gene [3985](https://www.ncbi.nlm.nih.gov/gene/3985):

> There are approximately 40 known eukaryotic LIM proteins, so named for the LIM domains they contain. LIM domains are highly conserved cysteine-rich structures containing 2 zinc fingers. Although zinc fingers usually function by binding to DNA or RNA, the LIM motif probably mediates protein-protein interactions. LIM kinase-1 and LIM kinase-2 belong to a small subfamily with a unique combination of 2 N-terminal LIM motifs and a C-terminal protein kinase domain. The protein encoded by this gene is …

**Accessions** — [HGNC:6614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6614) · Entrez [3985](https://www.ncbi.nlm.nih.gov/gene/3985) · UniProt [P53671](https://www.uniprot.org/uniprotkb/P53671) · Ensembl [ENSG00000182541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182541)

## Data

Gene col 11297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11297); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11297]; `tensor/DDL_lfc|DDL_z.npy` [11297]; `embed/gene_vectors.npy` [11297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11297 or target_col == 11297). Every well: [[LIMK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
