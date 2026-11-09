---
symbol: "SIAH1"
type: "gene"
col: 12216
ensembl_id: "ENSG00000196470"
name: "siah E3 ubiquitin protein ligase 1"
location: "16q12.1"
module: 46
arm: "+"
pooled_cpm: 53.44
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SIAH1

*siah E3 ubiquitin protein ligase 1* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +13.7, q 4e-40, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.396× (z -13.3, q 1e-37, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAF1]] (+0.68, fdr 1e-05), [[AHI1-DT]] (+0.68, fdr 5e-05), [[DICER1-AS1]] (+0.68, fdr 6e-05); moves opposite to [[EHD4]] (-0.59, fdr 2e-04), [[UBA6]] (-0.59, fdr 4e-04), [[GP6-AS1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +13.7 | 4e-40 | 46/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +13.0 | 3e-36 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.31×** | +11.0 | 9e-26 | 47/49 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.8 | 3e-20 | 45/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +8.9 | 6e-17 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.84×** | +8.8 | 1e-16 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +8.1 | 6e-14 | 39/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +7.3 | 2e-11 | 38/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.5 | 2e-06 | 27/49 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 3e-05 | 30/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 5e-04 | 29/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.18× | +3.3 | 0.044 | 10/48 (SHP-77, A-427, …) | top dose only | position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.044 | 19/48 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.070 | 17/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.070 | 21/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.396×** | -13.3 | 1e-37 | 46/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -13.0 | 2e-36 | 46/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.492×** | -10.2 | 5e-22 | 47/48 (HOP62, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.479×** | -10.1 | 5e-22 | 34/42 (A-427, HCT15, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.513×** | -9.6 | 1e-19 | 37/48 (NCI-H2347, SHP-77, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.619×** | -6.9 | 6e-10 | 43/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.790×** | -3.4 | 0.062 | 24/48 (NCI-H2347, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.6 | 7 (2 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.00× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.352× (z -10.9) |
| [[SW480 (line)]] | alt | 54.8 | 6 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.352× (z -11.7) |
| [[PANC-1 (line)]] | alt | 45.3 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.348× (z -12.6) |
| [[HOP62 (line)]] | alt | 66.2 | 3 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -11.7) |
| [[KATO III (line)]] | alt | 67.6 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 50.7 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.329× (z -11.1) |
| [[SW 900 (line)]] | alt | 46.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.33× (z +10.0) | — |
| [[A-172 (line)]] | wt | 49.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.312× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -8.7) |
| [[A549 (line)]] | wt | 65.6 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 48.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 52.2 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.377× (z -9.0) |
| [[SW1417 (line)]] | alt | 73.7 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.319× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 36.4 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.23× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 50.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 70.8 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 41.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 61.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.381× (z -8.8) |
| [[A498 (line)]] | wt | 65.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -9.4) |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.333× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 40.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Belzutifan (drug)]] 5 µM 0.112× (z -8.5) |
| [[Hs 766T (line)]] | wt | 51.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 65.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -9.2) |
| [[LoVo (line)]] | wt | 42.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 54.5 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.339× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 62.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.319× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 62.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 51.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 70.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -9.2) |
| [[C32 (line)]] | wt | 39.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 12.2× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 48.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.6) | — |
| [[H4 (line)]] | wt | 42.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.31× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 40.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 49.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.162× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 55.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAF1]] | +0.68 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.68 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[DICER1-AS1]] | +0.68 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[IDNK]] | +0.68 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[TSTD3]] | +0.67 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[WAC-AS1]] | +0.67 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[RBM33]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[TAPT1]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LINC00938]] | +0.66 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.65 | +0.41 / +0.28 | both halves | 3e-04 |  |
| [[GALNT7-DT]] | +0.65 | +0.40 / +0.28 | both halves | 3e-04 |  |
| [[DYRK1A]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.59 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[UBA6]] | -0.59 | -0.40 / -0.25 | both halves | 4e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[GP6-AS1]] | -0.58 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SIAH1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (2.1, 18.3); signed map (25.8, -16.2). **Vector** length 94.2, 28.1% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.0 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +0.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.6 | +0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +1.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -13.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -13.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.5 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | -1.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | siah E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:48,356,364-48,448,402 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hSIAH1 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | PEROXISOME |
| Reactome | 7 pathways, smallest: Netrin-1 signaling; Amyloid fiber formation; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUQ4](https://www.uniprot.org/uniprotkb/Q8IUQ4) (E3 ubiquitin-protein ligase SIAH1):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent proteasomal degradation of target proteins. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Mediates E3 ubiquitin ligase activity either through direct binding to substrates or by functioning as the essential RING domain subunit of larger E3 complexes. Triggers the ubiquitin-mediated degradation of many …

**Summary**, from NCBI Gene [6477](https://www.ncbi.nlm.nih.gov/gene/6477):

> This gene encodes a protein that is a member of the seven in absentia homolog (SIAH) family. The protein is an E3 ligase and is involved in ubiquitination and proteasome-mediated degradation of specific proteins. The activity of this ubiquitin ligase has been implicated in the development of certain forms of Parkinson's disease, the regulation of the cellular response to hypoxia and induction of apoptosis. Alternative splicing results in several additional transcript variants, some encoding …

**Accessions** — [HGNC:10857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10857) · Entrez [6477](https://www.ncbi.nlm.nih.gov/gene/6477) · UniProt [Q8IUQ4](https://www.uniprot.org/uniprotkb/Q8IUQ4) · Ensembl [ENSG00000196470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196470)

## Data

Gene col 12216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12216); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12216]; `tensor/DDL_lfc|DDL_z.npy` [12216]; `embed/gene_vectors.npy` [12216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12216 or target_col == 12216). Every well: [[SIAH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIAH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
