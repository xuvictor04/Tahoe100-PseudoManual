---
symbol: "ARMC9"
type: "gene"
col: 5783
ensembl_id: "ENSG00000135931"
name: "armadillo repeat containing 9"
location: "2q37.1"
module: 23
arm: "-"
pooled_cpm: 63.74
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ARMC9

*armadillo repeat containing 9* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.76× (z +27.2, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -16.0, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMERB1]] (+0.57, fdr 4e-05), [[GNA12]] (+0.56, fdr 1e-04), [[CLIP2]] (+0.55, fdr 4e-05); moves opposite to [[C12orf60]] (-0.60, fdr 8e-05), [[SEPTIN7-DT]] (-0.56, fdr 1e-04), [[NECTIN3-AS1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.76×** | +27.2 | 0e+00 | 47/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.44×** | +23.9 | 0e+00 | 45/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +23.6 | 0e+00 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +11.6 | 5e-29 | 38/47 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +8.9 | 5e-17 | 31/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +7.6 | 3e-12 | 31/47 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +6.1 | 7e-08 | 24/47 (RPMI-7951, NCI-H1573, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +6.0 | 1e-07 | 25/47 (HT-29, A-172, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.38×** | +4.5 | 4e-04 | 13/47 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.19× | +4.4 | 6e-04 | 11/47 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.17× | +4.2 | 0.001 | 15/47 (HEC-1-A, hTERT-HPNE, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.1 | 0.002 | 20/47 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.16× | +3.9 | 0.004 | 9/47 (A-427, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.15× | +3.8 | 0.007 | 17/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.011 | 5/47 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +3.5 | 0.015 | 7/47 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.027 | 7/47 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.034 | 7/47 (A549, BT-474, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 5 µM |  | 1.13× | +3.3 | 0.034 | 8/47 (NCI-H1792, A498, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.056 | 6/47 (RKO, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -16.0 | 0e+00 | 36/47 (SNU-423, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -8.1 | 1e-13 | 28/48 (HT-29, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -6.5 | 2e-08 | 25/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.793×** | -6.2 | 7e-08 | 23/47 (SW 900, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.833×** | -6.2 | 7e-08 | 22/47 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -6.1 | 1e-07 | 23/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.653×** | -6.0 | 2e-07 | 19/35 (A-172, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.816×** | -5.5 | 3e-06 | 22/47 (LoVo, HT-29, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.810×** | -5.4 | 3e-06 | 18/47 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.831×** | -5.0 | 4e-05 | 20/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.829×** | -4.7 | 2e-04 | 21/44 (NCI-H1792, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.726×** | -4.5 | 3e-04 | 19/47 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -4.1 | 0.002 | 13/47 (A549, A498, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | 0.856× | -4.0 | 0.003 | 14/47 (HOP62, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.864× | -3.9 | 0.003 | 20/46 (SW480, SW 900, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.909× | -3.7 | 0.008 | 14/47 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.865× | -3.6 | 0.010 | 18/46 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.871× | -3.6 | 0.010 | 16/46 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.894× | -3.5 | 0.014 | 15/47 (HOP62, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.882× | -3.4 | 0.020 | 15/46 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.901× | -3.1 | 0.044 | 15/47 (HOP62, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 123 | 3 | 11 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -11.5) |
| [[C32 (line)]] | wt | 66.6 | 7 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 0.5 µM 4.11× (z +11.8) | — |
| [[LoVo (line)]] | wt | 51.9 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.238× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 117 | 0 | 7 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.637× (z -18.0) ⚠ position not correctable · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.5) |
| [[HT-29 (line)]] | alt | 40.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.45× (z +13.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -10.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 56.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +12.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.5) |
| [[PANC-1 (line)]] | alt | 76.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.0) |
| [[SW480 (line)]] | alt | 70.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 78.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.0) | [[Lonafarnib (drug)]] 5 µM 0.186× (z -10.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 59.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -12.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 49.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.59× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 22.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.54× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.204× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 46.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.35× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 51.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 128 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 35.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 55.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 31.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.11× (z +12.0) | — |
| [[J82 (line)]] | alt | 26.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[KATO III (line)]] | alt | 34.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 28.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.03× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 116 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.27× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 37.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +17.3) | — |
| [[RKO (line)]] | wt | 72.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -19.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.5) |
| [[SW 900 (line)]] | alt | 151 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.319× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 29.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +12.9) | — |
| [[A498 (line)]] | wt | 89.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 49.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.46× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.2) |
| [[HS-578T (line)]] | alt | 79.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +8.5) | [[Lonafarnib (drug)]] 5 µM 0.183× (z -9.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 60.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 79.2 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -12.4) |
| [[H4 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 83.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 36.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 122 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 42.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.80× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 89.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.9) |
| [[AN3 CA (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMERB1]] | +0.57 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[GNA12]] | +0.56 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[CLIP2]] | +0.55 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[GGA1]] | +0.54 | +0.38 / +0.34 | both halves | 1e-04 |  |
| [[TUSC3]] | +0.53 | +0.53 / +0.49 | both halves | 2e-05 |  |
| [[C2CD2]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ABAT]] | +0.52 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[ACP7]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[RNF168]] | +0.51 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[PBX4]] | +0.51 | +0.38 / +0.27 | both halves | 3e-04 |  |
| [[PI4K2A]] | +0.51 | +0.47 / +0.27 | both halves | 3e-04 |  |
| [[ARHGEF4]] | +0.50 | +0.45 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf60]] | -0.60 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[SEPTIN7-DT]] | -0.56 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[NECTIN3-AS1]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SENP8]] | -0.55 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[PPP2R3C]] | -0.54 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[DDX59]] | -0.54 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.54 | -0.42 / -0.21 | both halves | 7e-04 |  |
| [[UBR5]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ERCC6L2-AS1]] | -0.52 | -0.36 / -0.23 | both halves | 5e-04 |  |
| [[F8]] | -0.52 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[DERA]] | -0.52 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[PUS10]] | -0.51 | -0.48 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ARMC9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (1.9, 14.5); signed map (-1.5, 55.5). **Vector** length 117, 31.3% of its response variance represented; |z| ≥ 3 in 1,537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.2 | +23.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +27.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +23.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.7 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +4.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +7.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.4 | -16.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.0 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,198,546-231,376,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12584, KIAA1868, ARM, KU-MEL-1 |
| Gene groups (HGNC) | Armadillo repeat containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3E5](https://www.uniprot.org/uniprotkb/Q7Z3E5) (LisH domain-containing protein ARMC9):

> Involved in ciliogenesis. It is required for appropriate acetylation and polyglutamylation of ciliary microtubules, and regulation of cilium length. Acts as a positive regulator of hedgehog (Hh)signaling (By similarity). May participate in the trafficking and/or retention of GLI2 and GLI3 proteins at the ciliary tip (By similarity).

**Summary**, from NCBI Gene [80210](https://www.ncbi.nlm.nih.gov/gene/80210):

> Enables identical protein binding activity. Predicted to be involved in cilium assembly and positive regulation of smoothened signaling pathway. Located in centriole and ciliary basal body. Implicated in Joubert syndrome 30. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20730) · Entrez [80210](https://www.ncbi.nlm.nih.gov/gene/80210) · UniProt [Q7Z3E5](https://www.uniprot.org/uniprotkb/Q7Z3E5) · Ensembl [ENSG00000135931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135931)

## Data

Gene col 5783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5783); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5783]; `tensor/DDL_lfc|DDL_z.npy` [5783]; `embed/gene_vectors.npy` [5783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5783 or target_col == 5783). Every well: [[ARMC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
