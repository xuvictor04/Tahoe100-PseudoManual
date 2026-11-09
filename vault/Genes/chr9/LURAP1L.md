---
symbol: "LURAP1L"
type: "gene"
col: 7733
ensembl_id: "ENSG00000153714"
name: "leucine rich adaptor protein 1 like"
location: "9p23"
module: 133
arm: "+"
pooled_cpm: 37.96
n_lines_expressing: 38
n_dd_up: 42
n_dd_down: 18
n_dd_up_clean: 30
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# LURAP1L

*leucine rich adaptor protein 1 like* — 9p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (12 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.67× (z +10.0, q 9e-21, up in 27 of 36 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.74× (z +7.6, q 5e-12, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.324× (z -22.0, q 0e+00, down in 33 of 35 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.396× (z -12.8, q 1e-35, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBR2]] (+0.64, fdr 1e-05), [[SLC7A11]] (+0.61, fdr 1e-05), [[SLC3A2]] (+0.60, fdr 2e-05); moves opposite to [[HIVEP3]] (-0.59, fdr 3e-05), [[DOT1L]] (-0.56, fdr 2e-05), [[PFN1]] (-0.52, fdr 2e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SPINK1]] → it (grade B ⚠); 6 go from it, the strongest it → [[CCPG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.67×** | +10.0 | 9e-21 | 27/36 (COLO 205, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +7.6 | 5e-12 | 23/36 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +7.6 | 5e-12 | 20/36 (SHP-77, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +7.5 | 1e-11 | 23/36 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +6.8 | 1e-09 | 20/35 (H4, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.60×** | +6.2 | 6e-08 | 16/35 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.44×** | +6.0 | 2e-07 | 18/36 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.53×** | +5.9 | 3e-07 | 20/36 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.50×** | +5.6 | 1e-06 | 17/36 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +5.3 | 6e-06 | 17/36 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 1e-05 | 20/37 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.29×** | +5.0 | 3e-05 | 18/36 (SW48, J82, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.41×** | +4.7 | 1e-04 | 15/34 (LoVo, HT-29, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.6 | 1e-04 | 15/36 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.40×** | +4.5 | 3e-04 | 19/35 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 3e-04 | 16/36 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.37×** | +4.3 | 5e-04 | 16/35 (SW48, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 7e-04 | 14/36 (Panc 03.27, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 7e-04 | 15/36 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.001 | 14/36 (MIA PaCa-2, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[BI-3406 (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.002 | 13/36 (MIA PaCa-2, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.003 | 12/36 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7733.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.324×** | -22.0 | 0e+00 | 33/35 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.275×** | -17.8 | 0e+00 | 27/34 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.308×** | -16.3 | 0e+00 | 33/36 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.305×** | -15.8 | 0e+00 | 31/35 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.377×** | -13.5 | 3e-39 | 30/36 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.380×** | -13.4 | 1e-38 | 34/36 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.388×** | -13.1 | 4e-37 | 31/36 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.396×** | -12.8 | 1e-35 | 31/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.502×** | -9.5 | 1e-19 | 25/35 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.555×** | -8.2 | 2e-14 | 26/36 (KATO III, SW48, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -7.3 | 2e-11 | 25/35 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.678×** | -5.4 | 3e-06 | 19/36 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.742×** | -4.1 | 0.002 | 17/33 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.743×** | -3.9 | 0.004 | 14/36 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.742×** | -3.8 | 0.005 | 15/33 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.544×** | -3.6 | 0.013 | 11/34 (LS 180, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.66 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.0 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.166× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 72.5 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -22.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -10.2) |
| [[KATO III (line)]] | alt | 146 | 0 | 11 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0960× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.303× (z -9.0) |
| [[PANC-1 (line)]] | alt | 25.1 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -19.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.254× (z -9.8) |
| [[COLO 205 (line)]] | alt | 251 | 1 (1 ⚠) | 9 (8 ⚠) | [[Selinexor (drug)]] 5 µM 2.29× (z +9.2) ⚠ cell-cycle shift, explains ~61% of this change | [[Panobinostat (drug)]] 5 µM 0.0257× (z -28.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -9.1) |
| [[HT-29 (line)]] | alt | 125 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.280× (z -9.2) |
| [[LoVo (line)]] | wt | 81.1 | 1 (1 ⚠) | 7 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.23× (z +8.7) ⚠ cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -22.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -11.2) |
| [[LS 180 (line)]] | wt | 137 | 0 | 8 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 102 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -17.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.167× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 41.5 | 0 | 7 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0815× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 79.1 | 1 (1 ⚠) | 5 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +10.7) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -21.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.318× (z -8.6) |
| [[SW 900 (line)]] | alt | 49.0 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 40.9 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -10.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 53.4 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -13.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 60.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.63× (z +8.6) ⚠ cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 29.9 | 1 | 2 (2 ⚠) | [[5-Azacytidine (drug)]] 5 µM 4.57× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 31.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.201× (z -8.7) |
| [[CHP-212 (line)]] | wt | 60.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -11.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -9.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.112× (z -9.1) |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.39× (z +9.0) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBR2]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[SLC7A11]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SLC3A2]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[LINC01564]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SLC6A9]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.57 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[LURAP1L-AS1]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GHITM]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ADGRF4]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DMGDH]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ATP6V1E1]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[HSPA9]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MIA2]] | +0.53 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP3]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[DOT1L]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PFN1]] | -0.52 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[OSBPL5]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[STMN3]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[CD82]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MAP3K14]] | -0.46 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[COL13A1]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PRR7]] | -0.45 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SPRED1]] | -0.45 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PTGS1]] | -0.45 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[TRAF2]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK1]] | B | SPINK1 activity raises LURAP1L's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without SPINK1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[CYP4F3]] | B | CYP4F3 activity raises LURAP1L's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without CYP4F3 | 0.075 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCPG1]] | B | LURAP1L activity raises CCPG1's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without LURAP1L | 0.008 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[NTN4]] | B | LURAP1L activity raises NTN4's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without LURAP1L | 0.023 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[SLC3A2]] | B | LURAP1L activity raises SLC3A2's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.45× lower at baseline in the lines without LURAP1L | 0.030 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[ZNF117]] | B | LURAP1L activity raises ZNF117's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without LURAP1L | 0.039 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[ABHD4]] | B | LURAP1L activity raises ABHD4's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without LURAP1L | 0.049 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[AKR1C1]] | B | LURAP1L activity raises AKR1C1's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 3.23× lower at baseline in the lines without LURAP1L | 0.079 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.3, 47.7); signed map (-13.0, 21.2). **Vector** length 111, 30.8% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.4 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +6.0 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.3 | -15.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.2 | -22.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.2 | -16.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.1 | -13.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.8 | -13.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -5.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich adaptor protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p23 — chr9:12,775,020-12,823,060 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46502, FLJ38505, bA3L8.2, LRAP35b; previously C9orf150 |
| Matched by | ensembl_id |

UniProt [Q8IV03](https://www.uniprot.org/uniprotkb/Q8IV03) carries no function annotation.

**Summary**, from NCBI Gene [286343](https://www.ncbi.nlm.nih.gov/gene/286343):

> Predicted to be involved in positive regulation of canonical NF-kappaB signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31452) · Entrez [286343](https://www.ncbi.nlm.nih.gov/gene/286343) · UniProt [Q8IV03](https://www.uniprot.org/uniprotkb/Q8IV03) · Ensembl [ENSG00000153714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153714)

## Data

Gene col 7733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7733); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7733]; `tensor/DDL_lfc|DDL_z.npy` [7733]; `embed/gene_vectors.npy` [7733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7733 or target_col == 7733). Every well: [[LURAP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LURAP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
