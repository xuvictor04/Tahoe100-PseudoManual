---
symbol: "KATNIP"
type: "gene"
col: 517
ensembl_id: "ENSG00000047578"
name: "katanin interacting protein"
location: "16p12.1"
module: 185
arm: "+"
pooled_cpm: 76.31
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# KATNIP

*katanin interacting protein* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.46× (z +19.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.593× (z -10.9, q 8e-25, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.740× (z -9.2, q 6e-18, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT43]] (+0.67, fdr 7e-06), [[FBXO36]] (+0.67, fdr 7e-06), [[SMG6]] (+0.63, fdr 1e-05); moves opposite to [[TSPAN12]] (-0.54, fdr 4e-05), [[TLCD4]] (-0.51, fdr 2e-04), [[SLC25A30]] (-0.50, fdr 1e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMSB15B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.46×** | +19.5 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +17.2 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +14.7 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +13.8 | 3e-41 | 47/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +11.9 | 1e-30 | 37/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.70×** | +11.4 | 3e-28 | 44/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +9.1 | 6e-18 | 40/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +8.7 | 3e-16 | 38/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +8.2 | 2e-14 | 41/48 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +7.2 | 3e-11 | 38/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 5e-06 | 32/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.1 | 1e-05 | 21/48 (SW1417, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +4.7 | 1e-04 | 22/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +4.5 | 2e-04 | 25/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.3 | 8e-04 | 20/45 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.2 | 8e-04 | 21/48 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.016 | 20/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -10.9 | 8e-25 | 35/43 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -9.5 | 4e-19 | 35/49 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -9.2 | 6e-18 | 42/48 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.695×** | -7.9 | 5e-13 | 39/49 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -7.8 | 7e-13 | 31/45 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.741×** | -6.5 | 9e-09 | 30/48 (CHP-212, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -6.1 | 8e-08 | 34/47 (LOX-IMVI, SNU-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.0 | 4e-05 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.770×** | -4.0 | 0.004 | 22/48 (NCI-H1573, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.903× | -3.1 | 0.10 | 8/48 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.867× | -3.1 | 0.11 | 15/48 (SW 1271, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 72.6 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.26× (z +18.5) | — |
| [[LOX-IMVI (line)]] | wt | 88.9 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.376× (z -11.8) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 78.3 | 6 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -14.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 86.0 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.489× (z -11.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 80.7 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.267× (z -10.6) |
| [[HOP62 (line)]] | alt | 55.3 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 68.7 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +11.8) | — |
| [[RKO (line)]] | wt | 67.3 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.3) | [[Tucidinostat (drug)]] 5 µM 0.520× (z -8.9) |
| [[A-172 (line)]] | wt | 74.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 78.9 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -17.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 85.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 94.6 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 69.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 68.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 62.6 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 69.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 58.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 60.5 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -23.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 133 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 71.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 64.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 66.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -13.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 93.5 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 59.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 59.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 91.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 84.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 77.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 110 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 80.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 56.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 57.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +10.0) | — |
| [[C32 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 70.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0494× (z -15.6) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 65.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.2) | — |
| [[KATO III (line)]] | alt | 87.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[NCI-H596 (line)]] | alt | 81.2 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.189× (z -8.7) |
| [[PANC-1 (line)]] | alt | 100 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.1) | — |
| [[SW 1271 (line)]] | alt | 68.6 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0729× (z -10.5) |
| [[SW 900 (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[SW48 (line)]] | wt | 57.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.97× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT43]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[FBXO36]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SMG6]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CHMP1A]] | +0.62 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[ULK4]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NSMCE2]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SFSWAP]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[UMAD1]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ZFYVE26]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[VAC14]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CCDC157]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN12]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TLCD4]] | -0.51 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[SLC25A30]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PM20D2]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ABHD10]] | -0.49 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RYK]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PGM2]] | -0.48 | -0.66 / -0.38 | both halves | 6e-05 |  |
| [[PRTG]] | -0.47 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[SPOPL]] | -0.47 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CYB5A]] | -0.47 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[PLEKHA1]] | -0.47 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[EPB41L4B]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMSB15B]] | B | TMSB15B activity raises KATNIP's level | lines that do not express TMSB15B (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without TMSB15B | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000288597, PRKD1, GRIK4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.2, -12.0); signed map (-18.9, 2.4). **Vector** length 110, 33.8% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +8.7 | +13.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.1 | +11.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +8.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.5 | +9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -13.5 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -11.6 | -7.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.2 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | katanin interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:27,550,133-27,780,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JBTS26; previously KIAA0556 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60303](https://www.uniprot.org/uniprotkb/O60303) (Katanin-interacting protein):

> May influence the stability of microtubules (MT), possibly through interaction with the MT-severing katanin complex.

**Summary**, from NCBI Gene [23247](https://www.ncbi.nlm.nih.gov/gene/23247):

> This gene encodes a novel, evolutionarily conserved, ciliary protein. In human hTERT-RPE1 cells, the protein is found at the base of cilia, decorating the ciliary axoneme, and enriched at the ciliary tip. The protein binds to microtubules in vitro and regulates their stability when it is overexpressed. A null mutation in this gene has been associated with Joubert syndrome, a recessive disorder that is characterized by a distinctive mid-hindbrain and cerebellar malformation and is also often …

**Accessions** — [HGNC:29068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29068) · Entrez [23247](https://www.ncbi.nlm.nih.gov/gene/23247) · UniProt [O60303](https://www.uniprot.org/uniprotkb/O60303) · Ensembl [ENSG00000047578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047578)

## Data

Gene col 517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 517); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 517]; `tensor/DDL_lfc|DDL_z.npy` [517]; `embed/gene_vectors.npy` [517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 517 or target_col == 517). Every well: [[KATNIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KATNIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
