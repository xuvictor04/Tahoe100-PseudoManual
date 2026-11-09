---
symbol: "UBE3B"
type: "gene"
col: 7490
ensembl_id: "ENSG00000151148"
name: "ubiquitin protein ligase E3B"
location: "12q24.11"
module: 148
arm: "+"
pooled_cpm: 33.93
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# UBE3B

*ubiquitin protein ligase E3B* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.46× (z +34.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.605× (z -9.7, q 2e-19, down in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.733× (z -8.8, q 6e-16, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.79, fdr 1e-05), [[ATXN1L]] (+0.77, fdr 7e-06), [[PBLD]] (+0.75, fdr 5e-05); moves opposite to [[FCHO1]] (-0.71, fdr 1e-05), [[RSAD1]] (-0.71, fdr 1e-05), [[FAM118A]] (-0.68, fdr 3e-05).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.46×** | +34.9 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +18.9 | 0e+00 | 43/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +16.1 | 0e+00 | 43/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +14.4 | 1e-44 | 44/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +9.3 | 1e-18 | 29/47 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 4e-09 | 35/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.9 | 6e-05 | 20/48 (NCI-H23, SHP-77, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +4.8 | 1e-04 | 19/48 (PANC-1, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 18/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.005 | 17/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.070 | 13/47 (RKO, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.073 | 7/48 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.073 | 10/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.075 | 1/48 (SW480) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -9.7 | 2e-19 | 35/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -8.8 | 6e-16 | 34/48 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.690×** | -7.4 | 2e-11 | 32/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -7.4 | 2e-11 | 29/47 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -7.2 | 7e-11 | 30/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -6.6 | 3e-09 | 27/48 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -6.6 | 4e-09 | 26/48 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.739×** | -6.0 | 1e-07 | 30/48 (RPMI-7951, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.746×** | -5.9 | 3e-07 | 23/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.756×** | -5.6 | 1e-06 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -5.3 | 7e-06 | 22/48 (C-33 A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.799×** | -4.5 | 4e-04 | 21/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -4.1 | 0.002 | 19/48 (HCT15, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.005 | 18/47 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.833× | -3.6 | 0.010 | 16/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.057 | 9/48 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.899× | -3.0 | 0.086 | 4/48 (SW48, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.753×** | -3.0 | 0.086 | 11/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.3 | 3 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +21.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.322× (z -12.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.420× (z -10.0) |
| [[PANC-1 (line)]] | alt | 42.2 | 4 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +22.5) | [[Digitoxin (drug)]] 5 µM 0.442× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.489× (z -9.0) |
| [[HOP62 (line)]] | alt | 33.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +15.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.322× (z -9.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 34.5 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +15.8) | [[Ixazomib citrate (drug)]] 5 µM 0.401× (z -8.5) |
| [[SW1417 (line)]] | alt | 31.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +18.4) | — |
| [[SW480 (line)]] | alt | 37.1 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +22.1) | [[Digitoxin (drug)]] 0.5 µM 0.467× (z -9.6) |
| [[C32 (line)]] | wt | 27.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +14.3) | — |
| [[HEC-1-A (line)]] | alt | 34.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 24.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +15.1) | — |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.201× (z -10.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +18.1) | — |
| [[NCI-H1573 (line)]] | alt | 43.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +20.6) | — |
| [[NCI-H23 (line)]] | alt | 46.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 32.1 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +13.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -8.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 32.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +14.6) | — |
| [[A-172 (line)]] | wt | 31.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 25.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 33.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +12.5) | — |
| [[H4 (line)]] | wt | 31.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.126× (z -11.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 52.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +11.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.321× (z -8.5) |
| [[Hs 766T (line)]] | wt | 33.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +15.5) | — |
| [[J82 (line)]] | alt | 28.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +14.5) | — |
| [[LoVo (line)]] | wt | 40.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +16.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.392× (z -10.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 30.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 34.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +12.8) | — |
| [[RKO (line)]] | wt | 29.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +16.7) | — |
| [[A-427 (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.6) | — |
| [[A549 (line)]] | wt | 31.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.5) | — |
| [[AsPC-1 (line)]] | alt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +21.3) | — |
| [[C-33 A (line)]] | alt | 34.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +12.0) | — |
| [[KATO III (line)]] | alt | 37.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +16.0) | — |
| [[LS 180 (line)]] | wt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 39.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 39.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.2) | — |
| [[SW48 (line)]] | wt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.79 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.77 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PBLD]] | +0.75 | +0.75 / +0.40 | both halves | 5e-05 |  |
| [[MMADHC-DT]] | +0.75 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[ZBED5]] | +0.73 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | +0.73 | +0.74 / +0.39 | both halves | 6e-05 |  |
| [[PEF1]] | +0.73 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SENP8]] | +0.72 | +0.75 / +0.35 | both halves | 1e-04 |  |
| [[MAILR]] | +0.72 | +0.76 / +0.22 | both halves | 6e-04 |  |
| [[MFF-DT]] | +0.71 | +0.71 / +0.29 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | +0.71 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[DNASE1]] | +0.71 | +0.72 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | -0.71 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[RSAD1]] | -0.71 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.68 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[MAST3]] | -0.68 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[CAMK2G]] | -0.67 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.67 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[PACC1]] | -0.66 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SLC23A2]] | -0.66 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TSPAN33]] | -0.66 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[WASF3]] | -0.66 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[RADX]] | -0.66 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SLC27A1]] | -0.66 | -0.63 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBE3B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers UBE3B's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.793). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (6.9, 10.8); signed map (22.9, -9.4). **Vector** length 111, 29.0% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +18.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +34.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +16.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.4 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.0 | -6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.4 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.6 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,477,402-109,536,705 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3V4](https://www.uniprot.org/uniprotkb/Q7Z3V4) (Ubiquitin-protein ligase E3B):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Ubiquitinates BCKDK and targets it for degradation, thereby regulating various metabolic processes (By similarity). Involved in the positive regulation of neurite branching in hippocampal neurons and the control of neuronal spine number and morphology, through the ubiquitination of PPP3CC (By similarity).

**Summary**, from NCBI Gene [89910](https://www.ncbi.nlm.nih.gov/gene/89910):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: E1 ubiquitin-activating enzymes, E2 ubiquitin-conjugating enzymes, and E3 ubiquitin-protein ligases. This gene encodes a member of the E3 ubiquitin-conjugating enzyme family which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme and transfers the ubiquitin to the targeted substrates. A …

**Accessions** — [HGNC:13478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13478) · Entrez [89910](https://www.ncbi.nlm.nih.gov/gene/89910) · UniProt [Q7Z3V4](https://www.uniprot.org/uniprotkb/Q7Z3V4) · Ensembl [ENSG00000151148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151148)

## Data

Gene col 7490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7490); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7490]; `tensor/DDL_lfc|DDL_z.npy` [7490]; `embed/gene_vectors.npy` [7490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7490 or target_col == 7490). Every well: [[UBE3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
