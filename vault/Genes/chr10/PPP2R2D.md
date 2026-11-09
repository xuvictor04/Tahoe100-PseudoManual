---
symbol: "PPP2R2D"
type: "gene"
col: 10613
ensembl_id: "ENSG00000175470"
name: "protein phosphatase 2 regulatory subunit Bdelta"
location: "10q26.3"
module: 37
arm: "+"
pooled_cpm: 87.59
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PPP2R2D

*protein phosphatase 2 regulatory subunit Bdelta* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.92× (z +21.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.638× (z -8.6, q 5e-15, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.671× (z -7.9, q 4e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELMOD3]] (+0.65, fdr 1e-05), [[DEAF1]] (+0.64, fdr 1e-05), [[BANP]] (+0.62, fdr 3e-05); moves opposite to [[BMS1]] (-0.56, fdr 2e-05), [[PDHB]] (-0.55, fdr 3e-05), [[ECHS1]] (-0.54, fdr 2e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.92×** | +21.3 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +18.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.14×** | +15.2 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.94×** | +13.2 | 8e-38 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.94×** | +11.2 | 4e-27 | 45/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +10.9 | 1e-25 | 36/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +10.0 | 2e-21 | 45/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +9.6 | 8e-20 | 36/48 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +8.4 | 4e-15 | 37/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.47×** | +7.7 | 1e-12 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +6.7 | 1e-09 | 37/48 (H4, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +6.3 | 1e-08 | 31/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +5.6 | 1e-06 | 31/48 (HT-29, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.7 | 1e-04 | 21/49 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +4.0 | 0.002 | 24/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 22/48 (HT-29, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.021 | 16/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.048 | 17/48 (NCI-H1573, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -8.6 | 5e-15 | 30/44 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.661×** | -8.1 | 2e-13 | 38/49 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.671×** | -7.9 | 4e-13 | 38/48 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -6.7 | 4e-09 | 33/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.726×** | -6.4 | 2e-08 | 37/48 (LOX-IMVI, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.800×** | -6.3 | 3e-08 | 28/48 (AsPC-1, SW 900, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -5.3 | 1e-05 | 24/48 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.783×** | -4.9 | 8e-05 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.787×** | -4.4 | 7e-04 | 23/45 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.804×** | -4.3 | 8e-04 | 27/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.809×** | -4.2 | 0.001 | 24/49 (SHP-77, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.826×** | -3.8 | 0.007 | 24/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.836× | -3.6 | 0.016 | 19/49 (HS-578T, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.844× | -3.4 | 0.030 | 18/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.850× | -3.2 | 0.044 | 11/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.850× | -3.2 | 0.044 | 13/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.851× | -3.2 | 0.047 | 15/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.047 | 12/48 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.854× | -3.1 | 0.047 | 16/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.1 | 10 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -14.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 107 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +20.4) | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 93.9 | 9 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +24.4) | [[Dinaciclib (drug)]] 0.5 µM 0.534× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 103 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 73.4 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -23.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 87.1 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +21.1) | — |
| [[H4 (line)]] | wt | 70.1 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 146 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +15.9) | — |
| [[NCI-H1792 (line)]] | alt | 72.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +14.5) | — |
| [[A-427 (line)]] | wt | 88.2 | 2 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.44× (z +11.8) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.585× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 92.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 79.2 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.03× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 103 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.60× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 50.1 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 106 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -17.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 67.6 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.05× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 121 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 91.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.52× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 94.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 108 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 110 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.31× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 119 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 69.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 56.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 98.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.56× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 97.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +11.3) | — |
| [[SW48 (line)]] | wt | 131 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +11.4) | — |
| [[A549 (line)]] | wt | 89.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 79.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 93.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 89.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 85.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 87.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +10.0) | — |
| [[A498 (line)]] | wt | 70.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 104 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[C32 (line)]] | wt | 68.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 57.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.5) | — |
| [[A-172 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD3]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DEAF1]] | +0.64 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[BANP]] | +0.62 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[GUCA1B]] | +0.60 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | +0.60 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[GARS1-DT]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[RAB4B]] | +0.56 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[SUZ12P1]] | +0.56 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZCCHC8]] | +0.55 | +0.40 / +0.44 | both halves | 5e-05 | STRING 651 |
| [[SLC35D2]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SNX31]] | +0.53 | +0.26 / +0.38 | both halves | 3e-04 |  |
| [[ZBTB8OS]] | +0.53 | +0.34 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PDHB]] | -0.55 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[ECHS1]] | -0.54 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[GALNT4]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[KIFAP3]] | -0.48 | -0.32 / -0.30 | both halves | 2e-04 |  |
| [[CHML]] | -0.48 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[AKAP11]] | -0.48 | -0.54 / -0.37 | both halves | 7e-05 |  |
| [[VCL]] | -0.47 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[CORO1C]] | -0.47 | -0.29 / -0.29 | both halves | 2e-04 | same gene group |
| [[HTATSF1]] | -0.46 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[PDHA1]] | -0.46 | -0.35 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PPP2R2D's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PPP2R2D's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.5, 27.8); signed map (9.7, 1.3). **Vector** length 77.6, 22.3% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.1 | -6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit Bdelta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:131,901,008-131,959,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS026, B55delta, B55D |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits |
| Reactome | 5 pathways, smallest: MASTL Facilitates Mitotic Progression; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q66LE6](https://www.uniprot.org/uniprotkb/Q66LE6) (Serine/threonine-protein phosphatase 2A 55 kDa regulatory subunit B delta isoform):

> Substrate-recognition subunit of protein phosphatase 2A (PP2A) that plays a key role in cell cycle by controlling mitosis entry and exit. Involved in chromosome clustering during late mitosis by mediating dephosphorylation of MKI67 (By similarity). The activity of PP2A complexes containing PPP2R2D (PR55-delta) fluctuate during the cell cycle: the activity is high in interphase and low in mitosis (By similarity).

**Summary**, from NCBI Gene [55844](https://www.ncbi.nlm.nih.gov/gene/55844):

> Predicted to enable enzyme-substrate adaptor activity and protein phosphatase regulator activity. Predicted to be involved in exit from mitosis and regulation of chromosome segregation. Predicted to be located in cytoplasm. Predicted to be part of protein phosphatase type 2A complex. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23732) · Entrez [55844](https://www.ncbi.nlm.nih.gov/gene/55844) · UniProt [Q66LE6](https://www.uniprot.org/uniprotkb/Q66LE6) · Ensembl [ENSG00000175470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175470)

## Data

Gene col 10613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10613); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10613]; `tensor/DDL_lfc|DDL_z.npy` [10613]; `embed/gene_vectors.npy` [10613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10613 or target_col == 10613). Every well: [[PPP2R2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
