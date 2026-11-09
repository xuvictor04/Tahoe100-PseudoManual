---
symbol: "ROBO1"
type: "gene"
col: 9860
ensembl_id: "ENSG00000169855"
name: "roundabout guidance receptor 1"
location: "3p12.3"
module: 9
arm: "+"
pooled_cpm: 193.06
n_lines_expressing: 37
n_dd_up: 29
n_dd_down: 27
n_dd_up_clean: 24
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ROBO1

*roundabout guidance receptor 1* — 3p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +23.7, q 0e+00, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.529× (z -13.7, q 6e-40, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRISPLD1]] (+0.60, fdr 1e-05), [[COL11A1]] (+0.59, fdr 3e-05), [[LINC00882]] (+0.57, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.52, fdr 1e-05), [[SH3BP5L]] (-0.51, fdr 2e-05), [[NBPF20]] (-0.50, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MXRA8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SOBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +23.7 | 0e+00 | 27/35 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +11.2 | 8e-27 | 26/35 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +11.0 | 1e-25 | 23/35 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +8.9 | 6e-17 | 22/35 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +8.5 | 2e-15 | 24/36 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +8.3 | 8e-15 | 24/34 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +8.1 | 5e-14 | 20/35 (A-172, J82, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.9 | 2e-13 | 20/35 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +7.8 | 3e-13 | 23/35 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +7.5 | 4e-12 | 22/35 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.37×** | +7.2 | 2e-11 | 23/37 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +6.9 | 3e-10 | 25/35 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.5 | 3e-09 | 19/35 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +6.1 | 5e-08 | 17/35 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +5.8 | 3e-07 | 17/36 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +5.7 | 4e-07 | 22/35 (HOP62, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 5e-07 | 23/34 (C32, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.529×** | -13.7 | 6e-40 | 31/35 (SW480, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -12.2 | 9e-32 | 28/34 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.656×** | -9.1 | 2e-17 | 23/36 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.667×** | -8.1 | 1e-13 | 22/33 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -7.9 | 4e-13 | 21/35 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.701×** | -7.6 | 2e-12 | 23/35 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -7.4 | 1e-11 | 24/35 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -7.1 | 9e-11 | 25/35 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -7.0 | 1e-10 | 23/36 (NCI-H1573, CHP-212, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.724×** | -6.9 | 2e-10 | 25/34 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.728×** | -6.8 | 4e-10 | 22/35 (NCI-H1573, CHP-212, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.558×** | -6.6 | 2e-09 | 20/28 (SW 900, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -6.5 | 4e-09 | 24/35 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -6.4 | 7e-09 | 24/32 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.744×** | -6.4 | 8e-09 | 25/35 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.753×** | -6.1 | 4e-08 | 25/35 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.756×** | -5.8 | 2e-07 | 22/34 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.709×** | -5.3 | 4e-06 | 21/35 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.799×** | -4.5 | 2e-04 | 17/34 (A549, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **0.682×** | -4.3 | 4e-04 | 19/33 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.686×** | -4.2 | 5e-04 | 17/35 (RKO, SNU-423, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.815×** | -4.2 | 5e-04 | 18/35 (A549, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 314 | 13 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +19.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -8.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 191 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +28.4) | — |
| [[J82 (line)]] | alt | 94.3 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +31.4) | — |
| [[SHP-77 (line)]] | alt | 804 | 0 | 11 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -17.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.466× (z -15.6) |
| [[PANC-1 (line)]] | alt | 231 | 1 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.1) | [[Auranofin (drug)]] 5 µM 0.408× (z -13.4) |
| [[SW480 (line)]] | alt | 750 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -19.6) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.233× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 143 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +23.8) | — |
| [[SW 900 (line)]] | alt | 105 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +22.2) | [[Lonafarnib (drug)]] 5 µM 0.153× (z -10.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 370 | 1 (1 ⚠) | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.451× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 120 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +28.6) | — |
| [[Panc 03.27 (line)]] | alt | 151 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +28.3) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.392× (z -10.2) |
| [[A-427 (line)]] | wt | 242 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.511× (z -9.0) |
| [[A498 (line)]] | wt | 61.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.4) | — |
| [[HepG2_C3A (line)]] | wt | 1,002 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -14.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.433× (z -10.0) |
| [[SNU-423 (line)]] | alt | 273 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -9.1) |
| [[A-172 (line)]] | wt | 86.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.6) | — |
| [[RKO (line)]] | wt | 109 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.354× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -9.4) |
| [[C-33 A (line)]] | alt | 191 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.304× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~16% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.438× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 386 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -12.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 397 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +24.9) | — |
| [[hTERT-HPNE (line)]] | wt | 298 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +26.5) | — |
| [[A549 (line)]] | wt | 228 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 3.08× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 67.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +23.5) | — |
| [[LS 180 (line)]] | wt | 87.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 383 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.9) | [[Auranofin (drug)]] 5 µM 0.407× (z -11.1) |
| [[AN3 CA (line)]] | alt | 251 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.280× (z -10.6) |
| [[CHP-212 (line)]] | wt | 274 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.289× (z -8.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 159 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +13.3) ⚠ position not correctable | — |
| [[NCI-H661 (line)]] | alt | 925 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SK-MEL-2 (line)]] | alt | 303 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 99.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 38.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 525 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRISPLD1]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[COL11A1]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[LINC00882]] | +0.57 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GRIK2]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NREP]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CDH12]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[DMD]] | +0.54 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CDH10]] | +0.54 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[ZNF608]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.53 | +0.55 / +0.56 | both halves | 1e-05 | same gene group |
| [[AKR1B1]] | +0.53 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[MAPK10]] | +0.52 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SH3BP5L]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[NBPF20]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CUTC]] | -0.49 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[FAM131A]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GNAS-AS1]] | -0.47 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[STARD3]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ERCC3]] | -0.46 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[DPP9]] | -0.46 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RBAK-RBAKDN]] | -0.45 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[KCNC4]] | -0.45 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RBM14-RBM4]] | -0.45 | -0.51 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MXRA8]] | B | MXRA8 activity raises ROBO1's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.05× lower at baseline in the lines without MXRA8 | 0.062 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[CTNNA2]] | B | CTNNA2 activity raises ROBO1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.82× lower at baseline in the lines without CTNNA2 | 0.070 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |
| [[ADGRL2]] | B | ADGRL2 activity raises ROBO1's level | lines that do not express ADGRL2 (19) vs lines expressing it (31) | 2.54× lower at baseline in the lines without ADGRL2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM23, SCN9A, WDR17 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ROBO1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | ROBO1 activity raises SOBP's level | lines that do not express ROBO1 (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without ROBO1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CRMP1, PEG10, MGAT5B |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, 30.8); signed map (38.9, 33.2). **Vector** length 119, 35.9% of its response variance represented; |z| ≥ 3 in 1,463 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +23.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +8.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +8.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +6.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +5.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -12.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | roundabout guidance receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p12.3 — chr3:78,597,239-79,767,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DUTT1, FLJ21882, SAX3 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family; Roundabout guidance receptor family |
| Reactome | 11 pathways, smallest: Regulation of cortical dendrite branching; SLIT2:ROBO1 increases RHOA activity; Inactivation of CDC42 and RAC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6N7](https://www.uniprot.org/uniprotkb/Q9Y6N7) (Roundabout homolog 1):

> Receptor for SLIT1 and SLIT2 that mediates cellular responses to molecular guidance cues in cellular migration, including axonal navigation at the ventral midline of the neural tube and projection of axons to different regions during neuronal development. Interaction with the intracellular domain of FLRT3 mediates axon attraction towards cells expressing NTN1. In axon growth cones, the silencing of the attractive effect of NTN1 by SLIT2 may require the formation of a ROBO1-DCC complex (By …

**Summary**, from NCBI Gene [6091](https://www.ncbi.nlm.nih.gov/gene/6091):

> Bilateral symmetric nervous systems have special midline structures that establish a partition between the two mirror image halves. Some axons project toward and across the midline in response to long-range chemoattractants emanating from the midline. The product of this gene is a member of the immunoglobulin gene superfamily and encodes an integral membrane protein that functions in axon guidance and neuronal precursor cell migration. This receptor is activated by SLIT-family proteins, …

**Accessions** — [HGNC:10249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10249) · Entrez [6091](https://www.ncbi.nlm.nih.gov/gene/6091) · UniProt [Q9Y6N7](https://www.uniprot.org/uniprotkb/Q9Y6N7) · Ensembl [ENSG00000169855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169855)

## Data

Gene col 9860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9860); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9860]; `tensor/DDL_lfc|DDL_z.npy` [9860]; `embed/gene_vectors.npy` [9860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9860 or target_col == 9860). Every well: [[ROBO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ROBO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
