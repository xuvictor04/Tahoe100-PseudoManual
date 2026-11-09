---
symbol: "RTCA"
type: "gene"
col: 6105
ensembl_id: "ENSG00000137996"
name: "RNA 3'-terminal phosphate cyclase"
location: "1p21.2"
module: 171
arm: "+"
pooled_cpm: 43.77
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# RTCA

*RNA 3'-terminal phosphate cyclase* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +11.0, q 2e-25, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -21.4, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX4]] (+0.77, fdr 7e-06), [[OTULIN]] (+0.73, fdr 7e-06), [[MINDY3]] (+0.73, fdr 7e-06); moves opposite to [[PFN1]] (-0.63, fdr 2e-05), [[SKIL]] (-0.63, fdr 1e-05), [[DPH1-AS1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +11.0 | 2e-25 | 44/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +10.5 | 2e-23 | 43/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +9.8 | 2e-20 | 43/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +5.8 | 8e-07 | 28/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.23×** | +5.4 | 9e-06 | 25/48 (RKO, C32, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +5.1 | 3e-05 | 24/48 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.2 | 0.002 | 21/44 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.013 | 17/48 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.022 | 15/48 (A-427, NCI-H460, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.034 | 15/48 (RKO, AsPC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.045 | 12/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.052 | 14/48 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +3.2 | 0.052 | 18/48 (SW48, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.054 | 10/48 (BT-474, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -21.4 | 0e+00 | 42/48 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -12.7 | 1e-34 | 42/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -11.9 | 4e-30 | 40/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.541×** | -11.4 | 8e-28 | 39/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -10.6 | 3e-24 | 36/48 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -10.2 | 2e-22 | 35/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.603×** | -9.4 | 6e-19 | 37/48 (A-172, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.720×** | -6.1 | 8e-08 | 26/48 (AsPC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.723×** | -6.0 | 1e-07 | 30/48 (AsPC-1, NCI-H1573, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.748×** | -5.4 | 4e-06 | 25/48 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -5.2 | 1e-05 | 24/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.0 | 3e-05 | 24/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -4.4 | 6e-04 | 20/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.3 | 6e-04 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.797×** | -4.2 | 1e-03 | 20/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.871× | -3.6 | 0.009 | 13/48 (KATO III, AsPC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.840× | -3.2 | 0.034 | 15/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.729×** | -3.1 | 0.056 | 14/48 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.849× | -3.0 | 0.059 | 11/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.065 | 5/48 (LS 180, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 37.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 55.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -18.6) |
| [[PANC-1 (line)]] | alt | 28.2 | 3 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 3.04× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.9) |
| [[HS-578T (line)]] | alt | 58.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 56.8 | 1 | 4 | [[Bortezomib (drug)]] 0.05 µM 3.14× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.2) |
| [[A498 (line)]] | wt | 56.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -17.1) |
| [[Hs 766T (line)]] | wt | 68.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -12.2) |
| [[SW480 (line)]] | alt | 45.3 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.466× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.477× (z -9.2) |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 34.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -17.2) |
| [[SHP-77 (line)]] | alt | 47.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.8) |
| [[C32 (line)]] | wt | 41.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 49.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 40.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.0) |
| [[J82 (line)]] | alt | 52.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.7) |
| [[LoVo (line)]] | wt | 37.8 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 46.6 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.9) |
| [[LS 180 (line)]] | wt | 71.1 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.248× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 64.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.2) |
| [[A-427 (line)]] | wt | 25.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +8.6) | — |
| [[A549 (line)]] | wt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.2) |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[HCT15 (line)]] | alt | 55.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.6) |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.3) |
| [[RKO (line)]] | wt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.4) |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.1) |
| [[SNU-423 (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.8) |
| [[SW 900 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.8) |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX4]] | +0.77 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[OTULIN]] | +0.73 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[RAB18]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[SAMM50]] | +0.71 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[ZW10]] | +0.70 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.70 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[MKRN2]] | +0.69 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[VPS33B]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CDC40]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[TENT2]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.63 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[SKIL]] | -0.63 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.61 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.60 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[HES1]] | -0.60 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[NR4A3]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[THOC6]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[JUNB]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.803). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-4.6, -11.4); signed map (-31.9, -12.2). **Vector** length 120, 34.8% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.8 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +9.7 | +5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +10.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.6 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.6 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.9 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.6 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -21.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.0 | -3.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA 3'-terminal phosphate cyclase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,266,216-100,292,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPC, RTC1; previously RTCD1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O00442](https://www.uniprot.org/uniprotkb/O00442) (RNA 3'-terminal phosphate cyclase):

> Catalyzes the conversion of 3'-phosphate to a 2',3'-cyclic phosphodiester at the end of RNA. The mechanism of action of the enzyme occurs in 3 steps: (A) adenylation of the enzyme by ATP; (B) transfer of adenylate to an RNA-N3'P to produce RNA-N3'PP5'A; (C) and attack of the adjacent 2'-hydroxyl on the 3'-phosphorus in the diester linkage to produce the cyclic end product. Likely functions in some aspects of cellular RNA processing. Function plays an important role in regulating axon …

**Summary**, from NCBI Gene [8634](https://www.ncbi.nlm.nih.gov/gene/8634):

> This gene encodes a member of the RNA 3'-phosphate cyclase family. The encoded protein plays a role in RNA metabolism by catalyzing the ATP-dependent conversion of the 3'-phosphate of RNA substrates to a 2',3'-cyclic phosphodiester. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:17981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17981) · Entrez [8634](https://www.ncbi.nlm.nih.gov/gene/8634) · UniProt [O00442](https://www.uniprot.org/uniprotkb/O00442) · Ensembl [ENSG00000137996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137996)

## Data

Gene col 6105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6105); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6105]; `tensor/DDL_lfc|DDL_z.npy` [6105]; `embed/gene_vectors.npy` [6105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6105 or target_col == 6105). Every well: [[RTCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
