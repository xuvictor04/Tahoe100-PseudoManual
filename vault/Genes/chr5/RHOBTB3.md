---
symbol: "RHOBTB3"
type: "gene"
col: 8919
ensembl_id: "ENSG00000164292"
name: "Rho related BTB domain containing 3"
location: "5q15"
module: 217
arm: "+"
pooled_cpm: 149.04
n_lines_expressing: 40
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# RHOBTB3

*Rho related BTB domain containing 3* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +20.6, q 0e+00, up in 34 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +8.5, q 3e-15, up in 22 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.614× (z -10.2, q 1e-21, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF608]] (+0.61, fdr 1e-05), [[TGFB2]] (+0.60, fdr 2e-05), [[MBNL1]] (+0.59, fdr 2e-05); moves opposite to [[ZNRD2]] (-0.59, fdr 2e-05), [[SPRYD3]] (-0.56, fdr 3e-05), [[ESS2]] (-0.55, fdr 3e-05).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ATOH8]] → it (grade B ⚠); 6 go from it, the strongest it → [[SMIM10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +20.6 | 0e+00 | 34/39 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +18.8 | 0e+00 | 33/34 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +10.3 | 1e-22 | 27/34 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.5 | 3e-15 | 22/38 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +8.3 | 1e-14 | 26/39 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.6 | 4e-09 | 21/38 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.1 | 8e-08 | 20/38 (SNU-423, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +5.7 | 8e-07 | 24/38 (SW 900, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 4e-05 | 22/39 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +4.7 | 1e-04 | 23/38 (A-172, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.25×** | +4.7 | 1e-04 | 23/38 (HOP62, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 19/39 (HOP62, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +4.0 | 0.002 | 17/38 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.20×** | +3.9 | 0.005 | 21/38 (HOP62, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.20×** | +3.8 | 0.006 | 16/38 (HOP62, SW 900, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.006 | 19/37 (PANC-1, C32, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.008 | 18/38 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.009 | 16/38 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.009 | 18/38 (PANC-1, A498, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.011 | 13/38 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.016 | 9/38 (HS-578T, PANC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.19× | +3.4 | 0.018 | 15/39 (CFPAC-1, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.614×** | -10.2 | 1e-21 | 29/38 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.678×** | -8.1 | 1e-13 | 28/38 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -8.0 | 3e-13 | 24/38 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.561×** | -6.3 | 4e-08 | 27/38 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -5.9 | 5e-07 | 26/38 (COLO 205, C32, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -5.8 | 5e-07 | 22/38 (SW480, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.806×** | -4.5 | 5e-04 | 22/38 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.807×** | -4.5 | 5e-04 | 20/38 (NCI-H1792, J82, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.663×** | -4.5 | 5e-04 | 23/38 (COLO 205, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.667×** | -4.4 | 5e-04 | 19/39 (COLO 205, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.821×** | -4.0 | 0.004 | 18/37 (H4, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -3.9 | 0.004 | 17/38 (NCI-H460, AN3 CA, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.840× | -3.6 | 0.011 | 14/37 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.847× | -3.5 | 0.020 | 13/37 (LS 180, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.890× | -3.5 | 0.020 | 20/39 (COLO 205, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 245 | 13 (2 ⚠) | 5 (1 ⚠) | [[Trametinib (drug)]] 5 µM 2.69× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 2.65× (z +11.1) | [[Ixazomib citrate (drug)]] 5 µM 0.325× (z -12.1) |
| [[COLO 205 (line)]] | alt | 721 | 0 | 13 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -31.1) |
| [[HOP62 (line)]] | alt | 152 | 9 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +18.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 205 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.227× (z -25.9) |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -14.4) |
| [[PANC-1 (line)]] | alt | 184 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 2.60× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 137 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.00× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 253 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.9) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.374× (z -10.2) |
| [[A-172 (line)]] | wt | 646 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +23.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.84× (z +8.8) | — |
| [[J82 (line)]] | alt | 335 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.418× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 153 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.3) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 0.05 µM 0.346× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 230 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +19.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.9) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H2030 (line)]] | alt | 110 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 190 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -16.2) |
| [[SNU-423 (line)]] | alt | 422 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +25.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.09× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.473× (z -11.2) |
| [[A498 (line)]] | wt | 75.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +12.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.68× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 263 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +13.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.467× (z -8.7) |
| [[HS-578T (line)]] | alt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +16.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 235 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 100 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 70.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +12.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 250 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.364× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 101 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 0.5 µM 0.436× (z -8.6) |
| [[HT-29 (line)]] | alt | 68.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +11.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 72.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 69.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 78.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 39.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.0) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.236× (z -10.3) ⚠ cell-cycle shift, explains ~74% of this change |
| [[SK-MEL-2 (line)]] | alt | 258 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0835× (z -9.5) |
| [[SW 900 (line)]] | alt | 190 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 33.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 297 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[TGFB2]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MBNL1]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[RDX]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[FIGN]] | +0.57 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[ARHGAP24]] | +0.56 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[GPNMB]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[AK3]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CFH]] | +0.54 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[COL12A1]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ENAH]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ALCAM]] | +0.54 | +0.58 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRD2]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SPRYD3]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ESS2]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NGRN]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[YKT6]] | -0.54 | -0.69 / -0.26 | both halves | 3e-04 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[RABIF]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[EFL1]] | -0.53 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[ZBTB49]] | -0.53 | -0.46 / -0.42 | both halves | 4e-05 | same gene group |
| [[CIB1]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[GCKR]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[PLAUR]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATOH8]] | B | ATOH8 activity raises RHOBTB3's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without ATOH8 | 0.030 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[SMIM10]] | B | SMIM10 activity raises RHOBTB3's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.43× lower at baseline in the lines without SMIM10 | 0.034 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[ARID5B]] | B | ARID5B activity raises RHOBTB3's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without ARID5B | 0.038 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[EFEMP1]] | B | EFEMP1 activity raises RHOBTB3's level | lines that do not express EFEMP1 (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without EFEMP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, IL31RA |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM10]] | B | RHOBTB3 activity raises SMIM10's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without RHOBTB3 | 0.039 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[AASS]] | B | RHOBTB3 activity raises AASS's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without RHOBTB3 | 0.049 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[SLC16A7]] | B | RHOBTB3 activity raises SLC16A7's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 3.53× lower at baseline in the lines without RHOBTB3 | 0.052 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[SH3BGRL]] | B | RHOBTB3 activity raises SH3BGRL's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 1.66× lower at baseline in the lines without RHOBTB3 | 0.071 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[ANGPT1]] | B | RHOBTB3 activity raises ANGPT1's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 3.36× lower at baseline in the lines without RHOBTB3 | 0.091 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[ARHGAP24]] | B | RHOBTB3 activity raises ARHGAP24's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 3.14× lower at baseline in the lines without RHOBTB3 | 0.095 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, 16.4); signed map (47.6, 19.7). **Vector** length 118, 32.2% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +20.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +18.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -6.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho related BTB domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:95,713,522-95,824,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0878 |
| Gene groups (HGNC) | BTB domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 6 pathways, smallest: RHOBTB3 ATPase cycle; Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [O94955](https://www.uniprot.org/uniprotkb/O94955) (Rho-related BTB domain-containing protein 3):

> Rab9-regulated ATPase required for endosome to Golgi transport. Involved in transport vesicle docking at the Golgi complex, possibly by participating in release M6PRBP1/TIP47 from vesicles to permit their efficient docking and fusion at the Golgi. Specifically binds Rab9, but not other Rab proteins. Has low intrinsic ATPase activity due to autoinhibition, which is relieved by Rab9.

**Summary**, from NCBI Gene [22836](https://www.ncbi.nlm.nih.gov/gene/22836):

> Enables ATP binding activity; ATP hydrolysis activity; and small GTPase binding activity. Involved in retrograde transport, endosome to Golgi. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18757) · Entrez [22836](https://www.ncbi.nlm.nih.gov/gene/22836) · UniProt [O94955](https://www.uniprot.org/uniprotkb/O94955) · Ensembl [ENSG00000164292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164292)

## Data

Gene col 8919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8919); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8919]; `tensor/DDL_lfc|DDL_z.npy` [8919]; `embed/gene_vectors.npy` [8919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8919 or target_col == 8919). Every well: [[RHOBTB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOBTB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
