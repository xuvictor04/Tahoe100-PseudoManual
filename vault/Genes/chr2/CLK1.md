---
symbol: "CLK1"
type: "gene"
col: 273
ensembl_id: "ENSG00000013441"
name: "CDC like kinase 1"
location: "2q33.1"
module: 69
arm: "+"
pooled_cpm: 97.21
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CLK1

*CDC like kinase 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.94× (z +15.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.313× (z -11.3, q 1e-26, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.518× (z -6.3, q 5e-08, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBP1]] (+0.69, fdr 7e-06), [[RSRP1]] (+0.67, fdr 1e-05), [[OSER1-DT]] (+0.66, fdr 1e-05); moves opposite to [[IPO9]] (-0.63, fdr 7e-06), [[RAB10]] (-0.61, fdr 2e-05), [[GFM1]] (-0.59, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.94×** | +15.4 | 0e+00 | 47/48 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +9.5 | 7e-19 | 46/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.66×** | +8.1 | 1e-13 | 48/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.20×** | +8.0 | 2e-13 | 43/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.29×** | +7.7 | 2e-12 | 45/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.5 | 8e-12 | 43/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.85×** | +5.8 | 4e-07 | 35/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +5.1 | 2e-05 | 38/48 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +4.8 | 1e-04 | 32/48 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +4.6 | 2e-04 | 30/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +4.5 | 4e-04 | 37/48 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.4 | 5e-04 | 33/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.004 | 34/49 (RKO, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.004 | 34/48 (A498, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.016 | 26/48 (A-172, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.025 | 24/48 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.064 | 29/50 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.313×** | -11.3 | 1e-26 | 41/44 (NCI-H2347, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -7.6 | 6e-12 | 44/49 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.485×** | -7.3 | 5e-11 | 43/48 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.518×** | -6.3 | 5e-08 | 41/48 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.553×** | -6.0 | 3e-07 | 42/48 (CFPAC-1, HepG2/C3A, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -4.0 | 0.007 | 34/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.679×** | -3.5 | 0.043 | 33/48 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.695×** | -3.4 | 0.048 | 25/45 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **0.696×** | -3.2 | 0.078 | 27/48 (SHP-77, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.706× | -3.1 | 0.11 | 26/49 (CFPAC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.809× | -3.0 | 0.13 | 27/48 (SHP-77, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 85.5 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +15.1) | — |
| [[KATO III (line)]] | alt | 61.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +20.6) | — |
| [[LoVo (line)]] | wt | 80.7 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.54× (z +17.8) | — |
| [[AsPC-1 (line)]] | alt | 122 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 108 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.19× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 75.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +17.9) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 76.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 85.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 180 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -9.5) |
| [[HT-29 (line)]] | alt | 80.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 140 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 92.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.41× (z +15.3) | — |
| [[RKO (line)]] | wt | 85.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +18.5) | — |
| [[SW1417 (line)]] | alt | 106 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 78.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +11.9) | — |
| [[A-427 (line)]] | wt | 48.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 62.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 87.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 70.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0848× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H2347 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -18.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 56.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 149 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 66.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 73.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -14.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 117 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -12.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 106 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 121 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.58× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.278× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 82.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 58.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.8) | — |
| [[C32 (line)]] | wt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -14.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 104 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 95.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.0) | — |
| [[J82 (line)]] | alt | 95.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +13.6) | — |
| [[SNU-1 (line)]] | wt | 89.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBP1]] | +0.69 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.67 | +0.57 / +0.61 | both halves | 1e-05 | STRING 550 |
| [[OSER1-DT]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CCNG2]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[RAB21]] | +0.64 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CREB3L4]] | +0.64 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ACP6]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CD27-AS1]] | +0.62 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ARID4B]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.61 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[TRA2A]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 | STRING 799 |
| [[PIK3CA]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[RAB10]] | -0.61 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[GFM1]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.57 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.57 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[EIF2B3]] | -0.57 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[PPM1G]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[EFTUD2]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[DDX10]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[SMARCA4]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[URB2]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PITPNB]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CLK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.4, -41.0); signed map (-11.1, 8.5). **Vector** length 94.7, 38.1% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.2 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | -0.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | -0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | -0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.5 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.0 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.1 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | +9.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | CDC like kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,853,009-200,864,691 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | CDC like kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P49759](https://www.uniprot.org/uniprotkb/P49759) (Dual specificity protein kinase CLK1):

> Dual specificity kinase acting on both serine/threonine and tyrosine-containing substrates. Phosphorylates serine- and arginine-rich (SR) proteins of the spliceosomal complex and may be a constituent of a network of regulatory mechanisms that enable SR proteins to control RNA splicing. Phosphorylates: SRSF1, SRSF3 and PTPN1. Regulates the alternative splicing of tissue factor (F3) pre-mRNA in endothelial cells.

**Summary**, from NCBI Gene [1195](https://www.ncbi.nlm.nih.gov/gene/1195):

> This gene encodes a member of the CDC2-like (or LAMMER) family of dual specificity protein kinases. In the nucleus, the encoded protein phosphorylates serine/arginine-rich proteins involved in pre-mRNA processing, releasing them into the nucleoplasm. The choice of splice sites during pre-mRNA processing may be regulated by the concentration of transacting factors, including serine/arginine rich proteins. Therefore, the encoded protein may play an indirect role in governing splice site …

**Accessions** — [HGNC:2068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2068) · Entrez [1195](https://www.ncbi.nlm.nih.gov/gene/1195) · UniProt [P49759](https://www.uniprot.org/uniprotkb/P49759) · Ensembl [ENSG00000013441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013441)

## Data

Gene col 273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 273); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 273]; `tensor/DDL_lfc|DDL_z.npy` [273]; `embed/gene_vectors.npy` [273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 273 or target_col == 273). Every well: [[CLK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
