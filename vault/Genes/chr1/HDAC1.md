---
symbol: "HDAC1"
type: "gene"
col: 3798
ensembl_id: "ENSG00000116478"
name: "histone deacetylase 1"
location: "1p35.2-p35.1"
module: 11
arm: "-"
pooled_cpm: 54.07
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 599
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# HDAC1

*histone deacetylase 1* — 1p35.2-p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +24.8, q 0e+00, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.56× (z +10.2, q 4e-22, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.652× (z -13.8, q 3e-40, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLSTN1]] (+0.71, fdr 7e-06), [[GUSB]] (+0.67, fdr 1e-05), [[NUDT21]] (+0.66, fdr 1e-05); moves opposite to [[PBDC1]] (-0.69, fdr 1e-05), [[RPP38]] (-0.69, fdr 1e-05), [[TRIP11]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SOAT1]] → it (grade C ⚠); 599 go from it, the strongest it → [[CDC23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +24.8 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +23.3 | 0e+00 | 38/38 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +15.3 | 0e+00 | 41/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +10.2 | 4e-22 | 39/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +9.0 | 3e-17 | 36/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.7 | 3e-16 | 36/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +8.6 | 8e-16 | 35/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +7.6 | 2e-12 | 29/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.8 | 6e-10 | 31/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +5.5 | 2e-06 | 24/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 1e-05 | 29/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.25×** | +5.1 | 2e-05 | 22/48 (SW480, SW1417, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.20×** | +4.0 | 0.003 | 22/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.9 | 0.005 | 14/34 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +3.6 | 0.010 | 15/47 (RKO, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.17× | +3.6 | 0.011 | 12/48 (HS-578T, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.036 | 8/49 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3798.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.652×** | -13.8 | 3e-40 | 37/48 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -12.1 | 4e-31 | 33/47 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -11.8 | 1e-29 | 39/48 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.754×** | -6.2 | 9e-08 | 27/48 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.773×** | -5.9 | 5e-07 | 28/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.795×** | -5.2 | 2e-05 | 22/48 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.7 | 2e-04 | 23/48 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.7 | 0.015 | 19/49 (SW 900, COLO 205, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.852× | -3.7 | 0.016 | 19/48 (LOX-IMVI, H4, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.908× | -3.1 | 0.100 | 13/48 (HOP62, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 77.2 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.6) |
| [[LoVo (line)]] | wt | 60.9 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +14.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -14.1) |
| [[A-427 (line)]] | wt | 50.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0857× (z -22.8) |
| [[SW480 (line)]] | alt | 75.2 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +15.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -10.7) |
| [[A-172 (line)]] | wt | 33.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.6) |
| [[HS-578T (line)]] | alt | 68.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.7) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 79.1 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.81× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.3) |
| [[SNU-423 (line)]] | alt | 66.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.1) |
| [[SW 900 (line)]] | alt | 59.4 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 59.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 60.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +14.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 55.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.0) |
| [[HT-29 (line)]] | alt | 84.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 39.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.1) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.4) |
| [[KATO III (line)]] | alt | 71.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +13.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 96.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 39.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +11.4) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.120× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 52.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -13.0) |
| [[PANC-1 (line)]] | alt | 58.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +20.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 25.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 46.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 34.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -8.7) |
| [[HCT15 (line)]] | alt | 79.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.7) |
| [[J82 (line)]] | alt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +12.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 49.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 25.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 61.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -14.5) |
| [[SW 1088 (line)]] | alt | 70.4 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0767× (z -8.8) |
| [[SW1417 (line)]] | alt | 46.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 55.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.174× (z -8.8) |
| [[C-33 A (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 93.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 51.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +13.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 50.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.0) |
| [[SHP-77 (line)]] | alt | 73.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.382× (z -8.5) |
| [[A498 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLSTN1]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GUSB]] | +0.67 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 | STRING 473 |
| [[PABIR2]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[AGO1]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 | pathway: Adherens junctions interactions; STRING 909 |
| [[FAM102B]] | +0.65 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[CEP131]] | +0.65 | +0.63 / +0.27 | both halves | 3e-04 |  |
| [[BCAM]] | +0.65 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TECR]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.64 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.64 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[LRFN3]] | +0.64 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.69 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[RPP38]] | -0.69 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.68 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.67 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[RBBP6]] | -0.66 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[RRP8]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[CCDC122]] | -0.63 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZNF689]] | -0.63 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[KRCC1]] | -0.63 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[C6orf62]] | -0.63 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[NAIF1]] | -0.62 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ACTR3-AS1]] | -0.62 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOAT1]] | C | SOAT1 activity lowers HDAC1's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.82× higher at baseline in the lines without SOAT1 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

### Downstream of this gene

*599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 12 strongest; 587 more arrows (587 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC23]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CMIP]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CROCCP3]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CYB561]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DNAJC2]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000288899]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM78B]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FBXW9]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FMN1]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LRRC51]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MRPS7]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCBP3]] | B | HDAC1, [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.8, 6.1); signed map (-28.3, -35.7). **Vector** length 120, 33.0% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +23.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +24.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.3 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +9.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -13.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2-p35.1 — chr1:32,292,083-32,333,635 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HD1, GON-10, KDAC1; previously RPD3L1 |
| Gene groups (HGNC) | Histone deacetylases, class I; EMSY complex; NuRD complex subunits; SIN3 histone deacetylase complex subunits; CoREST complex subunits; MiDAC complex subunits |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 108 pathways, smallest: Loss of MECP2 binding ability to 5mC-DNA; MECP2 regulates transcription of neuronal ligands; p75NTR negatively regulates cell cycle via SC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13547](https://www.uniprot.org/uniprotkb/Q13547) (Histone deacetylase 1):

> Histone deacetylase that catalyzes the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. As …

**Summary**, from NCBI Gene [3065](https://www.ncbi.nlm.nih.gov/gene/3065):

> Histone acetylation and deacetylation, catalyzed by multisubunit complexes, play a key role in the regulation of eukaryotic gene expression. The protein encoded by this gene belongs to the histone deacetylase/acuc/apha family and is a component of the histone deacetylase complex. It also interacts with retinoblastoma tumor-suppressor protein and this complex is a key element in the control of cell proliferation and differentiation. Together with metastasis-associated protein-2, it deacetylates …

**Accessions** — [HGNC:4852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4852) · Entrez [3065](https://www.ncbi.nlm.nih.gov/gene/3065) · UniProt [Q13547](https://www.uniprot.org/uniprotkb/Q13547) · Ensembl [ENSG00000116478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116478)

## Data

Gene col 3798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3798); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3798]; `tensor/DDL_lfc|DDL_z.npy` [3798]; `embed/gene_vectors.npy` [3798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3798 or target_col == 3798). Every well: [[HDAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
