---
symbol: "ALPK1"
type: "gene"
col: 1047
ensembl_id: "ENSG00000073331"
name: "alpha kinase 1"
location: "4q25"
module: 70
arm: "+"
pooled_cpm: 68.46
n_lines_expressing: 45
n_dd_up: 20
n_dd_down: 39
n_dd_up_clean: 19
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 13
direction_downstream: 15
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# ALPK1

*alpha kinase 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.90× (z +7.7, q 1e-11, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.280× (z -15.8, q 0e+00, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCOA7]] (+0.60, fdr 1e-05), [[GBP2]] (+0.59, fdr 1e-05), [[CFB]] (+0.58, fdr 1e-05); moves opposite to [[CROCCP3]] (-0.52, fdr 2e-05), [[CROCCP3-1]] (-0.50, fdr 1e-05), [[ADCK5]] (-0.47, fdr 4e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[IFI16]] → it (grade B ⚠); 15 go from it, the strongest it → [[NMI]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.90×** | +7.7 | 1e-11 | 37/42 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.66×** | +6.3 | 6e-08 | 38/45 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.53×** | +6.3 | 7e-08 | 32/43 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +5.8 | 9e-07 | 22/42 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 1e-05 | 31/42 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 2e-05 | 30/43 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +4.9 | 8e-05 | 30/44 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +4.8 | 9e-05 | 31/43 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 2e-04 | 30/44 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 27/43 (NCI-H2347, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 27/43 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 24/43 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.86×** | +4.0 | 0.003 | 27/45 (AsPC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +4.0 | 0.003 | 28/43 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.004 | 26/44 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.004 | 27/43 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -15.8 | 0e+00 | 39/43 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.290×** | -15.4 | 0e+00 | 38/43 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.382×** | -12.0 | 1e-30 | 37/43 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.377×** | -11.7 | 3e-29 | 38/42 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.429×** | -10.5 | 9e-24 | 35/43 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.452×** | -9.9 | 5e-21 | 39/43 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.441×** | -9.5 | 2e-19 | 40/44 (COLO 205, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.474×** | -8.9 | 4e-17 | 37/42 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.478×** | -8.5 | 2e-15 | 29/39 (SK-MEL-2, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.496×** | -8.4 | 3e-15 | 29/36 (Panc 03.27, HT-29, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.335×** | -7.1 | 7e-11 | 32/42 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.357×** | -6.7 | 1e-09 | 25/34 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -6.3 | 1e-08 | 33/44 (SK-MEL-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -6.1 | 4e-08 | 31/43 (KATO III, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -5.5 | 2e-06 | 30/43 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.717×** | -4.0 | 0.002 | 25/43 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.003 | 23/44 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.554×** | -3.8 | 0.004 | 23/43 (SNU-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.652×** | -3.8 | 0.004 | 22/43 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.738×** | -3.8 | 0.004 | 21/43 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.584×** | -3.5 | 0.011 | 21/43 (NCI-H1573, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.745×** | -3.4 | 0.013 | 20/43 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.742×** | -3.4 | 0.013 | 21/43 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 221 | 0 | 15 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0505× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0994× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 63.5 | 0 | 15 (10 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.132× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 150 | 0 | 14 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -14.3) |
| [[HT-29 (line)]] | alt | 103 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -16.5) |
| [[A549 (line)]] | wt | 74.4 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 9 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.197× (z -11.3) |
| [[COLO 205 (line)]] | alt | 284 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0786× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.206× (z -20.5) |
| [[H4 (line)]] | wt | 150 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.110× (z -14.6) |
| [[LoVo (line)]] | wt | 80.3 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.127× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -17.0) |
| [[LS 180 (line)]] | wt | 117 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 127 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.362× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 56.9 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -14.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.196× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 87.3 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -11.4) |
| [[RKO (line)]] | wt | 183 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -11.1) |
| [[SW48 (line)]] | wt | 78.5 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0978× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 80.7 | 2 (1 ⚠) | 2 (1 ⚠) | [[Trametinib (drug)]] 0.5 µM 2.78× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -9.3) |
| [[A-172 (line)]] | wt | 49.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.8) | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0923× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 40.1 | 0 | 3 | — | [[Ponatinib (drug)]] 5 µM 0.147× (z -11.6) |
| [[HOP62 (line)]] | alt | 45.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +21.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.74× (z +12.1) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -13.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 79.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -10.5) |
| [[SNU-1 (line)]] | wt | 62.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.119× (z -12.7) |
| [[SNU-423 (line)]] | alt | 43.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.278× (z -9.6) |
| [[HS-578T (line)]] | alt | 36.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +14.8) | — |
| [[hTERT-HPNE (line)]] | wt | 86.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -9.7) |
| [[A498 (line)]] | wt | 85.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 64.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -9.2) |
| [[C32 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0665× (z -10.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.226× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 78.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.380× (z -10.1) |
| [[J82 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 40.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.212× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 64.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.262× (z -9.6) |
| [[SW 900 (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -10.3) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA7]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GBP2]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CFB]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CFH]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MVP-DT]] | +0.56 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[KCNT2]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLFN5]] | +0.54 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | +0.54 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[TYMP]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[IFI16]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PDZK1IP1]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CROCCP3-1]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ADCK5]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[AP3M2]] | -0.47 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CTNNBIP1]] | -0.46 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[ABCC10]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[S100A16]] | -0.46 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[KCNC4]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ABTB3]] | -0.45 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[SLC25A15]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[FXYD5]] | -0.45 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[LOXL1]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI16]] | B | IFI16 activity raises ALPK1's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.48× lower at baseline in the lines without IFI16 | 0.001 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[GBP2]] | B | GBP2 activity raises ALPK1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without GBP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[TYMP]] | B | TYMP activity raises ALPK1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without TYMP | 0.031 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[S100A16]] | B | S100A16 activity raises ALPK1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without S100A16 | 0.031 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[IL7]] | B | IL7 activity raises ALPK1's level | lines that do not express IL7 (7) vs lines expressing it (43) | 2.89× lower at baseline in the lines without IL7 | 0.034 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, HIPK2; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises ALPK1's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without HLA-F | 0.034 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[KYNU]] | B | KYNU activity raises ALPK1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without KYNU | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[GBP1]] | B | GBP1 activity raises ALPK1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without GBP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ALPK1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TLR3]] | B | TLR3 activity raises ALPK1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without TLR3 | 0.054 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[TNFSF14]] | B | TNFSF14 activity raises ALPK1's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.40× lower at baseline in the lines without TNFSF14 | 0.077 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[PSMB8]] | C | PSMB8 activity raises ALPK1's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 3.15× lower at baseline in the lines without PSMB8 | 0.059 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMI]] | B | ALPK1 activity raises NMI's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 2.93× lower at baseline in the lines without ALPK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[FXYD5]] | B | ALPK1 activity raises FXYD5's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 3.39× lower at baseline in the lines without ALPK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[CASP10]] | B | ALPK1 activity raises CASP10's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 4.48× lower at baseline in the lines without ALPK1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[TRANK1]] | B | ALPK1 activity raises TRANK1's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 3.14× lower at baseline in the lines without ALPK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[GBP1]] | B | ALPK1 activity raises GBP1's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 5.26× lower at baseline in the lines without ALPK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[PSMB8]] | B | ALPK1 activity raises PSMB8's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 2.77× lower at baseline in the lines without ALPK1 | 0.036 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[IFIH1]] | B | ALPK1 activity raises IFIH1's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without ALPK1 | 0.048 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[SP100]] | B | ALPK1 activity raises SP100's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 3.16× lower at baseline in the lines without ALPK1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[GBP2]] | B | ALPK1 activity raises GBP2's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 5.22× lower at baseline in the lines without ALPK1 | 0.055 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[TRIM38]] | B | ALPK1 activity raises TRIM38's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 4.00× lower at baseline in the lines without ALPK1 | 0.058 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[DDX60]] | B | ALPK1 activity raises DDX60's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 2.93× lower at baseline in the lines without ALPK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |
| [[HLA-F]] | B | ALPK1 activity raises HLA-F's level | lines that do not express ALPK1 (5) vs lines expressing it (45) | 3.00× lower at baseline in the lines without ALPK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: GARIN1B, ZHX2, OAF; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.2, 49.3); signed map (60.1, 27.6). **Vector** length 105, 36.2% of its response variance represented; |z| ≥ 3 in 1,604 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *CASP4 inflammasome assembly* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.1 | -0.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.6 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +4.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -11.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.4 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.6 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | alpha kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:112,285,509-112,442,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Lak, FLJ22670, KIAA1527 |
| Gene groups (HGNC) | Alpha kinases |
| Reactome | 23 pathways, smallest: Alpha-protein kinase 1 signaling pathway; TAK1-dependent IKK and NF-kappa-B activation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QP1](https://www.uniprot.org/uniprotkb/Q96QP1) (Alpha-protein kinase 1):

> Serine/threonine-protein kinase that detects bacterial pathogen-associated molecular pattern metabolites (PAMPs) and initiates an innate immune response, a critical step for pathogen elimination and engagement of adaptive immunity. Specifically recognizes and binds ADP-D-glycero-beta-D-manno-heptose (ADP-Heptose), a potent PAMP present in all Gram-negative and some Gram-positive bacteria. ADP-Heptose-binding stimulates its kinase activity to phosphorylate and activate TIFA, triggering …

**Summary**, from NCBI Gene [80216](https://www.ncbi.nlm.nih.gov/gene/80216):

> This gene encodes an alpha kinase. Mice which were homozygous for disrupted copies of this gene exhibited coordination defects (PMID: 21208416). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:20917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20917) · Entrez [80216](https://www.ncbi.nlm.nih.gov/gene/80216) · UniProt [Q96QP1](https://www.uniprot.org/uniprotkb/Q96QP1) · Ensembl [ENSG00000073331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073331)

## Data

Gene col 1047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1047); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1047]; `tensor/DDL_lfc|DDL_z.npy` [1047]; `embed/gene_vectors.npy` [1047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1047 or target_col == 1047). Every well: [[ALPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
