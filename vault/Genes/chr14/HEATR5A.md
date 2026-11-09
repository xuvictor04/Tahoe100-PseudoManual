---
symbol: "HEATR5A"
type: "gene"
col: 4980
ensembl_id: "ENSG00000129493"
name: "HEAT repeat containing 5A"
location: "14q12"
module: 56
arm: "+"
pooled_cpm: 71.63
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# HEATR5A

*HEAT repeat containing 5A* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.86× (z +11.3, q 6e-27, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.248× (z -13.2, q 3e-37, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WIPI1]] (+0.63, fdr 2e-05), [[SLC30A5]] (+0.62, fdr 1e-05), [[LARP1B]] (+0.62, fdr 7e-06); moves opposite to [[TEX9]] (-0.53, fdr 4e-04), [[ZNF780A]] (-0.52, fdr 4e-04), [[PAFAH2]] (-0.49, fdr 6e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PPP1R3B-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +11.3 | 6e-27 | 42/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +10.0 | 3e-21 | 38/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +9.8 | 3e-20 | 43/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +9.3 | 2e-18 | 39/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.6 | 8e-16 | 34/49 (SHP-77, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.4 | 1e-08 | 31/50 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 3e-05 | 29/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +4.8 | 1e-04 | 27/49 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.6 | 2e-04 | 23/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.28×** | +4.5 | 3e-04 | 23/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +4.2 | 0.001 | 24/48 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.24×** | +3.7 | 0.010 | 22/47 (CFPAC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.019 | 11/49 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.021 | 14/48 (LOX-IMVI, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.025 | 20/48 (SW480, CFPAC-1, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.248×** | -13.2 | 3e-37 | 48/49 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -12.8 | 5e-35 | 38/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.277×** | -12.2 | 8e-32 | 40/48 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.536×** | -11.3 | 2e-27 | 34/48 (PANC-1, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.605×** | -9.1 | 8e-18 | 33/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.640×** | -8.1 | 6e-14 | 29/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -8.0 | 7e-14 | 34/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -6.5 | 5e-09 | 27/45 (LoVo, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.703×** | -6.4 | 1e-08 | 31/49 (A-427, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.696×** | -6.3 | 1e-08 | 26/48 (HS-578T, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -6.0 | 1e-07 | 30/48 (HS-578T, A549, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.553×** | -5.6 | 9e-07 | 22/37 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.743×** | -5.0 | 3e-05 | 29/47 (HOP62, AN3 CA, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.752×** | -5.0 | 3e-05 | 24/43 (NCI-H1573, KATO III, …) | all doses, flat | composition shift |
| [[Radotinib (drug)]] 5 µM |  | 0.836× | -4.6 | 2e-04 | 22/48 (PANC-1, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -4.5 | 3e-04 | 25/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -4.1 | 0.001 | 24/48 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.014 | 18/49 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.835× | -3.3 | 0.028 | 20/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.048 | 15/48 (PANC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 90.8 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.202× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.169× (z -11.0) |
| [[SW480 (line)]] | alt | 61.6 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 78.5 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.171× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 29.0 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 53.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 68.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.317× (z -11.8) |
| [[PANC-1 (line)]] | alt | 62.6 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -17.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.188× (z -11.6) |
| [[J82 (line)]] | alt | 53.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.249× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.346× (z -10.6) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.145× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 73.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 62.0 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0567× (z -14.1) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 75.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 91.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -11.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 61.5 | 1 | 2 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.312× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.111× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 96.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -9.7) |
| [[A-172 (line)]] | wt | 45.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.308× (z -9.4) |
| [[A549 (line)]] | wt | 60.9 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.365× (z -9.0) |
| [[H4 (line)]] | wt | 65.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 44.1 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -9.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LS 180 (line)]] | wt | 83.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.36× (z +8.6) | [[TAK-901 (drug)]] 5 µM 0.183× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 72.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 55.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.285× (z -10.0) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SNU-1 (line)]] | wt | 53.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0742× (z -8.8) |
| [[SNU-423 (line)]] | alt | 40.8 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 68.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A498 (line)]] | wt | 72.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.359× (z -9.8) |
| [[BT-474 (line)]] | alt | 123 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.171× (z -8.6) |
| [[C-33 A (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[C32 (line)]] | wt | 66.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0664× (z -11.3) |
| [[COLO 205 (line)]] | alt | 40.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 83.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0845× (z -22.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 63.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.6) | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0706× (z -9.0) |
| [[SW48 (line)]] | wt | 78.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPI1]] | +0.63 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[SLC30A5]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[LARP1B]] | +0.62 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[NPIPB14P]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[KDELR2]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[FAM177A1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ARFGAP3]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SELENOS]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ERLEC1]] | +0.56 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[NDEL1]] | +0.56 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[TMEM165]] | +0.55 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[PDXDC2P-NPIPB14P]] | +0.55 | +0.39 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX9]] | -0.53 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[ZNF780A]] | -0.52 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[PAFAH2]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[CHIC1]] | -0.49 | -0.38 / -0.50 | both halves | 6e-05 | same gene group |
| [[CYB5RL]] | -0.49 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[DNAH7]] | -0.49 | -0.21 / -0.42 | both halves | 6e-04 |  |
| [[TTC5]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TTC30A]] | -0.48 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[NEK6]] | -0.48 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[VPS11]] | -0.48 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TGFBRAP1]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ACBD6]] | -0.46 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R3B-DT]] | B | PPP1R3B-DT activity lowers HEATR5A's level | lines that do not express PPP1R3B-DT (5) vs lines expressing it (45) | 1.17× higher at baseline in the lines without PPP1R3B-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: KNDC1; maybe low, not absent; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers HEATR5A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.4, -37.4); signed map (-48.2, 13.3). **Vector** length 110, 34.3% of its response variance represented; |z| ≥ 3 in 1,314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.4 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +1.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +0.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.1 | -13.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | +0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | HEAT repeat containing 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:31,291,788-31,420,550 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434I1735, p200b; previously C14orf125 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q86XA9](https://www.uniprot.org/uniprotkb/Q86XA9) carries no function annotation.

**Summary**, from NCBI Gene [25938](https://www.ncbi.nlm.nih.gov/gene/25938):

> Predicted to be involved in endocytosis; intracellular protein localization; and retrograde transport, endosome to Golgi. Predicted to be located in cytosol. Predicted to be active in Golgi apparatus and endocytic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20276) · Entrez [25938](https://www.ncbi.nlm.nih.gov/gene/25938) · UniProt [Q86XA9](https://www.uniprot.org/uniprotkb/Q86XA9) · Ensembl [ENSG00000129493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129493)

## Data

Gene col 4980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4980); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4980]; `tensor/DDL_lfc|DDL_z.npy` [4980]; `embed/gene_vectors.npy` [4980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4980 or target_col == 4980). Every well: [[HEATR5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEATR5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
