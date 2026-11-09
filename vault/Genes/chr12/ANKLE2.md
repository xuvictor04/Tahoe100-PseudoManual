---
symbol: "ANKLE2"
type: "gene"
col: 10766
ensembl_id: "ENSG00000176915"
name: "ankyrin repeat and LEM domain containing 2"
location: "12q24.33"
module: 65
arm: "-"
pooled_cpm: 113.47
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ANKLE2

*ankyrin repeat and LEM domain containing 2* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.70× (z +49.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.596× (z -13.8, q 7e-41, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30-DT]] (+0.68, fdr 1e-05), [[TIAM2]] (+0.66, fdr 1e-05), [[NEPRO-AS1]] (+0.66, fdr 1e-05); moves opposite to [[ATG4C]] (-0.70, fdr 1e-05), [[GMCL1]] (-0.69, fdr 7e-06), [[POGLUT2]] (-0.69, fdr 2e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.70×** | +49.4 | 0e+00 | 46/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +25.2 | 0e+00 | 46/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.64×** | +24.9 | 0e+00 | 42/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +14.9 | 0e+00 | 44/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +13.3 | 2e-38 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +11.7 | 1e-29 | 35/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +10.6 | 1e-24 | 39/48 (RKO, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +10.6 | 2e-24 | 38/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +10.4 | 1e-23 | 38/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +9.5 | 8e-20 | 34/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +9.2 | 2e-18 | 34/48 (SW480, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +8.9 | 2e-17 | 32/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +8.7 | 2e-16 | 36/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.9 | 1e-13 | 34/48 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +7.6 | 2e-12 | 41/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +6.8 | 3e-10 | 29/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +5.8 | 2e-07 | 30/48 (NCI-H460, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -13.8 | 7e-41 | 36/48 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.614×** | -13.1 | 2e-36 | 39/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -11.5 | 3e-28 | 35/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.776×** | -9.6 | 1e-19 | 36/48 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.729×** | -8.5 | 2e-15 | 37/48 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -6.6 | 4e-09 | 27/48 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.846× | -6.3 | 2e-08 | 22/49 (HEC-1-A, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.862× | -5.6 | 1e-06 | 14/48 (J82, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.818×** | -5.4 | 4e-06 | 25/49 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.705×** | -4.6 | 2e-04 | 25/49 (HEC-1-A, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.858× | -4.0 | 0.004 | 20/49 (SW 900, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.866× | -3.9 | 0.005 | 13/48 (NCI-H23, A-172, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 0.873× | -3.5 | 0.019 | 13/48 (LS 180, COLO 205, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.881× | -3.4 | 0.025 | 9/49 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.789×** | -3.1 | 0.064 | 12/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.891× | -3.1 | 0.065 | 8/48 (A-172, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.8 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +31.1) | — |
| [[A-172 (line)]] | wt | 133 | 6 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +32.8) | [[Panobinostat (drug)]] 5 µM 0.376× (z -14.0) |
| [[PANC-1 (line)]] | alt | 95.2 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +49.8) | — |
| [[SW 900 (line)]] | alt | 143 | 8 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +31.9) | [[Belinostat (drug)]] 5 µM 0.471× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 181 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +34.3) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -10.1) |
| [[A498 (line)]] | wt | 133 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +37.8) | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -10.5) |
| [[A549 (line)]] | wt | 125 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +39.3) | [[Panobinostat (drug)]] 5 µM 0.474× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 197 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +21.5) | [[Belinostat (drug)]] 5 µM 0.336× (z -15.8) |
| [[HOP62 (line)]] | alt | 107 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +41.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -9.4) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.550× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 149 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +35.6) | [[Panobinostat (drug)]] 5 µM 0.393× (z -11.8) |
| [[J82 (line)]] | alt | 181 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +26.4) | [[Panobinostat (drug)]] 5 µM 0.396× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 127 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +24.6) | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -10.2) |
| [[RKO (line)]] | wt | 136 | 5 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0812× (z -34.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 152 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +30.1) | [[Belinostat (drug)]] 5 µM 0.384× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +29.1) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 5 | 1 | [[Harringtonine (drug)]] 5 µM 6.36× (z +25.2) | [[Panobinostat (drug)]] 0.5 µM 0.521× (z -9.3) |
| [[SW48 (line)]] | wt | 128 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +26.8) | — |
| [[AsPC-1 (line)]] | alt | 136 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +28.5) | [[Panobinostat (drug)]] 5 µM 0.363× (z -13.3) |
| [[BT-474 (line)]] | alt | 142 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +24.5) | — |
| [[HT-29 (line)]] | alt | 108 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 98.8 | 3 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.48× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[COLO 205 (line)]] | alt | 103 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +18.0) | — |
| [[HS-578T (line)]] | alt | 86.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +34.2) | — |
| [[hTERT-HPNE (line)]] | wt | 137 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +30.7) | — |
| [[LoVo (line)]] | wt | 123 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +25.6) | — |
| [[NCI-H23 (line)]] | alt | 114 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +20.0) | — |
| [[Panc 03.27 (line)]] | alt | 94.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +26.0) | [[Panobinostat (drug)]] 5 µM 0.489× (z -8.5) |
| [[Hs 766T (line)]] | wt | 85.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.9) | [[Belinostat (drug)]] 5 µM 0.427× (z -9.2) |
| [[KATO III (line)]] | alt | 66.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +17.4) | — |
| [[NCI-H2030 (line)]] | alt | 116 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +28.7) | — |
| [[RPMI-7951 (line)]] | alt | 97.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +20.3) | — |
| [[SNU-423 (line)]] | alt | 144 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +37.0) | — |
| [[A-427 (line)]] | wt | 72.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[C32 (line)]] | wt | 53.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.8) | — |
| [[H4 (line)]] | wt | 67.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +18.3) | — |
| [[SW 1088 (line)]] | alt | 98.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.0) | [[Omeprazole (sodium) (drug)]] 5 µM 0.0668× (z -10.8) |
| [[SW480 (line)]] | alt | 95.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 77.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +12.5) | — |
| [[C-33 A (line)]] | alt | 92.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 79.1 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.75× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 65.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.14× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 124 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TIAM2]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | +0.66 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[ST7L]] | +0.64 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[DNAJC8]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[DPP8]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SLC9A8]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[TASOR]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.62 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MCPH1]] | +0.62 | +0.56 / +0.50 | both halves | 1e-05 | STRING 577 |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | -0.70 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.69 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[POGLUT2]] | -0.69 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[SNX1]] | -0.66 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[ARL6]] | -0.66 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[ORC4]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[USP3]] | -0.65 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[HACE1]] | -0.64 | -0.62 / -0.49 | both halves | 1e-05 | same gene group |
| [[CNOT8]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[PDXP]] | -0.64 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[L2HGDH]] | -0.63 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[KIAA1958]] | -0.63 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ANKLE2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ANKLE2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.715). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (4.4, -11.5); signed map (16.3, -25.3). **Vector** length 114, 35.0% of its response variance represented; |z| ≥ 3 in 1,440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.6 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +25.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +49.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +24.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +5.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.4 | -13.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -8.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -9.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and LEM domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,725,503-132,761,832 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LEMD7, Lem4; previously KIAA0692 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; LEM domain containing |
| Reactome | 12 pathways, smallest: Initiation of Nuclear Envelope (NE) Reformation; Nuclear Envelope (NE) Reassembly; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XL3](https://www.uniprot.org/uniprotkb/Q86XL3) (Ankyrin repeat and LEM domain-containing protein 2):

> Involved in mitotic nuclear envelope reassembly by promoting dephosphorylation of BAF/BANF1 during mitotic exit. Coordinates the control of BAF/BANF1 dephosphorylation by inhibiting VRK1 kinase and promoting dephosphorylation of BAF/BANF1 by protein phosphatase 2A (PP2A), thereby facilitating nuclear envelope assembly. May regulate nuclear localization of VRK1 in non-dividing cells. It is unclear whether it acts as a real PP2A regulatory subunit or whether it is involved in recruitment of the …

**Summary**, from NCBI Gene [23141](https://www.ncbi.nlm.nih.gov/gene/23141):

> This gene encodes a member of the LEM family of inner nuclear membrane proteins. The encoded protein functions as a mitotic regulator through postmitotic formation of the nuclear envelope. Mutations in this gene cause morphology defects in the nuclear envelope and BAF hyperphosphorylation. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:29101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29101) · Entrez [23141](https://www.ncbi.nlm.nih.gov/gene/23141) · UniProt [Q86XL3](https://www.uniprot.org/uniprotkb/Q86XL3) · Ensembl [ENSG00000176915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176915)

## Data

Gene col 10766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10766); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10766]; `tensor/DDL_lfc|DDL_z.npy` [10766]; `embed/gene_vectors.npy` [10766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10766 or target_col == 10766). Every well: [[ANKLE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKLE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
