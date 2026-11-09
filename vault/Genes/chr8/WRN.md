---
symbol: "WRN"
type: "gene"
col: 9114
ensembl_id: "ENSG00000165392"
name: "WRN RecQ like helicase"
location: "8p12"
module: 36
arm: "+"
pooled_cpm: 140.57
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# WRN

*WRN RecQ like helicase* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.93× (z +13.6, q 2e-39, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.651× (z -12.5, q 3e-33, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERI3]] (+0.74, fdr 7e-06), [[URI1]] (+0.71, fdr 7e-06), [[IQCB1]] (+0.68, fdr 7e-06); moves opposite to [[ZNF436]] (-0.66, fdr 1e-05), [[MKLN1-AS]] (-0.64, fdr 3e-05), [[TRIM69]] (-0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ATXN1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +13.6 | 2e-39 | 48/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +10.8 | 7e-25 | 45/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +10.2 | 3e-22 | 44/47 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +10.1 | 5e-22 | 42/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +9.2 | 6e-18 | 45/48 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +8.2 | 3e-14 | 38/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.4 | 1e-11 | 33/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 2e-11 | 37/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +7.2 | 3e-11 | 36/48 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +6.2 | 3e-08 | 35/48 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.7 | 5e-07 | 31/45 (Hs 766T, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.5 | 2e-06 | 31/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.2 | 8e-06 | 32/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.7 | 9e-05 | 29/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 8e-04 | 30/49 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.2 | 8e-04 | 17/49 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.027 | 17/49 (C-33 A, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.028 | 16/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -12.5 | 3e-33 | 38/49 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -11.4 | 2e-27 | 34/44 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.607×** | -10.3 | 1e-22 | 40/49 (A498, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.749×** | -5.5 | 5e-06 | 25/45 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.771×** | -5.4 | 8e-06 | 31/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -5.4 | 8e-06 | 23/48 (A498, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.854× | -4.6 | 3e-04 | 17/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.804×** | -4.5 | 5e-04 | 25/49 (SW 1088, LS 180, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.807×** | -4.4 | 6e-04 | 29/48 (RKO, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.810×** | -4.3 | 8e-04 | 24/48 (KATO III, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.814×** | -4.2 | 0.001 | 26/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.835× | -4.2 | 0.001 | 22/48 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.823×** | -3.9 | 0.005 | 25/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.856× | -3.8 | 0.007 | 14/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.834× | -3.7 | 0.007 | 21/48 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.839× | -3.6 | 0.010 | 18/49 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.839× | -3.6 | 0.010 | 20/47 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.834× | -3.6 | 0.010 | 21/47 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.011 | 22/47 (SW 1271, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.847× | -3.4 | 0.016 | 19/48 (RKO, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 190 | 4 (2 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.40× (z +10.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.18× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -14.1) |
| [[A-172 (line)]] | wt | 129 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.8) |
| [[LoVo (line)]] | wt | 148 | 3 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.9) |
| [[RKO (line)]] | wt | 265 | 1 | 5 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.35× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -20.6) |
| [[A498 (line)]] | wt | 271 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -19.6) |
| [[HEC-1-A (line)]] | alt | 136 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.2) |
| [[J82 (line)]] | alt | 229 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.3) |
| [[A-427 (line)]] | wt | 197 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 119 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 244 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.96× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 93.8 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.523× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.5) |
| [[SW480 (line)]] | alt | 162 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 68.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 143 | 2 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -13.1) |
| [[SW 900 (line)]] | alt | 106 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 196 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -14.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 189 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.0) |
| [[SW48 (line)]] | wt | 199 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -15.0) |
| [[A549 (line)]] | wt | 185 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.0) |
| [[AN3 CA (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.610× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.45× (z +8.8) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 157 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[C32 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERI3]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[URI1]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[IQCB1]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.67 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TREX2]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[HERC2P9]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TOMM5]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[WDR5]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[DKC1]] | +0.64 | +0.68 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 516 |
| [[VKORC1L1]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF436]] | -0.66 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[MKLN1-AS]] | -0.64 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TRIM69]] | -0.62 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[MR1]] | -0.62 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[TMEM202-AS1]] | -0.62 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PATL2]] | -0.61 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[NCOA4]] | -0.61 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[TET2]] | -0.60 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SGO1-AS1]] | -0.60 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[EFCAB5]] | -0.59 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[TSGA10]] | -0.59 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[CHODL]] | -0.59 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1-AS1]] | B | ATXN1-AS1 activity lowers WRN's level | lines that do not express ATXN1-AS1 (6) vs lines expressing it (44) | 1.93× higher at baseline in the lines without ATXN1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ATXN1, LRRCC1, LAMB1 |
| [[GARNL3]] | C | GARNL3 activity raises WRN's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without GARNL3 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |
| [[BCL9L]] | C | BCL9L activity lowers WRN's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 2.05× higher at baseline in the lines without BCL9L | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent |
| [[NEIL2]] | C | NEIL2 activity raises WRN's level | lines that do not express NEIL2 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without NEIL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-3.7, -28.5); signed map (-43.4, -18.2). **Vector** length 122, 43.0% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.8 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.8 | +10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.7 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.6 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.6 | +0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -12.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.4 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | WRN RecQ like helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:31,033,788-31,176,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RECQL2, RECQ3 |
| Gene groups (HGNC) | Exonucleases; RecQ like helicases |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 37 pathways, smallest: Removal of the Flap Intermediate from the C-strand; Processive synthesis on the C-strand of the telomere; Impaired BRCA2 binding to PALB2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14191](https://www.uniprot.org/uniprotkb/Q14191) (Bifunctional 3'-5' exonuclease/ATP-dependent helicase WRN):

> Multifunctional enzyme that has magnesium and ATP-dependent 3'-5' DNA-helicase activity on partially duplex substrates. Also has 3'->5' exonuclease activity towards double-stranded (ds)DNA with a 5'-overhang. Has no nuclease activity towards single-stranded (ss)DNA or blunt-ended dsDNA. Helicase activity is most efficient with (d)ATP, but (d)CTP will substitute with reduced efficiency; strand displacement is enhanced by single-strand binding-protein (heterotrimeric replication protein A …

**Summary**, from NCBI Gene [7486](https://www.ncbi.nlm.nih.gov/gene/7486):

> This gene encodes a member of the RecQ subfamily of DNA helicase proteins. The encoded nuclear protein is important in the maintenance of genome stability and plays a role in DNA repair, replication, transcription and telomere maintenance. This protein contains a N-terminal 3' to 5' exonuclease domain, an ATP-dependent helicase domain and RQC (RecQ helicase conserved region) domain in its central region, and a C-terminal HRDC (helicase RNase D C-terminal) domain and nuclear localization signal. …

**Accessions** — [HGNC:12791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12791) · Entrez [7486](https://www.ncbi.nlm.nih.gov/gene/7486) · UniProt [Q14191](https://www.uniprot.org/uniprotkb/Q14191) · Ensembl [ENSG00000165392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165392)

## Data

Gene col 9114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9114); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9114]; `tensor/DDL_lfc|DDL_z.npy` [9114]; `embed/gene_vectors.npy` [9114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9114 or target_col == 9114). Every well: [[WRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
